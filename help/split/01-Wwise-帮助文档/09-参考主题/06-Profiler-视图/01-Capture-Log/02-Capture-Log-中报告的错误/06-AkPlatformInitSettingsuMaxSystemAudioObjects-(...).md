# AkPlatformInitSettings::uMaxSystemAudioObjects (...) does not meet minimum requirement of ... System Audio Objects. System Audio Objects will be mixed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AkPlatformInitSettings::uMaxSystemAudioObjects (...) does not meet minimum requirement of ... System Audio Objects. System Audio Objects will be mixed.

#### AkPlatformInitSettings::uMaxSystemAudioObjects (...) does not meet minimum requirement of ... System Audio Objects. System Audio Objects will be mixed.

“AkPlatformInitSettings::uMaxSystemAudioObjects (...) 不符合…系统音频对象的最低要求。将对系统音频对象实施混音。”在当前配置下，要有一定数量的 Audio Object，系统才能正常运行。不过，初始化设置对此数量做了限制。虽然限制 Audio Object 的数量是个很好的做法，但要满足最低要求才能按照预期播放所有声音。所有超出限值的 3D Audio Object 声音都将在音频 Bed 中实施混音。

注意，这其实不能所作错误，而只是表明当前设置并非最优的。

**推荐的解决步骤：**

- 检查工程中所用的 3D 对象数量，并根据需要增大 [`AkPlatformInitSettings::uMaxSystemAudioObjects`](https://www.audiokinetic.com/library/edge/?source=SDK&id=windows__ak_platform_init_settings.html)。

---