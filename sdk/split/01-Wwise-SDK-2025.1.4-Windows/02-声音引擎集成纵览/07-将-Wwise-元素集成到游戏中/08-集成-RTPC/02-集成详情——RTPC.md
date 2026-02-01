# 集成详情——RTPC

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成详情——RTPC

RTPC 是可使用 `AK::SoundEngine::SetRTPCValue()` 函数来更新的实时参数。由于事件动作无法更改 RTPC 值（译注：无法连续更改），因此设置它们是您的职责。

# RTPC 值

RTPC 值总是被当作 AkRtpcValue 传输，后者代表 32 位浮点数值。This value is used to directly interpolate in the RTPC curve the sound designer has previously defined in Wwise.

当参数超出在 Wwise 中定义的曲线时，将使用曲线上的极值。如果参数大于最大值，则使用曲线上最右侧的值；如果参数小于最小值，则使用曲线上最左侧的值。如果 RTPC 参数代表布尔值，则 1 表示 True，0 表示 False。

# 设置 RTPC 值

设置 RTCP 值的方式如下：

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [AK::SoundEngine::SetRTPCValue](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26)(

[AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0) in\_rtpcID, // ID of the RTPC

[AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) in\_value, // Value to set

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID = [AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34) // Associated game object ID

);

或者

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [AK::SoundEngine::SetRTPCValue](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26)(

const char \* in\_pszRtpcName, // Name of the RTPC

[AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) in\_value, // Value to set.

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID = [AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34) // 关联的游戏对象 ID

);

或者

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [AK::SoundEngine::SetRTPCValue](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26)(

const wchar\_t \* in\_pszRtpcName, // Name of the RTPC

[AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140) in\_value, // Value to set.

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID = [AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34) // 关联的游戏对象 ID

);

RTPC 值可影响在游戏对象、总线参数、源插件和效果器插件上正在播放的声音。We will consider all these possibilities.

## 启用 ID

要使用 ID，必须在选中 Wwise 中 Generate SoundBanks 对话框上的“Generate header file”选项的情况下生成 SoundBank。名为 Wwise\_IDs.h 的定义文件中包含所有必要的 ID。每次生成 SoundBank 时都会更新此文件。

## RTPC 和游戏对象

RTPCs can be used to modify the behavior of game objects by affecting a Sound SFX, a Sound Voice, a container or a Property Container. Switches can also be modified through the use of RTPCs (refer to [驱动切换开关](soundengine_switch.html#soundengine_switch_driving)).

您只需一次函数调用，即可为所有未赋值的游戏对象设置全局 RTPC 值。To do this, call the [AK::SoundEngine::SetRTPCValue()](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26) method using AK\_INVALID\_GAME\_OBJECT as game object ID, or without specifying an AkGameObjectID parameter. However, once the sound object receives a call to this method using valid AkRtpcID and AkGameObjectID inputs, the game object is considered assigned and will no longer be affected by the global RTPC value.

## RTPC 与总线

在 Wwise 中，有些总线参数可通过 RTPC 进行修改。总的来说，在总线参数上应用 RTPC 时，一般都要通过 AK\_INVALID\_GAME\_OBJECT 参数调用 [AK::SoundEngine::SetRTPCValue()](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26) 方法（如 [RTPC 和游戏对象](soundengine_rtpc.html#soundengine_rtpc_pergameobject) 中所述）。这样可以为所有总线提供一个 RTPC 值。

不过，若工程为总线应用 [3D Positioning](https://www.audiokinetic.com/library/edge/?source=Help&id=applying_positioning_to_busses)，则可能要为每条总线赋予特定的值。在这种情况下，请将与总线绑定的 Game Object/Listener 提供给 [AK::SoundEngine::SetRTPCValue()](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26) 函数。

## RTPC 与插件

In Wwise, RTPCs can affect the properties of effect and source plug-ins, such as their reverb levels, pitch, or low pass cut-off frequencies. 要让 RTPC 值正确调节插件所在总线上的这些属性，请参照上述 [RTPC 与总线](soundengine_rtpc.html#soundengine_rtpc_buses) 章节中所述的情况。

If the plug-ins are used in Container objects or your project, they will always be played on a Game Object. 大部分情况下，在调用 [AK::SoundEngine::SetRTPCValue()](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26) 方法时都要使用有效的 AkGameObjectID 值。However, it is still possible to only set a global default value for all Game Objects that don't have one specified directly by using AK\_INVALID\_GAME\_OBJECT.

|  |  |
| --- | --- |
|  | **备注:** 注意设置全局 RTPC 值与根据游戏对象设置 RTPC 值之间的差异，这点非常重要。If a Wwise object playing sounds, such as a switch container, is affected by RTPCs, it is important to make calls to the [AK::SoundEngine::SetRTPCValue()](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26) method with a valid AkGameObjectID value. On playback, if no such game object-specific value has been set, the sound engine will look for a global RTPC value that will have been set by calling [AK::SoundEngine::SetRTPCValue()](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26) with the AK\_INVALID\_GAME\_OBJECT parameter or with no specified game object. If this global value does not exist, the sound engine will use the Game Parameter's default value as specified in the Wwise authoring application. |

|  |  |
| --- | --- |
|  | **注意:** 注意，同一 RTPC 可能会同时用在声音、总线和效果器上，This may result in unexpected behavior, and we recommend you use different RTPCs for game objects, buses, and effects. For example, in a racing game, you might have set a default RPM value on the engines of ten cars. At the same time, a low pass filter on the bus playing the cars' engine sounds could be applied. If you follow this recommendation, it will be easier for you to identify the source of the low pass filter effect. |

有关集成RTPC的示例，请参阅 [RTPC 示例](quickstart_sample_integration_rtpc.html#soundengine_integration_rtpc) 。

[AK::SoundEngine::SetRTPCValue](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26)

AKSOUNDENGINE\_API AKRESULT SetRTPCValue(AkRtpcID in\_rtpcID, AkRtpcValue in\_value, AkGameObjectID in\_gameObjectID=AK\_INVALID\_GAME\_OBJECT, AkTimeMs in\_uValueChangeDuration=0, AkCurveInterpolation in\_eFadeCurve=AkCurveInterpolation\_Linear, bool in\_bBypassInternalValueInterpolation=false)

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AK\_INVALID\_GAME\_OBJECT](_ak_constants_8h_a82290a98a9cf7901722a69a590aeee34.html#a82290a98a9cf7901722a69a590aeee34)

static const AkGameObjectID AK\_INVALID\_GAME\_OBJECT

Invalid game object (may also mean all game objects)

**Definition:** [AkConstants.h:33](_ak_constants_8h_source.html#l00033)

[AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140)

AkReal32 AkRtpcValue

Real time parameter control value

**Definition:** [AkTypedefs.h:53](_ak_typedefs_8h_source.html#l00053)

[AkRtpcID](_ak_typedefs_8h_a77a3b6fec7d9181ef8e5bae2b37b80d0.html#a77a3b6fec7d9181ef8e5bae2b37b80d0)

AkUInt32 AkRtpcID

Real time parameter control ID

**Definition:** [AkTypedefs.h:52](_ak_typedefs_8h_source.html#l00052)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)