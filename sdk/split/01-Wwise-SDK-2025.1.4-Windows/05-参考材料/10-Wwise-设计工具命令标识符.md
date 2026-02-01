# Wwise 设计工具命令标识符

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise 设计工具命令标识符

| 名称 | 说明 | 参数 |
| --- | --- | --- |
| ActivateNextFloatingView | 激活下一浮动视图。 |  |
| ActivatePreviousFloatingView | 激活上一浮动视图。 |  |
| AddFolderToDatabase | Add the content of the folder to the Media Pool Database | **objects** - an array of exactly 1 object, which represent the Media Pool Database |
| AddMediaPoolAudioDescriptionFilter | Add a Audio Description Filter to Media Pool | **value** - the text (string) to be used for the description |
| AddMediaPoolAudioSimilarityFilter | Add a Audio Similarity Filter to Media Pool | **files** - an array of audio files. The files must present in the Media Pool. |
| AddMediaPoolFieldFilter | Add a Field Filter to Media Pool | **value** - the name (string) of the field to search on |
| CheckProjectFiles | 在磁盘上扫描发生了更改的 Project 和 Work Unit 文件。 |  |
| CloseCurrentObjectTab | 关闭当前对象选项卡。 |  |
| CloseObjectTabsToTheRight | 关闭右侧对象选项卡。 |  |
| CloseOtherObjectTabs | 关闭其他对象选项卡。 |  |
| CloseProject | 关闭工程。 |  |
| CloseView | 关闭活跃视图。 |  |
| Convert | 针对给定对象显示 Convert 对话框。 | **objects** – 此数组中包含一系列对象。 |
| ConvertAllPlatform | 针对所有平台对给定对象进行转换。 | **objects** – 此数组中包含一系列对象。 |
| ConvertCurrentPlatform | 针对给定平台对给定对象进行转换。若未指定，则使用当前平台或当前选定对象。 | **objects** – 此数组中包含一系列对象。  **platforms** – 此数组中包含一系列平台（一组 GUID 字符串）。 |
| ConvertSFXToVoice | 将给定对象转换为 Sound Voice 对象。 | **objects** – 此数组中包含一系列对象。 |
| ConvertToSoundSFX | 将给定对象转换为 Sound SFX 对象。 | **objects** – 此数组中包含一系列对象。 |
| CopyFilenamesToClipboard | Copies the filename of the specified objects or files to clipboard. | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| CopyGUIDsPathsToClipboard | 将给定对象的唯一 ID (GUID) 复制到剪贴板。 | **objects** – 此数组中包含一系列对象。 |
| CopyPathsToClipboard | 将给定对象的 Wwise 工程路径复制到剪贴板。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| CopyShortIDsToClipboard | 将给定对象的 Short ID（32 位无符号整数）复制到剪贴板。 | **objects** – 此数组中包含一系列对象。 |
| CopyWAQLToClipboard | 针对给定对象路径生成 WAQL 查询并将其复制到剪贴板。 | **objects** – 此数组中包含一系列对象。 |
| CreateInGAC | 针对给定对象使用 Game Audio Connect 创建关联的 Nuendo 对象。 | **objects** – 此数组中包含一系列对象。 |
| CreateMediaPoolDatabaseFromFolder | Creates a new Media Pool Database from a folder | **objects** - an array of objects with a single object that will be the parent of the newly created Media Pool database |
| CreateNewSoundbank | 创建新的 SoundBank。 |  |
| DetachCurrentObjectTab | 解绑当前对象选项卡。 |  |
| DuplicateCurrentObjectTab | 复制当前对象选项卡。 |  |
| EditUserPreferences | 显示 User Preferences 对话框以便进行编辑。 |  |
| ExcludeAllMediaPoolDatabaseId | Exclude All Media Pool Databases. | **objects** - an array objects, which represent the Media Pool Databases |
| ExpandCollapsePropertyEditorLeftInObjectTab | Expand or Collapse the Property Editor on the left side bar of the latest object tab. |  |
| ExpandCollapsePropertyEditorRightInObjectTab | Expand or Collapse the Property Editor on the right side bar of the latest object tab. |  |
| FindInProjectExplorerNewPinnedView | 在 Project Explorer 中查找给定对象 (New Pinned View)。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerNoSyncGroup | 在 Project Explorer 中查找给定对象 (No Sync Group)。已弃用（参见 FindInProjectExplorerNewPinnedView）。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSelectionChannel1 | 在 Project Explorer 中查找给定对象 (Selection Channel 1)。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSelectionChannel2 | 在 Project Explorer 中查找给定对象 (Selection Channel 2)。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSelectionChannel3 | 在 Project Explorer 中查找给定对象 (Selection Channel 3)。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSelectionChannel4 | 在 Project Explorer 中查找给定对象 (Selection Channel 4)。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSyncGroup1 | 在 Project Explorer 中查找给定对象 (Sync Group 1)。已弃用（参见 FindInProjectExplorerSelectionChannel1）。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSyncGroup2 | 在 Project Explorer 中查找给定对象 (Sync Group 2)。已弃用（参见 FindInProjectExplorerSelectionChannel2）。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSyncGroup3 | 在 Project Explorer 中查找给定对象 (Sync Group 3)。已弃用（参见 FindInProjectExplorerSelectionChannel3）。 | **objects** – 此数组中包含一系列对象。 |
| FindInProjectExplorerSyncGroup4 | 在 Project Explorer 中查找给定对象 (Sync Group 4)。已弃用（参见 FindInProjectExplorerSelectionChannel4）。 | **objects** – 此数组中包含一系列对象。 |
| FindSimilarInMediaPool | Adds a find similar filter using the selected sound | **objects** - an array of objects containing 1 sound. |
| FocusNext | 聚焦当前视图中的下一控件。 |  |
| FocusPrevious | 聚焦当前视图中的上一控件。 |  |
| ForceReloadProject | Reloads the current Wwise project and force the loading of its work units. |  |
| ForceSaveProject | 将所有 Work Unit 设为未同步状态并保存工程。 |  |
| GenerateAllSoundbanksAllPlatforms | 针对所有平台生成所有 SoundBank。 |  |
| GenerateAllSoundbanksAllPlatformsAutoClose | 针对所有平台生成所有 SoundBank（在操作完成时自动关闭进度对话框）。 |  |
| GenerateAllSoundbanksCurrentPlatform | 针对给定平台生成所有 SoundBank。若未指定，则使用当前平台。 | **platforms** – 此数组中包含一系列平台（一组 GUID 字符串）。 |
| GenerateAllSoundbanksCurrentPlatformAutoClose | 针对给定平台生成所有 SoundBank。若未指定，则使用当前平台（在操作完成时自动关闭进度对话框）。 | **platforms** – 此数组中包含一系列平台（一组 GUID 字符串）。 |
| GenerateSelectedSoundbanksAllPlatforms | 针对所有平台生成给定 SoundBank 对象。 | **objects** – 此数组中包含一系列对象。 |
| GenerateSelectedSoundbanksAllPlatformsAutoClose | 针对所有平台生成给定 SoundBank 对象（在操作完成时自动关闭进度对话框）。 | **objects** – 此数组中包含一系列对象。 |
| GenerateSelectedSoundbanksCurrentPlatform | 针对给定平台生成给定 SoundBank 对象。若未指定，则使用当前平台或当前选定对象。 | **objects** – 此数组中包含一系列对象。  **platforms** – 此数组中包含一系列平台（一组 GUID 字符串）。 |
| GenerateSelectedSoundbanksCurrentPlatformAutoClose | 针对给定平台生成给定 SoundBank 对象。若未指定，则使用当前平台或当前选定对象（在操作完成时自动关闭进度对话框）。 | **objects** – 此数组中包含一系列对象。  **platforms** – 此数组中包含一系列平台（一组 GUID 字符串）。 |
| GenerateSoundbanksWithCurrentSettings | 使用当前 SoundBank Manager 设置生成 SoundBank（在操作完成时自动关闭进度对话框）。 |  |
| Help | 显示 Wwise Help。 |  |
| IncludeAllMediaPoolDatabaseId | Include All Media Pool Databases. | **objects** - an array object, which represent the Media Pool Databases |
| IncludeSelectedOnlyMediaPoolDatabaseId | Include only selected Media Pool Databases. | **objects** - an array objects, which represent the Media Pool Databases or Virtual Folders |
| Inspect | 检视给定对象。 | **objects** – 此数组中包含一系列对象。 |
| InspectNext | 检视下一被检视对象。 |  |
| InspectParent | 检视当前被检视对象的父对象。 |  |
| InspectPrevious | 检视上一被检视对象。 |  |
| KeepOpenCurrentObjectTab | 保持打开当前对象选项卡。 |  |
| LoadCaptureSession | Load the profiling session. |  |
| LoadPreset | 针对活跃视图显示 Load Preset 对话框。 |  |
| LoadThemeClassic | 加载 Classic 主题。 |  |
| LoadThemeDark | 加载 Dark 主题。 |  |
| LoadThemeLight | 加载 Light 主题。 |  |
| LoadUnloadedWorkUnits | 加载当前卸载的 Work Unit。 |  |
| MaximizeView | 将活跃视图最大化。 |  |
| MinimizeView | 将活跃视图最小化。 |  |
| MoveCurrentObjectTabToTheLeft | 向左移动当前选项卡。 |  |
| MoveCurrentObjectTabToTheRight | 向右移动当前选项卡。 |  |
| Mute | Mute 给定对象。若未指定任何对象，则 Mute 当前选定项。 | **value** – true 或 false：设置 Mute 状态。若未指定，则切换 Mute 状态。  **objects** – 此数组中包含一系列对象。 |
| NewProject | 显示 New Project 对话框。 |  |
| NextObjectTab | 转到下一对象选项卡。 |  |
| NextPerfFrame | 在 Performance Graph 中转到下一音频帧。 |  |
| OpenContainingFolderSoundbank | 打开 Windows Explorer 窗口并转到给定对象的 SoundBank 文件所在的文件夹。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenContainingFolderWAV | 打开 Windows Explorer 窗口并转到给定对象的 wav 文件所在的文件夹。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenContainingFolderWorkUnit | 打开 Windows Explorer 窗口并转到给定对象的 Work Unit 所在的文件夹。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenInExternalEditor | 在第一个 External Editor（索引 0）中打开给定对象。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenInExternalEditor1 | 在第二个 External Editor（索引 1）中打开给定对象。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenInExternalEditor2 | 在第三个 External Editor（索引 2）中打开给定对象。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenInExternalEditor3 | 在第四个 External Editor（索引 3）中打开给定对象。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenInExternalEditor4 | 在第五个 External Editor（索引 4）中打开给定对象。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenInGAC | 使用 Game Audio Connect 在 Nuendo 中打开给定对象。 | **objects** – 此数组中包含一系列对象。 |
| OpenInNewTab | 检视给定对象。 | **objects** – 此数组中包含一系列对象。 |
| OpenInNewWindow | 在新窗口中检视给定对象。 | **objects** – 此数组中包含一系列对象。 |
| OpenInWwiseWaveViewer | 在 Wwise Wave Viewer 中打开给定对象。 | **objects** – 此数组中包含一系列对象。  **files** - an array of files |
| OpenProject | 显示 Open Project 对话框。 |  |
| OpenPropertyEditorFavorites | Open the Property Editor Favorites |  |
| OpenRecycled | Open the object in recycled mode. | **objects** – 此数组中包含一系列对象。 |
| PinView | 锁定活跃视图。 |  |
| PopoutObjectTabPrimaryView | Popup the current primary editor as a floating view. |  |
| PopoutObjectTabSecondaryView | Popup the current secondary editor as a floating view. |  |
| PreviousObjectTab | 转到上一对象选项卡。 |  |
| PreviousPerfFrame | 在 Performance Graph 中转到上一音频帧。 |  |
| ProfilerFilterClearAll | 清理所有筛选器。 |  |
| ProfilerFilterClearCurrentView | 清理当前视图的性能分析器筛选器。 |  |
| ProfilerFilterExcludeObjectNameFromCurrent | 将选定对象的名称作为排除项添加到当前视图的筛选器文本中。 |  |
| ProfilerFilterPromoteCurrentToAll | 将当前视图的性能分析器筛选器复制到所有其他筛选器。 |  |
| ProfilerFilterSetNameToCurrent | 将选定对象的名称设为当前视图的筛选器文本。 |  |
| ProfilerFilterSetPipelineID | 设置性能分析器文本筛选器以与特定 Pipeline ID 匹配。 |  |
| ProfilerFilterSetSelectedObjectToCurrent | 在当前视图的性能分析器筛选器中设置当前选定对象。 |  |
| ProfilerFilterToggleCurrentMuteSolo | 在当前视图中打开/关闭 Mute/Solo 筛选器。 |  |
| ProfilerFilterToggleCurrentShowNothingWhenEmpty | 在筛选器为空时打开/关闭 Show Nothing。 |  |
| ProfilerFilterToggleLocalGlobal | 在 Link 和 Unlink 模式之间切换当前视图的性能分析器筛选器。 |  |
| Redo | 重做上一撤消的操作。 |  |
| ReloadCommandAddons | 重新加载所有对应目录中的所有自定义命令文件。 |  |
| ReloadCurrentTheme | 从磁盘重新加载当前 UI 主题。这样方便应用新的主题。 |  |
| RescanSelectedDatabases | Rescans the Media Pool Databases | **objects** - an array of objects, which represent the selected Media Pool Databases |
| ResetAllMutes | 重置当前活跃的所有 Mute。 |  |
| ResetAllSolos | 重置当前活跃的所有 Solo。 |  |
| RestoreView | 还原活跃视图。 |  |
| SaveAllCounters | 将 Performance Counter 转储到文件中。 |  |
| SaveCaptureSession | Saves the profiling session. |  |
| SavePreset | 针对活跃视图显示 Load Preset 对话框。 |  |
| SaveProject | 保存工程。 |  |
| Search | 将焦点放在搜索框上。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchCommands | 将焦点放在搜索框上，并启用命令搜索模式。 |  |
| SearchInCtrl | 在当前活跃控件中打开搜索框。 |  |
| SearchInCurrentView | 在 Current View 中搜索（如有“搜索”字段）。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInProjectExplorer | 在 Project Explorer 中搜索（第一个可用视图）。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInProjectExplorerNewPinnedView | 在 Project Explorer 中搜索 (New Pinned View)。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInProjectExplorerSelectionChannel1 | 在 Project Explorer 中搜索 (Selection Channel 1)。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInProjectExplorerSelectionChannel2 | 在 Project Explorer 中搜索 (Selection Channel 2)。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInProjectExplorerSelectionChannel3 | 在 Project Explorer 中搜索 (Selection Channel 3)。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInProjectExplorerSelectionChannel4 | 在 Project Explorer 中搜索 (Selection Channel 4)。 | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SearchInPropertyEditor | Searches for property names or values in the Property Editor. | **value** –“搜索”字段所要使用的文本（字符串）。 |
| SelectOnlineDocumentation | 选择 CHM 作为文档来源。 |  |
| SetColor | 针对特定对象显示 Color Picker 对话框。 | **objects** – 此数组中包含一系列对象。 |
| SetPropertySheetSplitModeColumn | 将属性表分隔模式设为 Column split。 |  |
| SetPropertySheetSplitModeNo | 将属性表分隔模式设为 No split。 |  |
| SetPropertySheetSplitModeRow | 将属性表分隔模式设为 Row split。 |  |
| ShowAudioFileCacheClearDialog | 显示 Clear Audio File Cache 对话框。 |  |
| ShowAudioFileImporter | 显示 Audio File Importer 对话框。 | **objects** - an array of zero or one object to specify the import target  **files** - an array of file to import |
| ShowAudioFileRegionImporter | Shows the Audio File Importer dialog but expect regions in files. | **objects** - an array of zero or one object to specify the import target  **files** - an array of regions to import |
| ShowAudioFilesConversionDialog | 显示 Audio File Conversion 对话框。 |  |
| ShowAudioPreferences | 显示 Audio Preferences 对话框。 |  |
| ShowBatchRename | 打开 Batch Rename View 并显示给定对象。 | **objects** – 此数组中包含一系列对象。 |
| ShowBugReport | 显示 Bug Report 页面。 |  |
| ShowContactAK | 显示 [AK](namespace_a_k.html "Definition of data structures for AkAudioObject") 的“联系我们”页面。 |  |
| ShowContextualHelp | 针对给定属性显示 Contextual Help View 视图。 | **property** – 指向单个 CProp 对象。 |
| ShowControlSurfacesDlg | 显示 Control Surfaces Settings 对话框。 |  |
| ShowDefaultObjectValues | 显示 Default Object Values 对话框。 |  |
| ShowDetails | 打开 Details 视图并显示给定对象。 | **objects** – 此数组中包含一系列对象。 |
| ShowEULA | Shows the End-User License Agreement for Wwise. |  |
| ShowFileManager | 显示 File Manager 对话框。 |  |
| ShowGACSettings | 显示 Nuendo Game Audio Connect 设置。 |  |
| ShowGameObjectsVoiceExplorer | 将 Voice Explorer 聚焦在给定游戏对象上。 | **gameObjectIds** – 所要显示/选择的游戏对象的 ID。 |
| ShowKeyboardShortcuts | 显示 Keyboard Shortcuts 对话框。 |  |
| ShowLanguages | 显示 Language Manager 对话框。 |  |
| ShowLegalNotices | 显示 Legal Notices 对话框。 |  |
| ShowLicenseMgr | 显示 License Manager 对话框。 |  |
| ShowListView | 针对给定对象显示 List View。 | **objects** – 此数组中包含一系列对象。  **value** –“搜索”字段所要使用的文本（字符串）。 |
| ShowMediaPool | Shows the Show Media Pool view. |  |
| ShowMediaPoolDatabaseSettings | Shows the Show Media Pool Database Settings. | **objects** - an array of exactly 1 object, which represent the Media Pool Database |
| ShowMediaPoolFieldsDlg | Shows the Show Media Pool Fields dialog. |  |
| ShowMultiEditor | 针对给定对象显示 Multi Editor 视图。 | **objects** – 此数组中包含一系列对象。 |
| ShowObstructionOcclusionSettings | 针对 Obstruction/Occlusion 选项卡显示 Project Settings 对话框。 |  |
| ShowPasteProperties | 针对给定对象显示 Paste Properties 视图。 | **objects** – 此数组中包含一系列对象。 |
| ShowPlatformManager | 显示 Platform Manager 对话框。 |  |
| ShowProfilerSettings | 显示 Profiler Settings 对话框。 |  |
| ShowProjectSettings | 显示 Project Settings 对话框。 |  |
| ShowPropertyHelp | 针对给定属性显示 Property Help 视图。已弃用（参见 ShowContextualHelp）。 | **property** – 指向单个 CProp 对象。 |
| ShowReferenceView | 打开 Reference View 并显示给定对象。 | **objects** – 此数组中包含一系列对象。 |
| ShowRemoteConnections | 显示 Remote Connections 对话框。 |  |
| ShowSchematicView | 针对给定对象显示 Schematic View。 | **value** –“搜索”字段所要使用的文本（字符串）。  **objects** – 此数组中包含一系列对象。 |
| ShowSoundBankDefinitionImporter | 显示 Sound Bank Deficition Importer 对话框。 |  |
| ShowSoundbankSettings | 显示 Project Settings 对话框的 SoundBanks 选项卡。 |  |
| ShowSourceEditor | 针对给定对象显示 Source Editor。 | **objects** – 此数组中包含一系列对象。 |
| ShowSplashScreen | 打开初始 Wwise 加载视图并显示当前软件版本。 |  |
| ShowUserPreferences | 显示 User Preferences 对话框。 |  |
| ShowUserProjectSettings | 已弃用（参见 ShowDefaultObjectValues）。 |  |
| ShowUserSoundbankSettings | 显示 SoundBank Settings 对话框。 |  |
| ShowViewSettings | 针对活跃视图显示视图设置。 |  |
| ShowVoiceAssetsImporter | 显示 Voice Asset Importer 对话框。 |  |
| ShowVoiceInspector | 针对给定对象显示 Voice Inspector。 | **objects** – 此数组中包含一系列对象。  **voices** – 此数组中包含一系列声部管线 ID。 |
| ShowVoicesVoiceExplorer | 将 Voice Explorer 聚焦在给定声部上。 | **voiceIds** – 所要显示/选择的声部的 ID。 |
| ShowWwiseHelp | 显示 Wwise Help。 |  |
| ShowWwiseKnowledgeBase | 显示 Wwise Community Q&A。 |  |
| ShowWwiseSDKDocumentation | 显示 Wwise SDK 文档。 |  |
| Solo | Solo 给定对象。若未指定任何对象，则 Solo 当前选定项。 | **value** – true 或 false：设置 Solo 状态。若未指定，则切换 Solo 状态。  **objects** – 此数组中包含一系列对象。 |
| SourceControlAddWAV | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 wav 文件调用 Add 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlAddWWU | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 Work Unit 调用 Add 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlCheckoutWAV | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 wav 文件调用 Checkout 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlCheckoutWWU | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 Work Unit 调用 Checkout 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlCommitWAV | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 wav 文件调用 Commit 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlCommitWWU | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 Work Unit 调用 Commit/Submit 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlDiffWAV | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 wav 文件调用 Diff 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlDiffWWU | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 Work Unit 调用 Diff 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlRefreshIcons | 针对 Work Unit 刷新工程状态和 Source Control 图标。 |  |
| SourceControlRevertWAV | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 wav 文件调用 Revert 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlRevertWWU | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 Work Unit 调用 Revert 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlUpdateWAV | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 wav 文件调用 Update 命令。 | **objects** – 此数组中包含一系列对象。 |
| SourceControlUpdateWWU | 在 Source Control 插件（Perforce、SVN 等）上针对与给定对象关联的 Work Unit 调用 Update 命令。 | **objects** – 此数组中包含一系列对象。 |
| SplitCurrentTabToTheRight | 分隔当前选项卡（在右侧创建新的选项卡面板）。 |  |
| StartCapture | 开始捕获性能分析数据。若已经开始，则不执行任何操作。 |  |
| StartStopCapture | 开始捕获性能分析数据。若已经开始，则停止捕获。 |  |
| StopCapture | 停止捕获性能分析数据。若已经停止，则不执行任何操作。 |  |
| ToggleExpandCollapse | Toggles Expand/Collapse for the active floating view. |  |
| ToggleFollowCapture | 切换工具栏中的 Show Live Data 按钮。 |  |
| ToggleFollowObjectSelectionInProjectExplorer | Toggles the automatic following of object selection in Project Explorer. |  |
| ToggleMaximizeObjectTabPrimaryView | 将对象选项卡的当前默认视图最小化。 |  |
| ToggleMaximizeObjectTabSecondaryView | 将对象选项卡的当前默认视图最大化。 |  |
| ToggleOpenNewTabOnDoubleClick | Toggles the opening of a new object tab when double-clicking an object. |  |
| TransportDisableMonitor | 禁用 Transport Control 中的 Inclusion 按钮。 |  |
| TransportDisableOriginal | 禁用 Transport Control 中的 Original 按钮。 |  |
| TransportDisplayRTPC | 切换 Transport Control 以显示 Game Parameter。 |  |
| TransportDisplayStates | 切换 Transport Control 以显示 State。 |  |
| TransportDisplaySwitches | 切换 Transport Control 以显示 Switch。 |  |
| TransportDisplayTriggers | 切换 Transport Control 以显示 Trigger。 |  |
| TransportEnableMonitor | 启用 Transport Control 中的 Inclusion 按钮。 |  |
| TransportEnableOriginal | 启用 Transport Control 中的 Original 按钮。 |  |
| TransportPause | 暂停播放 Transport Control 中当前在播的对象。 |  |
| TransportPin | 锁定或解锁 Transport Control 中当前加载的对象。 |  |
| TransportPinSelected | 将给定对象锁定到 Transport Control。若未指定任何对象，则锁定当前选定项。 |  |
| TransportPlayDirectly | 通过旁通影响声音的属性（如音量）来播放 Transport Control 中当前加载的对象。 |  |
| TransportPlayStop | 播放 Transport Control 中当前加载的对象。若已在播放，则停止播放。 |  |
| TransportReset | 重置 Transport Control 播放和内部状态。 |  |
| TransportToggleMonitor | 切换 Transport Control 中的 Inclusion 按钮。 |  |
| TransportToggleOriginal | 切换 Transport Control 中的 Original 按钮。 |  |
| Undo | 撤消队列中的最后一项操作。 |  |
| UseAudioOutputSystem5 | 选择 5.1 作为音频输出系统。 |  |
| UseAudioOutputSystem7 | 选择 7.1 作为音频输出系统。 |  |
| UseAudioOutputSystemDefault | 选择默认音频输出系统。 |  |
| UseAudioOutputSystemStereoHeadphones | 选择立体声耳机作为音频输出系统。 |  |
| UseAudioOutputSystemStereoSpeakers | 选择立体声扬声器作为音频输出系统。 |  |
| UseOnlineDocumentation | 选择 Wwise 官网作为文档来源。 |  |