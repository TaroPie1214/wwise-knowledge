# ObjectMedia

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [ObjectMedia](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::ObjectMedia类 参考

[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.html#details)

`#include <HostObjectMedia.h>`

类 AK.Wwise::Plugin::V1::ObjectMedia 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a784ccc4c8f91d024f7bea572d85809df.html#a784ccc4c8f91d024f7bea572d85809dfa18ee9d461c6b3b863de6aa7bb3a1a548) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_MEDIA } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a784ccc4c8f91d024f7bea572d85809df.html#a784ccc4c8f91d024f7bea572d85809df) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_af2e1c36d372e0036ddab487520bb3a60.html#af2e1c36d372e0036ddab487520bb3a60acce5858c75ff22c27c5a077087a41bc5) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_af2e1c36d372e0036ddab487520bb3a60.html#af2e1c36d372e0036ddab487520bb3a60) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a19c5856e139c4c6c8e75f4db4aa1028e.html#a19c5856e139c4c6c8e75f4db4aa1028e) = [CHostObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a8022609c599c92d28ea192e81b3175c6.html#a8022609c599c92d28ea192e81b3175c6) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostObjectMedia >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostObjectMedia >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a4a7fe49717628bdfda765fbaee107d7a.html#a4a7fe49717628bdfda765fbaee107d7a) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | [SetMediaSource](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_aecc2d90460e0c684e027504f9fffe647.html#aecc2d90460e0c684e027504f9fffe647) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszFilePathToImport, unsigned int in\_Index, bool in\_bReplace) |
|  | Requests to set the specified file as a data input file. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_aecc2d90460e0c684e027504f9fffe647.html#aecc2d90460e0c684e027504f9fffe647) |
|  | |
| void | [RemoveMediaSource](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a2f1313b6fccb3488f68ff8f2ea5f45f1.html#a2f1313b6fccb3488f68ff8f2ea5f45f1) (unsigned int in\_Index) |
|  | Requests to remove the specified index file as data input file. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a2f1313b6fccb3488f68ff8f2ea5f45f1.html#a2f1313b6fccb3488f68ff8f2ea5f45f1) |
|  | |
| unsigned int | [GetMediaSourceCount](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a09d90dff8a24751c5599d427c38d667d.html#a09d90dff8a24751c5599d427c38d667d) () const |
|  | Retrieve the number of media source indexes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a09d90dff8a24751c5599d427c38d667d.html#a09d90dff8a24751c5599d427c38d667d) |
|  | |
| unsigned int | [GetMediaSourceFileName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a12818bd0d37ab3f579dd0c020a9ab706.html#a12818bd0d37ab3f579dd0c020a9ab706) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszFileName, unsigned int in\_uiBufferSize, unsigned int in\_Index) const |
|  | Retrieve the file name of the source plug-in data at the specified index, as provided in SetMediaSource. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a12818bd0d37ab3f579dd0c020a9ab706.html#a12818bd0d37ab3f579dd0c020a9ab706) |
|  | |
| unsigned int | [GetMediaSourceOriginalFilePath](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a64a31c1310cee111684620ebd96c0e52.html#a64a31c1310cee111684620ebd96c0e52) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszFilePath, unsigned int in\_uiBufferSize, unsigned int in\_Index) const |
|  | Retrieve the full file path of the source plug-in data at the specified index. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a64a31c1310cee111684620ebd96c0e52.html#a64a31c1310cee111684620ebd96c0e52) |
|  | |
| unsigned int | [GetMediaSourceConvertedFilePath](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_ac5a13e9ca433c6b4b6db754d85522b38.html#ac5a13e9ca433c6b4b6db754d85522b38) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszFilePath, unsigned int in\_uiBufferSize, const GUID &in\_guidPlatform, unsigned int in\_Index) const |
|  | Retrieve the full file path of the converted plug-in data at the specified index. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_ac5a13e9ca433c6b4b6db754d85522b38.html#ac5a13e9ca433c6b4b6db754d85522b38) |
|  | |
| void | [InvalidateMediaSource](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_ae4c1d088f8436e4984c7d3255d82c2d1.html#ae4c1d088f8436e4984c7d3255d82c2d1) (unsigned int in\_Index) |
|  | Request [Wwise](namespace_a_k_1_1_wwise.html) to perform any required conversion on the data. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_ae4c1d088f8436e4984c7d3255d82c2d1.html#ae4c1d088f8436e4984c7d3255d82c2d1) |
|  | |
| unsigned int | [GetOriginalDirectory](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a79a653850461d4c6809df9421ad5de77.html#a79a653850461d4c6809df9421ad5de77) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszDirectory, unsigned int in\_uiBufferSize) const |
|  | Obtain the Original directory for the plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a79a653850461d4c6809df9421ad5de77.html#a79a653850461d4c6809df9421ad5de77) |
|  | |
| unsigned int | [GetConvertedDirectory](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a45a950cbb4d47569d8d677747a1fe329.html#a45a950cbb4d47569d8d677747a1fe329) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pszDirectory, unsigned int in\_uiBufferSize, const GUID &in\_guidPlatform) const |
|  | Obtain the Converted directory for the plug-in and platform. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_a45a950cbb4d47569d8d677747a1fe329.html#a45a950cbb4d47569d8d677747a1fe329) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostObjectMedia >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Plug-in object media interface. Can be used to normalize media file handling inside the project.

在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 第 [298](_host_object_media_8h_source.html#l00298) 行定义.