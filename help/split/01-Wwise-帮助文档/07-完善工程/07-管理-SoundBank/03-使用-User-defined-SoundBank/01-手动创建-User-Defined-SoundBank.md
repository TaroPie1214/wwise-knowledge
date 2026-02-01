# 手动创建 User-Defined SoundBank

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [使用 User-defined SoundBank](00-使用-User-defined-SoundBank.md) > 手动创建 User-Defined SoundBank

### 手动创建 User-Defined SoundBank

在 Wwise 中，可手动创建并填充单个 SoundBank（音频包），也通过导入定义文件来批量创建并填充 SoundBank。该定义文件由用于将 Event（事件）集成到游戏中的 3D 应用程序或关卡编辑器生成。有关导入定义文件的详细信息，请参阅[“通过导入定义文件创建并填充 SoundBank”一节](02-通过导入定义文件创建并填充-SoundBank.md "通过导入定义文件创建并填充 SoundBank")。为此，可将 Wwise 配置为针对 Event 和 Auxiliary Bus（辅助总线）自动定义 SoundBank。请参阅 [“Auto-defined SoundBank”一节](../02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")。

您可以在 Wwise 的两个不同区域中手动创建 SoundBank：

- [在 Project Explorer 中创建 SoundBank 的方法是：](01-手动创建-User-Defined-SoundBank.md#to_create_soundbank_from_project_explorer "在 Project Explorer 中创建 SoundBank 的方法是：")
- [在 SoundBank Manager 中创建 SoundBank 的方法是：](01-手动创建-User-Defined-SoundBank.md#to_create_soundbank_from_soundbank_manager "在 SoundBank Manager 中创建 SoundBank 的方法是：")

|  |  |
| --- | --- |
| [备注] | 备注 |
| 第一次创建 SoundBank 时，Wwise 自动将它命名为"New\_SoundBank\_X"。您可以重命名 SoundBank，为它取一个更加有意义的名称。若打算重命名 SoundBank，请在开发过程的早期执行，因为后期更改的话可能还要额外编程。 |

**在 Project Explorer 中创建 SoundBank 的方法是：**

1. 通过执行以下任一操作切换到 SoundBank 布局：

   - 在菜单栏中，点击 **Layouts** > **SoundBank**。
   - 按 **F7**。
2. 在 Project Explorer 中，切换到 SoundBank 选项卡。
3. 执行以下操作之一：

   - 选择虚拟文件夹或工作单元，然后点击 Project Explorer 中的 **SoundBank** 图标。
   - 右键点击虚拟文件夹或工作单元，然后从快捷菜单中选择 **New Child** > **SoundBank**。

   此时新的 SoundBank 将高亮显示在 Project Explorer 中。
4. 输入 SoundBank 的新名称并按 **Enter**。

   SoundBank 于是创建完成并添加到 SoundBank 列表中了。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | SoundBank 名称中只能包含不带变音符号的的罗马字母、数字和下划线。名称还必须以字母或下划线开头。 |
5. 在 Max Size 文本框中，指定您要为 SoundBank 分配的最大游戏内存。

**在 SoundBank Manager 中创建 SoundBank 的方法是：**

1. 通过执行以下任一操作切换到 SoundBank 布局：

   - 在菜单栏中，点击 **Layouts** > **SoundBank**。
   - 按 **F7**。
2. 在 SoundBank Manager 中，点击 **New** 按钮。

   这时会打开 New SoundBank（新建音频包）对话框。
3. 在 SoundBank 层级结构中，选择您要在其中创建 SoundBank 的工作单元。
4. 在 Name 字段中，将默认名称替换成适合新 SoundBank 的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | SoundBank 名称中只能包含不带变音符号的的罗马字母、数字和下划线。名称还必须以字母或下划线开头。 |
5. 单击 **OK**（确定）。

   SoundBank 于是创建完成并添加到 SoundBank 列表中了。
6. 在 Max Size 文本框中，指定您要为 SoundBank 分配的最大游戏内存。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若使用版本控制插件且未签出在其中创建 SoundBank 的 Work Unit，Wwise 会询问是否希望仅在尝试保存工程时签出 Work Unit。 |

---