# PluginInstanceTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

PluginInstanceTypes.h 文件参考

Wwise Authoring Plug-in Instance Types
[更多...](#details)

[浏览源代码.](_plugin_instance_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_instance\_ptr](structak__wwise__plugin__base__instance.html) |
|  | Generic base for all plug-in instances. In C++, this is derived. In C, they are equivalent. [更多...](structak__wwise__plugin__base__instance.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) |
|  | Generic base for all plug-in instances in C++ [更多...](structak__wwise__plugin__cpp__base__instance.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html) |
|  | Plug-in backend instance. [更多...](structak__wwise__plugin__backend__instance.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_frontend\_instance](structak__wwise__plugin__frontend__instance.html) |
|  | Plug-in frontend instance. [更多...](structak__wwise__plugin__frontend__instance.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html "API to request host's current state and services."). [更多...](structak__wwise__plugin__host__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_conversion\_helpers\_instance\_v1](structak__wwise__plugin__host__conversion__helpers__instance__v1.html) |
|  | Base host-provided instance type for ak\_wwise\_plugin\_host\_conversion\_helpers\_v1. [更多...](structak__wwise__plugin__host__conversion__helpers__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_data\_writer\_v1](structak__wwise__plugin__host__data__writer__v1.html "Interface used to write data during sound bank generation."). [更多...](structak__wwise__plugin__host__data__writer__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_object\_media\_instance\_v1](structak__wwise__plugin__host__object__media__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_object\_media\_v1](structak__wwise__plugin__host__object__media__v1.html). [更多...](structak__wwise__plugin__host__object__media__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html "Custom inner property set interface."). [更多...](structak__wwise__plugin__host__object__store__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_property\_set\_v1](structak__wwise__plugin__host__property__set__v1.html "Interface used to interact with property sets."). [更多...](structak__wwise__plugin__host__property__set__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_reference\_set\_v1](structak__wwise__plugin__host__reference__set__v1.html "Interface used to interact with reference sets."). [更多...](structak__wwise__plugin__host__reference__set__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_undo\_manager\_instance\_v1](structak__wwise__plugin__host__undo__manager__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_undo\_manager\_v1](structak__wwise__plugin__host__undo__manager__v1.html "Host API to handle the plug-in's undo operations."). [更多...](structak__wwise__plugin__host__undo__manager__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) |
|  | Base host-provided instance type for reading XML files through [ak\_wwise\_plugin\_host\_xml\_v1](structak__wwise__plugin__host__xml__v1.html "API interface for XML-based plug-in persistence."). [更多...](structak__wwise__plugin__host__xml__reader__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) |
|  | Base host-provided instance type for writing XML files through [ak\_wwise\_plugin\_host\_xml\_v1](structak__wwise__plugin__host__xml__v1.html "API interface for XML-based plug-in persistence."). [更多...](structak__wwise__plugin__host__xml__writer__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_analysis\_task\_instance\_v1](structak__wwise__plugin__analysis__task__instance__v1.html) |
|  | Base instance type for providing analysis task services through ak\_wwise\_plugin\_analysis\_task\_v1. [更多...](structak__wwise__plugin__analysis__task__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_audio\_plugin\_instance\_v1](structak__wwise__plugin__audio__plugin__instance__v1.html) |
|  | Base instance type for providing audio plug-in backend services through [ak\_wwise\_plugin\_audio\_plugin\_v1](structak__wwise__plugin__audio__plugin__v1.html "Wwise API for general Audio Plug-in's backend."). [更多...](structak__wwise__plugin__audio__plugin__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_conversion\_instance\_v1](structak__wwise__plugin__conversion__instance__v1.html) |
|  | Base instance type for providing a conversion plug-in through ak\_wwise\_plugin\_conversion\_v1. [更多...](structak__wwise__plugin__conversion__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) |
|  | Base instance type for providing custom data loading and saving through [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1.html "Backend API to load and save custom data in XML format."). [更多...](structak__wwise__plugin__custom__data__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_property\_display\_name\_instance\_v1](structak__wwise__plugin__property__display__name__instance__v1.html) |
|  | Base instance type for providing display names to properties through [ak\_wwise\_plugin\_property\_display\_name\_v1](structak__wwise__plugin__property__display__name__v1.html "Backend API to specify display names for properties"). [更多...](structak__wwise__plugin__property__display__name__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_feedback\_aware\_instance\_v1](structak__wwise__plugin__feedback__aware__instance__v1.html) |
|  | Base instance type for providing property-based feedback through ak\_wwise\_plugin\_feedback\_aware\_v1. [更多...](structak__wwise__plugin__feedback__aware__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_gui\_conversion\_windows\_instance\_v1](structak__wwise__plugin__gui__conversion__windows__instance__v1.html) |
|  | Base instance type for providing a Windows frontend for a conversion plug-in through ak\_wwise\_plugin\_gui\_conversion\_windows\_v1. [更多...](structak__wwise__plugin__gui__conversion__windows__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) |
|  | Base instance type for providing a Windows frontend for an audio plug-in through [ak\_wwise\_plugin\_gui\_windows\_v1](structak__wwise__plugin__gui__windows__v1.html "Windows frontend plug-in API for Audio plug-ins."). [更多...](structak__wwise__plugin__gui__windows__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_link\_backend\_instance\_v1](structak__wwise__plugin__link__backend__instance__v1.html) |
|  | Base host-provided instance to retrieve the related backend instance, as shown in the frontend. [更多...](structak__wwise__plugin__link__backend__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_link\_frontend\_instance\_v1](structak__wwise__plugin__link__frontend__instance__v1.html) |
|  | Base host-provided instance to retrieve the related frontend instances related to the current backend. [更多...](structak__wwise__plugin__link__frontend__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_media\_converter\_instance\_v1](structak__wwise__plugin__media__converter__instance__v1.html) |
|  | Base instance type for providing custom media conversion through [ak\_wwise\_plugin\_media\_converter\_v1](structak__wwise__plugin__media__converter__v1.html "API to convert used object medias to a format usable by the plug-in's Sound Engine part."). [更多...](structak__wwise__plugin__media__converter__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_host\_instance\_v1](structak__wwise__plugin__notifications__host__instance__v1.html) |
|  | Base instance type for receiving notifications on host changes events. [更多...](structak__wwise__plugin__notifications__host__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_monitor\_instance\_v1](structak__wwise__plugin__notifications__monitor__instance__v1.html) |
|  | Base instance type for receiving Sound Engine's monitoring data. [更多...](structak__wwise__plugin__notifications__monitor__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_object\_media\_instance\_v1](structak__wwise__plugin__notifications__object__media__instance__v1.html) |
|  | Base instance type for receiving notifications on related object media's changes. [更多...](structak__wwise__plugin__notifications__object__media__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_object\_store\_instance\_v1](structak__wwise__plugin__notifications__object__store__instance__v1.html) |
|  | Base instance type for receiving notifications on related Object Store's changes. [更多...](structak__wwise__plugin__notifications__object__store__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_property\_set\_instance\_v1](structak__wwise__plugin__notifications__property__set__instance__v1.html) |
|  | Base instance type for receiving notifications on property set's changes. [更多...](structak__wwise__plugin__notifications__property__set__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_notifications\_reference\_set\_instance\_v1](structak__wwise__plugin__notifications__reference__set__instance__v1.html) |
|  | Base instance type for receiving notifications on reference set's changes. [更多...](structak__wwise__plugin__notifications__reference__set__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_source\_instance\_v1](structak__wwise__plugin__source__instance__v1.html) |
|  | Base instance type for providing source-specific information, through [ak\_wwise\_plugin\_source\_v1](structak__wwise__plugin__source__v1.html "API specific for source plug-in."). [更多...](structak__wwise__plugin__source__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) |
|  | Base instance type for providing custom undo operations through [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html "API to create a custom undo event in a plug-in."). [更多...](structak__wwise__plugin__undo__event__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_license\_instance\_v1](structak__wwise__plugin__license__instance__v1.html) |
|  | Base instance type for providing licensing information, through [ak\_wwise\_plugin\_license\_v1](structak__wwise__plugin__license__v1.html "Backend API to specify licensing requirements"). [更多...](structak__wwise__plugin__license__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_first\_time\_creation\_message\_instance\_v1](structak__wwise__plugin__first__time__creation__message__instance__v1.html) |
|  | Base instance type for providing a message shown the first time an instance is created through [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html "Plug-in that provides a special usage message when first instantiated."). [更多...](structak__wwise__plugin__first__time__creation__message__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_sink\_devices\_instance\_v1](structak__wwise__plugin__sink__devices__instance__v1.html) |
|  | Base instance type for providing a device list for your custom sink through [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html "Device enumerator for sink plug-ins."). [更多...](structak__wwise__plugin__sink__devices__instance__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_test\_service\_instance\_v1](structak__wwise__plugin__test__service__instance__v1.html) |
|  | |
| struct | [ak\_wwise\_plugin\_test\_service\_instance\_v2](structak__wwise__plugin__test__service__instance__v2.html) |
|  | |
| struct | [ak\_wwise\_plugin\_frontend\_instance\_v1](structak__wwise__plugin__frontend__instance__v1.html) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) |
|  | |
| struct | [ak\_wwise\_plugin\_host\_frontend\_model\_args\_v1](structak__wwise__plugin__host__frontend__model__args__v1.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_DERIVE\_FROM\_INSTANCE\_BASE](group__global_ga2832a26d2283aa1ad22a7beaa34aada6.html#ga2832a26d2283aa1ad22a7beaa34aada6)   : public [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) |
|  | Define a generic instance base, either in C or in C++. [更多...](group__global_ga2832a26d2283aa1ad22a7beaa34aada6.html#ga2832a26d2283aa1ad22a7beaa34aada6) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_INTERFACE\_EXTEND\_PREVIOUS](group__global_gad455fd4de54bbeab7fd956f45e0a2715.html#gad455fd4de54bbeab7fd956f45e0a2715)(interface, interface\_prev)    struct interface : public interface\_prev {}; |
|  | Define a generic instance base, either in C or in C++. [更多...](group__global_gad455fd4de54bbeab7fd956f45e0a2715.html#gad455fd4de54bbeab7fd956f45e0a2715) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_DERIVE\_FROM\_BACKEND\_INSTANCE](group__global_ga7549e1ba3f811921e9c26d28713121ce.html#ga7549e1ba3f811921e9c26d28713121ce)(x)    struct x : public [ak\_wwise\_plugin\_backend\_instance](structak__wwise__plugin__backend__instance.html) {} |
|  | Define an instance type as a backend. [更多...](group__global_ga7549e1ba3f811921e9c26d28713121ce.html#ga7549e1ba3f811921e9c26d28713121ce) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_DERIVE\_FROM\_FRONTEND\_INSTANCE](group__global_ga48ad2be17659d9177e929b2665804d9d.html#ga48ad2be17659d9177e929b2665804d9d)(x)    struct x : public [ak\_wwise\_plugin\_frontend\_instance](structak__wwise__plugin__frontend__instance.html) {} |
|  | Define an instance type as a frontend. [更多...](group__global_ga48ad2be17659d9177e929b2665804d9d.html#ga48ad2be17659d9177e929b2665804d9d) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef void | [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) |
|  | |
| using | [AK::Wwise::Plugin::CBaseInterface](namespace_a_k_1_1_wwise_1_1_plugin_a069641ed8537ba2dafcb828dfd5916a9.html#a069641ed8537ba2dafcb828dfd5916a9) = [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface.html) |
|  | Interface description and base class for every [Wwise](namespace_a_k_1_1_wwise.html) Authoring plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a069641ed8537ba2dafcb828dfd5916a9.html#a069641ed8537ba2dafcb828dfd5916a9) |
|  | |
| using | [AK::Wwise::Plugin::CInterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_ade5620136ec8b9def6c7e410f3a794b6.html#ade5620136ec8b9def6c7e410f3a794b6) = ak\_wwise\_plugin\_interface\_ptr |
|  | |
| using | [AK::Wwise::Plugin::CInterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_aca26b5c76f95d1a578548c56b0cf1ca5.html#aca26b5c76f95d1a578548c56b0cf1ca5) = [ak\_wwise\_plugin\_interface\_array\_item](structak__wwise__plugin__interface__array__item.html) |
|  | A single instantiatable plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aca26b5c76f95d1a578548c56b0cf1ca5.html#aca26b5c76f95d1a578548c56b0cf1ca5) |
|  | |
| using | [AK::Wwise::Plugin::CPluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_ac61a45449001d6c3d457a50230db20b8.html#ac61a45449001d6c3d457a50230db20b8) = [ak\_wwise\_plugin\_info](structak__wwise__plugin__info.html) |
|  | |
| using | [AK::Wwise::Plugin::CPluginContainer](namespace_a_k_1_1_wwise_1_1_plugin_acaeb7e0475ed47dda25a09fe722bb360.html#acaeb7e0475ed47dda25a09fe722bb360) = [ak\_wwise\_plugin\_container](structak__wwise__plugin__container.html) |
|  | Root interface allowing a logical unit (variable, library) to contain more than one interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_acaeb7e0475ed47dda25a09fe722bb360.html#acaeb7e0475ed47dda25a09fe722bb360) |
|  | |
| using | [AK::Wwise::Plugin::CWidget](namespace_a_k_1_1_wwise_1_1_plugin_ab9cbb84129fb7bc4f1eeadea41680ea3.html#ab9cbb84129fb7bc4f1eeadea41680ea3) = [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) |
|  | |
| using | [AK::Wwise::Plugin::BaseInterface](namespace_a_k_1_1_wwise_1_1_plugin_af12e29db650cd0c58e9880a64ff93b18.html#af12e29db650cd0c58e9880a64ff93b18) = CBaseInterface |
|  | Interface description and base class for every [Wwise](namespace_a_k_1_1_wwise.html) Authoring plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af12e29db650cd0c58e9880a64ff93b18.html#af12e29db650cd0c58e9880a64ff93b18) |
|  | |
| using | [AK::Wwise::Plugin::InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) = CInterfacePtr |
|  | |
| using | [AK::Wwise::Plugin::InterfaceArrayItem](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) = CInterfaceArrayItem |
|  | A single instantiatable plug-in interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_adbf11482a829b3ae6cc67b555e46db8c.html#adbf11482a829b3ae6cc67b555e46db8c) |
|  | |
| using | [AK::Wwise::Plugin::PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) = CPluginInfo |
|  | |
| using | [AK::Wwise::Plugin::PluginContainer](namespace_a_k_1_1_wwise_1_1_plugin_afa19c1aec7e87e47a7b3547a072713cc.html#afa19c1aec7e87e47a7b3547a072713cc) = CPluginContainer |
|  | Root interface allowing a logical unit (variable, library) to contain more than one interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_afa19c1aec7e87e47a7b3547a072713cc.html#afa19c1aec7e87e47a7b3547a072713cc) |
|  | |
| using | [AK::Wwise::Plugin::Widget](namespace_a_k_1_1_wwise_1_1_plugin_a9474b576cd95a3316ae3c4bba7ae18da.html#a9474b576cd95a3316ae3c4bba7ae18da) = CWidget |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK\_WWISE\_PLUGIN\_INTERFACE\_EXTEND\_PREVIOUS](group__global_ga2d3dca1d0980e5040a40d7a68da44859.html#ga2d3dca1d0980e5040a40d7a68da44859) (ak\_wwise\_plugin\_host\_instance\_v2, [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html)) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2.html "API to request host's current state and services."). [更多...](group__global_ga2d3dca1d0980e5040a40d7a68da44859.html#ga2d3dca1d0980e5040a40d7a68da44859) |
|  | |

## 详细描述

Wwise Authoring Plug-in Instance Types

在文件 [PluginInstanceTypes.h](_plugin_instance_types_8h_source.html) 中定义.