# verify

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

verify

Loads the project and does nothing else. 藉此，可查看日志以便进行验证，而无需实际执行迁移和保存。

# 示例

**`WwiseConsole verify "C:\MyProject\MyProject.wproj" --verbose`**

打开工程并启用详细日志记录。

# Arguments

**`PROJECT`**

工程文件 (.wproj) 的路径。

[参数架构](ak_wwise_cli_verify_args_schema.html)

# Options

**`--abort-on-load-issues`**

若检测到工程加载问题，则放弃执行该操作。日志记录的所有工程加载问题都会输出到屏幕上。

**`--quiet`**

禁用所有非错误主机文本输出。

**`--verbose`**

启用额外的主机文本输出。

[选项架构](ak_wwise_cli_verify_options_schema.html)

# Result

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_verify_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。