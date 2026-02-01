# I/O settings incompatible. Block size must be between one and Granularity and whole fraction of the granularity.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > I/O settings incompatible. Block size must be between one and Granularity and whole fraction of the granularity.

#### I/O settings incompatible. Block size must be between one and Granularity and whole fraction of the granularity.

“I/O 设置不兼容。块大小须介于 1 和‘粒度’设置之间。‘粒度’设置须为块大小的整数倍”。AkDeviceSettings 中的 I/O 设置不一致或无效。

**可能的原因：**

- Block Size（块大小）必须介于 1 和 Granularity（粒度）设置之间。Granularity 设置必须为 Block Size 的整数倍。
- uBufferSize 与平台的缓冲区对齐设置不一致（一般为 16 字节）

**推荐的解决步骤：**

- 检查调用  [`AK::StreamMgr::Create`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_stream_mgr_af9d67dd0e502e5603a2921099916e2ab.html) 时使用的  [`AkDeviceSettings`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_device_settings.html)。
- 采用 Debug 库编译游戏，并重现场景。将所有断言语句报告给 Audiokinetic 技术支持部门。
- 若游戏采用自行定制版本的 Stream Manager（流管理器）或 I/O 挂钩，请连接调试程序并查明错误。

---