# 将 Wwise 属性指派给游戏参数

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 RTPC](../00-使用-RTPC.md) > [使用 Game Parameter 控制属性值](00-使用-Game-Parameter-控制属性值.md) > 将 Wwise 属性指派给游戏参数

### 将 Wwise 属性指派给游戏参数

创建 Game Parameter 并定义它们的取值范围后，可以考虑将哪些游戏参数指派给哪些属性。

在将属性指派给 Game Parameter、Modulator 或 MIDI 对象后，将发生以下情况：

- 坐标图视图中显示 X 轴和 Y 轴。
- 坐标图视图中创建默认 RTPC 曲线。
- 属性值旁边的 RTPC 图标变为主题指定颜色（Classic 中为蓝色，Dark 中为橙色）。

![](../../../../../images/rtpc_indicator.png)

|  |  |
| --- | --- |
|  | 使用了 RTPC。 |
|  | 未使用 RTPC。 |

**将对象属性指派给游戏参数的方法是：**

1. 将对象、总线、Effect（效果器）或 Attenuation（衰减）实例加载到编辑器中。
2. 切换到 RTPC 选项卡。
3. 点击选择器按钮（**>>**），然后从列表中选择属性。

   新的 RTPC 曲线于是被创建，并被指定唯一的颜色。此时 Wwise 属性也被指派给坐标图视图中的 Y 轴。
4. 从 X Axis（X 轴）列表中选择您要指派给 Wwise 属性的游戏参数。

   游戏参数被指派给图形视图中的 X 轴。

#### 快速添加 RTPC

您可以将 RTPC 添加到任何具有活跃 RTPC 图标的属性。

**快速添加 RTPC：**

1. 找到具有活跃 RTPC 图标的属性，并右键单击文本框、滑杆或旁边的[标志图标](../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md "使用 Property Editor")。

   此时将会显示快捷菜单。
2. 在菜单中，选择 **Add RTPC**（添加 RTPC）。

   此时将打开子菜单并显示五个不同的 RTPC 对象选项（Game Parameters、MIDI、LFO、Envelope 和 Time）。
3. 选择符合 RTPC 需要的选项。

   此时将显示下一级子菜单。在此可选择新建 RTPC 对象、选择现有对象或浏览并查找特定对象。

   |  |
   | --- |
   |  |
4. 选择或创建 RTPC 对象。

   此时将转到 RTPC 选项卡，并在视图中高亮显示刚刚添加的 RTPC 对象。您可以根据需要进行编辑。

---