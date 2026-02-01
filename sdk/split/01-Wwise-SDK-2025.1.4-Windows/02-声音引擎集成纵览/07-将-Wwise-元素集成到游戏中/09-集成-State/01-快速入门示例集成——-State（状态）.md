# 快速入门示例集成—— State（状态）

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

快速入门示例集成—— State（状态）

# State 示例

以下代码显示您可以如何设置给定状态组（State Group）的当前状态（State）：

[AK::SoundEngine::SetState](namespace_a_k_1_1_sound_engine_a68dc9be195962c671b82fbb354b68cc5.html#a68dc9be195962c671b82fbb354b68cc5)( AK::STATES::PLAYERHEALTH::GROUP, AK::STATES::PLAYERHEALTH::STATE::NORMAL );

除 ID [外，AK::SoundEngine::SetState()](namespace_a_k_1_1_sound_engine_a68dc9be195962c671b82fbb354b68cc5.html#a68dc9be195962c671b82fbb354b68cc5) 方法还接受字符串（Unicode 或 Ansi）。在这种情况下，您将指定音频设计师定义的 State Group 和 State 的名称：

[AK::SoundEngine::SetState](namespace_a_k_1_1_sound_engine_a68dc9be195962c671b82fbb354b68cc5.html#a68dc9be195962c671b82fbb354b68cc5)( L"PlayerHealth", L"Normal" );

在应用程序示例中，您可以通过使用对话框 General 板块中的相应下拉列表来更改`PlayerHealth` 状态组的当前状态。

请参阅 [集成详情—— State（状态）](soundengine_states.html) 了解更多信息。

|  |  |
| --- | --- |
|  | **备注:** 此例程摘自 [示例](samplecode.html) 一节中的“声音引擎集成工程示例”部分。请参阅 [Integration Demo 示例](soundengine_integration_samplecode.html) 了解更多信息。 |

[AK::SoundEngine::SetState](namespace_a_k_1_1_sound_engine_a68dc9be195962c671b82fbb354b68cc5.html#a68dc9be195962c671b82fbb354b68cc5)

AKSOUNDENGINE\_API AKRESULT SetState(AkStateGroupID in\_stateGroup, AkStateID in\_state)