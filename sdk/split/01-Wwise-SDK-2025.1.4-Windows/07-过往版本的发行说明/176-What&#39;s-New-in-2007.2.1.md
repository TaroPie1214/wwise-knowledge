# What&#39;s New in 2007.2.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2007.2.1

The following sections list and describe the changes made to the Wwise SDK between version 2007.1.1 and version 2007.2.1.  *Changes between 2007.2 and 2007.2.1 are shown in italic.*

# API 变化

- The callback API has been revamped, adding support for End Of Dynamic Sequence Item notification. Callback details are now passed as a structure deriving from [AkCallbackInfo](struct_ak_callback_info.html) depending on the callback type.
- The platform-specific [AkThreadProperties](struct_ak_thread_properties.html) structure has a new member, uStackSize, across all platforms. This member allows users to specify the stack size of the lower engine, bank manager, and low-level I/O threads in the [AkPlatformInitSettings](struct_ak_platform_init_settings.html) structure during sound engine initialization. This parameter must be explicitly defined for the low-level I/O thread (refer to [初始化 Streaming Manager](workingwithsdks_initialization.html#initialization_streamingmgr) for more information). In contrast, using the [AK::SoundEngine::GetDefaultPlatformInitSettings()](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d) function will initialize it for the lower engine and bank manager threads (refer to [初始化声音引擎](workingwithsdks_initialization.html#initialization_soundengine) for more information).
- The AkHandle structure has been replaced by AkFileHandle.
- [IAkPluginMemAlloc.h](_i_ak_plugin_mem_alloc_8h.html) and [AkObject.h](_ak_object_8h.html) have been simplified for portability.
- The platform-specific AkPlatformFuncs.h files have been revamped.
- The overrides of [AK::IAkStreamMgr::CreateAuto()](class_a_k_1_1_i_ak_stream_mgr_afe30a576bd859ff4e9b60a3f8e1710fb.html#afe30a576bd859ff4e9b60a3f8e1710fb) and [AK::IAkStreamMgr::CreateStd()](class_a_k_1_1_i_ak_stream_mgr_a1de2a7935a2d3cddb71e7cc7f48effd6.html#a1de2a7935a2d3cddb71e7cc7f48effd6) that accept an [AkFileDesc](struct_ak_file_desc.html) input parameter have been removed from the SDK.
- The PLAYSTATION®3's AkEventStruct structure has been renamed AkEvent, and it now contains only two members: EventPort and EventQueue.
- The AkMallocMEM2 flag has been added to the AkMemPoolAttributes enum.
- The in\_uSize input of the [AK::MemoryMgr::dMalloc()](namespace_a_k_1_1_memory_mgr_a157a010cab9d463be18a871c350bd226.html#a157a010cab9d463be18a871c350bd226), [AK::MemoryMgr::Malloc()](namespace_a_k_1_1_memory_mgr_a8727fb3eaaefd366474f802b0467b296.html#a8727fb3eaaefd366474f802b0467b296) and [AK::MemoryMgr::Malign()](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5) methods is now of type size\_t instead of AkUInt32.
- The AkPluginAudioBuffer structure now has the following additional members: pR32Data, pI16Data, pI8Data, and pU8Data.
- The IsSendModeEffect() method has been added to the [AK::IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html) class, to identify the mode used by the plug-in (insert or send).

# 新功能

- Wwise now supports the Wii™ platform, in addition to the existing support for Windows®, Xbox 360™, and PLAYSTATION®3.
- Introduced Dynamic Sequence and Dynamic Dialogue. 请参阅 [集成详情——动态对白](soundengine_dynamicdialogue.html) 了解更多信息。
- The Wwise Matrix Reverb plug-in has been added.
- The following plug-ins can now be used as environmental effects: Wwise Reverb, Wwise Reverb Lite, Wwise Matrix Reverb, and Wwise Delay. Wwise Environmental Reverb has been removed, as its functionality is now performed by Wwise Reverb.
- A new plug-in sample has been added to the SDK: the AkAudioInput plug-in. Refer to [音频输入源插件](samplecode.html#samplecode_sourceplugins_audioinput) for more information.
- The Integration Demo has been extended to demonstrate Dynamic Sequences and the Audio Input plug-in.

# Behavior and Performance Changes

- **WG-6942**: Fixed the inconsistent behavior of RTPCs on bus effects.
- **WG-7051**: Instead of having its own game object in Wwise, the SoundFrame now uses Wwise's reserved game object as the default object for event and game sync handling. That is, the AK::SoundFrame::IGameObject::s\_GlobalGameObject game object ID has been replaced by AK::SoundFrame::IGameObject::s\_WwiseGameObject. The code of the CarSim, SFTest, and wwiseMax sample projects is affected by this behavior change. This makes the SoundFrame's handling of game objects more similar to that of the sound engine.
- **WG-7205**: A bug in the handling of sound priorities based on distance in a multiple-listener context has been fixed.
- **WG-7517**: The performance of ADPCM codec has been improved.
- **WG-7905**: Sample-accurate containers now correctly handle sounds with different sample rates.
- The speaker panning algorithm has been fine-tuned.
- The Delay, Wwise Expander, and Wwise Compressor effects have been refactored.
- The implementation of the PluginFPMax(), PluginFPMin(), and PluginFPSel() methods has been improved on the PLAYSTATION®3.
- The Delay effect's implementation has been improved on the PLAYSTATION®3.
- The memory alignment of audio buffers has been optimized on the PLAYSTATION®3.
- Unnecessary cache pollution has been removed from the PLAYSTATION®3's effect plug-ins.

# Bug Fixes and Miscellaneous Changes

- **WG-6589**: A situation in which the LFE channel is played before the other audio channels has been fixed.
- **WG-6695**: A potential bug in the bank manager thread's creation has been fixed.
- **WG-6717**: A stack size issue in the bank and event manager threads is now avoided.
- **WG-6877**: A memory leak in the Lower Engine Default pool has been fixed.
- **WG-6949**: These defines have been removed or changed to reduce the possibility of conflict with client code: PS3, USE\_SPU, SPU, and PROFILEINFO.
- **WG-7052**: A potential memory leak in game objects that have been assigned several RTPCs has been fixed.
- **WG-7492**: Fixed a crash in Interactive Music playback.
- **WG-7828**: Fixed a crash that occurred when quickly changing states to which music switch containers were registered.
- **WG-7828**: Fixed a crash caused by memory corruption related to stopping music switch containers.
- **WG-7951**: Fixed a crash that occurred when playing interactive music content from files and encountering source starvation.
- #include AkTypes.h directives have been added to various SDK header files.
- SDK header files have been modified to use system path for #include directives targeting the Wwise SDK.
- AkTypes.h has been reorganized to reference platform-specific variants of the file.
- The \include\[AK](namespace_a_k.html "Definition of data structures for AkAudioObject")\[AkWwiseSDKVersion.h](_ak_wwise_s_d_k_version_8h.html) file has been added to the SDK.
- SDK documentation has been split into platform-specific files. Platforms other than Windows are now properly documented.
- ***WG-6683**: Fixed a crash when stopping a paused interactive music playback which has pending stingers.*
- ***WG-7951**: Fixed a memory corruption occuring when releasing game objects on which interactive music content is playing.*
- ***WG-8158**: Improved accuracy of volume calculations on the Wii.*
- ***WG-8287**: Fixed a crash when unloading a bank while interactive music is playing.*
- ***WG-8309**: Fixed a memory leak in CAkDeviceBase on the Wii.*
- ***WG-8418**: Fixed a crash when playing a switch container that plays 2 continuous containers at the same time.*
- ***WG-8425**: 3D User-defined sounds did not behave as expected when the listener moved away from the origin of the 3D world.*