# UserProjectSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

UserProjectSettings

- **Plugin ID**: 51
- **Class ID**: 3342352

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AutoSoundBankAllEvents** | Auto SoundBank Generation - All Events | bool | false | None | false | None | false |
| **AutoSoundBankEnabled** | Enable Auto SoundBank Generation | bool | false | None | true | None | false |
| **Conversion** | Conversion Settings | Reference |  | **可能的类型：**   |  | | --- | | Conversion | | true |  |  |
| **ConvertExternalSources** | Convert External Sources | bool | true | None | true | None | false |
| **CopyLooseStreamedMedia** | Copy Loose/Streamed Media Files | bool | true | None | true | None | false |
| **DefaultSoundVolume** | **DefaultSoundVolume** | Real64 | 0 | [ -200 , 200 ] | false | None | false |
| **EventActionNamePosition** | Event Action Name Position | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | prefix | | 1 | suffix | | true | None | false |
| **EventCreationSettingsOverride** | Event Creation Settings Override | bool | false | None | true | None | false |
| **EventNameCaseType** | Event Name Case Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | all lowercase | | 1 | all uppercase | | true | None | false |
| **EventNameModifyCase** | Event Name Modify Case | bool | false | None | true | None | false |
| **ExternalSourcesInputPath** | External Sources Input Path | string |  | None | true | None | true |
| **ExternalSourcesOutputPath** | External Sources Output Path | string |  | None | true | None | true |
| **ExternalSourcesOverrideInputPath** | External Sources Override Input Path | bool | false | None | true | None | false |
| **ExternalSourcesOverrideOutputPath** | External Sources Override Output Path | bool | false | None | true | None | false |
| **GenerateMainSoundBank** | Generate Main SoundBank | bool | false | None | true | None | false |
| **GenerateMultipleBanks** | Generate Multiple Banks | bool | true | None | true | None | false |
| **GenerateSoundBankJSON** | Generate SoundBank JSON | bool | true | None | true | None | false |
| **GenerateSoundBankXML** | Generate SoundBank XML | bool | false | None | true | None | false |
| **MediaAutoBankSubFolders** | Sub-folders for Media and Auto-generated Bank Files | bool | false | None | true | None | false |
| **OverrideConversion** | Override Conversion Settings | bool | false | None | true | None | false |
| **PostGenerateStepUserOverride** | Post-Generate Step User Override | bool | false | None | true | None | false |
| **PreGenerateStepUserOverride** | Pre-Generate Step User Override | bool | false | None | true | None | false |
| **RemoveUnusedGeneratedFiles** | Remove Unused Generated Files | bool | true | None | true | None | false |
| **SettingsUserOverride** | Settings User Override | bool | false | None | true | None | false |
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
| **SoundBankPathUserOverride** | SoundBank Path User Override | bool | false | None | true | None | false |
| **SoundBankPaths** | SoundBank Paths | string |  | None | true | None | true |
| **SoundBankPostGenerateCustomCmdDescription** | SoundBank Post-Generate Custom Command Description | string |  | None | true | None | true |
| **SoundBankPostGenerateCustomCmdLines** | SoundBank Post-Generate Custom Command Lines | string |  | None | true | None | true |
| **SoundBankPreGenerateCustomCmdDescription** | SoundBank Pre-Generate Custom Command Description | string |  | None | true | None | true |
| **SoundBankPreGenerateCustomCmdLines** | SoundBank Pre-Generate Custom Command Lines | string |  | None | true | None | true |
| **SoundBankUpdateAudioFiles** | SoundBank Update Audio Files | bool | false | None | true | None | false |
| **SourceControlGeneratedFiles** | Generated Files in Source Control | bool | false | None | true | None | false |
| **UseActionNameForEvent** | Use Action Name For Event | bool | true | None | true | None | false |