# What&#39;s New in 2010.3.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2010.3.1

2010.3.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2010.3 and version 2010.3.1.

# 新功能

- **WG-18258** Sounbank content files can now be exported in Unicode so that Japanese and other non-ANSI characters are exported properly (new option in Project Settings > SoundBanks).

# 漏洞修复

- **WG-18596** Fixed: Vorbis prefetch data size stored in banks (for zero-latency) is 4 times larger than the value indicated in the authoring tool (regression in 2010.3).
- **WG-18602** Fixed: Assert or never-ending voice when Break action occurs on a streamed Vorbis source at a very specific timing.
- **WG-18621** Fixed: Project Settings > SoundBanks: "Generate max attenuation info for events" is disabled when "Generate SoundBank content files" is unchecked.
- **WG-18357** Fixed: SoundBank content files are badly formatted if exported "Notes" contain line breaks or tabs.