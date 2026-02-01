# AK Channel Router

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > AK Channel Router

## AK Channel Router

|  |  |
| --- | --- |
| [注意] | 注意 |
| 此插件目前仍处于实验阶段。 |

（请参阅下文的 [“AK Channel Router properties”一节](02-AK-Channel-Router.md#channel_router_plug_in_properties "AK Channel Router properties")。）

AK Channel Router 效果器插件可将多个采用不同声道配置的声音或总线混音并输出到单个总线。这在 Audio Device（音频设备）具有多个声道且需要非标准输出配置时特别有用。

在总线上插入此效果器后，可将 Channel Router Settings 元数据添加到任意子总线或输出到该总线的声音来配置子总线所输出到的声道。对于没有此元数据的子总线，将使用默认值 1。若有多个总线或声音输出到同一声道，则会将这些声道下混成单声道。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 此插件仅可插入到将 **Bus Configuration** 设为 **Audio Objects** 的总线上。所以，该插件无法插入到顶层总线上。 |

### Example usage

比方说，为 "Bus A" Audio Bus（音频总线）所输出到的 Audio Device（音频设备）包含 16 个声道，然后希望在前 8 个声道 (1 ~ 8) 输出 7.1 内容，接着在中间 4 个声道 (9 ~ 12) 输出 4.0 内容，最后在其余 4 个声道 (13 ~ 16) 输出无声内容。

1. 在 Bus A 所对应 Property Editor（属性编辑器）的 General Settings（常规设置）选项卡中，将 **Bus Configuration**（总线配置）设为 **Audio Objects**（音频对象）。
2. 在 Effects（效果器）选项卡中，添加 AK Channel Router 效果器插件。
3. 在 Bus A 下新建一条子 Audio Bus，并将其命名为 Audio Bus 7-1。
4. 在与 Audio Bus 7-1 对应的 Property Editor 中执行以下操作：

   1. 在 General Settings（常规设置）选项卡中，将 **Bus Configuration**（总线配置）设为 **7.1**。
   2. 在 Metadata（元数据）选项卡中，添加 Channel Router Settings 元数据。

      将 Channel Router Settings 元数据的 **Channel**（声道）属性保留设为 **1**，以此来将此子总线的输出输出到父总线的声道 1-8。
5. 在 Bus A 下另建一条子 Audio Bus，并将其命名为 Audio Bus 4-0。
6. 在与 Audio Bus 4-0 对应的 Property Editor 中执行以下操作：

   1. 在 General Settings（常规设置）选项卡中，将 **Bus Configuration**（总线配置）设为 **4.0**。
   2. 在 Metadata（元数据）选项卡中，添加 Channel Router Settings 元数据。
   3. 将 Channel Router Settings 元数据的 **Channel**（声道）属性保留设为 **9**，以此来将此子总线的输出输出到父总线的声道 9-13。

### AK Channel Router properties

| 界面元素 | 描述 |
| --- | --- |
| **总线属性** | |
| Bus Configuration | 总线配置。覆盖 Property Editor 中所选的总线配置。在默认情况下，会将此项设为使用与总线输出所输出到的 Audio Device 相同的总线配置。 |
| **元数据属性** | |
| Channel | 声道。决定输出总线的哪个声道会接收声音或总线的第一个输出声道。AK Channel Router 效果器必须插入到输出总线上。  比如，在将立体声声音的 Channel 属性设为 3 时，会输出到对应输出总线的声道 3 和 4。 |

---