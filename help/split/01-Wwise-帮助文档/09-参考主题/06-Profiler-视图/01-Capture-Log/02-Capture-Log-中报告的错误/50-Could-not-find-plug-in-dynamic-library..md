# Could not find plug-in dynamic library.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Could not find plug-in dynamic library.

#### Could not find plug-in dynamic library.

“无法找到插件动态库。”未在磁盘上找到指定的插件动态库。该错误会声明插件的名称。若在工程中使用了插件但未与游戏可执行文件进行静态链接，则将发生此错误。在出现此情况时，Wwise 会尝试查找对应的动态链接库文件（文件扩展名为 DLL、SO、BUNDLE 或 PRX，具体取决于平台）。

动态链接策略是可选的，游戏开发人员可根据个人偏好选择链接策略。不过，若 Wwise 工程中使用了插件，则其代码必须链接至游戏。请注意，可混合使用链接策略。比如，针对某些插件使用静态链接，针对其他插件使用动态链接。

**可能的原因：**

- 在静态链接时，未使用 AllPluginFactories.h（并无不妥），但缺少插件包含文件 (\*\*\*Factory.h) 或未链接库。
- 在动态链接时，未将动态链接库文件（文件扩展名为 .dll、.so、.bundle 或 .prx）部署至目标平台。
- 在动态链接时，未正确设置动态链接库搜索路径。在默认情况下，系统会自动正确设置。不过，有些实现人员希望通过  [`AkInitSettings::szPluginDLLPath`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_a65c27619257fb99581d3853016a434eb.html#a65c27619257fb99581d3853016a434eb) 进行手动更改。
- Unity 用户：更改 Wwise 工程时包含了新插件，但游戏版本未将所需 DLL 打包。

**推荐的解决步骤：**

- 确保游戏中有一个 .cpp 包含指定的插件 Factory 包含文件。确保静态链接对应的库。参阅 [集成详情 – 插件](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__plugins.html)。
- 若在游戏中更改了默认的 `AkInitSettings::szPluginDLLPath`，请确保该路径存在。
- 若使用动态链接，请确保所需动态链接库包含在打包/分发系统中，并安装到目标平台上。
- Unity 用户：重新构建游戏，并将缺失文件包含在内。

---