# Term

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginParam](class_a_k_1_1_i_ak_plugin_param.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ALL\_PLUGIN\_DATA\_ID](class_a_k_1_1_i_ak_plugin_param_a7d4422a73ca832f64edc0465e59be771.html#a7d4422a73ca832f64edc0465e59be771) | | [Clone](class_a_k_1_1_i_ak_plugin_param_a606e850fa44ca597e0f1b9c6ad5f32cb.html#a606e850fa44ca597e0f1b9c6ad5f32cb) | | [Init](class_a_k_1_1_i_ak_plugin_param_ab432d055afc355a17121ac2afdcd5639.html#ab432d055afc355a17121ac2afdcd5639) | | [SetParam](class_a_k_1_1_i_ak_plugin_param_ad47732326b85527316287e923d37a3e1.html#ad47732326b85527316287e923d37a3e1) | | [SetParamsBlock](class_a_k_1_1_i_ak_plugin_param_ae186f2f0aa56fe0e52ab1c2218df2c7c.html#ae186f2f0aa56fe0e52ab1c2218df2c7c) | | [Term](class_a_k_1_1_i_ak_plugin_param_ad558bb7f45851dc57b1bbf34ef74cd48.html#ad558bb7f45851dc57b1bbf34ef74cd48) | | [~IAkPluginParam](class_a_k_1_1_i_ak_plugin_param_a53cabae3b0052b34f68c973344724e33.html#a53cabae3b0052b34f68c973344724e33) | | [◆](#ad558bb7f45851dc57b1bbf34ef74cd48)Term() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkPluginParam::Term | ( | [IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \* | *in\_pAllocator* | ) |  | | pure virtual |  Called by the sound engine when a parameter node is terminated.   |  |  | | --- | --- | |  | **备注:** The self-destruction of the parameter node must be done using the [AK\_PLUGIN\_DELETE()](_i_ak_plugin_mem_alloc_8h_ac6fa6544d3120811e155136866fc24aa.html#ac6fa6544d3120811e155136866fc24aa) macro. |   返回  AK\_Success if successful, AK\_Fail otherwise  参见  - [AK::IAkPluginParam::Term()](soundengine_plugins.html#iakeffectparam_term)  参数  |  |  | | --- | --- | | in\_pAllocator | Interface to memory allocator to be used | |