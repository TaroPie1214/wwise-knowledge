# Pinning objects in the Transport Control

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [认识 Transport Control 视图](00-认识-Transport-Control-视图.md) > Pinning objects in the Transport Control

## Pinning objects in the Transport Control

Transport Control 自动加载 Property Editor 中当前显示的任何对象。但是，当您在 Project Explorer 中选择任何对象或事件时，在默认情况下，它将替代 Transport Control 中的内容。如果您希望无论您选择任何其它内容，Transport Control 中都会一直将对象保持为加载状态，则您可以固定（pin）该对象来阻止加载其它对象。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在实时混音时，您需要将对象加载到 Transport Control 中，以使针对该对象的相对属性的更改生效。确保在实时混音之前未固定对象。 |

### Using pinning - example

假设您正在试听 Random Container，很想知道混响效果器对于容器中特定对象的声音效果。您可以将对象固定（pin）在 Transport Control 中。然后在 Property Editor 中对父对象应用混响，单独试听该对象的效果。如果您不固定对象，则容器中的所有对象将以随机模式播放，并且您想试听的对象可能不会播放。通过固定对象，您可以修改父级设置，然后随时再次试听对象。

**固定 Transport Control 中加载的对象的方法是：**

1. 将对象加载到 Transport Control 中。
2. 在 Transport Control 中，点击 **Pin**。

   Pin 图标将变成红色，即使您将其他对象或事件加载到 Property Editor 中或者在 Project Explorer 中选择另一个对象，此对象或事件仍将保留在 Transport Control 中。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 按 **Ctrl+Alt+P** 以加载对象并将它固定在 Transport Control。要取消固定对象，则按 **Ctrl+P**。 |

---