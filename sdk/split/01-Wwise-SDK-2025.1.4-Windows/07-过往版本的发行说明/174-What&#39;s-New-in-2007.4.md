# What&#39;s New in 2007.4

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2007.4

The following sections list and describe the changes made to the Wwise SDK between version 2007.3 and version 2007.4.

# API 变化

- Asynchronous overloads of [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) and [AK::SoundEngine::UnloadBank()](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64) functions do not take the AkBankStatus parameter anymore. The result of the function call is now included in the AKRESULT returned by the function. The enum AkBankStatus was removed from the SDK.
- The AkBankCallbackFunc callback prototype now receives an AKRESULT instead of an AkBankStatus. Refer to the documentation for more information about the possible error codes returned.
- The two overloads of [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) that load banks from memory do not take a memory pool ID as a parameter anymore. The entire system has been reworked. When a bank is loaded from memory, the memory is now used in place instead of forcing a copy of the data to a section of memory reserved by the sound engine. The new system is faster and avoids copying data over twice. Note, however, that it is now the responsability of the caller to guarantee that the memory space provided will remain valid as long as the bank is loaded and that platform specific memory alignment restrictions are respected.
- AK\_INVALID\_UNIQUE\_ID macro is now defined to 0 instead of -1 or ( 0xffffffff ).
- Two new initialization parameters have been added to the structure [AkInitSettings](struct_ak_init_settings.html) ( uPrepareEventMemoryPoolID and bEnableGameSyncPreparation ).
- The following functions were removed:
  - AK::SoundEngine::EventNameToID
  - AK::SoundEngine::EnvNameToID
  - AK::SoundEngine::RTPCNameToID
  - AK::SoundEngine::SwitchGroupNameToID
  - AK::SoundEngine::SwitchNameToID
  - AK::SoundEngine::StateGroupNameToID
  - AK::SoundEngine::StateNameToID
  - AK::SoundEngine::TriggerNameToID
- And have been replaced by one unique function: [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)
- The functions [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) (multiple overloads), AK::SoundEngine::PrepareGameSync (multiple overloads), and [AK::SoundEngine::ClearPreparedEvents](namespace_a_k_1_1_sound_engine_af9648460be2ed1a0093ff09b42ef36f5.html#af9648460be2ed1a0093ff09b42ef36f5) were added to the SDK. Refer to [SoundBank 集成示例](sdk_bank_training.html) for more information on how to take advantage of these new functions.

# 新功能

- The bank management system has been completely revamped. Refer to [SoundBank 集成示例](sdk_bank_training.html) to read about new ways to manage your banks.
- The ".info" files that used to be generated with each SoundBank (they included references to streamed files)are no longer generated. Instead, Wwise generates one XML file per platform: "SoundBanksInfo.xml". You can parse it to retrieve all the files needed by the sound engine at run-time. Refer to [SoundBanksInfo.xml](soundengine_banks_general.html#soundengine_banks_general_identification_infofile) and the Wwise Help for more details.
- **WG-8590**: SoundBank Refactoring : Added profiling information on execution of prepare event commands.
- [File Packager 实用程序](samplecode.html#samplecode_integration_filepackager) was improved.
- **WG-8686**: Added the Events, Structures and Media optional flags to the SoundBank definition file syntax.

# Behavior and Performance Changes

- The sound engine no longer keeps a string table containing the name of all objects that can be accessed by name through the API. Only IDs are used now. Some error messages in the profiler may not include the name of a string unrecognized by the sound engine if the object was renamed or if there was an error in the object name passed to a function of the API.
- **WG-8502**: Refactored converted file management, now faster.
- **WG-8705, WG-8485, WG-8486**: ADPCM decoding on PS3 was improved.
- **WG-9145**: The default stream manager now considers the loop end heuristic in deadline computation. This reduces the risk of starvation when looping.

# Bug Fixes and Miscellaneous Changes

- The SoundBank settings are now persisted in Wwise projects. **Therefore they cannot be migrated**. You need to define them manually in the Project Settings dialog (SoundBanks tab). It is possible for users to override these settings locally. However, when Wwise is launched from the command line with the -generatesoundbank flag, SoundBanks are always generated according to the settings of the **project**. Some of these settings can be overridden directly. Refer to [使用命令行](bankscommandline.html) for details.
- Re-generating a bank will not create a different bank every time. The time stamp in the banks has been removed as it was causing issues with source control tools.
- **WG-8912**: Customer must use different parameters on the Wii to initialize comm memory. Now possible to use the platform independent parameter : DEFAULT\_MEMORY\_POOL\_ATTRIBUTES.
- **WG-8727**: Fixed Wwise\_IDs.h generation to use an unsigned type for IDs.
- **WG-8829**：修复了一个可能导致内存访问错误的漏洞，该漏洞发生在创建内存池时，其大小不是块大小的精确倍数。
- **WG-9004**：修复了一个可能在调试模式下触发断言，并可能导致某些声音在从虚声部返回时停止播放的漏洞（断言发生在 AkVPLPitchNode @ 第 47 行）。
- **WG-8735**: Fixed: Compile error in akplatformfuncs.h: "min" not found when using some compilators.
- **WG-8679**: Fixed: ADPCM encoding - Problem passing the step size to the next block which may generate non-optimal audio quality in first blocks.
- **WG-8699**: Fixed: AkFixedSizeBlocksMode not functional for memory pools created on user-allocated memory.
- **WG-3530**: Fixed: Windows Vista | Selection does not work properly in tree control.
- **WG-8815**: Fixed a situation where XMA file markers were randomly not sent when starving.
- **WG-8826**: Fixed a bug where AkNoAlloc was not considered as a valid argument to CreatePool when the memory was provided by the caller.
- **WG-8967**: Fixed a crash that would occur when encountering insufficient memory problem while allocating notifications for markers.
- **WG-8898**: Fixed : Less than 32KHz streamed sources in interactive music on the Wii can cause voice starvation errors.
- **WG-8649**: Fixed : Wwise I/O profiler was sometimes displaying invalid characters instead of the stream name.
- **WG-8929**: Updated Wii RVL SDK to patch 6.
- **WG-9089**: Fixed : Possible memory leak when performing transition reversals when using interactive music.
- **WG-9115**: Fixed : Leak caused by nodes of the interactive music hierarchy not being correctly stopped when [AK::MusicEngine::Term()](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f) is called.
- **WG-9117**: Fixed : Possible memory leak at shutdown with music tracks that have duplicated sources.
- **WG-9124**: Fixed : Possible deadlock between stream manager and profiler's threads.