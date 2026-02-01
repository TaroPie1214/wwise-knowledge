# Audio Devices

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Audio Devices

### Audio Devices

Advanced Profiler - Audio Devices（高级性能分析器 - 音频设备）选项卡会显示声音引擎中活跃的各个 Audio Device 的相关信息。您可以在调用 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f) 时使用 [`AkOutputSettings`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_output_settings.html) 来在声音初始化时指定活跃的设备，并通过调用 [`AK::SoundEngine::AddOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html)、[`AK::SoundEngine::ReplaceOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html) 或 [`AK::SoundEngine::RemoveOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a0932ed2a3669258ecc3bbe6448314020.html) 来添加、替换或移除活跃的设备。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Audio Devices | 音频设备。识别工程中的 Audio Device ShareSet。 |
| Device ID | 设备 ID。识别使用此 Audio Device ShareSet 的特定设备。 |
| Specified Listeners | 指定的听者。显示提供给 [`AK::SoundEngine::AddOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html) 的听者。只有在多个使用同一 ShareSet 的 Audio Device 同时处于活跃状态时才会考虑 Specified Listener。在使用多个共用同一 ShareSet 的 Audio Device 时，Specified Listener 会识别要将哪些听者输出到此设备。对于没有 Specified Listener 的 Audio Device，会接收来自未被任何其他使用同一 ShareSet 的 Audio Device 指定的听者的声音。 |

**相关主题**

- [“Audio Devices”一节](../../04-Project-Explorer/01-Audio-tab/01-Audio-Devices/00-Audio-Devices.md "Audio Devices")
- [“了解 Secondary Output”一节](../../../07-完善工程/01-管理输出/07-了解-Secondary-Output.md "了解 Secondary Output")

---