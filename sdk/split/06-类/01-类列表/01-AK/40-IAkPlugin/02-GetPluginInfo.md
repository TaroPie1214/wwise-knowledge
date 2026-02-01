# GetPluginInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPlugin](class_a_k_1_1_i_ak_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetPluginInfo](class_a_k_1_1_i_ak_plugin_a5c4cdef6822950045b66834528bd1b55.html#a5c4cdef6822950045b66834528bd1b55) | | [RelocateMedia](class_a_k_1_1_i_ak_plugin_aa63887024a5f2e2ff8f1fb98e864e129.html#aa63887024a5f2e2ff8f1fb98e864e129) | | [Reset](class_a_k_1_1_i_ak_plugin_a08c841c8b811acb993acd0353bd9db75.html#a08c841c8b811acb993acd0353bd9db75) | | [SupportMediaRelocation](class_a_k_1_1_i_ak_plugin_a0f93c3ed9f133524d8c2b36a00876152.html#a0f93c3ed9f133524d8c2b36a00876152) | | [Term](class_a_k_1_1_i_ak_plugin_a29db8d2afc4fe2571c2c75deb00a359d.html#a29db8d2afc4fe2571c2c75deb00a359d) | | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) | | [◆](#a5c4cdef6822950045b66834528bd1b55)GetPluginInfo() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkPlugin::GetPluginInfo | ( | [AkPluginInfo](struct_ak_plugin_info.html) & | *out\_rPluginInfo* | ) |  | | pure virtual |  Plug-in information query mechanism used when the sound engine requires information about the plug-in to determine its behavior.  警告  This function can be called before Init. Implementation of this function should not rely on internal state initialized in Init.  返回  AK\_Success if successful.  参见  - [AK::IAkPlugin::GetPluginInfo()](soundengine_plugins.html#iakeffect_geteffectinfo)  参数  |  |  | | --- | --- | | out\_rPluginInfo | Reference to the plug-in information structure to be retrieved | |