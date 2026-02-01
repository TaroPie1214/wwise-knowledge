# What&#39;s New in 2009.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2009.2

The following sections list and describe the changes made to Wwise between version 2009.1 and version 2009.2

*Changes that were provided in patches over 2009.1 are shown in italics.*

# Platform Support Changes

- **Mac**: The Mac platform is now supported

# API 变化s

平台 SDK 更新:

- **WG-15526**: [Microsoft](namespace_microsoft.html) XDK: Now compiling Wwise using version 9328 (June 2009).
- **WG-15580**：更新至 PS3 SDK 280

通用：

- **WG-15411**: Sine and Tone Generator source plug-in libraries now have a new name on the Wii: AkSine, AkToneGen
- **WG-15168**: Expose maximum number of frames passed to Execute() call through plugin context. AkUInt16 GetMaxBufferLength( ) was added to IAkEffectPluginContext and IAkSourcePluginContext to retrieve the maximum number of frames that Execute() will call for this effect. This new function can be used by the effect to make memory allocation at initialization based on this worst case scenario.
- **WG-14999**: Game object ID is now 64 bits on 64-bit platforms. This allows users to use an address directly as a game object ID on 64-bit platforms. AkGameObjectID has changed from: typedef AkUInt32 AkGameObjectID; to: typedef AkUIntPtr AkGameObjectID;
- **WG-14998**: AK::Wwise::IWriteData::WriteString() was removed, and replaced with WritePascalString() and WriteUtf16String(), which now works as expected. Passing of "String" properties to audio plug-ins is now correctly handled.
- **WG-14547**: Merged some of the sound engine binaries and removed pollution of game code by the communication layer. The behavioral (AkAudioEngine) and lower engines (AkLowerEngine) and the proxy (ProxyCentral) were merged in one lib: AkSoundEngine.lib. The music proxy (ProxyMusic) was merged with the music engine (AkMusicEngine). The initialization of the Communication module is much simpler. Include "AkCommunication.h", get the default settings and call [AK::Comm::Init()](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8). Call [AK::Comm::Term()](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f) to terminate it. AK::Comm::Perform() is now called internally in [AK::SoundEngine::RenderAudio()](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1). Refer to [初始化声音引擎模块](workingwithsdks_initialization.html) for more details. The following includes:
  - <AK/Comm/CommunicationCentralFactory.h>
  - <AK/Comm/ICommunicationCentral.h>
  - <AK/Comm/ProxyFrameworkFactory.h>
  - <AK/Comm/IProxyFrameworkConnected.h> were all replaced by one single include:
  - <[AK/Comm/AkCommunication.h](_ak_communication_8h.html)>

# 新功能

New Features in 2009.2:

- **WG-9490**: (PS3) Source plug-ins can now be executed on SPUs using AK::MultiCoreServices::DspProcess.
- **WG-15348**: Plug-ins can now define object definitions for their inner types. See [内部对象](plugin_xml.html#wwiseplugin_objectstore) for more information.

# Behavior and Performance Changes

Performance changes:

- **WG-15522**: XMA bank optimization: A smaller alignment is required for in-memory XMA decoded buffer (256 bytes instead of former 2KB). This buffer is easier to allocate, and has less impact on memory regarding fragmentation.
- **WG-15224, WG-15209**: PS3 Vorbis optimizations
- **WG-15169**: Improved performance when voices don't use built-in low-pass filtering (LPF = 0). This is particularly interesting on the PS3 where some maintenance was performed on the PPU, before it was completely removed by this optimization.

Introduced in 2009.1 Patch 1

- **WG-14994**: *Optimized Compressor, Peak Limiter and Expander on XBox360*
- **WG-15098**: *Streams that rely on minimal buffering (granularity greater than the equivalent target buffering length) take less memory in the I/O pool.*

# Bug Fixes and Miscellaneous Changes

漏洞修复：

- **WG-15579**: Fixed: Audio clips that end before the end of a music segment are not freed until the end of that segment is reached if they are in a virtual state. In the meantime, virtual time skip is performed for nothing.
- **WG-15212**: Possible audio click audible when changing pitch of a multi channel source on the PS3.
- **WG-15231**: A crash was fixed when running Wwise from the command line from a service or when no user is logged-on.
- **WG-15189**: WwiseCLI can now output to Visual Studio output window (and other similar applications).
- **WG-15186**: Disabled states on busses were not working correctly in a particular scenario.
- **WG-14940**: Fixed: Possible crash when deleting a point from the Position Editor while the sound is playing.
- **WG-14890**: Fixed: Can't play particular wave files containing invalid loop points.

Misc:

- **WG-15510**: Games are not required to define AKSOUNDENGINE\_STATIC anymore when linking statically with the libraries of the sound engine. On the other hand, they should define AKSOUNDENGINE\_DLL on Windows in order to import the methods of the sound engine API if they wrap all those libaries into a DLL (see soundengine\_integration\_cppprojectsettings\_various\_AKSOUNDENGINE\_DLL for more details).
- **WG-15484**: Bank version has been updated for 2009.1 to accommodate the new XMA encoder.
- **WG-15373**: Wwise Authoring file restructuration (Wwise installer and source code level 3):
  - The Wise Authoring Application sources were moved from "\\Wwise" to "\\Authoring\\source"
  - The Wwise Authoring Application binaries were moved from "[install directory]\\" to "[install directory]\\Authoring\\Win32\\Release\\bin"
  - WwiseCLI.exe was moved to "[install directory]\\Authoring\\Win32\\Release\\bin"
- **WG-15372**: Wwise SDK restructuration:
  - The folder "\\SDKs" was renamed to "\\SDK"

Introduced in 2009.1 Patch 1

- **WG-14957**: *XBOX360: Voice Starvation causes XMA voice to stop*
- **WG-15044**: *Fixed: Excessive amount of I/O requests when I/O memory pool is full and there are small looping sounds where the minimal buffering is greater than the device's nominal buffering.*
- **WG-15061**: *Fixed: (Monitoring) Out of memory errors ("Attempted alloc size") fail to display the pool on PS3. Pool name was not always showing in the Capture Log when a memory allocation failure occrus on the PS3.*
- **WG-15110**: *Audio To Motion voice doesn't stop if Center% is 100%*
- **WG-15164**: *Fixed: Illegal usage of "new" in ResolveDialogEvent( const char \* ) (introduced in 2009.1).*

Introduced in 2009.1 Patch 2

- **WG-15051**: *Replaced deprecated xmaencode.exe XMA encoder with xma2encode.exe. XMA 1 files (BlockSize == 0) are no longer supported. In existing projects, sources previously set to BlockSize == 0 will use a value of 64 KB at conversion time, and will generate a warning.*
- **WG-15188**: *SDK function [AK::SoundEngine::ClearBanks](namespace_a_k_1_1_sound_engine_ab934f98a6622976d24e0a096911eb0c8.html#ab934f98a6622976d24e0a096911eb0c8) is not always clearing all banks.*

Introduced in 2009.1 Patch 3

- **WG-15407**: *Invalid preprocessor command in header Plugin/PluginServices/PS3/MultiCoreServices.h*
- **WG-15415**: *Wwise Motion may not always work when using multiple controllers (Rumble doesn't always work on Player #2).*
- **WG-15356**: *Fixes in streamed XMA source (Xbox 360 only):*
  - *Fixed: Unable to seek properly when block size is larger than streaming granularity. If this occurs when a voice starts at a random location (typically with interactive music), the XMA context is never released and this can eventually result in the inability to play back new XMA voices (and an assert in debug).*
  - *Fixed: Inconsistent usage of [AK::MemoryMgr::Malign()](namespace_a_k_1_1_memory_mgr_aeb57745b9cfdc88c9775e5bc504e9ab5.html#aeb57745b9cfdc88c9775e5bc504e9ab5) vs [AK::MemoryMgr::Free()](namespace_a_k_1_1_memory_mgr_a6ee20149a37b11b31589c6f23f46db65.html#a6ee20149a37b11b31589c6f23f46db65). This has no consequence with the default implementation of the Memory Manager.*
  - *Optimization: The buffer for decoded XMA needs to be aligned on 256 bytes instead of 2KB.*
  - *Misc: Set default XMA block size to 16 KB, to be consistent with the default streaming granularity.*