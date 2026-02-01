# tab-delimited-import

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

tab-delimited-import

导入制表符分隔文件来创建和修改不同的对象层级结构。在必要时，会自动迁移工程。在导入之后，还会自动保存。

# 示例

**`WwiseConsole tab-delimited-import "C:\MyProject\MyProject.wproj" "C:\fileToImport.tsv" --quiet`**

使用默认的 useExisting 操作在安静 (quiet) 记录模式下导入制表符分隔文件。

# 参数

**`PROJECT`**

工程文件 (.wproj) 的路径。

**`FILE`**

所要导入的制表符分隔文件。

[参数架构](ak_wwise_cli_tabdelimitedimport_args_schema.html)

# 选项

**`--audio-source-from-original`**

在执行 Tab Delimited Import 时，工程内可能已经包含一些与所导入文件同名的音频源文件。在这种情况下，将使用已经存在的文件而非替换为制表符分隔文件描述的文件。

**`--continue-on-error`**

若无论是否出现错误都要继续执行，请使用此选项。

**`--custom-global-closing-cmd CMD`**

不沿用 Wwise 中定义的全局结束步骤。此选项后面必须紧跟新的命令行（如果命令中有空格，则要用引号括起来）。若为命令行指定了空白字符串 ("")，则不执行任何全局结束步骤。

**`--custom-global-opening-cmd CMD`**

不沿用 Wwise 中定义的全局开始步骤。此选项后面必须紧跟新的命令行（如果命令中有空格，则要用引号括起来）。若为命令行指定了空白字符串 ("")，则不执行任何全局开始步骤。

**`--import-language LANGUAGE`**

允许通过 Tab Delimited Import 操作导入语音。此选项用于指定所导入语音的语言。此选项之后须附加 –language 选项所列语言标识符之一。注意，此操作中仅添加音频文件；将忽略同时执行的所有其他操作（比如音量调整）。

**`--no-source-control`**

Skip automatic addition and checkout (if supported by project's source control plugin) of new and modified files to source control.

**`--quiet`**

禁用所有非错误主机文本输出。

**`--tab-delimited-operation createNew`**  
**`--tab-delimited-operation useExisting`**  
**`--tab-delimited-operation replaceExisting`**

决定如何在导入时创建各个对象。createNew：创建新的对象；在可能的情况下赋予对象以所需名称，否则使用新的不重名的名称。useExisting：使用现有对象（如有），并更新指定的属性；否则，创建新的对象。该项为默认值。replaceExisting：创建新的对象；若现有对象具有相同的名称，则销毁现有对象。  
可能的值：

- createNew
- useExisting
- replaceExisting

**`--verbose`**

启用额外的主机文本输出。

[选项架构](ak_wwise_cli_tabdelimitedimport_options_schema.html)

# 结果

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_tabdelimitedimport_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。