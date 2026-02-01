# Integration Demo 示例

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Integration Demo 示例

Integration Demo 应用程序包含一系列的演示，展示如何在游戏中集成声音引擎的各种功能。

|  |  |
| --- | --- |
|  | **备注:** 本节中展示的所有代码均可在 `samples\IntegrationDemo\` 目录下的示例工程中找到。 |

# Wwise 工程

此程序的 Wwise 工程也可在 `samples\IntegrationDemo\WwiseProject` 下找到。

|  |  |
| --- | --- |
|  | **备注:** 此程序的 Wwise 工程使用各种音频文件转码格式，某些格式可能不可用，具体取决于安装的 Wwise 支持的平台。在 Wwise 中打开工程后，您可能会看到诸如以下警告：   ``` \Containers\Dialogues\Captain_A\UNA-BM-AL_01\UNA-BM-AL_01 uses the conversion plugin 'XMA', which is not installed. ```   您可以将所有不可用平台的转码格式更改为 PCM，从而移除这些消息。有关详细信息，请参阅《Wwise 用户指南》中的以下主题：[音频文件转码](https://www.audiokinetic.com/library/edge/?source=Help&id=authoring_across_platforms_converting_audio_files)。 |

此工程的 SoundBank 也会与 SDK 一并安装到 `samples\IntegrationDemo\WwiseProject\GeneratedSoundBanks` 文件夹中。

要重新生成 SoundBank，请确保在 SoundBank Manager 中执行以下操作：

- 勾选 SoundBank 列表中的所有 SoundBank。
- 勾选经过测试的所有平台。
- 勾选语言列表中的所有语言。

这些设置一旦正确，您可以在 SoundBank Manager 中单击 **Generate** 来生成 SoundBank。

# 构建和运行演示

Integration Demo 二进制文件可在 `\[Debug|Profile|Release]\bin` 目录下找到。如果您想自己重新构建此应用程序，则按照以下步骤执行：

## Windows

- 确认在您的机器中安装的 DirectX SDK 版本与 [平台要求](reference_platform.html) 中提及的版本匹配。
- 在默认路径下为 Windows 生成 Integration Demo SoundBank。
- 打开 `samples\IntegrationDemo\Windows` 中的解决方案，并使用所需配置进行构建。

要运行 Integration Demo，只需启动在上述目录中找到的可执行文件即可。

# 使用说明

在 Windows 中，您可以使用键盘、连接的控制器或任何 DirectInput 兼容设备浏览 Integration Demo。

- 要在页面上的控件之间导航，使用 UP 和 DOWN 方向键或者游戏手柄上的 UP 和 DOWN 按钮。
- 要激活选中的控件，单击 Enter 键或者游戏手柄上的 A/X 按钮。
- 要在菜单中返回页面，单击 Esc 键或者游戏手柄上的 B/O 按钮。

某些控件（例如切换控件和数字滑块）可让您修改数值。要修改数值，单击 LEFT 和 RIGHT 方向键或者游戏手柄上的 LEFT 和 RIGHT 按钮。

|  |  |
| --- | --- |
|  | **技巧:** 此应用程序有联机帮助功能！要访问帮助页面，按键盘上的 F1 键或者游戏手柄上的 START 按钮。 |

# 演示

**所有演示代码均可在 `samples\IntegrationDemo\DemoPages` 目录下找到。**例如，您可以在该目录下的 `DemoLocalization.h` 和 `DemoLocalization.cpp` 文件中找到 Localization 演示代码。

|  |  |
| --- | --- |
|  | **技巧:** 有关每个演示的相关信息也可在 Integration Demo 应用程序联机帮助中找到。 |

## Dialogue

### Localization Demo

此演示展示如何实现本地化音频。本地化的音频对象位于 SoundBank 生成目录的子目录下的相关语言 SoundBank 中。我们通过卸载当前 SoundBank，然后加载期望的特定语言的 SoundBank 来达到本地化效果。

使用 **Language** 切换控件切换当前语言。然后按 **Say Hello** 按钮试听选定语言的问候。

有关语言和本地化的更多信息，请参阅 [集成详情——语言与语音](soundengine_languages.html) 。

### Dynamic Dialogue Demo

Dynamic Dialogue 演示运行一系列使用 Wwise Dynamic Dialogue 功能的测试。每项测试演示不同的控制流程，以便您可以试听它产生的效果：

- 测试 1：显示如何使用 Wwise ID 播放简单的动态序列。
- 测试 2：与测试 1 一样，但使用的是字符串而不是 ID。
- 测试 3：展示在播放期间如何向动态播放列表中添加项目。
- 测试 4：展示在播放期间如何向动态播放列表中插入项目。
- 测试 5：展示当向空播放列表中添加项目时的情况。
- 测试 6：展示如何针对动态序列使用 **Stop** 调用。
- 测试 7：展示如何针对动态序列使用 **Break** 调用。
- 测试 8：展示如何针对动态序列使用 **Pause** 和 **Resume** 调用。
- 测试 9：展示如何在将条目添加到动态序列队列中时使用 **Break** 调用。
- 测试 10：展示如何在播放期间清空播放列表。
- 测试 11：展示在停止和清空播放列表时的情况。
- 测试 12：展示在针对播放列表调用 **Break** 并将其清空时会发生什么。
- 测试 13：展示暂停和清空播放列表时的情况。
- 测试 14：展示在使用动态对白时如何使用带自定义参数的回调函数。
- 测试 15：显示如何使用回调执行任务（在这种情况下，在播放 3 个项目后取消播放）。
- 测试 16：显示如何使用回调执行任务（在这种情况下，在第一个序列结束后播放第二个序列）。
- 测试 17：显示如何结合 Dynamic Dialogue 使用 Wwise Event。

有关动态对白的更多信息，请参阅 [集成详情——动态对白](soundengine_dynamicdialogue.html)

## RTPC（汽车发动机）

此演示展示如何使用 RTPC。RPM 数字滑块链接到与发动机相关联的 RTPC 值（RPM）。按下 **Start Engine** 按钮，以启动/停止汽车发动机音频。使用 RPM 滑块更改 RTPC 值并试听效果。

有关 RTPC 的更多信息，请参阅 [集成详情——RTPC](soundengine_rtpc.html) 。

## 脚步

此演示展示在游戏中实现脚步声的各种方式。它还展示了基于表面类型驱动的 SoundBank 管理，以最大限度地降低当某个表面类型不用时的媒体和元数据内存占用。最后，此演示还展示了一个非常简单的环境效果器示例。

在本例中，脚步声由 2 个变量修改：行走速度和行走者体重。

- 行走速度问题（Footstep\_Speed RTPC） 此工程支持几乎在所有情况下的从行走到奔跑的顺畅过渡。对于此变量，我们假设存在以下条件：走得越快，脚步声越短，撞击地面越重。这分别相当于更改音高和音量。在工程中查找有关这些参数的 RTPC。在此演示中，速度 RTPC 直接由操纵杆位移来驱动。
- 行走人体重问题（Footstep\_Weight RTPC） 脚步结构支持各种行走人体重。我们假定在现实生活中，行走人体重越重，脚步声越长，并且越模糊。这分别相当于修改音高和 LPF。在工程中查找有关这些参数的 RTPC。

对于每种表面，我们展示了处理声音样本和变量的不同方式。它们只是一些您可以在自己的结构中使用的建议和想法。

- 碎石 我们的碎石样本非常相似，因此无需采集大量有关此表面的样本。使用一点音量、LPF 和音高随机化可以获得更多版本。体重影响通过 EQ 效果器来实现，它的增益参数由体重 RTPC 驱动。对于轻脚步声，提高频率，对于重脚步声，则采取相反的操作。注意 RTPC 对 Pitch 和 Volume 的影响。
- 木材： 对于木材表面，行走和奔跑样本迥然不同，就像轻轻的脚步声和沉重的脚步声一样。因此它的组织方式更偏向于传统 Switch 层级结构。两个 Switch Container 均由 RTPC 驱动的 Switch 驱动（查看 GameSync 选项卡中的 Footstep\_Gait 和 Footstep\_Weight）。
- 泥土 在这种表面上行走和奔跑的样本有些类似，因此我们决定使用 Blend Container 执行过渡。有关音高和音高的 RTPC 用于考虑体重。

**音频包管理：** 在 Footsteps 演示中，音频包分为四个媒体音频包（每种表面各一个）。我们将屏幕一分为四，每种表面之间有一个缓冲区，在该缓冲区内要加载两个媒体 SoundBank。其目的在于避免加载媒体 SoundBank 时导致脚步声中存在间隙。在 SoundBank 管理器中，查看 GameSync 选项卡。注意，每个表面 SoundBank 仅包含相应的表面 Switch。这仅包括与该 SoundBank 中的切换开关相关的层级结构，与其它的无关。在大型游戏中，这一设置有限制特定场景中用不上的样本数量，从而限制内存占用的优势。对于基于关卡或分区的游戏，识别所用的表面非常容易，因为在设计阶段就已经知道了。对于开放世界式游戏，这更为棘手，很大程度上取决于游戏的组织，但仍可以实现。例如，如果玩家目前位于一个温暖的城市，在长时间内不会移到寒冷的环境，那么在内存中保留“冰雪”表面声音则没有任何用处。

## 字幕/标记

此演示展示如何设置回调函数以在点击声音文件内部的标记时接收通知。对于此演示，我们使用标记来对字幕和音频轨进行同步。

有关标记的更多信息，请参阅 [集成 Marker](soundengine_markers.html) 。

## Music/MIDI

### 音乐同步回调演示

此演示展示一般如何使用音乐回调。节拍和小节通知从音乐节拍和拍号信息中生成。

### 音乐播放列表回调演示

此示例强制随机播放列表按顺序选择下一项目。播放列表项目也可通过回调来阻止。

### MIDI 回调演示

展示在回调期间游戏可收到的 MIDI 消息。MIDI 消息包括 MIDI 音符、CC 值、弯音、触后和程序变化。

有产在音乐回调的更多信息，请参阅 [集成详情——音乐回调](soundengine_music_callbacks.html) 。

### Interactive Music Demo

此示例使用音乐切换容器。尝试切换 State，方法是触发在演示页面中所列的 Event。切换状态可能产生立即结果，或者在音乐容器规则中指定的时间发生状态切换。

### MIDI API Demo

本例展示了如何使用 MIDI API。按下 **Start Metronome** 按钮，以模拟生效的节拍器。然后，选择 **BPM** 滑杆并按下 LEFT 或 RIGHT，以更改该值。该演示将使用注册的回调函数，并通过 `PostMIDIOnEvent` 函数将 MIDI Event 发布至声音引擎。

### Background Music Demo

本例展示了 Xbox One 和 PS4 相关 DVR 法律要求的应对措施。由于很多游戏中的音乐都受版权保护，所以一般不允许使用内置 DVR 进行录制。此演示展示了使用和不使用 DVR 录制的声音之间的差异。请参阅 Wwise Project 并检查 *BGMDemo* 文件夹中的声音设置，同时注意其通路及所用 Audio Device。Non-Recordable 声音将被发送到输出至 *DVR\_Bypass* 输出的总线。

参见
:   - [集成二路输出](integrating_secondary_outputs.html)

## 定位

这些演示展示了如何在 Wwise 中以各种方式进行 3D 定位。

在进入页面时，即开始播放直升机声。使用以下按键沿 X 和 Z 方向移动 o（屏幕平面）：

- 右摇杆
- 方向键： 试听声音随方位变化的效果。将在屏幕左下角显示坐标轴。

### 位置演示

此演示仅设有一个位置。

### 多位置演示

此演示设有两个位置。

### 3D Bus: Clustering/3D Submix

此演示展示了仅用在总线层级结构中的定位。在 Position + Orientation 3D Spatialization 和 Attenuation 仅应用于总线时，声音引擎在 3 个子声音混合在一起后才会应用空间化。

### 3D Bus: 3D Portal and Standard Room

此演示展示了可移动发声体和听者之间的交互作用。在 Room 内设有 Portal 时，清晰展示了：

- 辅助总线如何模拟内有听者的空间；
- 3D 总线链 (Room1 -> Wet\_Path\_3D) 如何模拟听者在其外的空间。

The 3D bus applies a reverb Effect, after which the output is positioned and spatialized before being mixed in the Main Audio Bus.

### 3D Bus: 2X 3D Portal

此演示展示在设有 Portal 的两个不同 Room 内，可移动发声体和听者之间的交互作用。根据游戏对象的位置，当 Room 离发声体够近时发声体输出声音将会激活该 Room 的声学效果。

The 3D bus applies a reverb Effect, after which the output is positioned and spatialized before being mixed in the Main Audio Bus.

## Spatial Audio

These demos show various ways to use Spatial Audio to model sound propagation across Rooms, Portals, and Geometry.

Each demo page includes a movable emitter and a movable listener. You can offset the listener from a Distance Probe to simulate a third-person listening experience.

参见
:   - [Spatial Audio](spatial_audio.html)

### Portal Demo

This demo shows the effect of Portals in Spatial Audio positioning. There are two Rooms with Portals and visible sound propagation paths. The resulting diffraction and transmission amounts are displayed in the lower-left corner. Same-room obstruction (emitter-listener and portal-listener) is calculated through a combination of Portal-driven propagation and a native game-side obstruction algorithm. Game object spread is calculated for the emitter with its set radial value. Finally, this demo shows how to use a Room to play multi-channel ambient sounds / room tones that contract and become point sources at portals.

参见
:   - [使用房间和门户](using_rooms_and_portals.html)

### Portal and Geometry Demo

This demo shows the effect of Portals in conjunction with the Spatial Audio Geometry API. There are two Rooms with Portals, Geometry for the wall inside and outside of the Room, an obstacle and visible sound propagation paths. The resulting diffraction and transmission amounts are displayed in the lower-left corner. Spatial Audio is set up so that diffraction/transmission controls both the project-wide curves and the built-in parameters, although only the former is used in the Wwise project. Spatial Audio handles diffraction and transmission using Portals and Geometry respectively. The demo does not compute additional obstruction and occlusion.

### Geometry Demo

This demo showcases the Wwise Spatial Audio Geometry API, usable for direct (dry) path diffraction and transmission. There are two walls and visible diffraction paths. The resulting diffraction and transmission amounts are displayed in the lower-left corner. Spatial Audio is set up so that diffraction/transmission controls both the project-wide curves and the built-in parameters, although only the former is used in the project.

参见
:   - [使用 Geometry API 模拟衍射和透射](spatial_audio_apigeometry_diffract.html)

### Reflect Demo

This demo showcases the Wwise Reflect plug-in using the Geometry API to simulate early reflection. There is a room and a separate wall, defined by Spatial Audio Geometry, and visible reflection paths. Spatial Audio is set up with a reflection order displayed in the lower-left corner. Additionally, Spatial Audio allows reflection paths to diffract. The room Geometry in this demo can change texture and be scaled in size demonstrating the adaptability of the Geometry API.

参见
:   - [使用 Geometry API 模拟早期反射](spatial_audio_apigeometry_er.html)
    - [早期反射的几何衍射](spatial_audio_apigeometry_diffract.html#spatial_audio_apigeometry_diffract_er)

### Portal and Reflect Demo

This demo showcases the Reflect plug-in within the context of Rooms and Portals. There are five Rooms, connected by Portals that can be toggled open or closed, some additional walls defined by Spatial Audio Geometry, and visible reflection paths.

### Reverb Zone Demo

This demo demonstrates the use of a Reverb Zone to create a space that has its own reverb effect and transitions into the outside Room without the use of Portals. There is a Room with a Portal that connects to a Reverb Zone, forming something like a covered balcony. The Reverb Zone's parent is the outdoor Room. There is also Geometry outside to show how paths can diffract around geometry, pass through the transparent surfaces of the Reverb Zone, and then continue through portals.

参见
:   - [使用 Reverb Zone](spatial_audio_roomsportals_reverbzones.html)

## Bank & Event Loading

### Prepare Event/Bank Demo

This page shows how to use the PrepareBank and PrepareEvent API functions.

When the page is loaded, a PrepareBank operation loads the lightweight structure and event data referenced by this demo, without loading any actual media into memory. When the user moves the cursor to an area button, a PrepareEvent operation loads the corresponding media file (a .wem file on disk) into memory in anticipation of a future PostEvent. When the user finally enters the area, the event is posted and the media is ready to play.

### External Sources Demo

此演示展示如何使用外部源。两个按钮播放同一声音结构，但在运行时使用源“1”、“2”和“3”或源“4”、“5”和“6”设置。

参见
:   - [集成 External Source](integrating_external_sources.html)

另外，外部源在文件包装程序中打包，并在打开演示页面时加载。See [Managing file packages](https://www.audiokinetic.com/library/edge/?source=Help&id=managing_file_packages) for more information on the File Packager, and [流播放/流管理器](streamingdevicemanager.html) for more details on the runtime aspect of file packages.

### Autobanks Demo

This demo demonstrates the pros and cons of automatic event bank generation. When this option is selected in the Project Settings, Wwise generates individual banks for any events that are not contained in manually created banks. However, these auto-banks do not contain any media, only structure and event data. To load media associated with these events, the game must call either [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) or [AK::SoundEngine::SetMedia](namespace_a_k_1_1_sound_engine_ae93bba30404755a4d2e592c3bfbf340c.html#ae93bba30404755a4d2e592c3bfbf340c).

## Microphone/AudioInput Demo

此演示展示如何记录来自话筒的音频以及在 Wwise 声音引擎中输入该音频。在 Integration Demo 中，选择 **Microphone Demo** 并对着话筒讲话，以试听从 Wwise 声音引擎播放出来的声音效果。切换 **Enable Delay** 以试听如何像 Wwise 中创建的其他声音一样处理被馈送到 Audio Input 插件的音频数据。

每个平台用来访问话筒的核心 API 大不相同。检查 Integration Demo 代码中的 `SoundInput` 和 `SoundInputMgr` 类以查看它们如何与 AudioInput 插件互动。

|  |  |
| --- | --- |
|  | **备注:** This demo is available on the following platforms: Windows, macOS, iOS, and tvOS. |

参见
:   - [音频输入源插件](referencematerial_audioinput.html).

## Motion Demo

这是多人游戏演示，展示如何将 Wwise 的振动引擎集成到游戏中。

在此演示中，每个玩家可选择是关闭房门还是使用他们手中所持的枪支开枪。靠近门这个游戏对象的每个玩家和玩家自己的枪支都设有听者。通过这种方法，当任何玩家关门时，所有玩家都会收到强制反馈反应。然而，只有开枪的玩家才会收到该事件的强制反馈。另外，在 PS4 和 PS5 上，将只在各个玩家对应的手柄扬声器中播放枪声。

|  |  |
| --- | --- |
|  | **备注:** 在 Windows 上，对于使用键盘的玩家，应插入手柄来参与此演示。 |

此代码展示了如何使用二路输出、Wwise Motion 以及 Listener/Emitter 管理。

参见
:   - [集成二路输出](integrating_secondary_outputs.html)
    - [集成 Wwise Motion](integrating_elements_motion.html)
    - [集成 Listener](soundengine_listeners.html)

## GME Demo

To use the GME Demo pages, install GME In-Game Voice Chat, generate soundbanks and recompile Integration Demo. Refer to the [GME documentation](https://www.audiokinetic.com/library/gme/?source=TencentGME&id=gme_integration_demo) for more information.

## Options 页面

此页面允许查看声音引擎的多项初始化设置。除此之外，您还可以为整个应用程序选择音频输出。示例代码将展示如何初始化和终止声音引擎，以及如何选择不同的物理音频输出。有关声音引擎初始化的更多详细信息，请参阅下面的对应章节。

参见
:   - [AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f)
    - [AkInitSettings](struct_ak_init_settings.html)
    - [AkPlatformInitSettings](struct_ak_platform_init_settings.html)
    - [AkMemSettings](struct_ak_mem_settings.html)
    - [AkCommSettings](struct_ak_comm_settings.html)
    - [集成二路输出](integrating_secondary_outputs.html)

# 更多例程

Integration Demo 及其 Wwise 工程做得非常简洁，其目的是演示声音引擎集成的基础知识。有关更加逼真的集成工程，请参阅 [AkCube 声音引擎集成工程示例](samplecode.html#samplecode_integration_akcube) 。