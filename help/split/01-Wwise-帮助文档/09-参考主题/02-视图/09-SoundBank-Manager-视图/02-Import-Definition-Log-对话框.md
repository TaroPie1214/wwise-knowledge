# Import Definition Log 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > [SoundBank Manager 视图](00-SoundBank-Manager-视图.md) > Import Definition Log 对话框

### Import Definition Log 对话框

Import Definition Log（导入定义日志）对话框会显示与使用定义文件导入的 SoundBank（音频包）相关的信息。日志为已执行的各个任务创建一个条目。出现以下情况时，条目会添加到日志中：创建 SoundBank、在现有 SoundBank 中添加 Event、删除 Event 或检测到 Event 缺失时，以及添加、删除 Game Sync 或报告其缺失时。若未对 SoundBank 进行任何更改，则日志显示 No Change Detected 消息。

| 界面元素 | 描述 |
| --- | --- |
| SoundBank | 导入的 SoundBank 的名称。 |
| Import Activity | 显示导入过程中发生的活动：  - **Event Added**：新的 Event 已添加到现有 SoundBank。 - **SoundBank Created**：创建了新的 SoundBank。 - **Event Deleted**：已从现有 SoundBank 删除 Event。 - **Event Missing**：工程中不再存在某 Event 或者某 Event 尚未创建。 - **Exclusion Added**：从现有 SoundBank 中弃用了一个 Game Sync。 - **Exclusion Deleted**：Game Sync 被重新包含至现有的 SoundBank。 - **Exclusion Missing**：Game Sync 在工程中不再存在或尚未创建 ，因此无法将其添加到弃用列表或从弃用列表中删除。 - **No Change Detected**：导入的 SoundBank 与 Wwise 中已有的 SoundBank 完全相同。 |
| Event | SoundBank 中添加或删除 Event 的名称，或者工程中缺失的 Event 的名称。 |
|  | 将日志中的信息复制到 Windows 剪贴板，以便将信息粘贴到新的文件中。 |
|  | 关闭。关闭 Import Definition Log 对话框。 |

**相关主题**

- [“通过导入定义文件创建并填充 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/02-通过导入定义文件创建并填充-SoundBank.md "通过导入定义文件创建并填充 SoundBank")

---