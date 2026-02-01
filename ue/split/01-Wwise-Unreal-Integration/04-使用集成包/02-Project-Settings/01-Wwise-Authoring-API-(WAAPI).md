# Wwise Authoring API (WAAPI)

|  |
| --- |
| Wwise Unreal Integration Documentation |

Wwise Authoring API (WAAPI)

Wwise Authoring API 可用于与 Wwise 设计工具进行通信。在同时运行 Unreal 和 Wwise 设计工具并将 Unreal 连接到 WAAPI 的情况下，WAAPI 允许 Unreal Integration 在会话期间获取和修改 Wwise 工程的相关信息。

有关 WAAPI 及其功能的详细信息，请参阅 <https://www.audiokinetic.com/library/edge/?source=SDK&id=waapi.html>。

|  |  |
| --- | --- |
|  | **注記：** WAAPI is only available on Windows and Mac in the Editor. |

# 连接到 WAAPI

After you integrate Wwise into your Unreal project, you must update an Unreal configuration setting to connect to WAAPI.

在 Unreal 工程中启用 WAAPI：

1. 在 Unreal Editor 中打开工程，并在 Wwise 设计工具中打开对应的 Wwise 工程。
2. 在 Unreal 中，依次单击 **Edit > Project Settings**。这时会打开 Unreal Project Settings 对话框。
3. 在左侧面板中，滚动到 Wwise 分区，然后单击 **User Settings**。
4. 选择 **Auto Connect to WAAPI**。WAAPI features such as inside the Wwise Browser are now enabled.

为了确保能够运行支持 WAAPI 的功能，Wwise 设计工具中打开的 Wwise 工程必须与 **Integration Settings** 中的 **Wwise Project Path** 所定义的工程匹配。

![](../../../../images/wwise_integration_settings.png)

Integration Settings

您可以在 Wwise User Settings 中配置用来连接到 WAAPI 的 IP 地址和端口。

![](../../../../images/wwise_user_settings.png)

User Settings

# 通过 C++ 使用 WAAPI

AkAudio 模块自带用于 [WAAPI C++ SampleClient](https://www.audiokinetic.com/library/edge/?source=SDK&id=waa__cpp__sample.html) 的 Unreal 封装类。

为了确保能够正常使用，您必须先按照 [Unreal Engine C++ 工程](using_cpp.html) 中所列步骤将 AkAudio 模块作为依赖项添加到游戏中。在完成此操作之后，便可使用 `FAkWaapiClient` 类。

You can also use the low-level WwiseAuthoring module bundled in the WwiseSoundEngine plug-in. This module is Editor-specific.