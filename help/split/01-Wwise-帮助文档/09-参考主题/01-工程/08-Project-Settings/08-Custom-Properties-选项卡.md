# Custom Properties 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > Custom Properties 选项卡

### Custom Properties 选项卡

|  |  |
| --- | --- |
| [备注] | 备注 |
| 此处的选项卡描述均针对原有的自定义属性定义方法。最新且更有效的自定义属性定义方法是使用 XML 文件（详见 SDK 文档的“ [定义自定义属性](https://www.audiokinetic.com/library/edge/?source=SDK&id=defining__custom__properties.html) ”页面）。不过，这两种方法仍然有效（详见 SDK 文档）。 |

In the Custom Properties tab of the Project Settings dialog, you can define your own properties for the Sound and Audio Source objects of the Containers hierarchy. 这些自定义属性随后可从以下位置访问：

- [“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）")
- [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor")
- [“Multi Editor”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/03-Multi-Editor.md "Multi Editor")

游戏还可查询这些属性的值。更改 Custom Property 列表将强制保存并重新加载 Wwise 工程。

| 界面元素 | 描述 |
| --- | --- |
| **Custom Properties（自定义属性）** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| ID | 属性的识别符号。游戏使用该识别符号，通过 Sound Engine API 查询该属性的值。无法编辑。 |
| Name | 属性的名称。注意，在保存到 XML 文件时会将前缀 Custom: 自动添加到属性名称中。 |
| Location | 属性的位置。可为以下项：  - Audio Source - 声音 |
| Type | 属性的类型。可为以下项：  - Boolean（布尔量） - Integer（整型） - Real（实数） |
| Default | 属性的默认值。 |
| Min（最小值） | 属性的最小值。 |
| Max（最大值） | 属性的最大值。 |
|  | 添加新自定义属性。 |
|  | 移除所选自定义属性。 |
|  | 确定。关闭 Project Settings 对话框并保存设置。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

---