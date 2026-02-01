# waapi-server

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

waapi-server

启动命令行 Wwise Authoring API 服务器，以便使用 Wwise Authoring API 连接客户端应用程序。

# 示例

**`WwiseConsole waapi-server "C:\MyProject\MyProject.wproj" --allow-migration --wamp-port 8085`**

加载 MyProject.wproj 并运行 WAAPI 服务器。在必要时，先迁移工程。使用 WAMP 端口 8085 和默认的 HTTP 端口 8090。

# 参数

**`[PROJECT]`**

(Optional) When no project is specified, no project is loaded. See [ak.wwise.console.project.open](ak_wwise_console_project_open.html) for information on how to open a project.  
The path to the project file (.wproj).

[参数架构](ak_wwise_cli_waapiserver_args_schema.html)

# 选项

**`--allow-migration`**

允许在执行操作前迁移并保存 Wwise 工程。

**`--allowed-addr ADDRESS`**  
**`--allowed-addr ADDRESS1,ADDRESS2,...`**

指定允许连接到 WAAPI 的 IP 地址。此选项之后必须附加逗号分隔的 IP 地址（如 127.0.0.1）列表。默认值为 127.0.0.1。

**`--allowed-origin HOST`**  
**`--allowed-origin HOST1,HOST2,...`**

指定允许连接到 WAAPI 的主机。此选项之后必须附加逗号分隔的主机列表（如 www.myhost.com,www.myhost2.com）。在 HTTP 标头（header） Origin 上会执行验证。始终允许未提供 Origin 标头的连接以及基于文件的连接（如 <file://>）。

**`--http-max-clients NUM`**

指定最多可有多少个 WAAPI 客户端同时通过 HTTP POST 连接到服务器。此选项后面必须附加一个 0 ~ 100 之间的数字。若使用 0，则禁止服务器运行。默认值为 2。  
范围：[0,100]

**`--http-port PORT`**

指定在通过 HTTP POST 连接时 WAAPI 所用的端口号。这一选项后面必须跟随一个介于0到65,535之间的端口号。若使用 0，则禁止服务器运行。默认值为 8090。  
范围：[0,65535]

**`--no-source-control`**

Skip automatic checkout (if supported by project's source control plugin) of migrated files from source control.

**`--quiet`**

禁用所有非错误主机文本输出。

**`--verbose`**

启用额外的主机文本输出。

**`--wamp-max-clients NUM`**

指定最多可有多少个 WAAPI 客户端同时通过 WAMP 连接到服务器。此选项后面必须附加一个 0 ~ 100 之间的数字。若使用 0，则禁止服务器运行。默认值为 5。  
范围：[0,100]

**`--wamp-port PORT`**

指定在通过 WAMP 连接时 WAAPI 所用的端口号。此选项在优先级上高于 User Preferences，其之后必须附加介于 0 和 65,535 之间的端口号。若使用 0，则禁止服务器运行。默认值为 8080。  
范围：[0,65535]

**`--watchdog-timeout 30`**

Time in seconds to set as a watchdog threshold. The watchdog is signaled every time a WAAPI function call is made. By default, the value is 0 and the watchdog is disabled.  
Range: [0,\*]

[选项架构](ak_wwise_cli_waapiserver_options_schema.html)

# 结果

WwiseConsole.exe 退出代码为 0 表示成功，为 1 表示至少出现了一项错误并可能出现了警告，为 2 表示仅出现了警告。

[结果架构](ak_wwise_cli_waapiserver_result_schema.html)

有关 Wwise Console 的详细信息，请参阅 [使用命令行](bankscommandline.html) 章节。