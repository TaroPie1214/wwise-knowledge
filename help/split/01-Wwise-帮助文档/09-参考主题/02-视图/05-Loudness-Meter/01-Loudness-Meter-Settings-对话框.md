# Loudness Meter Settings 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > [Loudness Meter](00-Loudness-Meter.md) > Loudness Meter Settings 对话框

### Loudness Meter Settings 对话框

Loudness Meter Settings（响度表设置）对话框由两列组成，一列是设置，另一列是各自的值。

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **显示选项：** | |
| Target Level | 目标电平。定义目标电平值，显示为绿色。此值还将定义 LUFS 到 LU 的转换函数。  EBU 建议值：-23 LUFS |
| Target Range | 目标范围。定义目标区域范围（绿色）。例如，具有 -23 LUFS 目标电平的1 LU 目标范围定义 -24 至 -22 的绿色区域。  EBU 建议值：1 LU  索尼全球工作室音频标准工作组（ASWG）建议值：2 LU |
| Target Extended Range | 目标扩展范围。定义扩展区域的范围（黄色） |
| Scale | 尺度。标准：-18 LU 至 +9 LU（-41 LUFS 至 -14 LUFS）  扩展：-36 LU 至 +18 LU（-59 LUFS 至 -5 LUFS） |
| Unit（单位） | LU（响度单位）：目标电平为 0 LU  LUFS （响度单位满量程）：目标电平由目标电平指定（默认值为 -23 LUFS）。 |
| **按钮：** | |
|  | 将设置复位至默认的 EBU R128 建议值。 |
|  | 应用您对 Loudness Meter Setting 所做的更改并关闭该对话框。 |

---