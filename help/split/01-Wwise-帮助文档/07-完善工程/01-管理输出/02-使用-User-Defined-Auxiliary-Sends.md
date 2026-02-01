# 使用 User-Defined Auxiliary Sends

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理输出](00-管理输出.md) > 使用 User-Defined Auxiliary Sends

## 使用 User-Defined Auxiliary Sends

In addition to the Audio Bus specified for the audio routing, every Interactive Music or Containers hierarchy object can specify up to four User-Defined Auxiliary Sends. 同样，Audio Bus 本身也可以具有最多四个 User-Defined Auxiliary Sends。辅助发送允许将音频信号的一部分发送到其他总线（即 Auxiliary Bus）中，进行并行处理。

用户定义的辅助总线用于在创作和编辑时直接定义静态辅助发送，游戏定义的辅助发送则与它不同，大多是通过在游戏中进行动态定义和控制。

下图显示了一个输出至 Audio Bus 的声音，总线上的辅助发送音量为 5dB，并且该声音还另有两个辅助发送。各个辅助发送都包含音量设置，并被连线至一条辅助发送总线。

|  |
| --- |
|  |

**添加用户定义的辅助发送**

1. 在 Project Explorer 中选择对象，察看该对象的属性。
2. 将一条辅助总线从工程浏览器中拖拽至用户定义的辅助发送列表，或

   点击浏览按钮 [...] 从 Project Explorer 列表中选择一个辅助总线。
3. 为所选的辅助总线设置发送音量

|  |  |
| --- | --- |
| [注意] | 注意 |
| 如果将总线发送至其自身的下级 Auxiliary Bus，则信号将被一系列相同的总线进行循环处理。这可能会导致延迟、音量异常巨大或产生其他不和谐音频效果。 |

  

### 使用 User-Defined Auxiliary Sends 控制游戏环境

辅助发送可以用于控制游戏中简单场景的环境效果。环境效果通常由密闭空间中的混响和早期反射声来决定。对于各个发声体，游戏可控制以下元素：

- **Send volume**（发送音量），对应湿声部分或反射声大小。
- **Output bus volume**（输出总线音量），对应干声部分或直达声大小。
- **Output bus low-pass filter**（输出总线低通滤波器），对应阻挡或封闭效果的多少，影响直达声或干声部分的频率响应。

通过将游戏参数关联至前两个值，您可以控制各个游戏对象干声信号和湿声信号的大小。之后游戏会计算听者和发声体之间的距离，并将该值指派至游戏参数。在游戏参数指派中，RTPC 曲线将定义信号的湿声和干声部分如何随距离而变化。

通过将游戏参数关联至输出总线的 Low-Pass Filter， 可以根据游戏参数来控制声音中多少高频会被阻挡或削弱。

---