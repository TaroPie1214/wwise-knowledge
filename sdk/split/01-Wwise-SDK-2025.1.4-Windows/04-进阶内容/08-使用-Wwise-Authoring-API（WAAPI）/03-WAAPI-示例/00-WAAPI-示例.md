# WAAPI 示例

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

WAAPI 示例

以下的示例页面给出了简单的示范，展示了如何设置不同语言和协议的 WAAPI，如何为相应基础工程写代码，如何运行工程。

不过，首先应尝试在浏览器中打开 `<Wwise 安装路径>/SDK/samples/WwiseAuthoringAPI/js/hello-wwise-web-http/index.html`，确认已正确设置并可正常运行 WAAPI。若显示 `Hello Wwise v###.#.#!`，则表示已连接至对应版本的 Wwise 并可转至其他示例。若显示 `Not connected.`，则表示无法使用其他示例。请确保:

1. 打开对应版本的 Wwise；
2. 在 Wwise [User Preferences](https://www.audiokinetic.com/library/edge/?source=Help&id=user_preferences) 内启用 WAAPI：选择 **Enable Wwise Authoring API**；
3. 未在 Wwise 中打开任何模式窗口；
4. 使用支持的浏览器（Chrome、Firefox 或 Opera）。

|  |  |
| --- | --- |
|  | **备注:** 以下大部分示例均需下载库文件，因此需要连接 Internet。 |

- [JavaScript, Node.js - WAMP](wamp_js_node.html)
  - [初始化工程](wamp_js_node.html#wamp_js_node_init)
  - [工程代码](wamp_js_node.html#wamp_js_node_code)
  - [运行工程](wamp_js_node.html#wamp_js_node_run)
- [浏览器中的 JavaScript - WAMP](wamp_js_browser.html)
  - [初始化工程](wamp_js_browser.html#wamp_js_browser_init)
  - [工程代码](wamp_js_browser.html#wamp_js_browser_code)
  - [运行工程](wamp_js_browser.html#wamp_js_browser_run)
- [JavaScript, Node.js - HTTP POST](http_post_js.html)
  - [初始化工程](http_post_js.html#httpPost_js_init)
  - [工程代码](http_post_js.html#httpPost_js_code)
  - [运行工程](http_post_js.html#httpPost_js_run)
- [Python (Waapi-Client) – 远程过程调用](waapi_client_python_rpc.html)
  - [初始化工程](waapi_client_python_rpc.html#waapi_client_python_rpc_init)
  - [工程代码](waapi_client_python_rpc.html#waapi_client_python_rpc_code)
  - [运行工程](waapi_client_python_rpc.html#waapi_client_python_rpc_run)
- [Python (Waapi-Client) – 订阅](waapi_client_python_subscription.html)
  - [初始化工程](waapi_client_python_subscription.html#waapi_client_python_subscription_init)
  - [工程代码](waapi_client_python_subscription.html#waapi_client_python_subscription_code)
  - [运行工程](waapi_client_python_subscription.html#waapi_client_python_subscription_run)
- [C# WaapiClient - WAMP](wamp_cs.html)
  - [初始化工程](wamp_cs.html#wamp_cs_init)
  - [工程代码](wamp_cs.html#wamp_cs_code)
  - [运行工程](wamp_cs.html#wamp_cs_run)
- [C++ - WAMP](waa_cpp_sample.html)
  - [在 Windows 上构建](waa_cpp_sample.html#waa_cpp_sample_compileOnWindows)
  - [在 OS X 上构建](waa_cpp_sample.html#waa_cpp_sample_compileOnMac)
  - [使用示例](waa_cpp_sample.html#waa_cpp_sample_usingTheSample)
  - [C++ 客户端和 WAMP 素材库](waa_cpp_sample.html#waa_cpp_sample_whatIsProvided)
  - [日志记录](waa_cpp_sample.html#waa_cpp_sample_logging)

|  |  |
| --- | --- |
|  | **注意:** 请确保在开始参看这些示例前已经理解 [网络安全](waapi_prepare.html#waapi_security) 。 |