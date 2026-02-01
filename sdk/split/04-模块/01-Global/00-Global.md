# Global

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[类](#nested-classes) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[函数](#func-members)

Global

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) |
|  | Interface description and base class for every Wwise Authoring plug-in interface. [更多...](structak__wwise__plugin__base__interface.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_undo\_event\_pair\_v1](structak__wwise__plugin__undo__event__pair__v1.html) |
|  | A definition of an undo event, with a specific interface and instance. [更多...](structak__wwise__plugin__undo__event__pair__v1.html#details) |
|  | |
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
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)(in\_interface, in\_version) |
|  | |
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
| typedef int | [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) |
|  | Unique identifier for a particular undo group. Useful to reopen an unapplied closed group session. [更多...](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) |
|  | |
| typedef uint32\_t | [ak\_wwise\_plugin\_property\_set\_braces](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) |
|  | Bitfield composed of values defined in `ak_wwise_plugin_property_set_braces_values` [更多...](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) |
|  | |
| typedef void | [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) {     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNKNOWN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a40958ac64b124869ebf623a003828a53), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PLUGIN\_CONTAINER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8624f25f696288e5fee92b38528105b7), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_ANALYSIS\_TASK](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ae716d6886ba8bb4197599bc60010d9a1), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af60f00124117a22873d01c98255478ed),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_CONVERSION](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aacac1da112b7cc901b36d44e2f3651a9), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_CUSTOM\_DATA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a866bd5f3bddd5bde6067ddc08ff882aa), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FEEDBACK\_AWARE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ace4bbfc9034adf76f63ab79791598eb4), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FIRST\_TIME\_CREATION\_MESSAGE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a72c782c40df28013cce3676850064c02),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LICENSE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aae5f79946e2cbff79d92163117f5dd8b), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_MEDIA\_CONVERTER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9acc6b762efd7653cabd05b42068cc7bc7), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a39cce7a5d163d7e82aac57807a80e831), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_MONITOR](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ac04b4cc07950e34f1b4aa9f93ec6d5a3),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_MEDIA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a3dad917a24d46fd680f342d8c6c299e8), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_STORE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a257b8a3c00de2195a4d19871830f93cd), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8393a83801f2e47851845c2d09b71659), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PROPERTY\_DISPLAY\_NAME](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af99e8cd163b565d2cc56a3822dec423d),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SINK\_DEVICES](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a821f9229a08f07baaf0783425ced53d1), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SOURCE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8d2a79ba3f9d7006fee4a710c35a2623), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNDO\_EVENT](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a84bd3a1272d5f343df1bab3a826ffe65), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_CONVERSION\_WINDOWS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a90c4e56d16e50a50d7b5770f531247da),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_WINDOWS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af55117f741b99ad4a3d7eb6668dc8efe), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af1c18a159e804b70aa8e3bafd53ccfe1), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_CONVERSION\_HELPERS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a28a5d7dd31d6afec3d2a0a3303761df6), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_MEDIA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a123cdd811f15c89c6d15915c62fa0116),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_STORE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a548777b0657519d6b6e634574170c29f), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a76f67f330dab04093a4600d4d63d4446), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_UNDO\_MANAGER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a07328d19f39944a12c7b57ae1955f520), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_DATA\_WRITER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa1aa181e6241b63d3a1d204e403a94ad),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_XML](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a6544a9fc6225dbd24d33f5bef7495d18), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_BACKEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a7e6d9382217615a4d0205bcd87ffb8f8), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_FRONTEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a487278fb36df685b23d6ffbb7512b80a), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_ISERVICEPROVIDER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a70148864943ddf2510d5f2ea86ab7be2),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWAUDIODEVICEPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a169314fdd3f8ad945b201194845bfd35), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWCONVERSIONPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a59d059908689a126d9d81da1e993100f), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWEFFECTPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a99c558667099b96a17fa73d90dc87b5d), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWSOURCEPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a0c676701ca4f200f0f28d1ef2cf2f815),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_TESTSERVICE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa350fb41f83e8b444aed3f757dac68f5), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FRONTEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa58ee40b40c495300ba7b919da18bceb), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_FRONTEND\_MODEL](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a59544c57eb30361f5a4df4f25fe8ca2a), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_REFERENCE\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aea11355fbccff969a4def18261402dc5),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_REFERENCE\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aaebf595516f8a6f606ec4f08c12d8175), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NUM](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ad55211fa812319b74aa814d44f58a146)   } |
|  | List of every single interface known to the plug-in system [更多...](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) |
|  | |
| enum | [ak\_wwise\_plugin\_undo\_group\_close\_action](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) {     [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_CLOSE](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65cab2808bcde599ec2d8622deb9ddb449f3), [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65ca7b066ecc400936abe8602ec9deb27e5f), [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY\_FIRST\_EVENT\_NAME](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65cacd212f32bc852fcb9abc5a44bf906776), [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY\_LAST\_EVENT\_NAME](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65ca9b23a997b9bde905fbb6a1282a601f93),     [AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_CANCEL](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65cac2211c2692785e248eaa51ffd5e4c0dd)   } |
|  | Action to apply once this undo group is closed. [更多...](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) |
|  | |
| enum | [ak\_wwise\_plugin\_property\_set\_braces\_values](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#ga3cfc97efdbbda4629a10f0e53e914eb9) {     [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_NO\_NOTIFY](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a6dff872c6af8fb5f681332bef9926c58) = 1 << 0, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_NO\_UNDO\_EVENTS](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9ab38bef13078d1c5551ed26629a62920c) = 1 << 1, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_SET\_VALUE](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a2d3687f237127acb70930ab25721d775) = 1 << 2, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_REORDER\_CHILDREN](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9ad88f6db345109a3b576a42832153ee88) = 1 << 3,     [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_DISABLE\_PROPERTY\_CONSTRAINTS](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a8c890977bfa84797f378e909e75066f7) = 1 << 4, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_NO\_DIRTY](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9aa950b9a5fe6890beb0816607483361a7) = 1 << 5, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_CREATE\_PROPERTY\_ON\_SET\_VALUE](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a495faffff7fa5e3a9b86e9bb8b247624) = 1 << 6, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_CHANGE\_TO\_EXISTING\_VALUE\_TYPE](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9ac740cc44214287bc9ae50b8bfcb87265) = 1 << 7,     [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_LOADING](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a82ad89401e7643e3db226f15e9acdf90) = 1 << 8, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_UNLOADING](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9a48784d71f3015ddf7cc7def725db76ad) = 1 << 9, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_DELETING](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9af6b7ca3eb4b0186443eb76b4d7d8b934) = 1 << 10, [AK\_WWISE\_PLUGIN\_PROPERTY\_SET\_BRACES\_SET\_OBJECT\_LIST](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#gga3cfc97efdbbda4629a10f0e53e914eb9afa248dae2ff331d3a544ea0fae47a0f0) = 1 << 11   } |
|  | Bitfield values of brace types, used to delay or avoid certain actions normally triggered as a result of a property set mutation. [更多...](group__global_ga3cfc97efdbbda4629a10f0e53e914eb9.html#ga3cfc97efdbbda4629a10f0e53e914eb9) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK\_WWISE\_PLUGIN\_INTERFACE\_EXTEND\_PREVIOUS](group__global_ga2d3dca1d0980e5040a40d7a68da44859.html#ga2d3dca1d0980e5040a40d7a68da44859) (ak\_wwise\_plugin\_host\_instance\_v2, [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html)) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2.html "API to request host's current state and services."). [更多...](group__global_ga2d3dca1d0980e5040a40d7a68da44859.html#ga2d3dca1d0980e5040a40d7a68da44859) |
|  | |

## 详细描述