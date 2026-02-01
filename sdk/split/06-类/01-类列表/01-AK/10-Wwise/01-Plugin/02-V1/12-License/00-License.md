# License

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [License](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::License类 参考

`#include <License.h>`

类 AK.Wwise::Plugin::V1::License 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a3cb5d4ff8a71db1d1ac030983f93d586.html#a3cb5d4ff8a71db1d1ac030983f93d586af4e84ec689d1528c3014a8a54b337324) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LICENSE } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a3cb5d4ff8a71db1d1ac030983f93d586.html#a3cb5d4ff8a71db1d1ac030983f93d586) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a7891cddc6af94d6b80ecf2fd0a64f9f8.html#a7891cddc6af94d6b80ecf2fd0a64f9f8ac7a359c8fd9b04782281f25dae318440) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a7891cddc6af94d6b80ecf2fd0a64f9f8.html#a7891cddc6af94d6b80ecf2fd0a64f9f8) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_aaea371a7cf3340f77053dff66793c820.html#aaea371a7cf3340f77053dff66793c820) () |
|  | |
| [CLicense::Instance](structak__wwise__plugin__license__v1_aeb5502440bfc400f8c509bb1f9a6a66a.html#aeb5502440bfc400f8c509bb1f9a6a66a) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a4f943e7e8da0e1b7469ed16230a7fbac.html#a4f943e7e8da0e1b7469ed16230a7fbac) () |
|  | |
| const [CLicense::Instance](structak__wwise__plugin__license__v1_aeb5502440bfc400f8c509bb1f9a6a66a.html#aeb5502440bfc400f8c509bb1f9a6a66a) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_aaf3c1f5bf60b643c208d9763ce4664ba.html#aaf3c1f5bf60b643c208d9763ce4664ba) () const |
|  | |
|  | [License](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a9f13c941fb630f81f1541b339d564ee8.html#a9f13c941fb630f81f1541b339d564ee8) () |
|  | |
| virtual | [~License](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a159760ffc9ebd02f105e8b5fa81e6879.html#a159760ffc9ebd02f105e8b5fa81e6879) () |
|  | |
| virtual [LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) | [GetLicenseStatus](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a33cea73844b7198f466ddfd911b4bc59.html#a33cea73844b7198f466ddfd911b4bc59) (const GUID &in\_guidPlatform, [Severity](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) &out\_eSeverity, char \*out\_pszMessage, unsigned int in\_uiBufferSize) const |
|  | Retrieve the licensing status of the plug-in for the given platform. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_a33cea73844b7198f466ddfd911b4bc59.html#a33cea73844b7198f466ddfd911b4bc59) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [License.h](_license_8h_source.html) 第 [98](_license_8h_source.html#l00098) 行定义.