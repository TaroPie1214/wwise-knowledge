# What&#39;s New in 2011.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2011.1.2

2011.1.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2011.1.1 and version 2011.1.2.

# 新功能

- iOS: Updated to SDK 4.3.

# 漏洞修复

- **WG-19379** 3DS: Workaround for compiler optimization failure in volume calculation (performance issue).
- **WG-19483** Fixed: Bad throughput heuristic set on xWMA streams: results in inconsistent xWMA stream profiling data, and suboptimal I/O scheduling when there are xWMA files playing.
- **WG-19496** Fixed: Possible crash in the voice limiting system in "out of memory" situations.
- **WG-19515** Fixed: Crash in game when connecting with Wwise and syncing interactive music hierarchy with specific memory conditions.
- **WG-19556** Fixed: Not possible to have positive values in State tab and possible crash and erroneous behavior when editing state value in multi-selection.
- **WG-19576** Fixed: Streamed files used by multiple banks were reported in the definition file (.txt) of only one of these banks.
- **WG-19580** Fixed: Source starvation with streamed XMA in interactive music, if seeking is required when a segment starts.
- **WG-19581** Fixed: Crash when exclusively converting external sources files at command line.
- **WG-19634** Fixed: Crash in xWMA source when out of memory.