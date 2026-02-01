# Advanced Folder Picker

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > Advanced Folder Picker

### Advanced Folder Picker

Advanced Folder Picker（高级文件夹选取器）对话框方便指定和构建某些工程设置的路径（如 Original 和 Cache 文件夹）。尤其是，您可以利用该对话框来预览这些设置所用环境变量的启用情况。

| 界面元素 | 描述 |
| --- | --- |
| Path | 路径。在通过单击 OK 关闭对话框时返回的字符串。 |
| Browse | 浏览。打开文件夹选取器对话框以转到文件夹所在位置。 |
| Preview | 预览。预览估算得出的 **Path**，同时将环境变量扩展为实际值。若设置了 **Preview as Absolute Path**，则还会尝试将 Path 由相对路径转换为绝对路径，以与对应系统实际所用的路径保持一致。 |
| Environment Variables | 环境变量。列出可用作路径的宏的环境变量。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。环境变量的名称。 |
| Current Value | 当前值。环境变量的当前值。 |
|  | 插入。将所选环境变量添加到 Path。  变量将添加至指针所在位置，或替换命令行中的所选文本。  除单击 Insert 外，还可双击列表中的变量来将其添加到命令行。 |
|  | 确定。关闭对话框并返回路径。 |
|  | 取消。关闭对话框而不返回路径。 |

**相关主题**

- [“定义 Originals 文件夹设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#defining_originals_folder_settings "定义 Originals 文件夹设置")
- [“定义缓存文件夹设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/01-定义工程的常规设置.md#defining_cache_folder_settings "定义缓存文件夹设置")
- [“为 External Source 指定工程设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/06-为-External-Source-指定工程设置.md "为 External Source 指定工程设置")

---