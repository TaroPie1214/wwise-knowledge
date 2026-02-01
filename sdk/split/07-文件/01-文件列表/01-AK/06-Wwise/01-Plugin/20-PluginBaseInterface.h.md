# PluginBaseInterface.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[枚举](#enum-members)

PluginBaseInterface.h 文件参考

Wwise Authoring Plug-ins - Standardized header for all the plug-in interfaces.
[更多...](#details)

`#include "PluginDef.h"`  
`#include <type_traits>`

[浏览源代码.](_plugin_base_interface_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) |
|  | Interface description and base class for every Wwise Authoring plug-in interface. [更多...](structak__wwise__plugin__base__interface.html#details) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)(in\_interface, in\_version) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) {     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNKNOWN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a40958ac64b124869ebf623a003828a53), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PLUGIN\_CONTAINER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8624f25f696288e5fee92b38528105b7), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_ANALYSIS\_TASK](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ae716d6886ba8bb4197599bc60010d9a1), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af60f00124117a22873d01c98255478ed),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_CONVERSION](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aacac1da112b7cc901b36d44e2f3651a9), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_CUSTOM\_DATA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a866bd5f3bddd5bde6067ddc08ff882aa), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FEEDBACK\_AWARE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ace4bbfc9034adf76f63ab79791598eb4), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FIRST\_TIME\_CREATION\_MESSAGE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a72c782c40df28013cce3676850064c02),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LICENSE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aae5f79946e2cbff79d92163117f5dd8b), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_MEDIA\_CONVERTER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9acc6b762efd7653cabd05b42068cc7bc7), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a39cce7a5d163d7e82aac57807a80e831), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_MONITOR](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ac04b4cc07950e34f1b4aa9f93ec6d5a3),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_MEDIA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a3dad917a24d46fd680f342d8c6c299e8), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_STORE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a257b8a3c00de2195a4d19871830f93cd), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8393a83801f2e47851845c2d09b71659), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PROPERTY\_DISPLAY\_NAME](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af99e8cd163b565d2cc56a3822dec423d),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SINK\_DEVICES](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a821f9229a08f07baaf0783425ced53d1), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SOURCE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a8d2a79ba3f9d7006fee4a710c35a2623), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_UNDO\_EVENT](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a84bd3a1272d5f343df1bab3a826ffe65), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_CONVERSION\_WINDOWS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a90c4e56d16e50a50d7b5770f531247da),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_WINDOWS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af55117f741b99ad4a3d7eb6668dc8efe), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af1c18a159e804b70aa8e3bafd53ccfe1), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_CONVERSION\_HELPERS](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a28a5d7dd31d6afec3d2a0a3303761df6), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_MEDIA](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a123cdd811f15c89c6d15915c62fa0116),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_STORE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a548777b0657519d6b6e634574170c29f), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_PROPERTY\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a76f67f330dab04093a4600d4d63d4446), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_UNDO\_MANAGER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a07328d19f39944a12c7b57ae1955f520), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_DATA\_WRITER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa1aa181e6241b63d3a1d204e403a94ad),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_XML](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a6544a9fc6225dbd24d33f5bef7495d18), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_BACKEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a7e6d9382217615a4d0205bcd87ffb8f8), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_FRONTEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a487278fb36df685b23d6ffbb7512b80a), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_ISERVICEPROVIDER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a70148864943ddf2510d5f2ea86ab7be2),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWAUDIODEVICEPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a169314fdd3f8ad945b201194845bfd35), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWCONVERSIONPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a59d059908689a126d9d81da1e993100f), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWEFFECTPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a99c558667099b96a17fa73d90dc87b5d), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NATIVE\_IWSOURCEPLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a0c676701ca4f200f0f28d1ef2cf2f815),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_TESTSERVICE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa350fb41f83e8b444aed3f757dac68f5), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FRONTEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa58ee40b40c495300ba7b919da18bceb), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_FRONTEND\_MODEL](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a59544c57eb30361f5a4df4f25fe8ca2a), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_REFERENCE\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aea11355fbccff969a4def18261402dc5),     [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_REFERENCE\_SET](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aaebf595516f8a6f606ec4f08c12d8175), [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NUM](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ad55211fa812319b74aa814d44f58a146)   } |
|  | List of every single interface known to the plug-in system [更多...](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Standardized header for all the plug-in interfaces.

在文件 [PluginBaseInterface.h](_plugin_base_interface_8h_source.html) 中定义.