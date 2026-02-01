# Plug-in not found.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Plug-in not found.

#### Plug-in not found.

“未找到插件”。此错误表示游戏所加载的 SoundBank（音频包）使用了未知的源、效果器、混音器或 sink 插件。因此，无法找到可执行此插件的代码。

**可能的原因：**

- 游戏代码无法与插件库建立静态链接。所有 Unreal 游戏和大部分自研引擎都可能出现此问题。
- 游戏无法找到插件动态库（DLL 或 SO）。所有 Unity 游戏和部分自研引擎都可能出现此问题。
- 游戏因缺少依赖关系而无法加载插件动态库（DLL 或 SO）。查看相关插件文档中的要求。
- SoundBank 没有更新。
- SoundBank 已损坏。
- Init.bnk 没有加载调用 `AK::SoundEngine::GetDeviceList` 的插件，或者没有通过 `AK::SoundEngine::RegisterPlugin` 显式调用该插件。

**推荐的解决步骤：**

- 若游戏与 Wwise 库静态链接，请确认游戏的 #include "ThePluginFactory.h" 和链接选项。详见：  [集成详情 – 插件](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine__integration__plugins.html)
- 若游戏使用动态链接（比如 Unity），请重新生成 SoundBank 并构建游戏。
- 重新生成 SoundBank，并重新打包到游戏中（包括 Init.bnk）。
- For sink plug-ins, verify that a ShareSet for this plug-in is associated with at least one main bus.

---