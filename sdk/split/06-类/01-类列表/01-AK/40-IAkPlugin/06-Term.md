# Term

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPlugin](class_a_k_1_1_i_ak_plugin.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetPluginInfo](class_a_k_1_1_i_ak_plugin_a5c4cdef6822950045b66834528bd1b55.html#a5c4cdef6822950045b66834528bd1b55) | | [RelocateMedia](class_a_k_1_1_i_ak_plugin_aa63887024a5f2e2ff8f1fb98e864e129.html#aa63887024a5f2e2ff8f1fb98e864e129) | | [Reset](class_a_k_1_1_i_ak_plugin_a08c841c8b811acb993acd0353bd9db75.html#a08c841c8b811acb993acd0353bd9db75) | | [SupportMediaRelocation](class_a_k_1_1_i_ak_plugin_a0f93c3ed9f133524d8c2b36a00876152.html#a0f93c3ed9f133524d8c2b36a00876152) | | [Term](class_a_k_1_1_i_ak_plugin_a29db8d2afc4fe2571c2c75deb00a359d.html#a29db8d2afc4fe2571c2c75deb00a359d) | | [~IAkPlugin](class_a_k_1_1_i_ak_plugin_a49ab8f8ae589b2b53d6977afbf7703e4.html#a49ab8f8ae589b2b53d6977afbf7703e4) | | [◆](#a29db8d2afc4fe2571c2c75deb00a359d)Term() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkPlugin::Term | ( | [IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \* | *in\_pAllocator* | ) |  | | pure virtual |  Release the resources upon termination of the plug-in.  返回  AK\_Success if successful, AK\_Fail otherwise  |  |  | | --- | --- | |  | **备注:** The self-destruction of the plug-in must be done using [AK\_PLUGIN\_DELETE()](_i_ak_plugin_mem_alloc_8h_ac6fa6544d3120811e155136866fc24aa.html#ac6fa6544d3120811e155136866fc24aa) macro. |  参见  - [AK::IAkPlugin::Term()](soundengine_plugins.html#iakeffect_term)  参数  |  |  | | --- | --- | | in\_pAllocator | Interface to memory allocator to be used by the plug-in | |