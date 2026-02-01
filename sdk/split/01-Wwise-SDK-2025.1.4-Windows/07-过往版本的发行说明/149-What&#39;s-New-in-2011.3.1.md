# What&#39;s New in 2011.3.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2011.3.1

2011.3.1 属于补丁发布. The following sections describe the changes made to Wwise between version 2011.3 and version 2011.3.1.

# 平台 SDK 更新

- Xbox 360: updated to XDK 21076.6 (December 2011)
- PS3: updated to SDK 400.001
- VITA: updated to SDK 1.5
- 3DS: updated to CTR-SDK 2.4.2

# 漏洞修复

- **WG-20224** Fixed: 3D positioning doesn't work on WiiU
- **WG-20279** Fixed: IntegrationDemo: assert in MemoryMgr when switching to another task and coming back on Android 4.0
- **WG-20289** Fixed: Rare crash on Nintendo 3DS in function CAkParameterNode::IsOrIsChildOf
- **WG-20310** Fixed: The render column in the effect tab can disappear and never come back
- **WG-20380** Fixed: Crash when connecting to game when an attenuation shareset has RTPC bindings
- **WG-20410** Fixed: Sound Engine may crash (only in debug or profile) when triggering a break event on no specific game object when the target object is unloaded
- **WG-20411** Fixed: Splitting non-localized structure and media content in localized and non-localized banks may cause media to not be found at run time
- **WG-20417** Fixed: Bypass effect ignored if "virtual voice behavior" is not "Continue to play"
- **WG-20419** Fixed: Non-unlinkable properties (Sound Loop Count and Rnd/Seq Container Transition Time) are not loaded correctly in project when a modifier or RTPC is set
- **WG-20461** Fixed: crash in CAkMusicSwitchCtx::CanRestartPlaying