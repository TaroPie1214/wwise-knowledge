# GetLatest

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)
- [InterfaceInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html)
- [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetLatest](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack_affd94260b3874205287fe65f888db24f.html#affd94260b3874205287fe65f888db24f) | | [◆](#affd94260b3874205287fe65f888db24f)GetLatest() template<typename PluginT >  template<InterfaceType in\_interfaceType>  template<uint32\_t... in\_versions>   |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | static constexpr uint32\_t [AK.Wwise::Plugin::PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)< PluginT >::[InterfaceInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html)< in\_interfaceType >::[VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html)< in\_versions >::GetLatest | ( |  | ) |  | | inlinestaticconstexpr |  Get the latest version stored in the container. Assumes the container is sorted in ascending order.  返回  uint32\_t The latest version of the pack.  在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [358](_plugin_info_generator_8h_source.html#l00358) 行定义. |