# Incompatible plug-in dynamic library file.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Incompatible plug-in dynamic library file.

#### Incompatible plug-in dynamic library file.

“不兼容的插件动态库文件”。由于文件的格式与平台的标准动态库文件格式不匹配，导致尝试加载插件动态库失败。

**可能的原因：**

- 打包游戏文件的过程中文件损坏。
- 针对不同的平台编译了所要打包的库。
- 编译库时所用的 SDK 版本低于平台固件支持的版本。

**推荐的解决步骤：**

- 检查工程的打包步骤，确保复制与目标平台对应的库文件。
- 在打包过程中通过文件哈希机制验证文件复制操作，以此来检测文件损坏错误。
- 在编译插件时，确保针对目标平台使用最新的 SDK 版本。

---