# Configuring the positioning timeline

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [认识时间线](00-认识时间线.md) > Configuring the positioning timeline

## Configuring the positioning timeline

在创建空间路径时，需要定义对象沿路径传输的时间。Position Editor 时间线可让您指定各个控制点所对应的时间。与坐标图视图一样，您可以缩放和平移时间线，以便更加准确地定位控制点。您还可以为您创建的各条路径配置时间线长度。

您可以配置时间线的属性和行为。例如，您可以指定时间线的长度或者定义时间线上的控制点在添加新控制点时的行为。时间线的长度自动定义选定路径的长度。您可以配置时间线，使您创建的各条路径具有不同的时长。

When the timeline is in linear mode, you can only define the length of the timeline
because the behaviors of the points on the timeline are predetermined.

**To configure the timeline:**

1. 在 Position Editor (3D Automation) 中，单击 **Configure Timeline**（配置时间线）按钮。

   The Timeline Configuration dialog opens.
2. 在 Length 字段中，以 mm:ss.ms 为格式输入时间线的时长。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 时间线的最大长度为 59:59:999。 |
3. 如果您要更改时间线的长度，并且时间线处于非线性模式下，则选择以下其中一个选项：

   - **Stretch proportionally** -- 按比例拉伸。重新定位现有控制点，使它们之间保持相对比例。
   - **Preserve key values** -- 保留关键值。保持现有控制点的位置。

     |  |  |
     | --- | --- |
     | [备注] | 备注 |
     | 如果您使用 Preserve key values 选项来缩短时间线的长度，则某些控制点可能会被删除。如果准备删除控制点，则删除前会显示确认消息。 |
4. 在 Insert Key Every 字段中，输入您要在上一个现有控制点与时间线上插入的任何新控制点之间添加的时间量。
5. 点击 **OK** 以接受更改。

   时间线于是按照新的设置进行重新配置。

---