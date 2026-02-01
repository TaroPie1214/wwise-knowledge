# What&#39;s New in 2010.3.3

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2010.3.3

2010.3.3 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2010.3.2 and version 2010.3.3.

# 新功能

- **WG-19025**  Xbox 360: Update to XDK February 2011 (20500).

# 漏洞修复

- **WG-18764**  Fixed: while connected to a game, clicking a music object stops the music in the game.
- **WG-18767**  Fixed: possible race condition when generating banks with several convolution reverb sharesets, leading to error in bank generation or inconsistent playback behavior.
- **WG-18772**  Fixed: rare crash when converting audio files on a multiple core CPU.
- **WG-18793**  Fixed: crash in the Capture Log when selecting specific filtering options.
- **WG-18796**  Fixed: notifications messages such as SetSwitch may not appear in the capture log in some scenarios.
- **WG-18869**  Fixed: stream manager's scheduler may perform I/O for streams that already reached their target buffering; unwanted transfers occur when stopping other streams.
- **WG-18964**  Fixed: Bus randomly stay blocked in ducked state when the ducking bus is explicitely stopped during the recovery time.
- **WG-18965**  Fixed: potential DMA failure on PS3 with corrupted streamed vorbis sources.
- **WG-18992**  Fixed: rare crash with volume fades while ducking and mixing under low-memory conditions.