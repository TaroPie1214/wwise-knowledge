# PropertyDisplayName

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::PropertyDisplayName类 参考

`#include <PropertyDisplayName.h>`

类 AK.Wwise::Plugin::V1::PropertyDisplayName 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_ad84270e7a4c5c223f1cefc189afd4e89.html#ad84270e7a4c5c223f1cefc189afd4e89a929ff14fc8323600fea34eb4a6f19607) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_PROPERTY\_DISPLAY\_NAME } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_ad84270e7a4c5c223f1cefc189afd4e89.html#ad84270e7a4c5c223f1cefc189afd4e89) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a9f269feed6ce8e0aa7842b326de8d399.html#a9f269feed6ce8e0aa7842b326de8d399a1d66e8781b423d00a2e3ef481eca9fda) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a9f269feed6ce8e0aa7842b326de8d399.html#a9f269feed6ce8e0aa7842b326de8d399) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a0cbc552a05adf7f52aeba39c278d5d8d.html#a0cbc552a05adf7f52aeba39c278d5d8d) () |
|  | |
| [CPropertyDisplayName::Instance](structak__wwise__plugin__property__display__name__v1_ab4b234d53a8cb1cdd6e34a8371ec8b66.html#ab4b234d53a8cb1cdd6e34a8371ec8b66) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a9f7d5602fafb7de1ed947580fc957435.html#a9f7d5602fafb7de1ed947580fc957435) () |
|  | |
| const [CPropertyDisplayName::Instance](structak__wwise__plugin__property__display__name__v1_ab4b234d53a8cb1cdd6e34a8371ec8b66.html#ab4b234d53a8cb1cdd6e34a8371ec8b66) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a1233cc5f215c26b6ca35c323e9beb04c.html#a1233cc5f215c26b6ca35c323e9beb04c) () const |
|  | |
|  | [PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_ac088f65a4dff72edd924aa5b496275f4.html#ac088f65a4dff72edd924aa5b496275f4) () |
|  | |
| virtual | [~PropertyDisplayName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a2aac307b69964709c4f95f6d58c5403d.html#a2aac307b69964709c4f95f6d58c5403d) () |
|  | |
| virtual bool | [DisplayNameForProp](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a7e2d1eb64f740de7921fc3d793dc4f37.html#a7e2d1eb64f740de7921fc3d793dc4f37) (const char \*in\_pszPropertyName, char \*out\_pszDisplayName, uint32\_t in\_unCharCount) const |
|  | Gets the user-friendly name of the specified property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a7e2d1eb64f740de7921fc3d793dc4f37.html#a7e2d1eb64f740de7921fc3d793dc4f37) |
|  | |
| virtual bool | [DisplayNamesForPropValues](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a2d1788ed6ead7d8d9d38b16ff0c868a9.html#a2d1788ed6ead7d8d9d38b16ff0c868a9) (const char \*in\_pszPropertyName, char \*out\_pszValuesName, uint32\_t in\_unCharCount) const |
|  | Get the user-friendly names of possible values for the specified property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_display_name_a2d1788ed6ead7d8d9d38b16ff0c868a9.html#a2d1788ed6ead7d8d9d38b16ff0c868a9) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [PropertyDisplayName.h](_property_display_name_8h_source.html) 第 [137](_property_display_name_8h_source.html#l00137) 行定义.