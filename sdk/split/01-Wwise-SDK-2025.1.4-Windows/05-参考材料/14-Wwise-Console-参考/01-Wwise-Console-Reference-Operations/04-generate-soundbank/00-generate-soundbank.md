# generate-soundbank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

generate-soundbank

SoundBank 生成。SoundBank 生成操作遵循工程中存储的设置。在从命令行启动 SoundBank 生成操作时，一般会忽略 User SoundBanks Settings 设置。However, when using the Source Control for generated SoundBanks, the User Project Settings are loaded for the Source Control settings. 另外，还可通过命令行来覆盖其中的部分设置。

# 示例

**`WwiseConsole generate-soundbank "C:\MyProject\MyProject.wproj" --platform "Windows" "Linux" --language "English(US)"`**

针对 Windows 和 Linux 平台使用 English (US) 语言生成 MyProject.wproj 的所有 SoundBank。

# 参数

**`PROJECT`**

工程文件 (.wproj) 的路径。

[参数架构](ak_wwise_cli_generatesoundbank_args_schema.html)

# 选项

**`--abort-on-load-issues`**

若检测到工程加载问题，则放弃执行该操作。日志记录的所有工程加载问题都会输出到屏幕上。

**`--audio-source-from-original`**

在执行 Tab Delimited Import 时，工程内可能已经包含一些与所导入文件同名的音频源文件。在这种情况下，将使用已经存在的文件而非替换为制表符分隔文件描述的文件。

**`--bank SOUNDBANK`**  
**`--bank SOUNDBANK1 SOUNDBANK2 ...`**  
**`--bank FILE`**

指定要生成哪些 SoundBank。此选项后面必须紧跟将要生成的 SoundBank 的名称。可以指定多个 SoundBank。若未指定任何 SoundBank，则生成所有 SoundBank。除此之外，也可指定包含 SoundBank 名称列表的文本文件。为此，可指定该文本文件的完整路径（包括 .txt 扩展名）。

**`--cache PATH`**

Overrides the project's cache directory path and instead uses the (relative) path specified in the command.

**`--clear-audio-file-cache`**

Deletes the content of the Wwise audio file cache directory prior to converting source files and generating SoundBanks, which ensures that all source files are reconverted. 注意，无论采用怎样的 –platform 选项，都会将所有平台的缓存全部清除。

**`--continue-on-error`**

若无论是否出现错误都要继续执行，请使用此选项。

**`--custom-global-closing-cmd CMD`**

不沿用 Wwise 中定义的全局结束步骤。此选项后面必须紧跟新的命令行（如果命令中有空格，则要用引号括起来）。若为命令行指定了空白字符串 ("")，则不执行任何全局结束步骤。

**`--custom-global-opening-cmd CMD`**

不沿用 Wwise 中定义的全局开始步骤。此选项后面必须紧跟新的命令行（如果命令中有空格，则要用引号括起来）。若为命令行指定了空白字符串 ("")，则不执行任何全局开始步骤。

**`--custom-post-gen-cmd PLATFORM CMD`**  
**`--custom-post-gen-cmd PLATFORM1 CMD1 --custom-post-gen-cmd PLATFORM2 CMD2 ...`**

不沿用 Wwise 中为此平台定义的自定义生成后步骤命令行。此选项后面必须紧跟平台标识符（见上文列表），后面再紧跟新的命令行（如果命令中有空格，则要用引号括起来）。要想不沿用另一平台的自定义生成后步骤命令行，可重复添加 –custom-post-gen-cmd 选项，并在其之后附加该平台的标识符及新的命令行。若为命令行指定了空白字符串 ("")，则不执行任何生成后步骤。

**`--custom-pre-gen-cmd PLATFORM CMD`**  
**`--custom-pre-gen-cmd PLATFORM1 CMD1 --custom-pre-gen-cmd PLATFORM2 CMD2 ...`**

不沿用 Wwise 中为此平台定义的自定义生成前步骤命令行。此选项后面必须紧跟平台标识符（见上文列表），后面再紧跟新的命令行（如果命令中有空格，则要用引号括起来）。要想不沿用另一平台的自定义生成前步骤命令行，可重复添加 –custom-pre-gen-cmd 选项，并在其之后附加该平台的标识符及新的命令行。若为命令行指定了空白字符串 ("")，则不执行任何生成前步骤。

**`--header-file`**

即便没有在工程设置中指定此选项，也会生成 Wwise\_IDs.h 头文件。

**`--header-file-path`**

(DEPRECATED) Use root-output-path instead. 不沿用工程设置中指定的头文件路径。此选项后面必须紧跟将写入头文件（Wwise\_IDs.h）的路径（绝对或相对路径）。只有在需要创建头文件时，此选项才会生效。

**`--import-definition-file FILE`**  
**`--import-definition-file FILE1 FILE2 ...`**  
**`--import-definition-file FILE1 --import-definition-file FILE2 ...`**

导入 SoundBank 定义文件。此选项后面必须紧跟将要导入的 SoundBank Definition File 的完整路径。可指定多个文件。若未指定 –save 选项，则不会长久保存导入定义文件后对工程所作的更改。

**`--import-language LANGUAGE`**

允许通过 Tab Delimited Import 操作导入语音。此选项用于指定所导入语音的语言。此选项之后须附加 –language 选项所列语言标识符之一。注意，此操作中仅添加音频文件；将忽略同时执行的所有其他操作（比如音量调整）。

**`--language LANGUAGE`**  
**`--language LANGUAGE1 --language LANGUAGE2 ...`**

指定要针对哪些语言生成 SoundBank。该选项后面必须加上工程中定义的语言标识符。所有指定的语言之前都要附加此选项。

**`--license LICENSE`**

设置所要使用的授权。该授权不会保存到工程中。

**`--license-file FILE`**

Sets the license to the contents of the file specified. 该授权不会保存到工程中。

**`--no-decode`**

Avoids generating DECODED files in the .cache directory, which saves CPU and disk space for your Wwise project. 同时，缩短 SoundBank 的生成时间。警告：若不生成 DECODED 文件，则在 Wwise 设计工具中播放这些声音可能会导致播放过期内容或根本无法播放。建议在使用此选项后清除文件缓存。

**`--no-source-control`**

跳过 Source Control 操作，即便已在 SoundBank Project Settings 中启用。

**`--output PLATFORM PATH`**  
**`--output PLATFORM1 PATH1 --output PLATFORM2 PATH2 ...`**  
**`--output PATH`**

允许在此选项之后附加平台和输出路径，以此来覆盖该平台的输出路径，进而实施 External Source 转码。可针对其他平台重复添加此选项。If only a directory is specified, sources for all platforms are generated in that directory.

**`--platform PLATFORM`**  
**`--platform PLATFORM1 PLATFORM2 ...`**  
**`--platform PLATFORM1 --platform PLATFORM2 ...`**

指定要针对哪些平台生成 SoundBank。该选项之后必须附加平台标识符。

**`--quiet`**

禁用所有非错误主机文本输出。

**`--readable-soundbanks`**

即便没有在工程设置中指定此选项，也会生成可读 SoundBank (.rbnk)。

**`--root-output-path`**

Overrides the root output path specified in the SoundBank settings. 此选项后必须紧跟工程层级的路径（绝对或相对）。将写入跨平台文件。此类文件包括 Wwise\_IDs.h 和 ProjectInfo.(xml|json)。

**`--save`**

在生成 SoundBank 前保存工程。If a tab-delimited import file was provided, the imported content is saved as well. Saving also migrates the project first, if required. This option does not save the project for other instances of Wwise that are currently running.

**`--skip-languages`**

不在工程中生成任何本地化 SoundBank。

**`--soundbank-path PLATFORM PATH`**  
**`--soundbank-path PLATFORM1 PATH1 --soundbank-path PLATFORM2 PATH2 ...`**

不沿用为此平台指定的 SoundBank 路径。此选项后面必须紧跟平台标识符（见上文列表），再紧跟新路径（绝对或相对路径，如果路径中有空格，则要用引号括起来）。要想不沿用另一平台的路径，可重复添加 –soundbank-path 选项，并在其之后附加该平台的标识符及新的命令行。

**`--source-by-platform PLATFORM FILE`**  
**`--source-by-platform PLATFORM1 FILE1 --source-by-platform PLATFORM2 FILE2 ...`**

Specifies the WSOURCES files to use by platform for external source conversion. 在针对特定平台进行指定时，会覆盖工程设置设定用于该平台的 WSOURCES 文件。对于未作相应指定的平台，将沿用工程设置所作设定。Specify the platform first, then the WSOURCES files to use for this platform. 可针对每个平台和 WSOURCES 文件重复该项操作。

**`--source-file FILE`**  
**`--source-file FILE1 FILE2 ...`**

Specifies the WSOURCES files to use for external source conversion. 这些 WSOURCES 文件将用于所有平台。

**`--tab-delimited-import-file FILE`**  
**`--tab-delimited-import-file FILE1 FILE2 ...`**  
**`--tab-delimited-import-file FILE1 --tab-delimited-import-file FILE2 ...`**

所要导入的制表符分隔文件。可在此选项之后指定多个所要导入的文件。

**`--tab-delimited-operation createNew`**  
**`--tab-delimited-operation useExisting`**  
**`--tab-delimited-operation replaceExisting`**

决定如何在导入时创建各个对象。createNew：创建新的对象；在可能的情况下赋予对象以所需名称，否则使用新的不重名的名称。useExisting：使用现有对象（如有），并更新指定的属性；否则，创建新的对象。该项为默认值。replaceExisting：创建新的对象；若现有对象具有相同的名称，则销毁现有对象。  
可能的值：

- createNew
- useExisting
- replaceExisting

**`--use-stable-guid`**

Give the SoundBank a stable GUID across multiple builds if you don't want to save the project.

**`--use-user-overrides`**

Use user overrides for Project Settings and SoundBank Settings.

**`--verbose`**

启用额外的主机文本输出。

[选项架构](ak_wwise_cli_generatesoundbank_options_schema.html)

# 结果

SoundBank 生成操作的进程退出代码。Although your SoundBanks might generate properly with warnings, it is strongly recommended that you consider these warnings as errors. 比如，在缺少源文件时，WwiseConsole.exe 会返回错误代码。Although a missing source file does not prevent your SoundBanks from being generated, the resulting SoundBanks might potentially be incomplete. 您可以在 Wwise 中依次转到 Project Settings > Logs，来更改 SoundBank 生成期间遇到的大部分消息的严重性。更改消息的严重性会影响返回代码。  
WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_generatesoundbank_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。