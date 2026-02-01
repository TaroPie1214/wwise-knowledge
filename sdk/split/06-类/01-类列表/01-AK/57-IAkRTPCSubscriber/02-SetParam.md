# SetParam

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkRTPCSubscriber](class_a_k_1_1_i_ak_r_t_p_c_subscriber.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [SetParam](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a93a2b097a6e34482c7381f388e500ff0.html#a93a2b097a6e34482c7381f388e500ff0) | | [~IAkRTPCSubscriber](class_a_k_1_1_i_ak_r_t_p_c_subscriber_a4c061df60a4e69355ee377e9643e4a12.html#a4c061df60a4e69355ee377e9643e4a12) | | [◆](#a93a2b097a6e34482c7381f388e500ff0)SetParam() |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkRTPCSubscriber::SetParam | ( | [AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) | *in\_paramID*, | |  |  | const void \* | *in\_pParam*, | |  |  | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | *in\_uParamSize* | |  | ) |  |  | | pure virtual |  This function will be called to notify the subscriber every time a selected value is entered or modified  返回  AK\_Success if successful, AK\_Fail otherwise  参数  |  |  | | --- | --- | | in\_paramID | Plug-in parameter ID | | in\_pParam | Parameter value pointer | | in\_uParamSize | Parameter size |  在 [AK::IAkPluginParam](class_a_k_1_1_i_ak_plugin_param_ad47732326b85527316287e923d37a3e1.html#ad47732326b85527316287e923d37a3e1) 内被实现. |