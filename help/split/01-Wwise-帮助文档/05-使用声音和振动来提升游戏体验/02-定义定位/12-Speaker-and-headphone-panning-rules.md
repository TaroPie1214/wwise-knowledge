# Speaker and headphone panning rules

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [定义定位](00-定义定位.md) > Speaker and headphone panning rules

## Speaker and headphone panning rules

In Wwise there are two different panning rules: speaker and headphone. By default, all platforms use the speaker panning rule with the exception of portable consoles (such as Android and iOS), which use the headphone panning rule. 两种模式之间的差异很小，但有助于提供逼真、准确的音频体验；具体取决于您的聆听方式。此设置可以在 Wwise 中试听，也可以在游戏中运行时设置。

|  |
| --- |
|  |

|  |
| --- |
|  |

试听这两种模式的方法是：

- From the menu bar, click **Audio > Main Mix Channel Configuration > 2.0 (Speaker Panning)**
- From the menu bar, click **Audio > Main Mix Channel Configuration > 2.0 (Headphone Panning)**

|  |  |
| --- | --- |
| [备注] | 备注 |
| To set the panning rule in the game, refer to [AK::SoundEngine::SetPanningRule](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a3e61f70b39d53dd7b8350f2696d9c59e.html) in the SDK documentation. |

---