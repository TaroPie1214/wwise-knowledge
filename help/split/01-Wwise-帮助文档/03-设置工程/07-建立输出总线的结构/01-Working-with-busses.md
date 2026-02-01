# Working with busses

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [建立输出总线的结构](00-建立输出总线的结构.md) > Working with busses

## Working with busses

### 添加总线

To create the structure for your audio routing, you can add Audio Busses to the
Main Audio Bus. You can also create other main busses to mix for other outputs.
When using Motion, you should also create a main bus for motion devices, and route
all sounds (motion is only low-frequency audio) to a bus in that hierarchy. After
you have created a child bus under the main bus, you can create any number of
parent and child busses to build your routing structure.

**To add a child bus in the Busses hierarchy:**

1. 在 Project Explorer 的 Audio 选项卡中，右键点击您要为其创建新父总线子的总线。
2. 从菜单中，选择以下选项之一：

   - **New Child > Audio Bus**（新建子项 > 音频总线）。
   - **New Child > Auxiliary Bus**（新建子项 > 辅助总线）。

   The new child bus is added to the Busses hierarchy.

**To create a parent bus in the Busses hierarchy:**

1. 在 Project Explorer 的 Audio 选项卡中，右键点击您要为其创建新父总线的总线。
2. 从菜单中，选择以下选项之一：

   - **New Parent > Audio Bus**（新建父项 > 音频总线）。
   - **New Parent > Auxiliary Bus**（新建父项 > 辅助总线）。

   The new parent bus is added to the Busses hierarchy.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 辅助总线不能位于层级结构的顶部。因此在层级顶部，New Parent > Auxiliary Bus 选项将禁用。 |

A Main Audio Bus can be added to any Work Unit or Virtual Folder in the Busses
Hierarchy, as long as there's no Main Audio Bus above that location in the
hierarchy.

**To add a new Main Audio Bus in the Busses hierarchy:**

1. In the Audio tab in the Project Explorer, right-click on a Work Unit or
   virtual folder in the Busses hierarchy.
2. 从菜单中，选择以下选项之一：

   - **New Child > Audio Bus**（新建子项 > 音频总线）。

   The new Main Audio Bus is added to the Busses hierarchy.

添加总线的另一种方法是，复制现有总线并将其粘贴至所需位置。

**To copy and paste an audio bus in the Busses hierarchy:**

1. In the Audio tab in the Project Explorer, right-click the desired bus in
   the Busses hierarchy.
2. 在菜单中，选择 **Copy**（复制）或按下 Ctrl+C。
3. Select another bus in the Busses hierarchy under which you'd like
   to paste the copied bus.
4. 在菜单中，选择 **Paste**（粘贴）或按下 Ctrl+V。

   这时将创建一条与所复制总线的设置完全相同的新总线，并在其名称结尾后缀 \_## 以示区分。

### 移动总线

在已添加总线之后，您可能会需要更改总线的位置以产生总线之间的不同关系。

**To move a bus to another location in the Busses hierarchy:**

1. 将总线拖动到所需位置。

   总线及其子总线都会移动到新位置。通过更改位置，移动后的总线现在将受其新父属性影响。

### 删除总线

如果您不小心创建了错误的总线或不再需要特定总线，则可以删除它。在删除一条总线时，其所有子总线也会被删除。连接到该总线上的对象现在已重新指派给该层级结构中的下一个父对象。对象重新指定通路后，其不沿用父对象（Override Parent）的属性保持不变。

下图说明了在删除某条总线后，会对该总线上传输的声音对象造成的影响。

|  |
| --- |
|  |

**To delete a bus in the Busses hierarchy:**

1. 在 Project Explorer 的 Audio 选项卡中，选择要删除的总线，然后执行以下操作之一：

   - 按 **Delete** 键。
   - 在总线的快捷菜单中，选择 **Delete Selection**（删除选中项）。
2. 总线及其子总线可能会被删除，之前连接到删除的总线上的对象现在会连接到父总线上进行传输。

---