# GetMixerCtx

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [CreateOutputObjects](class_a_k_1_1_i_ak_effect_plugin_context_a96f65eb02b520f2ca5af497e645971a0.html#a96f65eb02b520f2ca5af497e645971a0) | | [GetMixerCtx](class_a_k_1_1_i_ak_effect_plugin_context_a003265e118a7fac508d5a47a94f95f20.html#a003265e118a7fac508d5a47a94f95f20) | | [GetOutputObjects](class_a_k_1_1_i_ak_effect_plugin_context_ad0b9c549569b25dea349d2a352f02e58.html#ad0b9c549569b25dea349d2a352f02e58) | | [GetSidechainMixChannelConfig](class_a_k_1_1_i_ak_effect_plugin_context_ae9aed89a6cf7530e7cc3a011eb683f45.html#ae9aed89a6cf7530e7cc3a011eb683f45) | | [GetVoiceInfo](class_a_k_1_1_i_ak_effect_plugin_context_a65bf3ee948fceba3225fe2a3f501cab5.html#a65bf3ee948fceba3225fe2a3f501cab5) | | [IsSendModeEffect](class_a_k_1_1_i_ak_effect_plugin_context_ab8ec44868a3781a40320336c2eedf82e.html#ab8ec44868a3781a40320336c2eedf82e) | | [ReceiveFromSidechainMix](class_a_k_1_1_i_ak_effect_plugin_context_ae9c831158402c426f22a3a59e2938dd3.html#ae9c831158402c426f22a3a59e2938dd3) | | [SendToSidechainMix](class_a_k_1_1_i_ak_effect_plugin_context_a3143735cd105b3b7673ee11179756ed7.html#a3143735cd105b3b7673ee11179756ed7) | | [~IAkEffectPluginContext](class_a_k_1_1_i_ak_effect_plugin_context_a993d03fa58554d45b1eaa0c31f467248.html#a993d03fa58554d45b1eaa0c31f467248) | | [◆](#a003265e118a7fac508d5a47a94f95f20)GetMixerCtx() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual [IAkMixerPluginContext](class_a_k_1_1_i_ak_mixer_plugin_context.html)\* AK::IAkEffectPluginContext::GetMixerCtx | ( |  | ) |  | | pure virtual |  Obtain the interface to access services available on busses.  返回  The interface to mixing context if the plugin is instantiated on a bus. NULL if it is instantiated on a voice. |