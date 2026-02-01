# Contents Editor: Soundseed Woosh

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Soundseed Air Woosh](00-Soundseed-Air-Woosh.md) > Contents Editor: Soundseed Woosh

### Contents Editor: Soundseed Woosh

您可以通过 Contents Editor 快速访问与 Soundseed Air (Woosh) 插件中的最常用属性。您必须点击 Soundseed Air (Woosh) 源才能显示相关联的列标题。

要了解 Soundseed Woosh 插件的概况，请参阅[“Soundseed Air Woosh”一节](00-Soundseed-Air-Woosh.md "Soundseed Air Woosh")。

| 界面元素 | 描述 |
| --- | --- |
| Name | Tone Generator 插件的名称。 |
| Use | 采用。决定声音对象内的哪个源将会被：  - 将被播放。 - 将被包括在 SoundBank 中。 - 此选项仅在声音对象内具有多个源时才可见。 |
| Speed | 运动速度最快的导流体的平均速度。运动速度最快的导流体是距锚点（如果存在）最远的导流体。  对象速度将使场景中导流体产生能量偏置。该属性定义了移动速度对导流体共振频率造成的影响。  默认值：0  滑杆范围：-50 至 50 |
| Frequency Shift | 频率偏移。全局属性，定义所有导流体中心频率的上下偏移量。例如，值为 1 时，中心频率将加倍，而值为 -1 时，中心频率减半。  Default value: 0.0  Range: -4.0 to 4.0 |
| Q Factor Shift | 品质因数。全局属性，定义所有导流体 品质因数的上下偏移量。例如，值为 1 时，品质因数将加倍，而值为 -1 时，品质因数将减半。  Default value: 0.0  Range: -4.0 to 4.0 |
| Gain Offset | 增益偏置。全局属性，定义了所有导流体增益的偏置量。该属性可以用作主增益控制。  Default value: 0.0  Range: -96.3 to 24.0  Units: dB |
| Notes | 备注。有关 Soundseed Woosh 插件的其它信息。 |
|  | 向声音对象中添加新的源。  当您点击 **Add Source**（添加源）按钮时，会显示一个可以添加的[*源插件*](../00-源插件.md "源插件")列表。 |

---