# PluginInfoGenerator.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members)

PluginInfoGenerator.h 文件参考

Wwise Authoring Plug-ins - C++ class helper to automatically determine the plug-in interfaces used in a class.
[更多...](#details)

`#include "PluginContainer.h"`  
`#include <array>`  
`#include <memory>`

[浏览源代码.](_plugin_info_generator_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AK.Wwise::Plugin::PluginInfoTLS< bool >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s.html) |
|  | The interface information of the plug-in currently being instantiated. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_t_l_s.html#details) |
|  | |
| class | [AK.Wwise::Plugin::CBaseInterfaceGlue< CInterface >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): For each plug-in interface type, provides a single static instance used throughout this plug-in container. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html#details) |
|  | |
| class | [AK.Wwise::Plugin::CBaseInstanceGlue< CInterface, CInstance >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Associates an existing C Interface with a variable that can be used. Derives from the instance that uses it. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html#details) |
|  | |
| class | [AK.Wwise::Plugin::HostInterfaceGlue< CPPInstance, in\_baseInstance >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Base class for every C++ instance that retrieves a service from the [Wwise](namespace_a_k_1_1_wwise.html) Authoring host. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html#details) |
|  | |
| class | [AK.Wwise::Plugin::HostInterfaceGlue< CPPInstance, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_3_01_c_p_p_instance_00_01true_01_4.html) |
|  | |
| struct | [AK.Wwise::Plugin::KnownInterfaceClass< in\_interfaceType, in\_interfaceVersion >](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Compile-time dictionary of known interface-version. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< T >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Requests a host-provided service, and optionally receives a variable containing the default instance. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::LatestInterfaceVersion< in\_interfaceType >](struct_a_k_1_1_wwise_1_1_plugin_1_1_latest_interface_version.html) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Defines a compile-time dictionary with the latest version known to the SDK for each interface. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_latest_interface_version.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::KnownInterfaceClass< AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PLUGIN\_CONTAINER, 1 >](struct_a_k_1_1_wwise_1_1_plugin_1_1_known_interface_class_3_01_a_k___w_w_i_s_e___p_l_u_g_i_n___i2061849bd7ce9e600e94611bde4bbe05.html) |
|  | |
| struct | [AK.Wwise::Plugin::LatestInterfaceVersion< AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PLUGIN\_CONTAINER >](struct_a_k_1_1_wwise_1_1_plugin_1_1_latest_interface_version_3_01_a_k___w_w_i_s_e___p_l_u_g_i_n_1f919b2745dd48bfee90f50effc527af.html) |
|  | |
| struct | [AK.Wwise::Plugin::PluginInfoGenerator< PluginT >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html) |
|  | C++ PluginInfo Generator. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html) |
|  | Compile-time dictionary about a particular interface type. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::VersionPack< in\_versions >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html) |
|  | Compile-time container of version numbers. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_version_pack.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::InterfaceInfo< in\_interfaceType >::ToInterfaceClassImpl< bool >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html) |
|  | Casts the plug-in class to the requested interface class. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_interface_info_1_1_to_interface_class_impl.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::GenerateConstructor< in\_interfaceType >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor.html) |
|  | Generates the constructor for our particular type [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::PluginInfoGenerator< PluginT >::GenerateConstructorArray< in\_interfaceType >](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array.html) |
|  | Recursively generates the constructors and interface pointer updater for all the Interfaces. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator_1_1_generate_constructor_array.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
| namespace | [AK.Wwise](namespace_a_k_1_1_wwise.html) |
|  | |
|  | [AK::Wwise::Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISESDK\_VERSION\_NATIVE\_COMBINED](_plugin_info_generator_8h_a9afdbf293029fdc36aa8573104724f67.html#a9afdbf293029fdc36aa8573104724f67)   (([AK\_WWISESDK\_VERSION\_MAJOR](_ak_wwise_s_d_k_version_8h_aab262241e216d4409eb5f788ce3f2180.html#aab262241e216d4409eb5f788ce3f2180) << 19) | ([AK\_WWISESDK\_VERSION\_MINOR](_ak_wwise_s_d_k_version_8h_a2b4cb41fdb8eae65c81c8ea46830175c.html#a2b4cb41fdb8eae65c81c8ea46830175c) << 16) | [AK\_WWISESDK\_VERSION\_SUBMINOR](_ak_wwise_s_d_k_version_8h_a99b795691d5e8ba1f53b7e666fe38dca.html#a99b795691d5e8ba1f53b7e666fe38dca)) |
|  | The specific version for native plug-in interfaces. Must be identical down to the build number. [更多...](_plugin_info_generator_8h_a9afdbf293029fdc36aa8573104724f67.html#a9afdbf293029fdc36aa8573104724f67) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](_plugin_info_generator_8h_ab8bfc0e1cd12101281bb88707b676311.html#ab8bfc0e1cd12101281bb88707b676311)(in\_name) |
|  | PluginInfoGenerator: Defines a C++ known interface-version to Type dictionary entry. [更多...](_plugin_info_generator_8h_ab8bfc0e1cd12101281bb88707b676311.html#ab8bfc0e1cd12101281bb88707b676311) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_HOST\_INTERFACE](_plugin_info_generator_8h_ab59889d5959f61466b84345e66eb4adc.html#ab59889d5959f61466b84345e66eb4adc)(in\_name, in\_varname, ...) |
|  | PluginInfoGenerator: Creates a C++ host specialization for interface class specified in in\_name, and creates a variable instance named m\_ followed by in\_varname. [更多...](_plugin_info_generator_8h_ab59889d5959f61466b84345e66eb4adc.html#ab59889d5959f61466b84345e66eb4adc) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_HOST\_INTERFACE\_NO\_BASE\_INSTANCE](_plugin_info_generator_8h_a8b82643bd6e054d76692f6c6bc1d6786.html#a8b82643bd6e054d76692f6c6bc1d6786)(in\_name, in\_varname) |
|  | PluginInfoGenerator: Creates a C++ host specialization for interface class specified in in\_name. [更多...](_plugin_info_generator_8h_a8b82643bd6e054d76692f6c6bc1d6786.html#a8b82643bd6e054d76692f6c6bc1d6786) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](_plugin_info_generator_8h_a6b3974e2e8620254611b67cc82f3e156.html#a6b3974e2e8620254611b67cc82f3e156)(in\_interface) |
|  | PluginInfoGenerator: Creates a C++ link to the latest version known to the SDK for each interface. [更多...](_plugin_info_generator_8h_a6b3974e2e8620254611b67cc82f3e156.html#a6b3974e2e8620254611b67cc82f3e156) |
|  | |
| #define | [AK\_PLUGIN\_USERGENERATEDPLUGININFO\_NAMESPACE\_NAME](_plugin_info_generator_8h_a99181be399b7be43d2c22a7b61992f44.html#a99181be399b7be43d2c22a7b61992f44)   AK\_PLUGIN\_USERGENERATEDPLUGININFO\_NAMESPACE\_NAME1(UserGeneratedPluginInfo, \_\_COUNTER\_\_) |
|  | Creates an unique PluginInfo instance for the plug-in registration [更多...](_plugin_info_generator_8h_a99181be399b7be43d2c22a7b61992f44.html#a99181be399b7be43d2c22a7b61992f44) |
|  | |
| #define | [AK\_DECLARE\_PLUGIN\_CONTAINER](_plugin_info_generator_8h_a0f672a0fccb6e6d06ec89d31250007d7.html#a0f672a0fccb6e6d06ec89d31250007d7)(ContainerName)    extern "C" \_\_declspec(dllexport) [AK::Wwise::Plugin::PluginContainer](namespace_a_k_1_1_wwise_1_1_plugin_afa19c1aec7e87e47a7b3547a072713cc.html#afa19c1aec7e87e47a7b3547a072713cc)\* GetPluginContainer ## ContainerName() |
|  | (C++) Declares the plug-in container. [更多...](_plugin_info_generator_8h_a0f672a0fccb6e6d06ec89d31250007d7.html#a0f672a0fccb6e6d06ec89d31250007d7) |
|  | |
| #define | [AK\_DEFINE\_PLUGIN\_CONTAINER](_plugin_info_generator_8h_abfa289aa9dd9fd63a3ad3b152ac828af.html#abfa289aa9dd9fd63a3ad3b152ac828af)(ContainerName) |
|  | (C++) Defines the unique plug-in container. [更多...](_plugin_info_generator_8h_abfa289aa9dd9fd63a3ad3b152ac828af.html#abfa289aa9dd9fd63a3ad3b152ac828af) |
|  | |
| #define | [AK\_EXPORT\_PLUGIN\_CONTAINER](_plugin_info_generator_8h_ab198136f861ed921af8857efe36b7007.html#ab198136f861ed921af8857efe36b7007)(ContainerName) |
|  | (C++) Exports the plug-in container for a shared library. [更多...](_plugin_info_generator_8h_ab198136f861ed921af8857efe36b7007.html#ab198136f861ed921af8857efe36b7007) |
|  | |
| #define | [AK\_ADD\_PLUGIN\_CLASS\_TO\_CONTAINER](_plugin_info_generator_8h_ae72bc9efe38504b8f47686c01f5882f8.html#ae72bc9efe38504b8f47686c01f5882f8)(ContainerName, WwiseClassName, AudioEngineRegisteredName) |
|  | (C++) Adds a Wwise Authoring plug-in and a Sound Engine plug-in to a plug-in container. [更多...](_plugin_info_generator_8h_ae72bc9efe38504b8f47686c01f5882f8.html#ae72bc9efe38504b8f47686c01f5882f8) |
|  | |
| #define | [AK\_ADD\_PLUGIN\_CLASSID\_TO\_CONTAINER](_plugin_info_generator_8h_a38d201b97ec257331b3b4e23f15f20d5.html#a38d201b97ec257331b3b4e23f15f20d5)(ContainerName, WwiseClassName, CompanyID, PluginID, Type) |
|  | (C++) Adds a plug-in to a plug-in container. [更多...](_plugin_info_generator_8h_a38d201b97ec257331b3b4e23f15f20d5.html#a38d201b97ec257331b3b4e23f15f20d5) |
|  | |
| #define | [AK\_AUDIOPLUGIN\_USERGENERATEDPLUGININFO\_NAMESPACE\_NAME](_plugin_info_generator_8h_a891f58b2e7325d37a41c2d6cd7bc1fbb.html#a891f58b2e7325d37a41c2d6cd7bc1fbb)   [AK\_PLUGIN\_USERGENERATEDPLUGININFO\_NAMESPACE\_NAME](_plugin_info_generator_8h_a99181be399b7be43d2c22a7b61992f44.html#a99181be399b7be43d2c22a7b61992f44) |
|  | |
| #define | [DECLARE\_AUDIOPLUGIN\_CONTAINER](_plugin_info_generator_8h_a7173d5b0d21ec2df1758d6208f721206.html#a7173d5b0d21ec2df1758d6208f721206)(x)   [AK\_DECLARE\_PLUGIN\_CONTAINER](_plugin_info_generator_8h_a0f672a0fccb6e6d06ec89d31250007d7.html#a0f672a0fccb6e6d06ec89d31250007d7)(x) |
|  | |
| #define | [DEFINE\_AUDIOPLUGIN\_CONTAINER](_plugin_info_generator_8h_ab1c8be3af6ebbecc8b8390b24d23c591.html#ab1c8be3af6ebbecc8b8390b24d23c591)(x)   [AK\_DEFINE\_PLUGIN\_CONTAINER](_plugin_info_generator_8h_abfa289aa9dd9fd63a3ad3b152ac828af.html#abfa289aa9dd9fd63a3ad3b152ac828af)(x) |
|  | |
| #define | [EXPORT\_AUDIOPLUGIN\_CONTAINER](_plugin_info_generator_8h_a75cdf71bbb38c3d3c02dcb296a3673a1.html#a75cdf71bbb38c3d3c02dcb296a3673a1)(x)   [AK\_EXPORT\_PLUGIN\_CONTAINER](_plugin_info_generator_8h_ab198136f861ed921af8857efe36b7007.html#ab198136f861ed921af8857efe36b7007)(x) |
|  | |
| #define | [ADD\_AUDIOPLUGIN\_CLASS\_TO\_CONTAINER](_plugin_info_generator_8h_aec78414cc40288b8ea0f1a993e1278bd.html#aec78414cc40288b8ea0f1a993e1278bd)(x, y, z)   [AK\_ADD\_PLUGIN\_CLASS\_TO\_CONTAINER](_plugin_info_generator_8h_ae72bc9efe38504b8f47686c01f5882f8.html#ae72bc9efe38504b8f47686c01f5882f8)(x, y, z) |
|  | |
| #define | [ADD\_AUDIOPLUGIN\_CLASSID\_TO\_CONTAINER](_plugin_info_generator_8h_ad7b094a4427a29052333144eedaa17db.html#ad7b094a4427a29052333144eedaa17db)(x, y, a, b, c)   [AK\_ADD\_PLUGIN\_CLASSID\_TO\_CONTAINER](_plugin_info_generator_8h_a38d201b97ec257331b3b4e23f15f20d5.html#a38d201b97ec257331b3b4e23f15f20d5)(x, y, a, b, c) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::InterfaceType](namespace_a_k_1_1_wwise_1_1_plugin_a32695b07bf576e5426c1b727bf4f541b.html#a32695b07bf576e5426c1b727bf4f541b) = decltype(BaseInterface::m\_interface) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Type for the m\_interface value in BaseInterface [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a32695b07bf576e5426c1b727bf4f541b.html#a32695b07bf576e5426c1b727bf4f541b) |
|  | |
| using | [AK::Wwise::Plugin::InterfaceTypeValue](namespace_a_k_1_1_wwise_1_1_plugin_af1b35c028fe0e61c30385aba36fa6372.html#af1b35c028fe0e61c30385aba36fa6372) = std::underlying\_type< InterfaceType >::type |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Underlying storage type for the m\_interface value in BaseInterface [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af1b35c028fe0e61c30385aba36fa6372.html#af1b35c028fe0e61c30385aba36fa6372) |
|  | |
| using | [AK::Wwise::Plugin::InterfaceVersion](namespace_a_k_1_1_wwise_1_1_plugin_a7fa905741ba9846fd2f0c4bfa3fc416b.html#a7fa905741ba9846fd2f0c4bfa3fc416b) = decltype(BaseInterface::m\_version) |
|  | [PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Type for the m\_version value in BaseInterface [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a7fa905741ba9846fd2f0c4bfa3fc416b.html#a7fa905741ba9846fd2f0c4bfa3fc416b) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - C++ class helper to automatically determine the plug-in interfaces used in a class.

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 中定义.