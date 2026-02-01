# Release Notes 2023.1.11

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Release Notes 2023.1.11

The following sections list and describe the changes to Wwise between version 2023.1.10 and version 2023.1.11.  
此处提供了有关平台的特定信息：

[Windows 2023.1.11](windows_releasenotes_2023_1_11.html)

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [New Features](whatsnew_2023_1_11.html#generic_feature_changes_2023_1_11)
- [Behavior Changes](whatsnew_2023_1_11.html#generic_behavior_changes_2023_1_11)
- [Bug Fixes](whatsnew_2023_1_11.html#generic_bugs_2023_1_11)
- [Fixes for Community-Reported Bugs](whatsnew_2023_1_11.html#generic_community_bugs_2023_1_11)
- [Documentation Improvements](whatsnew_2023_1_11.html#generic_documentation_improvements_2023_1_11)

# New Features

- **WG-73102** 在打开网络驱动器上的工程时，现在会显示消息并建议将缓存文件夹设在本地驱动器上。

# Behavior Changes

- **WG-76146** WAAPI HTTP 服务器现在采用 Keep-Alive 机制提升连接性能。

# Bug Fixes

- **WG-75217** 已修复：插件属性 `PersistWhenDefault` 读取错误。
- **WG-76168** 已修复：在处理 AkGeometry 边界边缘时，个别情况下会触发错误的调试断言。
- **WG-76247** 已修复：插件基架中使用了已被弃用的宏。
- **WG-76424** 已修复：(Spatial Audio) 在足够靠近 Portal 的情况下，在 Reverb Zone 和父级 Room 之间穿越时，透射损失不连续。
- **WG-76511** 已修复：在自定义插件内直接使用 [AkInitSettings.szPluginDLLPath](struct_ak_init_settings_a381f6978151d3e205f3b493523ed3b57.html#a381f6978151d3e205f3b493523ed3b57 "When using DLLs for plugins, specify their path. Leave NULL if DLLs are in the same folder as the gam...") 时发生崩溃。
- **WG-76574** 已修复：在所读取 SoundBank 的文件大小刚好是粒度 `AkDeviceSetting.uGranularity` 的倍数时 StreamMgr 触发断言。

# Fixes for Community-Reported Bugs

- **WG-71736** 已修复：现有 Wwise 会话中的 Override Loudness Normalization 选项不会自动更新播放的内容。
- **WG-71881** 已修复：在将音乐过渡复制到另一音乐容器时，源对象和目标对象丢失。
- **WG-72427** 已修复：在实时编辑 Game Parameter 的 "Bind to Built-In Parameter" 值时，会将 Transport Control 游戏对象的 RTPC 值重置为 0。
- **WG-73189** 已修复：在打开 Wwise 工程后没有按照预期的同步类型对 Music Segment 和 Music Track 的 State 实施过渡。
- **WG-75517** 已修复：在 Music Switch Editor 或 Dialogue Event Editor 的 Entries 窗格中双击路径时发生崩溃。
- **WG-75818** 已修复：(Spatial Audio) Reverb Zone 的内置衍射 RTPC 被设为了错误的值。
- **WG-76182** 已修复：在迁移工程时可能会因为音乐过渡发生崩溃。
- **WG-76208** 已修复：在 `AK::SoundEngine::Init` 之前或 `AK::SoundEngine::Term` 之后调用 Spatial Audio API 时发生崩溃。
- **WG-76217** 已修复：(Spatial Audio) 在移除 Room 或 Portal 后立即发送引用内置 RTPC 的房间底噪时发生崩溃。
- **WG-76235** 已修复：有时无法完整地生成 `Wwise_IDs.h` 文件。
- **WG-76241** 已修复：Tab Delimited Import 无法正确组织所导入的声音。
- **WG-76345** 已修复：随 Wwise 安装的 `libxml2.dll` 版本不正确。
- **WG-76371** 已修复：在出现磁盘流播放错误时退出 Unreal 游戏会停止响应。
- **WG-76392** 已修复：在将 Effect 设为 Render 时后台转码发生崩溃。
- **WG-76410** 已修复：无法加载不含任何声音引擎 Source、Effect 或 Metadata 插件的插件库。
- **WG-76528** 已修复：(WAAPI) `ak.wwise.core.soundbank.generated` 主题为错误的平台返回了消息。
- **WG-76530** 已修复：(WAAPI) 向 `ak.wwise.core.soundbank.generated` 主题订阅传递无效的返回选项会导致在生成 SoundBank 时发生崩溃。

# Documentation Improvements

- **WG-75958** (WAAPI) 在有关向音频源添加标记点的文档中补充了之前缺失的属性。
- **WG-76248** 添加了有关 Wwise 设计工具插件库格式以及如何在 Wwise 2021.1 对 API 重构后进行注册的详细信息。