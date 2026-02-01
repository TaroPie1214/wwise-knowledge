# WwiseSoundEngine 模块

|  |
| --- |
| Wwise Unreal Integration Documentation |

WwiseSoundEngine 模块

# 静态声音引擎桥接

WwiseSoundEngine 模块包含 Wwise 声音引擎 API 接口以及各种捆绑插件。

Wwise 声音引擎中的大部分函数都在尽可能低的层级实施桥接。为了调用 Wwise 声音引擎 API，必须通过桥接来调用这些函数：

auto\* SoundEngine = IWwiseSoundEngineAPI::Get();

if (UNLIKELY(!SoundEngine)) return;

|  |  |
| --- | --- |
|  | **注意：** 不要直接使用任何 `AK::` 或 `ak::` 函数，否则可能会导致链接器错误、不稳定或发生崩溃。 |

在 Wwise 2022.1 之前，需要在 `AkAudio` 模块内从 `AkAudioDevice` 执行所有 `AK::SoundEngine` 调用。现在不必再这样做了，但原有方法仍可使用。在有些情况下，原有方法可能更好用。因为其为用户代码提供了更多功能，包括由 Unreal 类转换为 Wwise 原生类型，以及通过 Blueprint 执行各种操作。

There are multiple optional modules, specifically WwiseSoundEngine followed by the Wwise version (such as WwiseSoundEngine\_2024\_1), which contains the code that bridges the WwiseSoundEngine interface and the actual Wwise Sound Engine API.

# Null SoundEngine

The Wwise Integration for Unreal connects the Wwise SoundEngine to the Unreal Engine. There are valid reasons to disable the SoundEngine at build time:

- **Executing a server**: The Wwise Integration for Unreal is client-specific. Avoid running a Wwise SoundEngine on a server.
- **Executing a program**: Unreal programs perform various tasks, such as building, packaging, or cooking. Unreal Frontend and Insights are examples of programs with user interfaces. The Wwise SoundEngine is meant to be used exclusively for what Unreal defines as Games, and the Editor.
- **Building for an unsupported platform or platform version**: The Wwise SoundEngine includes optimized binaries for many modern platforms, but the binary files might not be installed for a particular platform. There might also be a different platform SDK version installed and selected than the ones used to build the Wwise SoundEngine.

It is therefore impossible to link the actual Wwise SoundEngine to the final executable. In these cases, the build scripts use the null SoundEngine. The null SoundEngine is an empty implementor that sits on top of the SoundEngine abstraction provided in the WwiseSoundEngine bridging module. Most functions return **AK\_NotImplemented** without any side effects.

Because the bridge requires the Wwise SoundEngine type definitions to be accurate for the platform, the **ThirdParty/include** folder must contain an interface for the platform, even if it is not activated in the current context. It is therefore impossible to guarantee that a build for an unsupported platform will work, even with the null SoundEngine.

There are also valid reasons to disable the SoundEngine at runtime:

- **Using the null SoundEngine** from build time.
- **Disabling audio**: Multiple options allow a game or the editor to run without sound.
- **Running a commandlet**: Editor commandlet operations complete without displaying a user interface. These are specialized programs built inside the Unreal Editor itself.
- **Error in initialization**: If the Wwise SoundEngine fails to initialize, or if the SoundBanks were never Generated for the project.

Typically, the Wwise SoundEngine is disabled when the Wwise SoundEngine is linked inside the final executable package. Some of the issues can be fixed without restarting the Editor. Runtime issues do not use the null SoundEngine unless specified.

The logic for a supported target is executed during Unreal's project generation step in **WwiseUEPlatform.IsWwiseTargetSupported**. You can determine whether the null SoundEngine is used in UBT's logs: The "Wwise SoundEngine is disabled: Using the null SoundEngine instead." log will be displayed along with the reason. This message appears multiple times when building the Wwise SoundEngine as an Engine plug-in. The message is informative, not an error.

To help with debugging, a similar message is also repeated at runtime in the logs during the Wwise plug-in initialization: "Wwise SoundEngine is disabled: Using the null SoundEngine."