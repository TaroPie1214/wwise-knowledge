# RemoveInput

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkMixerInputMap](class_ak_mixer_input_map.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AddInput](class_ak_mixer_input_map_aa8e0ad3d5ecd8a24cc4c5011b4ffb1c9.html#aa8e0ad3d5ecd8a24cc4c5011b4ffb1c9) | | [BaseClass](class_ak_mixer_input_map_a8e79afd57e0ac98a70d00ca3d874045b.html#a8e79afd57e0ac98a70d00ca3d874045b) | | [EraseSwap](class_ak_mixer_input_map_ad839b271ff3a2213765456cefd569e5c.html#ad839b271ff3a2213765456cefd569e5c) | | [Exists](class_ak_mixer_input_map_ad9acf848722f5fb49c1184fc89aff4a2.html#ad9acf848722f5fb49c1184fc89aff4a2) | | [FindEx](class_ak_mixer_input_map_af9cf13aca17ab1e543319727f4134f8b.html#af9cf13aca17ab1e543319727f4134f8b) | | [RemoveAll](class_ak_mixer_input_map_af37914978f7cff8b5e3b398954b993aa.html#af37914978f7cff8b5e3b398954b993aa) | | [RemoveInput](class_ak_mixer_input_map_a0461595bdde4fe72fe828b94e741043a.html#a0461595bdde4fe72fe828b94e741043a) | | [Term](class_ak_mixer_input_map_acb435c00ea3ac90fe96f4367bdfd5e7e.html#acb435c00ea3ac90fe96f4367bdfd5e7e) | | [◆](#a0461595bdde4fe72fe828b94e741043a)RemoveInput() template<class KEY , class USER\_DATA >   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | bool [AkMixerInputMap](class_ak_mixer_input_map.html)< KEY, USER\_DATA >::RemoveInput | ( | KEY | *in\_key* | ) |  | | inline |  Removes an input and destroys its associated user data.  在文件 [AkMixerInputMap.h](_ak_mixer_input_map_8h_source.html) 第 [109](_ak_mixer_input_map_8h_source.html#l00109) 行定义.  引用了 [AK\_PLUGIN\_DELETE()](_i_ak_plugin_mem_alloc_8h_source.html#l00178), [AKASSERT](_ak_assert_8h_source.html#l00069) , 以及 [AkPluginArrayAllocator::GetAllocator()](_i_ak_plugin_mem_alloc_8h_source.html#l00212). |