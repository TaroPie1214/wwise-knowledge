# update-media-ids-in-single-file

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

update-media-ids-in-single-file

加载工程并更新 <project-name>.mediaid（如有）的内容。

# 示例

**`WwiseConsole update-media-ids-in-single-file "C:\MyProject\MyProject.wproj"`**

加载工程并更新 <project-name>.mediaid（如有）的内容。

# 参数

**`PROJECT`**

工程文件 (.wproj) 的路径。

[参数架构](ak_wwise_cli_updatemediaidsinsinglefile_args_schema.html)

# Result

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_updatemediaidsinsinglefile_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。