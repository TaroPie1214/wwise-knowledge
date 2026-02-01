# GetArray

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [LinkFrontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ForEach](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a8ad177ae489502dd73244cd09b511459.html#a8ad177ae489502dd73244cd09b511459) | | [GetArray](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_ab086d0ff5868bf672988ba5c4058fb24.html#ab086d0ff5868bf672988ba5c4058fb24) | | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a050f59682dfcaea2cef7dd6a9d2f59a3.html#a050f59682dfcaea2cef7dd6a9d2f59a3) | | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a6dca6f5baad734afa720a7343f9368fc.html#a6dca6f5baad734afa720a7343f9368fc) | | [◆](#ab086d0ff5868bf672988ba5c4058fb24)GetArray() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [ak\_wwise\_plugin\_frontend\_instance](structak__wwise__plugin__frontend__instance.html)\*\* AK.Wwise::Plugin::V1::LinkFrontend::GetArray | ( | int \* | *out\_count* | ) | const | | inline |  Retrieves an array of the plug-in's frontend instances.   |  |  | | --- | --- | |  | **备注:** The returned array is a temporary TLS pointer that is meant to be retrieved and processed immediately to execute commands. You should not store this data. |   参数  |  |  |  | | --- | --- | --- | | [out] | out\_count | How many frontend instances are in the array. |  返回  Temporary pointer to the array of frontend instances.  在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [230](_plugin_links_8h_source.html#l00230) 行定义.  引用了 [AK.Wwise::Plugin::CBaseInterfaceGlue< CLinkFrontend >::g\_cinterface](_plugin_info_generator_8h_source.html#l00089) , 以及 [ak\_wwise\_plugin\_link\_frontend\_v1::GetArray](_plugin_links_8h_source.html#l00105).  被这些函数引用 [AK.Wwise::Plugin::V1::LinkFrontend::ForEach()](_plugin_links_8h_source.html#l00248). |