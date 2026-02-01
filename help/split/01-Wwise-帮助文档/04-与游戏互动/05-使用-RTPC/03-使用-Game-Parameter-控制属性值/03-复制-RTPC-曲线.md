# 复制 RTPC 曲线

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 RTPC](../00-使用-RTPC.md) > [使用 Game Parameter 控制属性值](00-使用-Game-Parameter-控制属性值.md) > 复制 RTPC 曲线

### 复制 RTPC 曲线

在工程中，有时候您会希望跨属性甚至跨对象使用 RTPC 曲线。与其分别创建各条曲线，您可以先定义曲线形状，然后将它复制粘贴到同一对象的另一属性中，甚至工程中其它对象的属性中。

RTPC 曲线可以复制到 Wwise 的以下区域：

- RTPC tab of objects and busses within the Busses and Containers hierarchies.
- 效果的 RTPC 选项卡。
- 源插件的 RTPC 选项卡。
- Blend Track Editor。

**复制对象内和对象之间的 RTPC 曲线的方法是：**

1. 从曲线列表中选择您要复制的曲线。

   |  |
   | --- |
   |  |
2. 执行以下操作之一：

   - 右键点击选定的曲线，然后从菜单中选择 **Copy**。
   - 按 **Ctrl+C**。
3. 执行以下操作之一：

   - 右键点击并从菜单中选择 **Paste**。
   - 按 **Ctrl+V**。

   此时列表中被添加了一条完全一致的 RTPC 曲线。

   |  |
   | --- |
   |  |

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | To paste one or more curves within another object in your project, simply load the new object into the Property Editor, switch to the RTPC tab of the Primary Editor, and then proceed with Step 3. |
4. 点击选择器开关（**>>**），并从列表中选择任意属性。

   此时选定的属性就应用到曲线形状上了。

   |  |
   | --- |
   |  |

---