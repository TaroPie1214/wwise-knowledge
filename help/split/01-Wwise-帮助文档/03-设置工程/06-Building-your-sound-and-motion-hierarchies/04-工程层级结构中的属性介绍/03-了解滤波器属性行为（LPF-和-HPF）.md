# 了解滤波器属性行为（LPF 和 HPF）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [Building your sound and motion hierarchies](../00-Building-your-sound-and-motion-hierarchies.md) > [工程层级结构中的属性介绍](00-工程层级结构中的属性介绍.md) > 了解滤波器属性行为（LPF 和 HPF）

### 了解滤波器属性行为（LPF 和 HPF）

用户可将滤波器属性（如 Low-Pass filter 和 High-Pass filter）的累计行为设为以下两种方式之一：

- **Sum All Values**（累加所有值）：将属性值加在一起。
- **Use Highest Value**（使用最大值）：保留最大的属性值。

滤波器行为是针对整个工程定义的，其会应用于以下所列属性。

- Low-pass filter（低通滤波器）。
- High-pass filter（高通滤波器）。
- Output Bus Low-pass filter（输出总线低通滤波器）。
- Output Bus High-pass Filter（输出总线高通滤波器）。
- User-defined Auxiliary LPF 0（用户定义的辅助发送 LPF 0）。
- User-defined Auxiliary LPF 1（用户定义的辅助发送 LPF 1）。
- User-defined Auxiliary LPF 2（用户定义的辅助发送 LPF 2）。
- User-defined Auxiliary LPF 3（用户定义的辅助发送 LPF 3）。
- Game-defined Auxiliary Sends LPF（游戏定义的辅助发送 LPF）。
- User-defined Auxiliary HPF 0（游戏定义的辅助发送 HPF 0）。
- User-defined Auxiliary HPF 1（游戏定义的辅助发送 HPF 1）。
- User-defined Auxiliary HPF 2（游戏定义的辅助发送 HPF 2）。
- User-defined Auxiliary HPF 3（游戏定义的辅助发送 HPF 3）。
- Game-defined Auxiliary Sends HPF（游戏定义的辅助发送 HPF）。

若要配置工程的滤波器行为，请参阅“[“配置滤波器行为”一节](03-了解滤波器属性行为（LPF-和-HPF）.md#configuring_filter_behavior "配置滤波器行为")”。

下图展示了属性值会如何在工程层级结构内累计。

![](../../../../../images/dgm_hierarchy_properties_filter_behavior.png)

|  |  |
| --- | --- |
| **滤波器累计方式**。在本例中，我们为每个对象指定了 LPF 属性值。最终应用于声音的 LPF 值取决于所选的累计方式。 | |
|  | **Sum All Values**。将各个对象的 LPF 属性值加在一起。 |
|  | **Use Highest Value**。使用对象 LPF 属性值当中的最大值。 |

#### 配置滤波器行为

滤波器行为可通过 Project Settings（工程设置）来指定。

|  |  |
| --- | --- |
| [注意] | 注意 |
| 在更改滤波器行为时，Wwise 将执行以下操作：  - 修改 Work Unit 来针对滤波器属性调节 RTPC 曲线和 State 值。 - 保存、关闭并重新加载工程。  对 Work Unit 所作的修改无法撤消。若想稍后加以恢复，请确保在更改滤波器行为前保存工程副本。 |

**配置滤波器行为：**

1. 通过执行以下任一操作来打开 Project Settings 对话框：

   - 在 **Project**（工程）菜单中，选择 **Project Setting**。
   - 按 **Shift+K**。
2. 切换到 General（常规）选项卡。
3. 在 **Filter Behavior**（滤波器行为）分组中，选择所需滤波器行为：

   - **Sum All Values (Default)**。将滤波器属性值加在一起。
   - **Use Highest Value**。使用最大的滤波器属性值。
4. 点击 **OK** 以应用这些设置。

---