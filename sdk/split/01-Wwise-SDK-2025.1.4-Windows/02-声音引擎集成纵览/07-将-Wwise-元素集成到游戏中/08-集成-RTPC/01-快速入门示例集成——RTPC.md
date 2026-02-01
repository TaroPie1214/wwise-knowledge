# 快速入门示例集成——RTPC

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

快速入门示例集成——RTPC

# RTPC 示例

RTPC 使声音引擎可以通过评估曲线来计算属性值，曲线由音频设计师定义，其 X 值对应于游戏中的参数。例如，以下代码设置“RPM”游戏参数的值：

// 使用参数名称设置游戏参数值。我们可以使用它的

// ID， AK::GAME\_PARAMETERS::RPM (from Wwise\_IDs.h)

[AK::SoundEngine::SetRTPCValue](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26)( L"RPM", ([AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140))nRPM );

在示例程序中，您可以通过两种方式试验 RTPC：

- 在 Car 部分，选择`Play_Engine` 事件，单击 Post，然后移动 RPM 滑块。此操作将更改 RPM 游戏参数的值，声音引擎用此参数来更改音量和音高属性
- 在 Human 部分，选择/取消选择“Enable Effect”复选框，然后单击 Talk. 当选中此复选框时，“Enable\_Effect”游戏参数设为 100。 当取消选择它时，游戏参数设为 0。语音总线使用此游戏参数来设置/清空“Bypass Effect”属性。

请参阅 [集成详情——RTPC](soundengine_rtpc.html) 了解更多详情。

|  |  |
| --- | --- |
|  | **备注:** 此例程摘自 [示例](samplecode.html) 一节中的“声音引擎集成工程示例”部分。请参阅 [Integration Demo 示例](soundengine_integration_samplecode.html) 了解更多信息。 |

[AK::SoundEngine::SetRTPCValue](namespace_a_k_1_1_sound_engine_ab0e4ddefe5ea550b2f356edaa5a49a26.html#ab0e4ddefe5ea550b2f356edaa5a49a26)

AKSOUNDENGINE\_API AKRESULT SetRTPCValue(AkRtpcID in\_rtpcID, AkRtpcValue in\_value, AkGameObjectID in\_gameObjectID=AK\_INVALID\_GAME\_OBJECT, AkTimeMs in\_uValueChangeDuration=0, AkCurveInterpolation in\_eFadeCurve=AkCurveInterpolation\_Linear, bool in\_bBypassInternalValueInterpolation=false)

[AkRtpcValue](_ak_typedefs_8h_a86459d5c3b5e6055cc885b833661f140.html#a86459d5c3b5e6055cc885b833661f140)

AkReal32 AkRtpcValue

Real time parameter control value

**Definition:** [AkTypedefs.h:53](_ak_typedefs_8h_source.html#l00053)