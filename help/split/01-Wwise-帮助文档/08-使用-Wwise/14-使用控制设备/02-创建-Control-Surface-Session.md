# 创建 Control Surface Session

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用控制设备](00-使用控制设备.md) > 创建 Control Surface Session

## 创建 Control Surface Session

Control Surface Session（控制设备会话）定义硬件控件连接到 Wwise 功能或工程属性的方式。Control Surface Sessio 定义一列绑定。各个绑定都将一个硬件控件（按钮、滑杆、旋钮、键等）连接到 Wwise 元素（属性或命令）上。

在单个 Wwise 工程中可以创建多个 Control Surface Sessions，允许这样做有一些理由：

- Wwise 工程可能有多个用户，这些用户会使用不同的硬件设备。
- 不同的使用情形。
- 不同的用户有不同的需求或偏好。

您可以通过 Control Surface Bindings 视图或 Project Explorer 创建 Control Surface Session。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Control Surface Sessions 存储在工程内，并且可用在任何使用此工程的计算机上。 |

**通过 Control Surface Bindings 视图创建 Control Surface Session：**

1. 在 **Views**（视图）菜单中，依次单击 **Utilities > Control Surface Bindings**（实用工具 > 控制器绑定）。这时将打开 Control Surface Bindings 视图。
2. 单击选择器按钮 [>>] 来打开选择器菜单。
3. 点击 **New**（新建）。
4. 为会话输入名称。
5. 单击 **OK**（确定）。

   此时将会创建并加载会话。

**通过 Project Explorer 创建 Control Surface Session：**

1. 在 Project Explorer（工程资源管理器）中，打开 Sessions（会话）选项卡。
2. 在 Control Surface Sessions 文件夹中，选中所需 Work Unit（工作单元）。
3. 在 Project Explorer（工程资源管理器）中，单击 **Create new 'Control Surface Session'**（创建新的控制器会话）按钮 (![](../../../../images/btn_create_control_surface_session.png))。

   这时将在 Work Unit 下显示新建的 Control Surface Session 对象。
4. 为新建的会话键入名称并按下 **Enter**。

   这时将创建会话以供编辑。您可以在 Project Explorer 中双击来在 Object Tab 中打开会话。

---