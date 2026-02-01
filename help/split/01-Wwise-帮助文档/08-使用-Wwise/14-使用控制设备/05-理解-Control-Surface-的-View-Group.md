# 理解 Control Surface 的 View Group

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用控制设备](00-使用控制设备.md) > 理解 Control Surface 的 View Group

## 理解 Control Surface 的 View Group

您可以使用 View Group（视图分组）来将特定视图（对象）的内容与 Binding Group（绑定分组）的内容绑定。比如，您可以将 Mixing Desk 的对象映射到 Control Surface。

View Group 包含与视图中的对象关联的绑定，这些对象由视图中的索引进行标识。

下面展示了支持 View Group 的视图及其如何指派索引：

- **Mixing Desk**：调音台。各个垂直条带一个索引。
- **List View, Query Editor, Reference View, Busses Console**: one index per row.
- **Property Editor, Effect Editor, Source Editor, Modulator Editor**：属性编辑器、效果器编辑器、源编辑器、调制器编辑器。只能使用 1号索引，代表当前对象。
- **Soundcaster**：声音选角器。每个模块一个索引。

下面举例展示了可用在 Mixing Desk、List View 或 SoundCaster 内的 Control Surface View Group：

- **混音 View Group**：

  - 绑定：Property:Voice Volume - Index:1 - Key:MyController Ch.1 CC 0
  - 绑定：Property:Voice Volume - Index:2 - Key:MyController Ch.1 CC 1
  - 绑定：Property:Voice Volume - Index:3 - Key:MyController Ch.1 CC 2
  - 绑定：Property:Voice Volume - Index:4 - Key:MyController Ch.1 CC 3
  - 绑定：Command:Solo - Index:1 - Key:MyController Ch.1 CC 32
  - 绑定：Command:Solo - Index:2 - Key:MyController Ch.1 CC 33
  - 绑定：Command:Solo - Index:3 - Key:MyController Ch.1 CC 34
  - 绑定：Command:Solo - Index:4 - Key:MyController Ch.1 CC 35
  - 绑定：Command:Mute - Index:1 - Key:MyController Ch.1 CC 64
  - 绑定：Command:Mute - Index:2 - Key:MyController Ch.1 CC 65
  - 绑定：Command:Mute - Index:3 - Key:MyController Ch.1 CC 66
  - 绑定：Command:Mute - Index:4 - Key:MyController Ch.1 CC 67

此 View Group 会将：

- 4 个硬件滑杆映射到 4 个对象的 Voice Volume。
- 4 个硬件按钮映射到 4 个对象的 Solo。
- 4 个硬件按钮映射到 4 个对象的 Mute。

### 创建 View Group

您必须先创建分组才能将 View Group 与支持的视图关联。

**创建 View Group 的方法如下：**

1. 采用以下任一方式来打开 Control Surface Session：

   在 Project Explorer 中：

   1. 打开 Sessions（会话）选项卡，并双击所需 Control Surface Session。这时将在 Object Tab（对象选项卡）中打开会话。
   2. 单击“激活”图标 (![](../../../../images/activate_control_surface.png))。这时将加载并激活会话。

   在菜单栏中：

   1. 依次单击 **Views > Utilities > Control Surface Bindings**（视图 > 实用工具 > 控制器绑定）。这时将打开 Control Surface Bindings 视图。
   2. 单击选择器按钮 [>>]，并选中所需会话。这时将加载并激活会话。
2. 在视图或选项卡中，单击 **Add Group**（添加分组）。
3. 为分组键入名称并单击 **OK**（确定）。
4. 通过 **Add & Learn Binding**（添加并学习绑定）按钮在分组内创建绑定（如“[“创建 Control Surface Binding”一节](04-创建-Control-Surface-Binding.md "创建 Control Surface Binding")”中所述）。

### 将 View Group 与 Mixing Desk 关联

以下操作阐释了如何将 View Group 与 Mixing Desk 视图关联来复制本节开头示例中所述的映射。

要完成所述操作，请确保存在活跃的 Control Surface Session 和至少一个 View Group。

**将 View Group 与 Mixing Desk 相关联的方法如下：**

1. 在 **Views**（视图）菜单中，依次单击 **Editors > Mixing Desk**（编辑器 > 混音台）。
2. 在 Mixing Desk（混音台）的右上角单击选择器按钮 [>>]。
3. 在菜单中，单击所需 View Group：

   ![](../../../../images/mixing_desk_selector.png)

   这时将加载 View Group，并在 Mixing Desk 视图及 Control Surface Toolbar 中显示分组的名称。您可以通过单击任一位置的分组名称来激活或停用分组。

---