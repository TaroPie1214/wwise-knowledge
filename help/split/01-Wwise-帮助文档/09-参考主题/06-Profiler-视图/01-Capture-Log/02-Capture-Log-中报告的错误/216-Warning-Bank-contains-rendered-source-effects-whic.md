# Warning: Bank contains rendered source effects which can't be edited in Wwise.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Warning: Bank contains rendered source effects which can't be edited in Wwise.

#### Warning: Bank contains rendered source effects which can't be edited in Wwise.

“警告: 音频包所含源插件的效果器经过渲染后，无法在 Wwise 中编辑源插件”。此错误表示曾尝试实时修改 Source（源）插件的参数，而该插件被标记为 Render（渲染）。修改已标记为 Render 的 Effect（效果器）插件也会发生此错误。这些插件在生成 SoundBank（音频包）时已内嵌在音频中，因此无法进行实时编辑。

这只是一条警告消息。在下次生成 SoundBank 时，会采用新的参数设置。

---