# Control Surface Devices

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [工程](00-工程.md) > Control Surface Devices

## Control Surface Devices

Control Surface Device（控制设备）对话框用来配置与 Wwise 配合使用的硬件控制器设备。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 如果在 Wwise 处于打开状态时 MIDI 设备断开连接或被关闭，您可以打开 Control Surface Device 对话框来自动重新连接它们。 |

| 界面元素 | 描述 |
| --- | --- |
| **属性列** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Device Name | 设备名称。显示控制设备的名称。  此名称用在控制设备绑定中。 |
| Device Type | 设备的类型。 |
| Receive From | 发送端。要使用的输入设备。 |
| Status (Receive From) | 状态（输入端）。输入设备的连接状态。 |
| Send To | 接收端。要使用的输出设备。 |
| Status (Send To) | 状态接收端。输出设备的连接状态。 |
| **按钮** | |
| Add | 添加...。向 Wwise 中添加新设备。  在点击 **Add** 后，为设备输入相关名称并点击 **OK**（确定）。 |
| Remove | 从设备列表中删除所选设备。 |
| Rename | 重命名。更改设备名称。  |  |  | | --- | --- | | [注意] | 注意 | | Changing the device name breaks existing Bindings that use that device name. | |
| Close | 关闭。关闭对话框。  |  |  | | --- | --- | | [备注] | 备注 | | 列表中指定的设备会自动保存。 | |

---