# AK ASIO Input

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [源插件](00-源插件.md) > AK ASIO Input

## AK ASIO Input

|  |  |
| --- | --- |
| [注意] | 注意 |
| 此插件目前仍处于实验阶段。 |

（请参阅下文的 [“AK ASIO input properties”一节](01-AK-ASIO-Input.md#asio_input_plug_in_properties "AK ASIO input properties")。）

AK ASIO Input 插件可用于从兼容 ASIO 的设备输入声音。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 为了从相应设备捕获输入数据，必须配合 ASIO Audio Device ([“AK ASIO Output”一节](../01-Audio-Device-插件/01-AK-ASIO-Output.md "AK ASIO Output")) 来运行 AK ASIO Input。 |

### AK ASIO input properties

| 界面元素 | 描述 |
| --- | --- |
| **AK ASIO Input 属性** | |
| Channel Configuration | 声道配置。设置输入源的声道数及声道配置。有关详细信息，请参阅[“了解总线配置”一节](../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。 |
| Base Channel | 基准声道。对各输入声道进行偏置，以便将第一个输入声道设为基准声道。 |

### Example of different properties

下图阐释了声道配置和基准声道属性会对输入产生怎样的影响。本例适用于包含两个输入的设备，其声音将输出到 4.0 总线。

|  |
| --- |
|  |

**相关主题**

- [“AK ASIO Output”一节](../01-Audio-Device-插件/01-AK-ASIO-Output.md "AK ASIO Output")

---