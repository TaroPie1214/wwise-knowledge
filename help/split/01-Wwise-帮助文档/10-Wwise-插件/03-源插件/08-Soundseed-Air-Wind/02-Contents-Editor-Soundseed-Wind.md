# Contents Editor: Soundseed Wind

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Soundseed Air Wind](00-Soundseed-Air-Wind.md) > Contents Editor: Soundseed Wind

### Contents Editor: Soundseed Wind

您可以通过 Contents Editor 快速访问 Soundseed Wind 插件的一些最常用的属性。必须点击 Soundseed Wind 源才能显示相关的列标题。

要了解 Soundseed Wind 插件的概况，请参阅[“Soundseed Air Wind”一节](00-Soundseed-Air-Wind.md "Soundseed Air Wind")。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。Soundseed Wind 插件的名称。 |
| Use | 采用。决定声音对象内的哪个源将会被：  - 将被播放。 - 将被包括在 SoundBank 中。 - 此选项仅在声音对象内具有多个源时才可见。 |
| Notes | 备注。Soundseed Wind 插件的其它相关信息。 |
| Wind Speed | 风速。风的平均速度。风速会使场景中的导流体产生音高偏置。  Default value: 0  Range: -2400 to 2400 |
| Direction | 风向。风移动的路径或路线。0 度值表示风从正面（即北）吹来，180 度或 -180 度值表示风从背面（即南）吹来。  默认值：0  滑杆范围：-180 至 180  单位：度 |
| Variability | 多样性。因阵风造成的风速相对于时间的变化量。  默认值：0.25  滑杆范围：0 至 1 |
| Gustiness | 阵风。风的加速度随时间变化的可能性。  默认值：0.5  滑杆范围：0 至 1 |
| Gain Offset | 增益偏置。全局属性，定义所有导流体增益的偏置量。该属性可以用作主增益控制。  Default value: 0.0  Range: -96.3 to 24.0  Units: dB |
|  | 向声音对象中添加新的源。  当您点击 **Add Source**（添加源）按钮时，会显示一个可以添加的[*源插件*](../00-源插件.md "源插件")列表。 |

---