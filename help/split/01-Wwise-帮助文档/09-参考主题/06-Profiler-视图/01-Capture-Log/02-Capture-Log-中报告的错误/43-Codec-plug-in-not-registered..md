# Codec plug-in not registered.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Codec plug-in not registered.

#### Codec plug-in not registered.

“未注册编解码器插件”。未找到要求用于解码声音的编解码器插件。将不会播放声音。在使用 AllPluginFactories.h 时，默认包含所有编解码器，但可以自行选择。

**可能的原因：**

- 未使用 AllPluginFactories.h（并无不妥），但缺少编解码器包含文件 (\*\*\*Factory.h) 或未链接库。

**推荐的解决步骤：**

- 确保游戏中有一个 CPP 包含指定的编解码器 Factory 包含文件。确保静态链接对应的库。参阅[集成详情 – 插件](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__plugins.html)。

---