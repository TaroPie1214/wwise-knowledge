# Debugging Tips

|  |
| --- |
| Wwise Unreal Integration Documentation |

Debugging Tips

This topic contains tips and recommendations to help you debug your Wwise Unreal Integration projects.

# Logging

Integration 中的每个模块都有独立的详细级别。Log, Warning, and Error messages appear when something is wrong in most cases. If an error occurs, you can find which module produced the error and set the verbosity of that module's logs to **Verbose** or **VeryVerbose** to better understand why the error occurred. For example, **Verbose** or **VeryVerbose** can be helpful to diagnose asset loading and packaging problems.

您可以在 `DefaultEngine.ini` 文件的 `Core.Log` 部分更改各个模块的详细级别。A special logging category called `LogWwiseHints` is enabled by default across all modules, which warns about using deprecated functions and other bad habits.

以下为可能的详细级别：

- **Fatal**: Causes a crash when program execution cannot or should not continue, such as if required plug-in modules are not loaded.
- **Error**：在音频无法正常运行时阻止对游戏进行打包。
- **Warning**：指示非关键功能可能具有无法预测的行为。在必要时，还可阻止打包。
- **Display**：记录有关模块初始化的信息并提供 Commandlet 信息。
- **Log**：记录各种重要操作。
- **Verbose**：记录模块执行的所有操作。
- **VeryVerbose**：记录模块执行的每一步操作。

在以下示例中，可看到与各个模块关联的详细级别：

[Core.Log]

LogAkAudio=Verbose

LogAudiokineticTools=Log

LogWwiseAudioLink=Verbose

LogWwiseConcurrency=Verbose

LogWwiseFileHandler=Verbose

LogWwiseHints=Warning

LogWwiseResourceLoader=Warning

LogWwiseResourceCooker=Log

LogWwiseProjectDatabase=Log

LogWwiseSimpleExtSrc=Error

For more information about setting log verbosity and verbosity levels, see [Logging in Unreal](https://dev.epicgames.com/documentation/unreal-engine/logging-in-unreal-engine) and [ELogVerbosity::Type](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Core/ELogVerbosity__Type).

# Stats

If you have issues with memory usage and performance, you can use the Stats in the low-level Wwise constructs to troubleshoot. Use the Unreal Frontend to start a profiling session, or use the Stats menu to enable real-time visualization of the available statistics. For example, the WwiseFileHandler stats have information about all currently loaded assets.

The Integration includes the following Stats:

- **AkAudioDevice**：记录有关 Post Event Async 调用的信息。
- **AkSoundBankGenerationSource**：记录与 SoundBank 生成相关的 WAAPI 调用。
- **WwiseConcurrency**: Logs information about memory used to manage multi-threading.
- **WwiseFileHandler**：记录有关所加载媒体、SoundBank 和外部源的信息。
- **WwiseFileHandlerLowLevelIO**：记录有关流播放声音的信息。
- **WwiseMemory**: Logs information about memory usage.
- **WwiseObstructionOcclusion**: Logs information about obstruction and occlusion calculations.
- **WwiseProjectDatabase**: Logs information about memory used by the WwiseProjectDatabase module.
- **WwiseResourceLoader**：记录有关被引用 AkType 的信息。
- **WwiseSoundEngine**：记录有关 API 调用的信息。

若要访问这些信息，请在 Unreal 的 Viewport Options 中选择感兴趣的 Stats。

![](../../../images/DebugStat.png)

For more information about Stats, see [Stat Commands](https://dev.epicgames.com/documentation/unreal-engine/stat-commands-in-unreal-engine).

# GeneratedSoundBanks Folder

GeneratedSoundBanks 文件夹的路径通常与工程根目录相对。When using the editor with the `-Game` option, you might need to set the working directory to the same folder as the root that contains your `.uproject` file.