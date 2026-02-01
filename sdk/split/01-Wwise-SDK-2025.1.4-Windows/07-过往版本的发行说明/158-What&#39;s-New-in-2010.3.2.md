# What&#39;s New in 2010.3.2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2010.3.2

2010.3.2 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2010.3.1 and version 2010.3.2.

# 新功能

- **WG-18732** Xbox 360: Update to XDK 20353 November 2010

# 漏洞修复

- **WG-18649** Fixed: Possible Wwise crash on bank generation when using rendered McDSP effects
- **WG-18684** Fixed: Sound may fail to play and Log the message "Inconsistent source status" When pausing two or more sounds that were scheduled to play at the exact same time.
- **WG-18688** Fixed: memory leak in Default Pool when editing a RTPC curve on an effect shareset.
- **WG-18703** Fixed: Adressable device IO memory ([AkDeviceSettings::uIOMemorySize](struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html#a75893592924a59881fe2cbca4e4ddd04 "Size of memory for I/O (for automatic streams). It is passed directly to AK::MemoryMgr::Malign(),...")) is rounded up to a multiple of the granularity ([AkDeviceSettings::uGranularity](struct_ak_device_settings_abd4879bfd150b9a2f898102e3815dbe2.html#abd4879bfd150b9a2f898102e3815dbe2 "I/O requests granularity (typical bytes/request).")). This leads to memory overflow if the device is initialized with a memory size that is not a multiple of the granularity. It must be rounded down.
- **WG-18710** Fixed: Asserts and crash if low-level I/O hook implementations of IAkIOHookDeferred::Read() return AK\_Fail (deferred devices only). Also, the streaming device is less vulnerable to invalid streaming data in general.
- **WG-18729** Fixed: Vorbis streamed file can fail to play on PS3 when seek table size is larger than streaming granularity.
- **WG-18730** Fixed: PrepareEvent cannot find media from mixed-type bank when Use Soundbank Names is OFF
- **WG-18734**  Fixed: Wwise Meter CRASH on PS3 when no Output Game Parameter selected
- **WG-18735** Fixed: PS3 crash when voice using source plug-ins is sent virtual from elapsed time.
- **WG-18759** Fixed: Invalid assertion in sample CAkDefaultIOHookDeferred on the PS3: transferred size should not be checked if the request was cancelled.
- **WG-18763** Fixed: DMA corruption in Flanger plug-in on PS3