# 在 SoundBank 中启用/弃用工程元素

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [完善工程](../../../00-完善工程.md) > [管理 SoundBank](../../00-管理-SoundBank.md) > [使用 User-defined SoundBank](../00-使用-User-defined-SoundBank.md) > [管理 SoundBank 内容](00-管理-SoundBank-内容.md) > 在 SoundBank 中启用/弃用工程元素

#### 在 SoundBank 中启用/弃用工程元素

在将 Event 或声音结构添加到 SoundBank 时，Wwise 会自动启用所有相应的 Event、声音结构和音频文件。鉴于对游戏使用的 SoundBank 策略，您可能会想从 SoundBank 中移除所有 Event、声音结构或媒体文件。

##### 示例 – 在 SoundBank 中启用/弃用工程元素

假设您拥有一个包含以下工程元素的小工程：

- 两个随机容器
- 六个声音对象
- 六个音频文件
- 两个播放 Event

您打算在调用 Event 前先通过 Prepare Event 来动态加载媒体文件，因此希望为工程中的所有 Event 构建一个 SoundBank。在这种情况下，您可以先创建 SoundBank，然后将两个 Event 拖到 SoundBank Editor 的 Add 选项卡。

![](../../../../../../images/SB_Inclusion_tab.png)

在默认情况下，两个随机容器和六个声音对象的数据，以及六个音频文件，也将添加到 SoundBank。您可以在 SoundBank Editor 的 Edit 选项卡上查看 SoundBank 的全部内容。

![](../../../../../../images/SB_Exclusion_tab.png)

要在此 SoundBank 中只包含 Event，您可以返回 Add 选项卡，取消选择 Structures 和 Media 列下的复选框。

![](../../../../../../images/SB_Inclusion_Events_Only.png)

现在 SoundBank 中只启用了两个 Event 的数据。您可以进一步优化 SoundBank，在 SoundBank Editor 的 Edit 选项卡上弃用个别元素。比如，您可能只想将其中某个 Event 包含到此 SoundBank 中以便弃用另一个不需要的 SoundBank。

![](../../../../../../images/SB_Exclusion_Events_Only.png)

对于包含媒体的 SoundBank，您可以查看有关各个媒体文件的信息，包括它的采样率、音频格式和文件大小。通过掌握这些附加信息，您可以轻松地微调各个文件的转码设置，以遵守特定平台的限制。要更改媒体文件的转码设置，只需右键点击列表中的条目并选择 Conversion Settings 即可。

通过为游戏采取正确的策略，并可灵活地在 SoundBank 中启用和弃用单个元素以及修改单个媒体文件的转码设置，您可以有效地克服游戏的内存约束。

**在 SoundBank 中启用工程元素类型的方法是：**

1. 将 SoundBank 加载到 SoundBank Editor。
2. 对于列表中的各个条目，选择以下任意或所有工程元素类型，以在您的 SoundBank 中启用它们：

   - **Event** —— 将在 SoundBank 中启用所有相应 Event 数据。
   - **Structure** —— 将在 SoundBank 中启用所有相应对象结构数据。
   - **Media** —— 将在 SoundBank 中启用所有相应媒体文件。

     |  |  |
     | --- | --- |
     | [备注] | 备注 |
     | 要弃用与特定工程元素相关的所有 Event、对象结构或媒体文件，则取消选中相应的复选框。要想加快这一操作，可在 Hierarchy Inclusion 列表中选择多个条目，然后再取消选中其中某个复选框。这将弃用所有选定条目的类型。 |

**从 SoundBank 中弃用单个工程元素的方法是：**

1. 将 SoundBank 加载到 SoundBank Editor。
2. 切换到 Edit（编辑）选项卡。

   此时将显示 SoundBank 中包含的所有 Event、对象结构和媒体文件的完整列表。
3. 使用搜索或筛选工具定位您要从 SoundBank 中弃用的工程元素。
4. 取消选择 Event、对象结构或媒体文件的相应复选框。

   工程元素及所有相关工程元素于是从 SoundBank 中弃用掉了。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在将父对象从 SoundBank 中弃用时，所有相应子对象也将被弃用。在将父对象重新添加到 SoundBank 之前，您不能选择任何子对象。 |
5. 重复执行步骤 3 和 4，直至将您要移除的所有工程元素都从 SoundBank 中弃用出去。

---