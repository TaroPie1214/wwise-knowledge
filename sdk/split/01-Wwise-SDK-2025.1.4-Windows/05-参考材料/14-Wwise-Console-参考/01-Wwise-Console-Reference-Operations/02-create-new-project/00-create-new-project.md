# create-new-project

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

create-new-project

新建空白工程。不得存在同名工程。If the directory does not exist, it is created.

# 示例

**`WwiseConsole create-new-project "C:\MyProject\MyProject.wproj" --platform "Windows" "Linux"`**

针对 Windows 和 Linux 平台创建 MyProject.wproj。

# 参数

**`PROJECT`**

工程文件 (.wproj) 的路径。

[参数架构](ak_wwise_cli_createnewproject_args_schema.html)

# 选项

**`--platform PLATFORM`**  
**`--platform PLATFORM1 PLATFORM2 ...`**  
**`--platform PLATFORM1 --platform PLATFORM2 ...`**

指定新的工程支持哪个平台。若未指定，则仅支持 Windows。

**`--quiet`**

禁用所有非错误主机文本输出。

**`--verbose`**

启用额外的主机文本输出。

[选项架构](ak_wwise_cli_createnewproject_options_schema.html)

# 结果

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_createnewproject_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。