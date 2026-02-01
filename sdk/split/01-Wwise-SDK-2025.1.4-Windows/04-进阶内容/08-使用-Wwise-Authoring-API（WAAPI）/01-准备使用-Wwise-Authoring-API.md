# 准备使用 Wwise Authoring API

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

准备使用 Wwise Authoring API

一般情况下都会默认启用 Wwise Authoring API。不过，最好在开始使用前查看下相应偏好设置。藉此检查重要的安全设置，并确认是否启用了 Wwise Authoring API：

启用 Wwise Authoring API：

- 在 Wwise 中，选择 *Project* > *User Preferences*。（默认快捷键：Shift + U）
- 在 **Wwise Authoring API** 组框中，选择 **Enable（启用） Wwise Authoring API**。
- 单击 **OK**。

接下来就可以开始使用 WAAPI 了。

# 网络安全

Since WAAPI allows you to control Wwise remotely, it must be used in a secure environment in order to prevent other people from gaining control of your computer. 假如没有正确配置，可能会出现安全风险。

|  |  |
| --- | --- |
|  | **备注:** 假如通过浏览器连接 WAAPI，必须**同时**添加 Web 服务器的 IP 地址和源端口，才允许连接到主机。 请参阅 [防止跨地域脚本](waapi_prepare.html#waapi_security_origin) 。 |

## 阻止访问 WAAPI 端口

WAAPI 提供了 WAMP 和 HTTP 的两个端口（默认：8080 and 8090）。为了进一步提升安全性，建议通过使用防火墙来阻止远程计算机访问这些端口。假如想要允许远程计算机访问 WAAPI，建议将其逐一添加到白名单中，而不要直接允许所有远程连接。

## 仅允许特定 IP 地址访问 WAAPI

在默认情况下，WAAPI 仅允许来自本地主机 (127.0.0.1 或 ::1) 的连接。

除非在 User Preferences 中添加远程计算机的 IP 地址，否则会无法通过其访问 WAAPI。允许特定 IP 地址连接 WAAPI：

- 从 Wwise 主菜单点击 *Project* > *User Preferences*。
- 在 **Allow connections from**（允许来自以下位置的连接）字段中添加 IP 地址。例如：
  - *203.0.113.255*（使用 IPv4 地址）
  - *2001:db8::*（使用 IPv6 地址）
- 单击 **OK** 。

|  |  |
| --- | --- |
|  | **注意:** 您可以通过添加 \* 来允许来自任意 IP 地址的连接。但是这样做并不安全，因此我们不建议这样做。 |

## 防止跨地域脚本

WAAPI 针对跨地域脚本提供了安全层。Otherwise, when you visit a webpage that contains JavaScript code, for example, that code could theoretically gain access to Wwise by connecting from the loaded webpage. 在这一情境下，防火墙是不够的。

这个 WAAPI 安全层依赖于您的浏览器安全设置。By default, WAAPI will only accept connections from local software or, in the case of browsers, only when opening HTML files on the local file system.

在别的主机（host）加载的网页中使用 WAAPI 会导致失败，除非您将该主机添加到了 User Preferences 中。将一个主机添加为 WAAPI 有效来源的方法是：

- 从 Wwise 主菜单点击 *Project* > *User Preferences*。
- 将您的主机 URI 添加到 **Allow browser connections from origins** 字段。例如：
  - *<http://www.myhost.com>*，使用端口 80；或
  - *<http://www.myhost.com:1234>*，不使用默认的 80，而是 1234。
- 单击 **OK** 。

|  |  |
| --- | --- |
|  | **注意:** 您可以添加 \* 来允许来自任意来源网页的连接。但是这样做并不安全，因此我们不建议这样做。 |

请参阅 [使用命令行](bankscommandline.html) 了解通过命令行使用“-Waapi”命令的更多信息。

|  |  |
| --- | --- |
|  | **备注:** **使用多客户端**  WAAPI 支持同时多个连接的使用。目前 WAAPI 接受的最大连接数是 20 个采用 WAMP 的连接，再加上 20 个采用 HTTP POST 的连接。 |

## 在 Mac 上使用 WAAPI

WAAPI uses Windows-style paths to access files, with the root folder "/" represented by drive Z and the home folder drive Y. For example, in order to load project "/Volumes/path/to/MyProject.wproj", you must use path "Z:\Volumes\path\to\MyProject.wproj".

如有疑问，请在 Wwise 中的 Recent Projects（最近打开的工程）下查看显示的工程路径。

## 下一步

您现在可以根据 [WAAPI 示例](waapi_samples.html) 来试试 WAAPI，这些示例给您展现了如何用您偏好的语言和协议使用 WAAPI。

参见
:   - [WAAPI 示例](waapi_samples.html)
    - [查询 Wwise 工程](waapi_query.html)
    - [订阅 Wwise Authoring API 中的话题](waapi_subscribe.html)
    - [导入音频文件和创建架构](waapi_import.html)
    - [在 Wwise 插件中使用 Wwise Authoring API](waapi_plugin.html)