# Conversion - In Progress/Stopped

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Audio File Conversion](00-Audio-File-Conversion.md) > Conversion - In Progress/Stopped

### Conversion - In Progress/Stopped

Conversion - In Progress（转码 - 处理中）对话框包含一个显示整体音频源转码进度的主进度条以及一组与正在转码的各个文件对应的次级进度条。次要进度条的数量将取决于设备中的处理器内核数。Wwise 将使用所有处理器内核，来尽可能快地完成转码过程。该对话框还会显示包含转码过程相关信息的日志（包括转码状态和错误）。

您可以随时停止转码过程。在转码中断时，Wwise 会自动显示 Conversion - Stopped（转码 - 停止）对话框。

| 界面元素 | 描述 |
| --- | --- |
| Operation | 操作。显示正在执行的高级任务的名称，以及各个正在转码的文件名称。 |
| Progress | 进度。一系列进度条将用来显示正在转换的各媒体文件的进度。  主进度条显示音频源转码的整个进度。多个次要进度条显示各个媒体文件的转码进度。如果您的设备具有多核处理器，则各个内核都有其自己的进度条。  如果转码停止，则此列将为空。 |
| Details | 详细信息。显示有关各个内核所执行特定任务的详细信息。  如果转码停止，则此列将为空。 |
| **Log（日志）** | |
| |  | | --- | |  |  (类型 —— 颜色) | 显示不同类型消息的对应颜色。日志中有以下类型：  - **Yellow** -- 黄色。针对转码警告。 - **Red** -- 红色。针对转码错误。 - **White** -- 白色。针对一般消息。 |
| Time | 警告、错误或消息的生成时间。 |
| ID | 该错误、警告或消息的 ID。 |
| Message | 消息。转码文件时遇到问题的描述。 |
| Platform | 发现问题的平台。 |
| Parameters | 参数。与错误、警告或消息有关的工程元素列表。  您可以双击某个工程元素，将其加载到编辑器中。 |
|  | 将 Message 文本框中的信息复制到 Windows 剪贴板，以便将信息粘贴到新的文件中。 |
|  | 停止。停止转码并显示 Conversion - Stopped 对话框。  此按钮仅在 Conversion - In Progress 对话框中可用。 |
|  | 关闭。关闭 Conversion Stopped 对话框。  此按钮仅在 Conversion - Stopped 对话框中可用。 |

---