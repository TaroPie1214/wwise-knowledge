# Game Parameter Settings

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Game Syncs 选项卡](../../00-Game-Syncs-选项卡.md) > [Game Parameters](../00-Game-Parameters.md) > [Game Parameter Property Editor](00-Game-Parameter-Property-Editor.md) > Game Parameter Settings

##### Game Parameter Settings

Modifying the Min or Max value of a Game Parameter affects the RTPC curves and blend
tracks that use that game perimeter for their X axes.

| 界面元素 | 描述 |
| --- | --- |
| Min（最小值） | 最小值。映射至 Wwise 中属性的 Game Parameter 最小值。 |
| Max（最大值） | The maximum value of the Game Parameter that is mapped to properties in Wwise. |
| Stretch | All items are kept, but their X positions might change as the curve/bend blend track is stretched or compressed to match the new range in X. Values of Set Game Parameter actions are also scaled. |
| Preserve X | Maintains the position of all items, but those that fall outside the new range are deleted. Values of Set Game Parameter actions are clamped. |

---