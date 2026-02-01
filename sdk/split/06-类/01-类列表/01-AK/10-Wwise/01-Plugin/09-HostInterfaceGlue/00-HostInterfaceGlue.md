# HostInterfaceGlue

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue-members.html) |
[Public 类型](#pub-types) |
[静态 Public 属性](#pub-static-attribs)

AK.Wwise::Plugin::HostInterfaceGlue< CPPInstance, in\_baseInstance > 模板类 参考

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Base class for every C++ instance that retrieves a service from the [Wwise](namespace_a_k_1_1_wwise.html) Authoring host.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html#details)

`#include <PluginInfoGenerator.h>`

类 AK.Wwise::Plugin::HostInterfaceGlue< CPPInstance, in\_baseInstance > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ad467cfe7dac33201b15351a8ef8845d5.html#ad467cfe7dac33201b15351a8ef8845d5a7073a51e4c074be721ffdd55fec927d4) = CPPInstance::k\_interfaceType } |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a44f1f0e850210433f2cb5e9847f581a1.html#a44f1f0e850210433f2cb5e9847f581a1a3ad9392320c1ead9a092222ed500c72d) = CPPInstance::k\_interfaceVersion } |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = CPPInstance |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

### template<typename CPPInstance, bool in\_baseInstance> class AK.Wwise::Plugin::HostInterfaceGlue< CPPInstance, in\_baseInstance >

[PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html "C++ PluginInfo Generator."): Base class for every C++ instance that retrieves a service from the [Wwise](namespace_a_k_1_1_wwise.html) Authoring host.

Compared to C, where the interface contains all the functions and the instance is an opaque block, the C++ version is the opposite; the instance is a class containing all the methods, and the interface is hidden as implementation details.

The [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html "PluginInfoGenerator: Base class for every C++ instance that retrieves a service from the Wwise Author...") helper class provides that distinction. Depending on the in\_baseInstance parameter, it will either have only a C interface (true) or also have its default instantiation (false).

模板参数
:   |  |  |
    | --- | --- |
    | CPPInstance | The C++ instance to instantiate. |
    | in\_baseInstance | Only provide a bridge (true) or also a default instance (false). |

参见
:   - [AK::Wwise::Plugin::PluginInfoGenerator](struct_a_k_1_1_wwise_1_1_plugin_1_1_plugin_info_generator.html)

在文件 [PluginInfoGenerator.h](_plugin_info_generator_8h_source.html) 第 [126](_plugin_info_generator_8h_source.html#l00126) 行定义.