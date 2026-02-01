# 有关 iOS 的特定信息

|  |
| --- |
| Wwise Unreal Integration Documentation |

有关 iOS 的特定信息

此页面列出了在开发者针对 iOS 使用 Unreal Integration 构建应用程序时的相关要求及特别注意事项。

# 通过 Windows 远程构建

You can build projects for iOS from a Windows system with remote build options. For more information, see [iOS for Windows Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-on-ios-projects-using-a-windows-machine-in-unreal-engine). 不过需要进行额外的一些配置，因为并非所有文件都会默认复制到远程 macOS 系统。

为了确保这种构建方式能够正常工作，必须创建 `RsyncProject.txt` 文件，来强制 Unreal 复制 `/Build/Rsync/` 路径下的文件。该文件须包含以下代码行：

+ /Plugins/Wwise/ThirdParty/include/\*\*

+ /Plugins/Wwise/ThirdParty/iOS/\*\*

# 使用 Unreal 音频

若在 iOS 上结合 Wwise 使用内置 Unreal 音频，可能会遇到错误并导致游戏发生崩溃或无法予以加载。If that happens, you must either disable Unreal audio or use [Combining Unreal and Wwise Audio with AudioLink](using_audio_link.html).

若要禁用 Unreal 音频，请确保选中 **Enable Wwise SoundEngine only** 音频通路选项（详请参见 [Selecting Audio Routing Options](using_audio_link.html#using_audio_link_enabling) 章节）。