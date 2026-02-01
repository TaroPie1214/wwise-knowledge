# C++ - WAMP

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

C++ - WAMP

这一页的示例展示了如何在 C++ 中使用 Wwise Authoring API。它也包含支持 Wwise 所用的 WAMP 协议的库代码，您也可以将其用于您自己的 C++ 工程。

# 在 Windows 上构建

Visual Studio 解决方案位于 “samples/WwiseAuthoringApi/cpp/SampleClient”。您必须安装 Wwise SDK 才能访问它。

Simply open SampleClientWindows\_TOOLSET.sln (where TOOLSET is vc160 or vc170) build the solution.

|  |  |
| --- | --- |
|  | **备注:** This example requires Visual Studio 2019 (vc160) or 2022 (vc170). |

# 在 OS X 上构建

您可以使用 samples/WwiseAuthoringApi/cpp/SampleClient/mac\_build.sh 构建所有目标。

# 使用示例

该示例是在命令行上运行的。默认情况下，当没有提供参数时，它会对 Wwise Authoring 运行 getInfo 这条 RPC 调用并显示基本信息。

您可以使用相关命令行参数来运行更多的示例：

- `TestWampClient：` 使用 `AkJson` 类来展示基本操作（如连接、调用、订阅）。
- `TestWampClientJsonString：与` `TestWampClient` 基本相同，只不过 JSON 使用 `std::string` 而非 `AkJson` 类。
- `PerfTest：` 通过重复执行同一调用来实施基本性能测试，并显示每项调用的平均执行时间以及总计时间。
- `TestErrors：` 生成并处理各种不同的错误，并显示如何使用记录功能。
- `TestMonitoring：` 展示如何监控 Wwise 的当前状态。它会检测 Wwise 何时启动、退出、加载或关闭工程以及任意给定时间加载的工程。

# C++ 客户端和 WAMP 素材库

此示例包含 AkAutobahn 库（基于 Autobahn|Cpp 的 WAMP\_POCO 库的改良版）、civetweb 库和 `Client` 类。AkAutobahn 包含在 Wwise SDK 中。`Client` 类为我们的 API 提供了简单的界面，该界面在内部使用“session” 类通过 WAMP 协议连接到 Wwise Authoring。 请随意使用初始的 `Client` 或将其改动以更好适应您的需求。

为了方便，`Client` 类会使用阻塞调用（通过调用 std::future::get）。因此，发起调用的线程会阻塞，直到 Wwise Authoring 提供结果为止。您可以使用超时参数来指定要在多长时间内阻止调用。“session”类会返回 std::future 用于线程同步，也就意味着如果异步版本的 `Client` 类更能满足您的需求，那么您可以实现自己的异步版 `Client` 类。

不支持从回调内调用 `Client` 类。也就是说，在 `Client` 已经向您发起调用时，您不可以再调用 `Client` 。

# 日志记录

日志记录是可选项，但它经常能对调试过程有所帮助。您可以调用 `Logger::Get()->SetLoggerFunction(logFunction)` 来提供您自己的日志记录函数。