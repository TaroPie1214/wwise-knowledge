# Plug-in version doesn't match sound engine version. Ensure the plug-in is compatible with this version of Wwise.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Plug-in version doesn't match sound engine version. Ensure the plug-in is compatible with this version of Wwise.

#### Plug-in version doesn't match sound engine version. Ensure the plug-in is compatible with this version of Wwise.

“插件版本与声音引擎版本不匹配。请确保插件与此 Wwise 版本兼容”。此错误表示编译环境不理想或 Unity 集成不完善。如果近期升级了 Wwise，之后通常会发生此错误。任何类型的插件（Effect、Source 等）都包含游戏端使用的库，需要链接游戏代码。在游戏端插件代码与其余声音引擎库不匹配时，将出现此错误。请注意，游戏库仍可正确链接，但无法在运行时正常工作。

**可能的原因：**

- 因文件权限问题而未更新旧版本库。
- 在 Unity 中，通常因文件权限问题导致 Plugins 文件夹中留有旧的 DLL/SO/BUNDLE/PRX。
- 在 Unity 中，平台/移动端上留有旧的 DLL/SO/BUNDLE/PRX，导致无法使用新文件替换。

**推荐的解决步骤：**

- 查看 Wwise/SDK/[Platform]/lib 文件夹，并确认所有库的时间戳均相同。
- 在 Unity 中，查看 Wwise/Plugins/DSP 文件夹，并确认所有库的时间戳均相同。
- 清理并重新编译游戏。
- 清理目标平台/移动端上的部署文件夹，然后重新部署游戏。

---