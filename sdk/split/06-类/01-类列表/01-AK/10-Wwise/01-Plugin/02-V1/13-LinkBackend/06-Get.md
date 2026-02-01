# Get

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [LinkBackend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [As](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a20ab757948a2d67eaea35ec525a5a3dd.html#a20ab757948a2d67eaea35ec525a5a3dd) | | [Get](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a60fcc8ce01bfeccf062a985258c95c78.html#a60fcc8ce01bfeccf062a985258c95c78) | | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_a3ade782d64961bbae9f35532fd29d601.html#a3ade782d64961bbae9f35532fd29d601) | | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend_ac7654e4696f2c587f1e6ddf792beff54.html#ac7654e4696f2c587f1e6ddf792beff54) | | [◆](#a60fcc8ce01bfeccf062a985258c95c78)Get() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html)\* AK.Wwise::Plugin::V1::LinkBackend::Get | ( |  | ) | const | | inline |  Retrieves a link to the plug-in's backend instance.   |  |  | | --- | --- | |  | **备注:** The returned pointer might be modified in the frontend lifetime. For example, a plug-in that would undo and redo a plug-in creation might return a different value. As such, you should not store the backend pointer in a class member, but query it at every operation. |   返回  Base pointer of the backend instance.  在文件 [PluginLinks.h](_plugin_links_8h_source.html) 第 [171](_plugin_links_8h_source.html#l00171) 行定义.  引用了 [AK.Wwise::Plugin::CBaseInterfaceGlue< CLinkBackend >::g\_cinterface](_plugin_info_generator_8h_source.html#l00089) , 以及 [ak\_wwise\_plugin\_link\_backend\_v1::Get](_plugin_links_8h_source.html#l00068).  被这些函数引用 [AK.Wwise::Plugin::V1::LinkBackend::As()](_plugin_links_8h_source.html#l00187). |