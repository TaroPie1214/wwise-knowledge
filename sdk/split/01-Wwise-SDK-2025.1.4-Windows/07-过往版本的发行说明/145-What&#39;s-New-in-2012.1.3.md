# What&#39;s New in 2012.1.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2012.1.3

2012.1.3 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2012.1.2 and version 2012.1.3.

# 漏洞修复

- **WG-20847** Fixed: Very long delay when connecting the profiler with a project with lots of busses and lots of states.
- **WG-20894** Fixed: inconsistent panning behavior when binding RTPC to front-rear or left-right, while in 3D user-defined positioning.
- **WG-20901** WiiU Optimization: tuned inlining parameters. Small gain obtained.
- **WG-20910** Fixed: Crash when connecting Wwise and there is not enough memory in the Communication pool.
- **WG-20913** Fixed: Connection to game is very slow if there is not enough memory to sync states.
- **WG-20912** Fixed: Nested workunits descendants were not packaged correctly in Soundbanks, and mute/solo logic was incorrect.
- **WG-20917** Fixed: Possible memory leak when preparing events in out of memory situations.