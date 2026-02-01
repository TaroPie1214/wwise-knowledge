# 创建 Control Surface Binding

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用控制设备](00-使用控制设备.md) > 创建 Control Surface Binding

## 创建 Control Surface Binding

Control Surface Binding 可将硬件控件（如按钮、滑杆、旋钮或按键）与 Wwise 元素（属性或命令）关联。

**每个绑定有三个元素：**

- **Property/Command**（属性/命令）：

  - Object Property：对象属性。目标对象上要修改的属性名。
  - Object Command（对象命令）：针对目标对象执行的命令或操作。
  - Global Command（全局命令）：针对所有对象执行的命令或操作。
- **Object/Index**：对象/索引。指定目标对象。
- **Controller Assignment**：控制器指派。用 MIDI 消息 ID 来识别硬件控件元素。

**绑定项存储在三个不同组内，每个组都具有定义目标对象的不同机制。**

- **Global**：全局。目标对象直接在绑定中指定。
- **Current Selection**（当前选中项）：Wwise 中最新选中的目标对象。
- **View Group**：视图组。根据当前加载 Binding Group 的视图（如 Mixing Desk 和 Mixing Session，或 Soundcaster 和 Soundcaster Session），决定控制哪些目标对象。视图中加载的每个对象都有一个索引。

您可以为多种场景创建绑定：

- [“为键盘快捷方式创建绑定”一节](04-创建-Control-Surface-Binding.md#creating_binding_for_keyboard_shortcut "为键盘快捷方式创建绑定")
- [“创建绑定以修改当前选中项”一节](04-创建-Control-Surface-Binding.md#creating_binding_to_modify_current_selection "创建绑定以修改当前选中项")
- [“创建绑定以修改特定对象属性值”一节](04-创建-Control-Surface-Binding.md#creating_binding_to_modify_specific_object_property_value "创建绑定以修改特定对象属性值")

### 为键盘快捷方式创建绑定

您可以使用 Global Binding（全局绑定）配置全局命令，继而通过 Keyboard Shortcut Manager（键盘快捷方式管理器）或 Control Surface Session（控制器会话）的绑定来触发。

**创建全局绑定：**

1. 采用以下任一方式来打开 Control Surface Session：

   在 Project Explorer 中：

   1. 打开 Sessions（会话）选项卡，并双击所需 Control Surface Session。这时将在 Object Tab（对象选项卡）中打开会话。
   2. 单击“激活”图标 (![](../../../../images/activate_control_surface.png))。这时将加载并激活会话。

   在菜单栏中：

   1. 依次单击 **Views > Utilities > Control Surface Bindings**（视图 > 实用工具 > 控制器绑定）。这时将打开 Control Surface Bindings 视图。
   2. 单击选择器按钮 [>>]，并选中所需会话。这时将加载并激活会话。
2. 选择 **Global**（全局）组。
3. 单击 **Add & Learn Binding**（添加并学习绑定）。

   这时将添加绑定条目。**Learn** 按钮的颜色会变为绿色（表示按钮处于激活状态）。
4. 单击选择器按钮 [>>]，然后单击 **Global commands**（全局命令）。这时将打开 Command Selection（命令选择）对话框。
5. 从列表中选择所需属性并单击 **OK**（确定）。
6. 使用所需的硬件控件来作绑定。

   这时将停用 **Learn** 按钮，并创建绑定以供编辑。

|  |  |
| --- | --- |
| [备注] | 备注 |
| **Global Commands** 的绑定可在其它组内进行创建，例如 **Current Selection**（当前选中项）组或 **View**（视图）组。 |

### 创建绑定以修改特定对象属性值

您可以创建 Control Surface Bindings 并让其指向工程中的特定对象属性值。这样方便将控制器指派关联到 Game Parameter 等对象。

**创建控制 Game Parameter 模拟值的绑定的方法如下：**

1. 采用以下任一方式来打开 Control Surface Session：

   在 Project Explorer 中：

   1. 打开 Sessions（会话）选项卡，并双击所需 Control Surface Session。这时将在 Object Tab（对象选项卡）中打开会话。
   2. 单击“激活”图标 (![](../../../../images/activate_control_surface.png))。这时将加载并激活会话。

   在菜单栏中：

   1. 依次单击 **Views > Utilities > Control Surface Bindings**（视图 > 实用工具 > 控制器绑定）。这时将打开 Control Surface Bindings 视图。
   2. 单击选择器按钮 [>>]，并选中所需会话。这时将加载并激活会话。
2. 选择 **Global**（全局）组。
3. 单击 **Add & Learn Binding**（添加并学习绑定）。

   这时将添加绑定条目。**Learn** 按钮的颜色会变为绿色（表示按钮处于激活状态）。
4. 采用以下任一方式来选择 Property/Command：

   - 在 Transport Control（走带控制）中单击 Game Parameter（游戏参数）的模拟值。
   - 单击选择器按钮 [>>] 并浏览属性：

     1. 在上下文菜单中，单击 **Object Properties**（对象属性）。
     2. 依次选择 **Game Syncs > Game Parameter > Simulation Value**（游戏同步器 > 游戏参数 > 模拟值）。
     3. 单击 **OK**（确定）。
5. 使用所需的硬件控件来作绑定。

   这时将停用 **Learn** 按钮，并创建绑定以供编辑。

### 创建绑定以修改当前选中项

在 Control Surface Session 中，可定义用来将选定对象的属性值与硬件控制器控件（如滑杆、旋钮或按钮）关联的绑定。

比如，将控制器的四个滑杆指派给以下属性：

- Voice Volume（声部音量）。
- Voice Pitch（声部音高）。
- Voice Low-pass Filter（声部低通滤波器）。
- Voice High-pass Filter（声部高通滤波器）。

在创建绑定后，会将四个滑杆与选定对象的这些属性关联。若配有电动推子（如 Mackie Control Universal Pro），则在当前选中项变化时各个推子会自动移到当前值。

**创建修改当前选中项 Voice Volume 的绑定的方法如下：**

1. 采用以下任一方式来打开 Control Surface Session：

   在 Project Explorer 中：

   1. 打开 Sessions（会话）选项卡，并双击所需 Control Surface Session。这时将在 Object Tab（对象选项卡）中打开会话。
   2. 单击“激活”图标 (![](../../../../images/activate_control_surface.png))。这时将加载并激活会话。

   在菜单栏中：

   1. 依次单击 **Views > Utilities > Control Surface Bindings**（视图 > 实用工具 > 控制器绑定）。这时将打开 Control Surface Bindings 视图。
   2. 单击选择器按钮 [>>]，并选中所需会话。这时将加载并激活会话。
2. 选择 **Current Selection**（当前选中项）组。
3. 单击 **Add & Learn Binding**（添加并学习绑定）。

   这时将添加绑定条目。**Learn** 按钮的颜色会变为绿色（表示按钮处于激活状态）。
4. 采用以下任一方式来选择 Property/Command：

   - 在 Transport Control（走带控制）中单击 Game Parameter（游戏参数）的模拟值。
   - 单击选择器按钮 [>>] 并浏览属性：

     1. 在上下文菜单中，单击 **Object Properties**（对象属性）。
     2. 依次选择 **Audio > General Settings > Voice > Voice Volume**（音频 > 常规设置 > 声部 > 声部音量）。
     3. 单击 **OK**（确定）。
5. 使用所需的硬件控件来作绑定。

   这时将停用 **Learn** 按钮，并创建绑定以供编辑。

当前选中项绑定还可用于触发当前选中项上的命令。比如，将一组按钮映射到以下命令：

- Mute（静音）
- Solo（单独播放）
- Play
- Stop（停止）

**创建对当前选中项静音的绑定的方法如下：**

1. 选择 **Current Selection**（当前选中项）组。
2. 单击 **Add & Learn Binding**（添加并学习绑定）。

   这时将添加绑定条目。**Learn** 按钮的颜色会变为绿色（表示按钮处于激活状态）。
3. 使用所需的硬件控件来作绑定。

   这时将停用 **Learn** 按钮，并创建绑定以供编辑。
4. 单击选择器按钮 [>>]。
5. 在上下文菜单中，依次单击 **Object commands > Mute**（对象命令 > 静音）。
6. 使用所需的硬件控件来作绑定。

   这时将停用 **Learn** 按钮，并创建绑定以供编辑。

若配有控制器按钮，其在静音时会亮起，在未静音时会熄灭。

---