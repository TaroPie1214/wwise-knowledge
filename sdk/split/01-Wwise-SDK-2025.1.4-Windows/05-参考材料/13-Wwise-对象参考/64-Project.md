# Project

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Project

- **Plugin ID**: 3
- **Class ID**: 196624

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AlwaysSaveMediaIDsFile** | Always persist the media IDs file on project save | bool | false | None | false | None | false |
| **AutoDetectFFTWindowSize** | Auto Detect FFT Window Size | int16 | 512 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 64 | 64 | | 128 | 128 | | 256 | 256 | | 512 | 512 | | 1024 | 1024 | | 2048 | 2048 | | true | None | false |
| **AutoDetectThresholdHigh** | Auto Detect Threshold High | Real64 | -50 | [ -96.3 , 0 ] | true | None | false |
| **AutoDetectThresholdLow** | Auto Detect Threshold Low | Real64 | -30 | [ -96.3 , 0 ] | true | None | false |
| **AutoDetectThresholdMedium** | Auto Detect Threshold Medium | Real64 | -40 | [ -96.3 , 0 ] | true | None | false |
| **AutoSoundBankAllEvents** | Auto SoundBank Generation - All Events | bool | false | None | false | None | false |
| **AutoSoundBankEnabled** | Enable Auto SoundBank Generation | bool | false | None | true | None | false |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **CommPortDiscoveryBroadcast** | Communication Port Discovery Broadcast | Uint16 | 24024 | [ 1 , 65535 ] | true | None | false |
| **CommPortDiscoveryResponse** | Communication Port Discovery Response | Uint16 | 0 | [ 0 , 65535 ] | true | None | false |
| **CommSerialPortBase** | Communication Serial Port Base | Uint16 | 8 | [ 0 , 12 ] | true | None | false |
| **CopyLooseStreamedMedia** | Copy Loose/Streamed Media Files | bool | true | None | true | None | false |
| **DSFEmphasis** | DSF Emphasis | Real64 | 0 | [ -1 , 1 ] | true | None | true |
| **DefaultLanguage** | Reference Language | string | English(US) | None | true | None | false |
| **EnvironmentalCurves** | Environmental Curves | Reference |  | **可能的类型：**   |  | | --- | | Attenuation | | true |  |  |
| **EventActionNamePosition** | Event Action Name Position | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | prefix | | 1 | suffix | | true | None | false |
| **EventNameCaseType** | Event Name Case Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | all lowercase | | 1 | all uppercase | | true | None | false |
| **EventNameModifyCase** | Event Name Modify Case | bool | false | None | true | None | false |
| **ExternalSourcesInputPath** | External Sources Input Path | string |  | None | true | None | true |
| **ExternalSourcesOutputPath** | External Sources Output Path | string |  | None | true | None | true |
| **FilterBehavior** | Filter Behavior | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sum all values (default) | | 1 | Use highest value | | true | None | false |
| **GarbageCollectWaveAnalysis** | **GarbageCollectWaveAnalysis** | bool | true | None | false | None | false |
| **GenerateMainSoundBank** | Generate Main SoundBank | bool | false | None | true | None | false |
| **GenerateMultipleBanks** | Generate Multiple Banks | bool | true | None | true | None | false |
| **GenerateSoundBankJSON** | Generate SoundBank JSON | bool | true | None | true | None | false |
| **GenerateSoundBankXML** | Generate SoundBank XML | bool | false | None | true | None | false |
| **GlobalVoiceInstancesLimit** | Global Voice Instances Limit | int16 | 256 | [ 1 , 10000 ] | true | None | true |
| **LicenseKey** | **LicenseKey** | string |  | None | false | None | false |
| **LineEnding** | Line Ending | Uint16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | LF (default) | | 1 | CRLF | | true | None | false |
| **MaxDangerousVirtualVoices** | Max Dangerous Virtual Voices | Uint32 | 50 | None | true | None | false |
| **MaxMessagesPerMessageId** | Max Messages Per Message Id | Uint32 | 100 | None | true | None | false |
| **MediaAutoBankSubFolders** | Sub-folders for Media and Auto-generated Bank Files | bool | false | None | true | None | false |
| **MediaIDsInSingleFile** | Persist media IDs in single file | bool | false | None | false | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **RemoveUnusedGeneratedFiles** | Remove Unused Generated Files | bool | true | None | true | None | false |
| **SoundBankAllowExceedingSB** | SoundBank Allow ExceedingSB | bool | false | None | true | None | false |
| **SoundBankDefinitionFileFormat** | **SoundBankDefinitionFileFormat** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **SoundBankGenerateDefinitionFile** | SoundBank Generate Definition File | bool | true | None | true | None | false |
| **SoundBankGenerateEstimatedDuration** | SoundBank Generate Estimated Duration | bool | true | None | true | None | false |
| **SoundBankGenerateHeaderFile** | SoundBank Generate Header File | bool | false | None | true | None | false |
| **SoundBankGenerateMaxAttenuationInfo** | SoundBank Generate Max Attenuation Info | bool | true | None | true | None | false |
| **SoundBankGeneratePrintColor** | SoundBank Generate Print Color | bool | true | None | true | None | false |
| **SoundBankGeneratePrintGUID** | SoundBank Generate Print GUID | bool | true | None | true | None | false |
| **SoundBankGeneratePrintPath** | SoundBank Generate Print Path | bool | true | None | true | None | false |
| **SoundBankGenerateReadableFile** | **SoundBankGenerateReadableFile** | bool | false | None | false | None | false |
| **SoundBankHeaderFilePath** | SoundBank Header File Path | string |  | None | true | None | false |
| **SoundBankIncludeSoundbankNamesStrings** | SoundBank Include Soundbank Names Strings | bool | true | None | true | None | false |
| **SoundBankPaths** | SoundBank Paths | string |  | None | true | None | true |
| **SoundBankPostGenerateCustomCmdDescription** | SoundBank Post-Generate Custom Command Description | string |  | None | true | None | true |
| **SoundBankPostGenerateCustomCmdLines** | SoundBank Post-Generate Custom Command Lines | string |  | None | true | None | true |
| **SoundBankPreGenerateCustomCmdDescription** | SoundBank Pre-Generate Custom Command Description | string |  | None | true | None | true |
| **SoundBankPreGenerateCustomCmdLines** | SoundBank Pre-Generate Custom Command Lines | string |  | None | true | None | true |
| **SoundBankUpdateAudioFiles** | SoundBank Update Audio Files | bool | false | None | true | None | false |
| **SourceControlGeneratedFiles** | Generated Files in Source Control | bool | false | None | true | None | false |
| **UseActionNameForEvent** | Use Action Name For Event | bool | true | None | true | None | false |
| **UseDefaultLanguage** | Use Default Language | bool | true | None | true | None | false |
| **UseMaxDangerousVirtualVoices** | Use Max Dangerous Virtual Voices | bool | true | None | true | None | false |
| **UseMaxMessagesPerMessageId** | Use Max Messages Per Message Id | bool | true | None | true | None | false |
| **VolumeThreshold** | Volume Threshold | Real64 | -80 | [ -96 , 0 ] | true | None | true |
| **WwiseConsoleLoadUserSettings** | Load user project settings when running WwiseConsole | bool | false | None | false | None | false |
| **WwiseVersionWhenCreated** | Wwise Version When Created | string |  | None | true | None | false |