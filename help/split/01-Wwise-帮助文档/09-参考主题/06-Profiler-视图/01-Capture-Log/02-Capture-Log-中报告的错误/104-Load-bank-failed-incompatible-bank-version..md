# Load bank failed : incompatible bank version.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Load bank failed : incompatible bank version.

#### Load bank failed : incompatible bank version.

“音频包加载失败: 不兼容该音频包版本”。未加载指定的 SoundBank（音频包），因为生成时所用 Wwise 设计工具的版本与游戏声音引擎不同。记住，Wwise 包含两个组件：声音设计师使用的设计工具和游戏中包含的声音引擎组件（通常相互静态关联）。两者版本必须相同。

对于 Unity 和 Unreal 用户，声音引擎部分会随 Unity/Unreal Wwise Integration 一并安装。

此错误仅会在**大**版本更新导致版本存在差异时出现。大版本编号为 YEAR.MAJOR.PATCH.BUILD。若 PATCH 编号不为 0，则表示基于大版本的补丁版本/小版本。除非版本说明中另行声明，否则音频包在基于同一大版本的所有补丁版本之间兼容。

**可能的原因：**

- 近期更新 Wwise 时，仅更新了设计工具。针对工程的所有平台更新 SDK 组件或 Unity/Unreal Wwise Integration。
- 近期更新了 Wwise，但未针对工程的所有平台重新生成并重新部署 SoundBank。
- 所加载的 SoundBank 由不同版本的 Wwise 生成。确保同时将新的 SoundBank 复制到正确位置以便游戏读取。
- 当前加载的 SoundBank 在生成时，所选平台并非当前平台。例如，如果要在 Xbox 上运行，则请确保该 SoundBank 不是为 Windows 生成的。
- 包含该 SoundBank 的内存已损坏（在内存指针 in\_pInMemoryBankPtr 与 LoadBank 一起使用时）。
- 主机的测试沙盒磁盘上存在过时或落单的 SoundBank 文件。在这种情况下，请从主机删除所有 .bnk 文件并重新部署游戏。

---