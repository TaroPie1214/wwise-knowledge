# 集成 Wwise Motion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成 Wwise Motion

Motion 插件方便用户控制控制接口的触觉反馈。借助 Wwise，可使用同样的工具来管理应用程序中的振动效果和音频。从内部来说，振动数据与音频数据并无差别。所有适用于音频的功能同样适用于振动。振动功能可提供两种类型的触觉反馈：既可将工程中的音频信号转换为振动，也可使用 Motion 音频源生成专用振动信号。只要配有支持的控制器，就可在 Windows 上直接使用 Wwise 设计工具来测试振动效果。

# 振动组件

Motion 利用 Wwise 声音引擎插件系统在应用程序中实现自身功能，并可划分为两个模块：音频源 (*Motion*) 和音频设备 (*Wwise Motion*)。作为一个强大的可选工具，Motion 音频源方便精确而灵活地设计振动效果。

## Wwise Motion 音频设备插件

Wwise Motion 音频设备插件可被视为声音引擎和振动设备之间的连接纽带。正如其他音频设备插件，它从一组听者接收数据，并会将数据呈现给设备。此插件设在单独的库内，并需要同时包含在 Wwise 设计工具和应用程序中。请参阅 [设置振动](integrating_elements_motion.html#setup_motion) 一节了解更多信息。

## Motion 源插件

Motion 源插件方便用户设计触觉反馈效果器的行为。正如其他音频源一样，您可以将 Motion 添加至 Wwise 工程中的 Sound SFX 节点。为此，请确保将 Sound SFX 节点的 Output Bus 设为振动总线。有关详细信息，请参阅 [Motion](https://www.audiokinetic.com/library/edge/?source=Help&id=motion_source_plug_in)。

# 设置振动

为了在应用程序中使用振动功能，必须正确设置各个组件。注意，所有适用于音频流程的概念同样适用于振动。它使用相同的总线、听者和发声体（参阅“ [集成 Listener](soundengine_listeners.html) ”）。

## Wwise 设计工具设置

为了能向设备发送声音或振动数据，必须将经授权的 Wwise Motion Audio Device 添加至 Wwise 工程的 Audio Device 文件夹（位于 Project Explorer 的 Audio 选项卡中）。Wwise Motion Audio Device 是声音引擎用来与振动设备进行交互的插件。同时，必须将 Wwise Motion Audio Device 指派给顶层 Audio Bus。**“振动总线”统称指派有 "Wwise Motion" Audio Device 的顶层 Audio Bus。**为了方便排除故障和监控，最好在工程中使用单个振动总线层级结构。然后，便可将任何 Sound SFX 的 Output Bus 设为振动总线以创建触觉反馈。通常，使用振动总线的 Sound SFX 元素会同时使用 Motion 音频源。为了模拟音频和振动，Sound SFX 须至少拥有一条振动总线和一条音频总线（作为 Output Bus 或 Auxiliary Bus）。

## 游戏设置

在游戏端，首先要确保链接 `AkMotionSink` 库。此库为所支持平台的标准控制器提供支持。同时，还需包含 `SDK\include\AK\plugin` 下的 [AkMotionSinkFactory.h](_ak_motion_sink_factory_8h.html) 文件。此文件用于自动注册插件，因此必须包含在内。

|  |  |
| --- | --- |
|  | **备注:** 在 Unity 和 Unreal 中，会自动管理插件库。无需手动添加 `AkMotionSink` 。 |

有关支持的控制器及其他要求，请参阅下表。

|  |  |  |  |
| --- | --- | --- | --- |
| 平台 | 设备 | 设备声道配置和布局 | 其他要求 |
| Windows | XInput-compatible Controllers | Anonymous 2-channel:  Left motor, right motor | Xinput.lib |
| Windows | GameInput-compatible Controllers | Anonymous 4-channel and Stereo 2-channel | See [Support for GameInput on Windows](integrating_elements_motion.html#wwise_motion_gameinput_windows) for more information. |
| Windows | DualShock 4 and DualSense Controllers | Anonymous 2-channel and Stereo 2-channel | See the "Support for DualShock 4 and DualSense on Windows using libScePad" section below (login with PS5 license required) |

若应用程序要在一些设备上使用振动效果，则必须为每个设备添加专用输出。比如，对于连有四个玩家的分屏游戏，需要添加四个不同的输出以便各个控制器分别接收触觉反馈。若要添加输出设备，请使用 Wwise API 的 `AK::SoundEngine::AddOutput` 函数，并在 `AkOutputSettings` 参数中指定 ShareSet 名称（如 Wwise 工程中所定义）。另外，因为可能连接多个设备，所以还必须提供设备 ID。下表列出并描述了有关设备 ID 的详细信息。

|  |  |  |
| --- | --- | --- |
| 平台 | 设备 | 信息 |
| Windows | XInput-compatible Controllers | Use the player index between 0 to 3. |
| Windows | GameInput 兼容控制器 | 检索手柄的 GameInputDeviceInfo，并以 GameInputDeviceInfo::deviceId 的地址为参数调用 `AK::GetAppLocalDeviceIdHash` 。  Note that the Motion output is only initialized for devices with either a non-zero value for GameInputDeviceInfo::supportedRumbleMotors, or a non-zero value for GameInputHapticInfo::locationCount.  不支持仅使用力觉反馈的设备（比如有些赛车方向盘和飞行摇杆）。 |

|  |  |
| --- | --- |
|  | **备注:** 在除 Windows 外的所有其他平台上，若把设备 ID 指定为 0，将指向第一个支持振动效果的可用设备。在 Windows 上，若设备 ID 为 0，则初始化为 XInput 设备。 |

注意，游戏控制器可能因连接问题或通信问题而断开。除了会浪费一些资源，断开不会对声音引擎产生任何不利影响。若认为设备已经断开很长一段时间，请调用 `AK::SoundEngine::RemoveOutput` ，并提供调用 `AddOutput()` 函数时返回的 `AkOutputDeviceID`。

## Support for GameInput on Windows

Wwise Motion supports both rumble-based gamepads and haptic-based gamepads through the GameInput API for Windows.

If your project uses advanced haptics with GameInput, the following additional considerations apply:

- GameInput v2.0 or newer must be installed on the target Windows system.
- You must incorporate the GameInput redistributable in your application's installer yourself, according to the instructions provided in the [Microsoft](namespace_microsoft.html) documentation (see [Overview of GameInput](https://learn.microsoft.com/gaming/gdk/docs/features/common/input/overviews/input-overview)).

When you provide the device ID retrieved through `AK::GetAppLocalDeviceIdHash` as-is, Wwise Motion will default to the rumble-based Motion implementation for the gamepad associated with this device ID. In order to use the haptic-based implementation with a haptic-compatible device, you must first apply a bitwise-OR operation of the flag `AKMOTION_GAMEINPUT_HAPTICS_MODE` to the device ID before initializing the device. This flag is provided in the `AkMotionSinkGameInputHelpers.h` file. The following example demonstrates detection of a haptic-enabled device:

const GameInputDeviceInfo\* pDeviceInfo = nullptr;

pGameInputDevice->GetDeviceInfo(&pDeviceInfo);

//Get the AkDeviceID for the GameInput device

[AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) wwiseDeviceID = [AK::GetAppLocalDeviceIdHash](namespace_a_k_ab5ba05e30e949f4b26b949af3fe54f48.html#ab5ba05e30e949f4b26b949af3fe54f48)(&pDeviceInfo->deviceId);

//If the device supports haptics, apply the flag to the AkDeviceID before initialization.

GameInputHapticInfo hapticInfo;

pGameInputDevice->GetHapticInfo(&hapticInfo);

if (hapticInfo.locationCount > 0 && hapticInfo.locationCount <= GAMEINPUT\_HAPTIC\_MAX\_LOCATIONS)

{

wwiseDeviceID |= [AKMOTION\_GAMEINPUT\_HAPTICS\_MODE](_ak_motion_sink_game_input_helpers_8h_ae0b216fd3c95f6dcaa6d297cb0bbf5cd.html#ae0b216fd3c95f6dcaa6d297cb0bbf5cd);

}

|  |  |
| --- | --- |
|  | **备注:**  - When using GameInput advanced haptics, Wwise Motion creates a WASAPI audio session so that the waveform is automatically sent to the configured channels of the audio device for the gamepad. 要想正常运行相应功能，必须在 PC 上像常规音频设备一样激活该音频设备。 |

# 多人游戏考量因素

振动输出跟其他 Secondary Output 是一样的，因此也存在相同的限制和要求。假如您在制作单人游戏（即只有一个玩家在本地控制游戏），Listener/Game Object 设置会非常简单。一般情况下，新的振动输出会将同一默认 Listener 复用为主音频输出。也就是说，在单人设置中基本上不需要管理 Listener。

对于多人游戏，则须为每个振动输出创建一个 Listener/Game Object。只有如此，各个玩家才能分别获得游戏情境产生的对应触觉反馈。在 `AK::SoundEngine::AddOutput()` 初始化输出的同时，必须初始化与设备关联的 Listener。各个 Listener 会为声音或振动提供附加通路层。在针对只与某个玩家的 Listener 关联的 Game Object 上播放 Event 时，可让声音只被该玩家听到。您可以通过调用 `AK::SoundEngine::SetListeners` 来建立这一关联。另外，也可将多个 Listener 与同一 Game Object 关联，生成作用于所有 Listener 的“广播”效果。请参阅 [集成 Listener](soundengine_listeners.html) 了解有关Listeners和Game Objects的更多信息。

|  |  |
| --- | --- |
|  | **备注:** 即便 Emitter 有设为振动输出的 Listener，也要将对应的声音输出到振动总线层级结构。 |

# 示例

以下示例将展示如何设置应用程序以便使用振动效果。您也可以参阅 SDK 示例中 Integration Demo (DemoMotion.cpp) 的 Demo Motion。其中提供有所有支持平台的工作示例。

## 单人设置

首先，跟其他插件一样，您需要包含对应文件，并链接库（仅针对 Wwise 原生开发，对 Unity 来说并不需要）。

#include "[AkMotionSinkFactory.h](_ak_motion_sink_factory_8h.html)" // 链接至 AkMotionSink.lib

然后，使用 Wwise 工程中设置的 Wwise Motion Audio Device ShareSet 名称添加附加输出（在本例中名称为 Wwise\_Motion）。因为要使用第一个相连的游戏控制器，所以在此将 0 用作输出 ID。

[AkOutputSettings](struct_ak_output_settings.html) outputSettings("Wwise\_Motion", 0);

[AK::SoundEngine::AddOutput](namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html#a15ab79f954a307902f529d8ccde8ad48)(outputSettings);

然后，播放 Event。在 Wwise 工程中，"Play\_Explosion" Event 关联的 Sound SFX 会输出至将 "Wwise\_Motion" ShareSet 指派为 Audio Device 的总线。

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) explosionGO = 100;

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)(explosionGO, "Explosion");

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)("Play\_Explosion", explosionGO);

## 多人设置

本节将介绍如何为同一主机上而非网络游戏中的多个玩家设置振动效果。在多人设置中，必须分别设置振动效果或玩家专用输出，以便反映玩家在游戏世界中的视角。为此，每个玩家都需要分别设置 Listener。

int NUM\_PLAYERS = 4;

const [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) OBJ\_FOR\_PLAYER[MAX\_PLAYERS] = {100 ,200, 300, 400}; // Game Object ID 可以任选。

for(int i = 0; i < NUM\_PLAYERS; i++)

{

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)(OBJ\_FOR\_PLAYER[i]); // 注册要用作 Listener 的 GameObject。

[AK::SoundEngine::SetListeners](namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html#a2f85a55c38afa2e0dbc6172a7bec91d1)(OBJ\_FOR\_PLAYER[i], &OBJ\_FOR\_PLAYER[i], 1); // 让 Game Object 接收自己发出的声音。

}

然后，为每个玩家添加一个输出。每个 Audio Device ShareSet 都可多次使用，所以不用创建多个 Audio Device ShareSet。不过，必须为每个控制器设置一个实际设备 ID。本例适用于 Windows 上的 Xbox 控制器。有关如何针对特定平台检索设备 ID 的信息，请参阅“ [游戏设置](integrating_elements_motion.html#motion_application_setup) ”中的表格。

const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) DEVICE\_SPECIFIC\_ID[MAX\_PLAYERS] = {0, 1, 2, 3}; // 对于 Windows 上的 Xbox 控制器，设备 ID 为 0 ~ 3。其他平台有不同的要求。

for(i = 0; i < NUM\_PLAYERS; i++)

{

[AkOutputSettings](struct_ak_output_settings.html) settings("Wwise\_Motion", DEVICE\_SPECIFIC\_ID[i]); // 使用 Wwise\_Motion 共享集来驱动设备 DEVICE\_SPECIFIC\_ID[i]。

res = [AK::SoundEngine::AddOutput](namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html#a15ab79f954a307902f529d8ccde8ad48)(settings, &motionOutputIDs[i], &OBJ\_FOR\_PLAYER[i], 1); // 添加输出，并链接相应的 Listener。

}

然后，播放 Event。在 Wwise 工程中，"Play\_GunFire" Event 关联的 Sound SFX 会输出至将 "Wwise\_Motion" ShareSet 指派为 Audio Device 的总线。

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)("Play\_GunFire", OBJ\_FOR\_PLAYER[0]); // 鉴于 Game Object 和 Listener 的关系，将仅播放玩家控制的 0 号控制器。

若要播放的 Event 会影响多个设备，请设置新的 Game Object 并确保将其作用于所有玩家专用 Listener。

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)(explosionGO, "Explosion"); // 注册要播放爆炸声的 Game Object。

[AK::SoundEngine::SetListeners](namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html#a2f85a55c38afa2e0dbc6172a7bec91d1)(explosionGO, OBJ\_FOR\_PLAYER, 4); // 将玩家控制的 4 个 Listener 全部绑定至该 Game Object，以便都能接收 Motion Effect。

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)("Play\_Explosion",explosionGO ); // 因为 4 个 Listener 全部都绑定至 explosionGO，所以 Play\_Explosion 事件将广播给所有 Listener。

有关多人设置的例子，请参阅 IntegrationDemo 示例中的 `DemoMotion` 类。

# 核对清单与故障排除

为了确保特定设备可使用某个设备接收振动效果，必须执行以下操作：

1. 将 Wwise Motion Audio Device ShareSet 添加到工程中。
2. 创建顶层 Audio Bus，并将其 Audio Device 设为刚才添加的 Wwise Motion Audio Device ShareSet。
3. 创建 Sound SFX 并将其输出到振动总线层级结构。
4. 在游戏中，链接 `AkMotionSink` 库。包含 `AkMotionSinkFactory.h`，同时链接 `AkMotionSink` 库。

   |  |  |
   | --- | --- |
   |  | **备注:** 在 Unity 和 Unreal 中，会自动管理插件库。因此，没必要执行这一步。 |
5. 使用 `AK::SoundEngine::RegisterGameObj` 创建要调用和接收振动事件的 Game Object。
6. 使用 Wwise Motion ShareSet 和设备 ID 来调用 `Ak::SoundEngine::AddOutput` 。对于多人设置，请分别提供 Listener 对象。
7. 像音频 Event 一样触发 Event。

将 Motion 添加到 Wwise 工程中：

1. 将 Wwise Motion Audio Device ShareSet 添加到工程中。
2. 创建顶层 Audio Bus，并将其 Audio Device 设为刚才添加的 Wwise Motion Audio Device ShareSet。
3. 创建 Sound SFX 并将其输出到振动总线层级结构。
4. 在 Audio Preferences 中，找到要使用振动效果的总线，然后从列表中选择与之对应的设备并将其设为振动设备。

## 性能分析

为了排除故障，建议先对应用程序进行性能分析。在 Wwise 设计工具中，可按照[性能分析](https://www.audiokinetic.com/library/edge/?source=Help&id=profiling)中所述来对应用程序实施性能分析。您可以利用各项工具来了解问题的根源。在 Capture Log 视图中，可查看错误代码（显示为红色）。在 Graph 视图中，可查看声音引擎管线的图示。管线末端应会显示振动设备。若未显示任何振动设备，则表示声音引擎无法找到指定的设备。另外，Emitter/Listener 选项卡会显示所有 Emitter-Listener 组合。若 Motion Effect 出现问题，则表示 Emitter 可能没有关联针对振动设备指定的 Listener。

若触发 Motion Effect 时出现问题，请执行以下操作：

- 查看 Capture Log，确保插件无注册错误。若有错误，请确认是否已包含 `AkMotionSinkFactory.h` 并链接至 `AkMotionSink` 库。
- 确保声音引擎已对设备进行初始化。若未初始化，则从游戏调用 `AddOutput` 时将在 Capture Log 中显示相应错误。
- 确保将所播放的 Sound SFX 输出到指向振动设备的总线。为此，请查看 Sound SFX 的 Audio Bus 属性和总线的 Audio Device 属性。
- 在 Voices Graph 选项卡中，检查触发了哪个 Emitter。确保 Emitter-Listener 选项卡中设有关联的 Listener。该 Listener 与发声和收听的 Game Object 相同。若无关联 Listener，请检查 `RegisterGameObj` 、 `SetListeners` 和 `AddOutput` 调用。
- 确保 Listener 与规定输出设备关联。
- 查看各项 API 调用的结果，并检查有无错误。

对于 Android 设备，请在应用程序的 AndroidManifest.xml 文件中添加权限：

<uses-permission android:name="android.permission.VIBRATE"/>

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)

AKSOUNDENGINE\_API AKRESULT RegisterGameObj(AkGameObjectID in\_gameObjectID)

[AkOutputSettings](struct_ak_output_settings.html)

Platform-independent initialization settings of output devices.

**Definition:** [AkSoundEngineTypes.h:219](_ak_sound_engine_types_8h_source.html#l00218)

[AkMotionSinkFactory.h](_ak_motion_sink_factory_8h.html)

[AK::SoundEngine::SetListeners](namespace_a_k_1_1_sound_engine_a2f85a55c38afa2e0dbc6172a7bec91d1.html#a2f85a55c38afa2e0dbc6172a7bec91d1)

AKSOUNDENGINE\_API AKRESULT SetListeners(AkGameObjectID in\_emitterGameObj, const AkGameObjectID \*in\_pListenerGameObjs, AkUInt32 in\_uNumListeners)

[AK::SoundEngine::AddOutput](namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html#a15ab79f954a307902f529d8ccde8ad48)

AKSOUNDENGINE\_API AKRESULT AddOutput(const AkOutputSettings &in\_Settings, AkOutputDeviceID \*out\_pDeviceID=NULL, const AkGameObjectID \*in\_pListenerIDs=NULL, AkUInt32 in\_uNumListeners=0)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AKMOTION\_GAMEINPUT\_HAPTICS\_MODE](_ak_motion_sink_game_input_helpers_8h_ae0b216fd3c95f6dcaa6d297cb0bbf5cd.html#ae0b216fd3c95f6dcaa6d297cb0bbf5cd)

#define AKMOTION\_GAMEINPUT\_HAPTICS\_MODE

**Definition:** [AkMotionSinkGameInputHelpers.h:37](_ak_motion_sink_game_input_helpers_8h_source.html#l00037)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)

[AK::GetAppLocalDeviceIdHash](namespace_a_k_ab5ba05e30e949f4b26b949af3fe54f48.html#ab5ba05e30e949f4b26b949af3fe54f48)

static AkUInt32 GetAppLocalDeviceIdHash(const APP\_LOCAL\_DEVICE\_ID \*in\_pAppLocalDeviceId)

**Definition:** [AkMotionSinkGameInputHelpers.h:44](_ak_motion_sink_game_input_helpers_8h_source.html#l00044)

[AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260)

AkUInt32 AkDeviceID

I/O device ID

**Definition:** [AkTypedefs.h:57](_ak_typedefs_8h_source.html#l00057)