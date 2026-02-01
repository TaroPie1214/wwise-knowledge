# ForEach

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [LinkFrontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ForEach](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a8ad177ae489502dd73244cd09b511459.html#a8ad177ae489502dd73244cd09b511459) | | [GetArray](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_ab086d0ff5868bf672988ba5c4058fb24.html#ab086d0ff5868bf672988ba5c4058fb24) | | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a050f59682dfcaea2cef7dd6a9d2f59a3.html#a050f59682dfcaea2cef7dd6a9d2f59a3) | | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend_a6dca6f5baad734afa720a7343f9368fc.html#a6dca6f5baad734afa720a7343f9368fc) | | [◆](#a8ad177ae489502dd73244cd09b511459)ForEach() template<typename Frontend = ak\_wwise\_plugin\_frontend\_instance, typename Functor >   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | void AK.Wwise::Plugin::V1::LinkFrontend::ForEach | ( | Functor | *in\_operation* | ) | const | | inline |  Applies a function on each plug-in's frontend instances.   |  |  | | --- | --- | |  | **备注:** The frontend instances passed to the function are temporary TLS pointers that are meant to be retrieved and processed immediately to execute commands. You should not store this data. |   模板参数  |  |  | | --- | --- | | [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") | Expected type of the frontend instances (optional). If no explicit type is provided, the caller needs to manually perform the cast to the expected frontend instance type. If an explicit type is provided, the frontend instances will automatically be casted to the provided type and then forwarded to in\_operation if the cast was successful. |  参数  |  |  |  | | --- | --- | --- | | [in] | in\_operation | Function, functor or lambda taking a pointer of [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") as parameter. |  在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [248](_plugin_links_8h_source.html#l00248) 行定义.  引用了 [AK.Wwise::Plugin::V1::LinkFrontend::GetArray()](_plugin_links_8h_source.html#l00230). |