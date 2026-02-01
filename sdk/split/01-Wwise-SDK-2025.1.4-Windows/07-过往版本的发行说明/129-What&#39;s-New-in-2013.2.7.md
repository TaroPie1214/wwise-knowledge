# What&#39;s New in 2013.2.7

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.7

2013.2.7 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.6 and version 2013.2.7.

# Platform SDK changes

- Updated Wii U VSI to 2.3.5
- Added Visual Studio 2013 libraries for Windows and Metro

# 新功能

- (Xbox One) Support for XMA Streaming.
- CrankCase REV:
  - New cars added.
  - Added support for Xbox360 controller to simulate models.

# API 变化

- **WG-24503** New function GetFilesForOperation(...) added to [AK::Wwise::ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html).

# Performance Improvements

- **WG-24487** New C++-based CopyStreamedFiles helper application replaces the C#-based AkCopyStreamedFiles sample tool. 设计工具的 Windows 和 Mac 版本均可提供。
- **WG-24699** (PS4) ATRAC-9 hardware resources and memory optimisation for virtual voices.
- **WG-24503** File Manager: Submit Changes was re-factored for better performances (Perforce and SVN).

# 漏洞修复

- **WG-23550** Fixed: Metering of the master Secondary bus does not initially work correctly.
- **WG-24393** (PS4) Fixed: occasional assert after seeking in ATRAC-9 stream.
- **WG-24504** (Xbox One) Stability fixes in XMA decoding.
- **WG-24785** Fixed: Deadlock when connecting Wwise with a full command queue.
- **WG-24838** (iOS) Fixed: Compilation error in level 2 source code.
- **WG-24860** Fixed: Occasional nullpointer crash in CAkMixer when using out-of-place effects.
- **WG-24900** Fixed: Soundbanks: differences in some bytes after successive bank generations.
- **WG-24903** Fixed: Crankcase REV soundbank packaging issues.
- **WG-24910** (Xbox One) Disabled call to AcpHalAllocateShapeContexts when uMaxXMAVoices is 0.
- **WG-24916** Fixed: Authoring displays Secondary Output as stereo.
- **WG-24970** (PS4) Fixed: Possible deadlock when a controller battery dies.
- **WG-25008** Fixed: Suboptimal cached stream block pick in some scenarios.