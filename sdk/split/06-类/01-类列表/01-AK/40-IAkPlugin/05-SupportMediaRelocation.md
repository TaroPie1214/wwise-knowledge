# SupportMediaRelocation

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPlugin](class_a_k_1_1_i_ak_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetPluginInfo](class_a_k_1_1_i_ak_plugin_a5c4cdef6822950045b66834528bd1b55.html#a5c4cdef6822950045b66834528bd1b55) | | [RelocateMedia](class_a_k_1_1_i_ak_plugin_aa63887024a5f2e2ff8f1fb98e864e129.html#aa63887024a5f2e2ff8f1fb98e864e129) | | [Reset](class_a_k_1_1_i_ak_plugin_a08c841c8b811acb993acd0353bd9db75.html#a08c841c8b811acb993acd0353bd9db75) | | [SupportMediaRelocation](class_a_k_1_1_i_ak_plugin_a0f93c3ed9f133524d8c2b36a00876152.html#a0f93c3ed9f133524d8c2b36a00876152) | | [Term](class_a_k_1_1_i_ak_plugin_a29db8d2afc4fe2571c2c75deb00a359d.html#a29db8d2afc4fe2571c2c75deb00a359d) | | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) | | [◆](#a0f93c3ed9f133524d8c2b36a00876152)SupportMediaRelocation() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual bool AK::IAkPlugin::SupportMediaRelocation | ( |  | ) | const | | inlinevirtual |  Some plug-ins are accessing Media from the [Wwise](namespace_a_k_1_1_wwise.html) sound bank system. If the [IAkPlugin](class_a_k_1_1_i_ak_plugin.html) object is not using media, this function will not be used and should simply return false. If the [IAkPlugin](class_a_k_1_1_i_ak_plugin.html) object is using media, the RelocateMedia feature can be optionally implemented. To implement correctly the feature, the plugin must be able to "Hot swap" from a memory location to another one in a single blocking call ([AK::IAkPlugin::RelocateMedia](class_a_k_1_1_i_ak_plugin_aa63887024a5f2e2ff8f1fb98e864e129.html#aa63887024a5f2e2ff8f1fb98e864e129))  参见  - [AK::IAkPlugin::RelocateMedia](class_a_k_1_1_i_ak_plugin_aa63887024a5f2e2ff8f1fb98e864e129.html#aa63887024a5f2e2ff8f1fb98e864e129)  在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [819](_i_ak_plugin_8h_source.html#l00819) 行定义. |