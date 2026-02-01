# convert-external-source

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

convert-external-source

External sources conversion. 针对指定工程对外部源文件进行转码。可选择指定额外的 WSOURCES。External Sources are a special type of source that you can put in a sound object in Wwise. It indicates that the real sound data will be provided at runtime. While external source conversion can be triggered by SoundBank generation, this operation can be used to process sources not contained in the Wwise Project. See [集成 External Source](integrating_external_sources.html).

# 示例

**`WwiseConsole convert-external-source "C:\MyProject\MyProject.wproj"`**

针对所有平台使用当前工程设置对 MyProject.wproj 的外部源进行转码。

# 参数

**`PROJECT`**

工程文件 (.wproj) 的路径。

[参数架构](ak_wwise_cli_convertexternalsource_args_schema.html)

# 选项

**`--output PLATFORM PATH`**  
**`--output PLATFORM1 PATH1 --output PLATFORM2 PATH2 ...`**  
**`--output PATH`**

Allows you to follow this option with a platform, and a path to an output directory to override the output directory of this platform. 可针对其他平台重复添加此选项。If only an output directory is specified, sources for all platforms are generated in that directory.

**`--platform PLATFORM`**  
**`--platform PLATFORM1 PLATFORM2 ...`**  
**`--platform PLATFORM1 --platform PLATFORM2 ...`**

Specifies for which platforms the sources are converted using the project settings. 该选项之后必须附加平台标识符。

**`--quiet`**

禁用所有非错误主机文本输出。

**`--source-by-platform PLATFORM FILE`**  
**`--source-by-platform PLATFORM1 FILE1 --source-by-platform PLATFORM2 FILE2 ...`**

Specifies the WSOURCES files to use by platform. 在针对特定平台进行指定时，会覆盖工程设置设定用于该平台的 WSOURCES 文件。对于未作相应指定的平台，将沿用工程设置所作设定。Specify the platform first, then the WSOURCES files to use for this platform. 可针对每个平台和 WSOURCES 文件重复该项操作。

**`--source-file FILE`**  
**`--source-file FILE1 FILE2 ...`**

Specifies the WSOURCES files to use. 这些 WSOURCES 文件将用于所有平台。

**`--verbose`**

启用额外的主机文本输出。

[选项架构](ak_wwise_cli_convertexternalsource_options_schema.html)

# 结果

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_convertexternalsource_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。