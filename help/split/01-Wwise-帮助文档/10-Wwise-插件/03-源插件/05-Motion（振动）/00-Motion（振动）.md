# Motion（振动）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > Motion（振动）

## Motion（振动）

Motion 插件是一款源插件，其可用于为游戏所用不同设备（包括游戏控制器）生成振动效果。通过 Motion 插件，您可以为游戏所用不同振动设备的各个促动器应用不同的 Driver（驱动器）曲线。通过综合运用 Driver 偏置、State（状态）偏置和 RTPC 曲线，这八个 Driver 声道可定义振动效果的强度和时长。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 请不要将高通滤波器应用于振动对象。因为振动设备只会生成低频信号，所以所有高通滤波器都会抑制振动效果。 |

您可能注意到了 Source Editor（源编辑器）中的一些属性值旁边带有标志。该标志表明属性值是否通过 RTPC 与 Game Parameter 关联。

以下表格介绍了两种 RTPC 标志：

| 标志 | Name | 描述 |
| --- | --- | --- |
| |  | | --- | |  | | RTPC - 开启 | 属性值已使用 RTPC 绑定到游戏中的参数值。 |
| |  | | --- | |  | | RTPC - 关闭 | 属性值未与游戏中的参数值绑定。 |

**编辑器**

- [“Source Editor：Motion”一节](01-Source-Editor：Motion.md "Source Editor：Motion")
- [“Contents Editor：Motion”一节](02-Contents-Editor：Motion.md "Contents Editor：Motion")

---