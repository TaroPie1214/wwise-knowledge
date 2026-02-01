# Source

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Source类 参考abstract

[Wwise](namespace_a_k_1_1_wwise.html) API for general Audio Plug-in's backend.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.html#details)

`#include <Source.h>`

类 AK.Wwise::Plugin::V1::Source 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_a0200428d79824354f3fb257e9cdb6a0f.html#a0200428d79824354f3fb257e9cdb6a0fa64462cafab645513bf5d33cabbc91b78) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SOURCE } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_a0200428d79824354f3fb257e9cdb6a0f.html#a0200428d79824354f3fb257e9cdb6a0f) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_a6884cf571210d1d322e2adbc88dda5ba.html#a6884cf571210d1d322e2adbc88dda5baacde23489d250a9252ba48408db07cf05) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_a6884cf571210d1d322e2adbc88dda5ba.html#a6884cf571210d1d322e2adbc88dda5ba) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_aca97ceb2cb17d552aa760749204a9dc8.html#aca97ceb2cb17d552aa760749204a9dc8) = [CSource::Instance](structak__wwise__plugin__source__v1_aee1d28a6a4ef6f754a70fba412907a84.html#aee1d28a6a4ef6f754a70fba412907a84) |
|  | Base instance type for providing source-specific information. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_aca97ceb2cb17d552aa760749204a9dc8.html#aca97ceb2cb17d552aa760749204a9dc8) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_ac4f3f23b249a12394738a7f582dcbfb0.html#ac4f3f23b249a12394738a7f582dcbfb0) () |
|  | |
| [CSource::Instance](structak__wwise__plugin__source__v1_aee1d28a6a4ef6f754a70fba412907a84.html#aee1d28a6a4ef6f754a70fba412907a84) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_a0d44040366809b5816120731d232b54d.html#a0d44040366809b5816120731d232b54d) () |
|  | |
| const [CSource::Instance](structak__wwise__plugin__source__v1_aee1d28a6a4ef6f754a70fba412907a84.html#aee1d28a6a4ef6f754a70fba412907a84) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_afce7be73dc4fdc10c3cb2591558a711a.html#afce7be73dc4fdc10c3cb2591558a711a) () const |
|  | |
|  | [Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_a6fe7c268e8d4f925aac90c82c1421304.html#a6fe7c268e8d4f925aac90c82c1421304) () |
|  | |
| virtual | [~Source](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_aef34715038e3b073be7c0a89ca53d565.html#aef34715038e3b073be7c0a89ca53d565) () |
|  | |
| virtual bool | [GetSourceDuration](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_acecbec655a9c34630b5b5c8efb29fe1d.html#acecbec655a9c34630b5b5c8efb29fe1d) (double &out\_dblMinDuration, double &out\_dblMaxDuration) const =0 |
|  | Return the minimum and maximum duration, in seconds. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_acecbec655a9c34630b5b5c8efb29fe1d.html#acecbec655a9c34630b5b5c8efb29fe1d) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) API for general Audio Plug-in's backend.

参见
:   - [ak\_wwise\_plugin\_audio\_plugin\_instance\_v1](structak__wwise__plugin__audio__plugin__instance__v1.html) instance type
    - [AK::Wwise::Plugin::AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) C++ [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_source_1_1_interface.html "The C interface, fulfilled by your plug-in.")
    - [AK\_WWISE\_PLUGIN\_AUDIO\_PLUGIN\_V1\_ID](_audio_plugin_8h_af21f7290225f823c30ea9bba6173c2ae.html#af21f7290225f823c30ea9bba6173c2ae) Current ID for interface
    - [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af60f00124117a22873d01c98255478ed)
    - [设计工具插件的后端](wwiseplugin_backend.html)

在文件 [Source.h](_source_8h_source.html) 第 [90](_source_8h_source.html#l00090) 行定义.