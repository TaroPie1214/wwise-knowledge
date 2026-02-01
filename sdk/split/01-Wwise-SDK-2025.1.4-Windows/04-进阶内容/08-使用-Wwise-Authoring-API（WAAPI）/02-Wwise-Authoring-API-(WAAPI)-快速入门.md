# Wwise Authoring API (WAAPI) 快速入门

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Authoring API (WAAPI) 快速入门

# 协议

您可以通过不同的协议和 API 来访问 Wwise Authoring API：

- **WAMP：WAMP** 旨在连接分布式应用中的应用组件。WAMP 使用 WebSocket 作为其默认传输方式，允许有序、可靠、双向、信息为导向的通信。 WAMP 允许客户端使用 JSON 参数来调用函数并获取结构性 JSON 结果。WAMP 也允许客户端订阅通知。
- **HTTP** **POST：HTTP** 是分布式应用的一种应用协议。HTTP 是在互联网上传输内容的最常用手段。 POST 让调用者能发送一个文档主体，对于 Wwise Authoring API来说，这个文档就像 JSON 一样，对应函数参数。HTTP 的响应就是 JSON 结果。
- **Wwise 插件**：Wwise 设计工具插件可以通过 `AK::Wwise::Plugin::Host::WaapiCall()` 来调用 WAAPI 函数。请参阅 [在 Wwise 插件中使用 Wwise Authoring API](waapi_plugin.html) 。

`WAMP` 和 `HTTP` 协议可与各种语言结合使用，包括 `C++`、`C#`、`JavaScript`、`Python` 以及 `HTTP` 和 `WebSocket` 支持的其他一些语言。

|  |  |
| --- | --- |
|  | **备注:** WAMP 是一种开放式的标准 WebSocket 子协议，它可以提供统一的应用程序路由。WAMP implementations are available in the most popular programming languages. 如需进一步了解 WAMP，请转到 [https://wamp-proto.org](https://wamp-proto.org/)。 |

|  |  |
| --- | --- |
|  | **备注:** WAMP provides the best performance and experience because it reuses the same WebSocket connection for the whole session and provides bidirectional communications. |

下表概括列出了协议支持的各项功能：

|  |  |  |  |
| --- | --- | --- | --- |
| **API 功能** | **WAMP** | **HTTP POST** | **`AK::Wwise::Plugin::Host::WaapiCall()`** |
| **远程程序调用**    允许针对 Wwise 设计工具远程调用函数    参见 [Wwise Authoring API Reference](waapi_index.html) 章节 | 支持 | 支持 | 支持 |
| **发布 & 订阅**    允许在 Wwise 设计工具中出现变动时接收通知。 | 支持 | Not 支持 | Not 支持 |
| 最佳性能 | 是 | 否 | 是 |

# 编程语言

假如您想利用 WAMP 协议来调用 WAAPI，有多种语言可供选择。WAMP 实现库支持各种编程语言。 如需查看现有实现库列表，请登录 [wamp-proto.org](https://wamp-proto.org/)。

不过，有些实现库使用起来比较困难，需要具备一定的编程技能。由于 WAAPI 只会用到 WAMP 功能中的一个子集，因而为了增强 WAAPI 的易用性，我们为部分可用实现库提供了抽象层。下表列出了大部分常用语言的相关建议。

|  |  |
| --- | --- |
| **语言** | **建议** |
| C++     (**推荐**) | **使用 AkAutobahn**  AkAutobahn 是 Autobahn C++ 的一个分支库，相对而言依赖数较少，不仅接口更简洁，性能也很高。  **难度：** 需要具备中级 C++ 编程技能。  **说明：** [C++ - WAMP](waa_cpp_sample.html)   **源码：** \SDK\samples\WwiseAuthoringAPI\cpp\SampleClient\AkAutobahn   **示例：** \SDK\samples\WwiseAuthoringAPI\cpp\SampleClient\SampleClient   |  |  | | --- | --- | |  | **备注:** 另外，C++ 还可直接用在 Source 或 Effect 插件内。请参阅 [在 Wwise 插件中使用 Wwise Authoring API](waapi_plugin.html) 了解详情。 | |
| C#     (**推荐**) | **使用 WaapiClientCore 或 WaapiClientJson**  您可以选择：   - **WaapiClientCore：** C# 中使用的 WAAPI 客户端库，只依赖于 .NET 4.5，没有第三方引用。它包含 WAMP 客户端，可以连接到 Wwise，并访问 WAAPI 远程程序和主题订阅。该 API 基于字符串，因此可选用自定义 JSON 序列化方式。另外，此客户端还可兼容 Unity 2018.1+。 - **WaapiClientJson：** C# 中使用的 WAPPI 客户端库，依赖于 [Json.NET](https://www.newtonsoft.com/json)。为了便于操控 JSON，专门添加了 JSON 依赖库。不过，需要使用 NuGet 包管理器扩展。若同时从 Unity Store 安装了 Json.NET for Unity，则此客户端还可兼容 Unity。   **难度：** 使用起来非常简单。只需初级 C# 编程技能。  **说明：** [C# WaapiClient - WAMP](wamp_cs.html)   **示例：** SDK\samples\WwiseAuthoringAPI\cs\WaapiClientSample |
| 结合使用 JavaScript/TypeScript 和最新 Node.js LTS    (**推荐**) | **使用 waapi-client JS**  waapi-client 是 Autobahn JS 之上提供的一个抽象层。It adds promises and async/await support, and only expose the required WAMP functionality. 请注意，waapi-client 同时包含 TypeScript 绑定。  **难度：** 需要初级到中级 JavaScript 编程技能。  **Instructions:** [JavaScript, Node.js - WAMP](wamp_js_node.html)   **Npm:** <https://www.npmjs.com/package/waapi-client>   **Sources:** <https://github.com/audiokinetic/waapi-client>   **Sample:** SDK\samples\WwiseAuthoringAPI\js\hello-wwise-node-wamp |
| 在 Browser 中使用 JavaScript | **使用 autobahn-browser**  autobahn-browser 是一个可直接在浏览器中使用的 WAMP 实现库。  **难度：** 需要中级 JavaScript 和 Web 编程技能。  **说明：** [浏览器中的 JavaScript - WAMP](wamp_js_browser.html)   **源码：** <https://github.com/crossbario/autobahn-js-browser>   **示例：** SDK\samples\WwiseAuthoringAPI\js\hello-wwise-web-wamp |
| Python 3.7+     (**推荐**) | **使用 waapi-client Python**  waapi-client 是 Autobahn Python 之上提供的一个抽象层。它可以大大增强 WAPPI 的易用性，并且只会暴露所需 WAMP 功能。  **难度：** 使用起来非常简单。只需初级 Python 编程技能。  **说明：** [Python (Waapi-Client) – 远程过程调用](waapi_client_python_rpc.html)   **Pypi：** <https://pypi.org/project/waapi-client/>   **源码：** <https://github.com/audiokinetic/waapi-client-python>   **示例：** SDK\samples\WwiseAuthoringAPI\python\waapi-client-py3 |
| 其他语言 | 使用 <https://wamp-proto.org/> 上列出的 WAMP 实现库，或者直接结合 HTTP 使用 WAAPI。 |

请参阅 [WAAPI 示例](waapi_samples.html) 。