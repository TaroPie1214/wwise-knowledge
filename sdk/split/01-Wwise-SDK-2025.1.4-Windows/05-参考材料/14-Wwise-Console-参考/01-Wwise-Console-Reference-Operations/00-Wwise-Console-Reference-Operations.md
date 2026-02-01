# Wwise Console Reference - Operations

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Console Reference - Operations

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。

[convert-external-source](ak_wwise_cli_convertexternalsource.html)   
External sources conversion. 针对指定工程对外部源文件进行转码。可选择指定额外的 WSOURCES。External Sources are a special type of source that you can put in a sound object in Wwise. It indicates that the real sound data will be provided at runtime. While external source conversion can be triggered by SoundBank generation, this operation can be used to process sources not contained in the Wwise Project. See [集成 External Source](integrating_external_sources.html).

[create-new-project](ak_wwise_cli_createnewproject.html)   
新建空白工程。不得存在同名工程。If the directory does not exist, it is created.

[execute-lua-script](ak_wwise_cli_executeluascript.html)   
Execute a Lua script. Optionally, specify additional Lua search paths, additional modules, and additional Lua scripts to load prior to the main script. The script can return a value. All arguments will be passed to the Lua script in the "wa\_args" global variable.

[generate-soundbank](ak_wwise_cli_generatesoundbank.html)   
SoundBank 生成。SoundBank 生成操作遵循工程中存储的设置。在从命令行启动 SoundBank 生成操作时，一般会忽略 User SoundBanks Settings 设置。However, when using the Source Control for generated SoundBanks, the User Project Settings are loaded for the Source Control settings. 另外，还可通过命令行来覆盖其中的部分设置。

[migrate](ak_wwise_cli_migrate.html)   
Migrates and saves the project.

[move-media-ids-to-single-file](ak_wwise_cli_movemediaidstosinglefile.html)   
将工程的媒体 ID 从 Work Unit (.wwu) 移到单个文件 (<project-name>.mediaid)。This command forces a save of all the project's work units.

[move-media-ids-to-work-units](ak_wwise_cli_movemediaidstoworkunits.html)   
将工程的媒体 ID 从单个 XML 文件 (<project-name>.mediaid) 移到 Work Unit (.wwu)。This command forces a save of all the project's work units.

[tab-delimited-import](ak_wwise_cli_tabdelimitedimport.html)   
导入制表符分隔文件来创建和修改不同的对象层级结构。在必要时，会自动迁移工程。在导入之后，还会自动保存。

[update-media-ids-in-single-file](ak_wwise_cli_updatemediaidsinsinglefile.html)   
加载工程并更新 <project-name>.mediaid（如有）的内容。

[verify](ak_wwise_cli_verify.html)   
Loads the project and does nothing else. 藉此，可查看日志以便进行验证，而无需实际执行迁移和保存。

[waapi-server](ak_wwise_cli_waapiserver.html)   
启动命令行 Wwise Authoring API 服务器，以便使用 Wwise Authoring API 连接客户端应用程序。

[ak.wwise.ui.cli.executeLuaScript](ak_wwise_ui_cli_executeluascript.html)   
Execute a Lua script. Optionally, specify additional Lua search paths, additional modules, and additional Lua scripts to load prior to the main script. The script can return a value. All arguments will be passed to the Lua script in the "wa\_args" global variable.