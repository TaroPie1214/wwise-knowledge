# What&#39;s New in 2011.1.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2011.1.1

2010.1.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2011.1 and version 2011.1.1.

# 漏洞修复

- **WG-19192** Fixed: Added missing .wcmdline files for new platforms.
- **WG-19238** Fixed: Generated Wwise\_IDs.h does not compile when project contains 3DS effect sharesets
- **WG-19258** Fixed: Crash when using the Replace Files function in the Audio File Importer, and that Motion objects are present in the project.
- **WG-19260** Fixed: SoundBank Manager tree not refreshed upon creating a new SoundBank Work Unit
- **WG-19263** Fixed: Convolution Reverb produced a high pitched noise on top of the sound on iOS
- **WG-19288** Enabled rendering of the following effects on 3DS: McDSP FutzBox, McDSP Limiter, Wwise Delay.
- **WG-19290** Fixed compilation of READBANKDATA macro when using the SN Compiler on PS3.
- **WG-19293** Fixed: Occasional deadlock while loading soundbank on Xbox 360
- **WG-19295** Fixed: assert when using rendered effects on the 3DS.
- **WG-19296** Fixed: Crash when using arrow key on empty reference view in specific scenario
- **WG-19303** Fixed: Error when converting files used by multiple sounds which have been imported with varying case in filename.
- **WG-19312** Fixed: Crash in low memory conditions using McDSP ML1 effect
- **WG-19314** Fixed: overriding Playback Limit on environmental bus not functional in Wwise Authoring (although fine in-game).
- **WG-19329** Fixed: Multi-edit from List View or Query Editor does not work correctly when offsetting the values.