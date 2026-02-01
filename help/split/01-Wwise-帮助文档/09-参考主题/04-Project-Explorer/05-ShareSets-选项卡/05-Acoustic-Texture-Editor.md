# Acoustic Texture Editor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [ShareSets 选项卡](00-ShareSets-选项卡.md) > Acoustic Texture Editor

### Acoustic Texture Editor

在 Acoustic Texture Editor（声学材质编辑器）中，可定义 Acoustic Texture 的属性。

| 界面元素 | 描述 |
| --- | --- |
| Name | Acoustic Texture 的名称。 |
| Shared by | 共享对象。当前采用所选共享集的对象列表。 |
| Notes | 备注。Acoustic Texture 的其它信息。 |
| **声学材质设置** | |
| Frequency Absorption | 频率吸收。相应频率范围内声音的吸收百分比。以下各个频段对应的可调百分比滑块 (0 ~ 100) 会受到底部全局滑块 (-100 ~ 100%) 偏置影响，生成最终的百分比值 (-100 ~ 200)，并显示在频段滑块右侧方框中。  在应用 [“Reflect”一节](../../../10-Wwise-插件/04-效果器插件/19-Reflect.md "Reflect") 时，负值视为零。它表示无吸收的全反射，而非共振反射。  |  |  | | --- | --- | | [备注] | 备注 | | 虽然上述定义显示不同吸收频段之间存在明确界限，但是实际上频段会有一定的重叠。 |  The Hz values for each band are defined by the plug-in, such as Reflect, that works with the Acoustic Texture.  **Material Filtering** in the Reflect plug-in is by default set to Favor Performance, which uses four times less CPU. You can change this setting to Favor Quality in the [“Reflect properties”一节](../../../10-Wwise-插件/04-效果器插件/19-Reflect.md#wwise_reflect_properties "Reflect properties"). |
| **频段** | |
| Absorption Low | 吸收低频。低于 Mid Low 频段的所有频率。  Default value: 0  Range: 0 to 100 |
| Absorption Mid Low | 吸收中低频。所有低于 Mid High 频段但高于 Low 频段的频率。  Default value: 0  Range: 0 to 100 |
| Absorption Mid High | 吸收中高频。所有低于 High 频段但高于 Mid Low 频段的频率。  Default value: 0  Range: 0 to 100 |
| Absorption High | 吸收高频。高于 Mid High 频段的所有频率。  Default value: 0  Range: 0 to 100 |
| Absorption Offset | 吸收偏置。该滑块用于将以上所有频段的滑块移动相同的值，从而对吸收百分比进行偏置。  Default value: 0  Range: -100 to 100 |

When using the Reflect plug-in and Material Filtering is set to Favor Performance in the [“Reflect properties”一节](../../../10-Wwise-插件/04-效果器插件/19-Reflect.md#wwise_reflect_properties "Reflect properties"), the Absorption Mid Low and Absorption Mid High together parameterize a single mid-absorption. This mid-absorption is calculated as sqrt(Absorption Mid Low \* Absorption Mid High). For example, if Absorption Mid Low is 4 and Absorption Mid High is 25, the mid-absorption is 10 when Material Filtering is set to Favor Performance.

---