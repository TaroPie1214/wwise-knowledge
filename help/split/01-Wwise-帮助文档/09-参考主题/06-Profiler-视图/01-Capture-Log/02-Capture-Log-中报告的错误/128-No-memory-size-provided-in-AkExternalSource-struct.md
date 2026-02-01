# No memory size provided in AkExternalSource structure, but data pointer was used. Fill uiMemorySize.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > No memory size provided in AkExternalSource structure, but data pointer was used. Fill uiMemorySize.

#### No memory size provided in AkExternalSource structure, but data pointer was used. Fill uiMemorySize.

“AkExternalSource 结构中未提供内存大小，但使用了数据指针。填写 uiMemorySize。”在结合 External Source（外部源）使用 AK::SoundEngine::PostEvent 并在内存中预先加载了数据时，必须为  [`AkExternalSourceInfo`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_external_source_info.html) 结构提供有效的 pInMemory 和 uiMemorySize。

**推荐的解决步骤：**

- 使用预加载 WEM 文件的全部字节数填写 uiMemorySize。
- 改为在 szFile 中指定文件名称，以便使用从磁盘流播放的版本。

---