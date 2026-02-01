# What&#39;s New in 2013.2.4

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2013.2.4

2013.2.4 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2013.2.3 and version 2013.2.4.

# Platform SDK changes

- PS4: updated to SDK 1.500
- Xbox One: updated to XDK August 2013 QFE 10

# 新功能

- (Xbox One) Deferred I/O device implementation.

# API 变化

- **WG-24309** (PS4) New sink types added: AkSink\_Main\_NonRecordable, AkSink\_BGM\_NonRecordable. These should be used to create secondary devices that output content with recording restrictions.

# 漏洞修复

- **WG-23994** Fixed: rare crash when running out of memory in Lower Default pool while instantiating Convolution Reverb.
- **WG-24023** (3DS) Fixed: missing AkAudioInputSource library in SDK.
- **WG-24031** Fixed: crash when using some rendered effects with source trim.
- **WG-24240** (PS4) Fixed: ATRAC9 problem looping on specific sample count.
- **WG-24225** (PS3) Fixed: audible glitch using sample-accurate container starting with silence plug-in, followed by sounds.
- **WG-24265** Fixed: leaking streams when starving while being kicked by behavioral engine.
- **WG-24283** (Xbox One) Fixed: crash in Motion with negative values coming from Motion Generator plug-in.
- **WG-24289** (Xbox One) Fixed: freeze or memory corruption when playing a large number of simultaneous XMA sounds.
- **WG-24290** (Xbox One) Fixed: ASSERT in XMA source when applying large pitch offsets.
- **WG-24292** Fixed: crash when changing platform while list view item is inspected, with single-click workflow.
- **WG-24315** (PS4, PS Vita) Fixed: Filename marker missing when using ATRAC9 or VAG format.