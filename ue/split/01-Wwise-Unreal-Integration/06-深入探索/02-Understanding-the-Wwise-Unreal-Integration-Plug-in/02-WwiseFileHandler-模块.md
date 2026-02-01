# WwiseFileHandler 模块

|  |
| --- |
| Wwise Unreal Integration Documentation |

WwiseFileHandler 模块

The WwiseFileHandler module prepares and handles all External Sources, media, and SoundBank files. 该模块可预先加载、加载并以流方式传输文件，但其本身不会检查相关文件中有无依赖项。

每个文件都作为单独对象进行处理并且只会打开一次。对文件的使用通过 [File State](module_filehandler.html#filehandler_filestates) 单独追踪。在将 File State 提供给以下所述三个管理器之一后，可选择将对应文件提供给 [声音引擎的 I/O Hook 和 File Location Resolver](module_filehandler.html#filehandler_resolver) 。

WwiseFileHandler 需要 [WwiseResourceLoader](module_resourceloader.html) 先将文件及其选项一起注册为 *File State*。之后，声音引擎的 File Location Resolver 才可访问该文件。

因为元数据存储在 GeneratedSoundBanks 文件夹中并与素材一起作为打包信息进行烘焙，所以 [WwiseResourceLoader 模块](module_resourceloader.html) 可以决定需要哪些资源，之后再由 WwiseFileHandler 在加载可能需要它的资源之前提供所有 File State。

# File State

File State 会向 WwiseFileHandler 模块声明一个*已知文件*。借助 Load 和 Unload 操作，将文件提供给 WwiseFileHandler。藉此，确定其是否已经加载并需要计算引用计数。只要有用户使用文件，其 File State 就会保持活跃状态。

每项与 File State 相关的新操作都在其各自的 Execution Queue 中运行。队列中的操作按照次序异步执行。鉴于 File State 的异步特性，每个 File State 都有两个层面：公共的异步方法和受保护的同步方法。每个公共方法只不过是一个用于将操作推送到 Execution Queue 中的封装器。

主要状态有三种：Closed、Opened 和 Loaded。各个状态的定义有些随意，不过可以粗略定义如下：

- **Closed**：可安全删除文件。除少量内存外，其没有任何系统在使用的资源。
- **Opened**：已完成对文件操作的定义。文件已打开并可能在内存中部分或全部读取。对于流媒体，表示已打开文件并缓存了所需数量的预加载数据。对于内存中的媒体，表示已打开、完整读取并关闭文件；可用指针为其 **Opened** 状态。
- **Loaded**：已完成对声音引擎操作的定义。要么声音引擎获知该文件存在，要么向声音引擎提供了该文件。比如，对于流媒体，向 I/O Hook 提供了文件以便读取其内容。对于内存中加载的媒体文件，表示已通过 SetMedia 操作将其数据发送到声音引擎。同样，对于 SoundBank，表示已通过 LoadBank 方法类对其数据进行处理。

除此之外，还有表示向某一主要 File State 过渡的中间 File State。

![](../../../../images/dgm_filehandlingstates.png)

由于操作是异步的并且可能需要很长时间，所以有时会有多项操作等待加载同一文件。在这种情况下，只有一项操作会被继续执行。在返回状态前，所有其余操作会等待该操作完成。比如，有个包含 12 个不同 Event 的 User-Defined SoundBank。这 12 个 Event 可能会同时请求加载同一 SoundBank。在这种情况下，只有加载了该 SoundBank，才会继续处理这些 Event。

对于耗时较长的音频操作，在 Unloading 时要特别注意。比如，对于包含较长混响尾音的 AK Convolution Reverb 文件，完成回响后才能将其卸载。又如，对于不间断的循环媒体，可能永远不会停止播放。这些操作可能会在很长时间内保持某种过渡状态。

另外，在处理混响尾音的同时，可能会发出对同一文件的请求。比如，在为新的地图收集资源时，该地图恰好在请求访问同一媒体。这时并不会卡在 Unloading 状态，而会将状态更改为 Reloading，并在第一时间取消卸载操作，然后将状态恢复为 Loaded。

# 声音引擎的 I/O Hook 和 File Location Resolver

声音引擎的 I/O Hook 和 File Location Resolver 负责在生命周期内协同处理流媒体素材。首先，File Location Resolver 会请求 WwiseFileHandler 打开文件。在打开后，I/O Hook 会请求 WwiseFileHandler 根据需要完成对已打开文件的异步 Read 请求。

在通过 Resolver 打开文件时，涉及以下操作：

1. 根据传递的 Short ID 查找 File State 映射。
2. 请求 File State 确认新的流传输请求。这时可能会更改其状态（取决于 File State 算法）。
3. 将结果返回给声音引擎。

在一般的游戏中，不到一毫秒就可完成所有这些操作，但是照样可能会被认为耗时比较长。不过，因为 File State 已被打开并可马上使用，所以可能并不需要额外的系统 I/O 操作。

在打开文件以供流传输后，会专门通过另一 Execution Queue 处理 I/O Hook 的异步 Read 操作。该队列旨在高效、及时地加以处理，确保以最优方式批量处理 Read 操作。除此之外，它还提供对流媒体的 Close 操作，确保在完成所有待处理 Read 操作后再执行 Close 操作。

跟所有的声音引擎回调一样，这些操作会在 Unreal 以外的线程中调用。它们具有不同的 Unreal 线程本地数据，堆栈大小不一样，优先级也可能不同。很多 Unreal 操作会因此而失败（比如 Stats 收集）。

## 基于文件名的 Location Resolver

Location Resolver 中的大部分 Open 操作都是基于各个映射中存储的 Short ID 执行的。

Integration 并不支持基于文件的路径名称来打开文件。Integration 只会基于 Short ID 打开文件。不过，也存在声音引擎可以基于文件的路径名称打开文件的情况。比如，有些算法（如 XML Error Translator）请求获取 "SoundBanks.xml" 文件。或者，在声音引擎写入文件的时候。这样做通常是为了在 Profile 和 Debug 版本中生成日志。

# SoundBank Manager 和 Media Manager

SoundBank Manager 提供 LoadSoundBank 和 UnloadSoundBank 操作，Media Manager 则提供 LoadMedia 和 UnloadMedia 操作。这两个管理器会追踪都创建了哪些 File State，并在请求获取 File State 以进行流传输时将信息发送给 Location Resolver。

两者通过相同的 Execution Queue 模式异步运行。因为 File State 的创建过程相对来说比较高效，所以在同时执行多项操作时通常很少有延迟。不过，可能需要更多时间来执行回调。因为文件必须处于适合使用的状态，包括声音引擎的加载或卸载。

# External Source Manager

The External Source Manager (refer to [使用 External Source](using_features_ext_src.html)) manages File States for External Sources. It is designed to be overridden by a user-developed module that implements a data model to track External Source media dependencies. The Wwise Simple External Source Manager is an example that uses Data Tables (.csv files) to map the External Sources to their corresponding media.

The manager provides a supplemental, editor-only operation for cooking that the user can override to properly stage External Source files. With this approach, users don't have to override the [WwiseResourceCooker 模块](module_resourcecooker.html) only to support their External Source Manager implementations.

Because the posted Events must include the External Sources they use when they are posted, the Integration automatically queries the External Source Manager for this information at the appropriate time. 有关详细信息，请参阅 [使用 Wwise Simple External Source Manager](using_features_simpleexternalsourcemanager.html) 章节。