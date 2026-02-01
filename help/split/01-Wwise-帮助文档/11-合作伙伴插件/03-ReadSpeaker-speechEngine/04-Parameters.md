# Parameters

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [合作伙伴插件](../00-合作伙伴插件.md) > [ReadSpeaker speechEngine](00-ReadSpeaker-speechEngine.md) > Parameters

## Parameters

您可以在用户界面中调节以下插件参数。

**Pitch**

|  |  |
| --- | --- |
| Min（最小值） | 50 |
| Max（最大值） | 200 |
| Default | 125 |

**Speed**

|  |  |
| --- | --- |
| Min（最小值） | 50 |
| Max（最大值） | 400 |
| Default | 125 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 平时使用读屏软件的玩家一般会用快速文本转语音阅读器。此设置允许玩家逐级设置诵读的速度，使用起来非常便捷。 |

**Pause**

在文本中出现自然停顿时插入停顿。延长或缩短的停顿包括：

- 句末
- 省略号 (...)

|  |  |
| --- | --- |
| Min（最小值） | 0 |
| Max（最大值） | 3000 (ms) |
| Default | 0 |

**Comma Pause**

在句子中使用逗号时插入停顿。

|  |  |
| --- | --- |
| Min（最小值） | 0 |
| Max（最大值） | 3000 (ms) |
| Default | 0 |

**Voice**

为特定对象设置发音人。可用语音分为不同的语言/变体（可选）/发音人。

所有语音均可预览。不过，在将语音导出到 SoundBank 时需要获取授权。

**语音合成标记语言 (SSML)**

启用/禁用 SSML 处理。

SSML 标记的结构跟 XML 标记类似，前后都要加尖括号 (<>)。其中包含标记名称和可选属性。标记名称定义修改类型，属性则提供具体的参数。

比如，对于 `<emphasis level="strong">This is important</emphasis>`，阅读器会着重强调其中的表述。

有关详细信息，请参阅[语音合成标记语言 (SSML)](https://cloud.google.com/text-to-speech/docs/ssml)。

即便没有在文本中插入标记，启用 SSML 也会略微增加语音合成过程中对性能的影响。

|  |  |
| --- | --- |
| [备注] | 备注 |
| `<audio>` 和 `<voice>` 标记不适用于此插件。 |

**Text**

调用对象时使用的默认文本（可通过 `SendPluginCustomGameData()` 更改）。

---