# What&#39;s New in 2010.1.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2010.1.2

2010.1.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2010.1.1 and version 2010.1.2.

# Behavior and Performance Changes

- **WG-17817** Effect with tails have a different behavior when RTPC is applied on parameters which affect the tail length. Previously the tail was reset every time these parameters was changed (busses could thus never stop if the game keeps posting parameter changes) while now the maximum tail length is always used and the tail simply continues when new parameters are encountered.

# 漏洞修复

- **WG-16984** Fixed: pausing a sound in the exact same frame that it is resumes can cause the sound to stop when there is no transition time.
- **WG-17651** Fixed: AkManualEvent.h on the mac platform – improved synchronization mechanism to prevent deadlocks.
- **WG-17666** Fixed: occasional volume spikes with 3D user-defined sounds.
- **WG-17669** Fixed: crash when playing an inaudible sample-accurate container containing children with both 'kill voice' and 'from elapsed time' under-threshold behavior.
- **WG-17709** Fixed: memory corruption & crash with Motion Generator in "initially under threshold" case.
- **WG-17813** Fixed: deadlock possibility when the message queue gets overcrowded.
- **WG-17834** Fixed: possible error in computation of the busses volumes when multiple busses are processing effects on the same voice.
- **WG-17841** Fixed: sounds and segments do not go back to full volume after pausing and resuming with fade-in (by 0.4 dB).
- **WG-17845** Fixed: in rare situations where there is much more IO memory requirements than there is memory available, the IO thread may keep on spinning for a while. This is mostly noticeable on the Wii where it can hang the whole system.
- **WG-17865** Fixed: suboptimal behavior with transition reversals in interactive music.
- **WG-17867** Fixed: bypass of effects in the actor-mixer hierarchy would sometimes be ignored in the Release build.