# move-media-ids-to-single-file

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

move-media-ids-to-single-file

将工程的媒体 ID 从 Work Unit (.wwu) 移到单个文件 (<project-name>.mediaid)。This command forces a save of all the project's work units.

# 示例

**`WwiseConsole move-media-ids-to-single-file "C:\MyProject\MyProject.wproj"`**

将工程的媒体 ID 从 Work Unit 移到单个 XML 文件 (<project-name>.mediaid)。

# 参数

**`PROJECT`**

工程文件 (.wproj) 的路径。

[参数架构](ak_wwise_cli_movemediaidstosinglefile_args_schema.html)

# Result

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_movemediaidstosinglefile_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。