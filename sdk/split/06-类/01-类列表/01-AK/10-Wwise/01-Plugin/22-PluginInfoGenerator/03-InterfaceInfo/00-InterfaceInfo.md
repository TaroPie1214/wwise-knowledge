# InterfaceInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)
- [InterfaceInfo](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[静态 Public 成员函数](#pub-static-methods)

AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType > 模板结构体 参考

Compile-time dictionary about a particular interface type.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html#details)

`#include <PluginInfoGenerator.h>`

|  |  |
| --- | --- |
| 类 | |
| struct | [ToInterfaceClassImpl](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html) |
|  | Casts the plug-in class to the requested interface class. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html#details) |
|  | |
| struct | [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html) |
|  | Compile-time container of version numbers. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | { [k\_latestInterfaceVersion](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a239861723975d109cd1c64af548459ce.html#a239861723975d109cd1c64af548459cea89cd3b4a67985a130f534fca5e02aee8) = LatestInterfaceVersion<in\_interfaceType>::k\_interfaceVersion } |
|  | |
| enum | : bool |
|  | |
| enum | { [k\_interfaceVersion](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_abd0bf628dc46fd24558f7bcd53c149d0.html#abd0bf628dc46fd24558f7bcd53c149d0ad1644ce2be4baf13d43d4662d9f4fed5) = GetInterfaceVersion() } |
|  | |
| using | [UsedInterfaceVersions](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a244040ab9417b3c48f51ca6a8c5fb41b.html#a244040ab9417b3c48f51ca6a8c5fb41b) = decltype([GetUsedInterfaceVersions](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a8e2122aaece25b9eaea8f0afd4622ba9.html#a8e2122aaece25b9eaea8f0afd4622ba9)()) |
|  | Pair type containing a [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html "Compile-time container of version numbers.") of the requested versions and a [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html "Compile-time container of version numbers.") of the provided versions of the interface. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a244040ab9417b3c48f51ca6a8c5fb41b.html#a244040ab9417b3c48f51ca6a8c5fb41b) |
|  | |
| using | [RequestedInterfaceVersions](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a9ae888dd25d9f743693320af0e98ea39.html#a9ae888dd25d9f743693320af0e98ea39) = typename UsedInterfaceVersions::first\_type |
|  | [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html "Compile-time container of version numbers.") containing the requested versions of the interface by the plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a9ae888dd25d9f743693320af0e98ea39.html#a9ae888dd25d9f743693320af0e98ea39) |
|  | |
| using | [ProvidedInterfaceVersions](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a64b65097e14c9da8d5b948a4f63c51d6.html#a64b65097e14c9da8d5b948a4f63c51d6) = typename UsedInterfaceVersions::second\_type |
|  | [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html "Compile-time container of version numbers.") containing the provided versions of the interface by the plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a64b65097e14c9da8d5b948a4f63c51d6.html#a64b65097e14c9da8d5b948a4f63c51d6) |
|  | |
| using | [InterfaceClass](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_acdbef4d83b4072eaa4acc434070aa062.html#acdbef4d83b4072eaa4acc434070aa062) = typename [KnownInterfaceClass](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html)< in\_interfaceType, [k\_interfaceVersion](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_abd0bf628dc46fd24558f7bcd53c149d0.html#abd0bf628dc46fd24558f7bcd53c149d0ad1644ce2be4baf13d43d4662d9f4fed5) >::Type |
|  | Interface class of the versioned interface type. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_acdbef4d83b4072eaa4acc434070aa062.html#acdbef4d83b4072eaa4acc434070aa062) |
|  | |
| using | [ToInterfaceClass](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a26d150cef6dc6ef026919890aed3fbb0.html#a26d150cef6dc6ef026919890aed3fbb0) = [ToInterfaceClassImpl](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html)< k\_has > |
|  | Casts the plug-in class to the requested interface class. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a26d150cef6dc6ef026919890aed3fbb0.html#a26d150cef6dc6ef026919890aed3fbb0) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| template<uint32\_t in\_interfaceVersion = k\_latestInterfaceVersion, uint32\_t... in\_requestedVersions, uint32\_t... in\_providedVersions> | |
| static constexpr auto | [GetUsedInterfaceVersions](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a8e2122aaece25b9eaea8f0afd4622ba9.html#a8e2122aaece25b9eaea8f0afd4622ba9) ([VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html)< in\_requestedVersions... >={}, [VersionPack](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html)< in\_providedVersions... >={}) |
|  | Recursively accumulate each version of the interface requested or provided by the plug-in (there should be one or none). [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a8e2122aaece25b9eaea8f0afd4622ba9.html#a8e2122aaece25b9eaea8f0afd4622ba9) |
|  | |
| static constexpr uint32\_t | [GetInterfaceVersion](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a0be33c153ec912aeaa11a2a385e7b4d9.html#a0be33c153ec912aeaa11a2a385e7b4d9) () |
|  | Extract the version of the interface used by the plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_a0be33c153ec912aeaa11a2a385e7b4d9.html#a0be33c153ec912aeaa11a2a385e7b4d9) |
|  | |
| static [BaseInterface](namespace_a_k_1_1_wwise_1_1_plugin_af12e29db650cd0c58e9880a64ff93b18.html#af12e29db650cd0c58e9880a64ff93b18) \* | [GetPlaceholderPointer](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_aeda97cbd26a5f9dcf6b1c94b8baaee57.html#aeda97cbd26a5f9dcf6b1c94b8baaee57) () |
|  | Get a Placeholder Pointer object. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_aeda97cbd26a5f9dcf6b1c94b8baaee57.html#aeda97cbd26a5f9dcf6b1c94b8baaee57) |
|  | |

## 详细描述

### template<typename PluginT> template<InterfaceType in\_interfaceType> struct AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >

Compile-time dictionary about a particular interface type.

模板参数
:   |  |  |
    | --- | --- |
    | in\_interfaceType | The interface ID with the information to request. |

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [335](_plugin_info_generator_8h_source.html#l00335) 行定义.