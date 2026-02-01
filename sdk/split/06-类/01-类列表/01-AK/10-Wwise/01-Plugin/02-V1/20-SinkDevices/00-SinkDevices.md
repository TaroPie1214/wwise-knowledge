# SinkDevices

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [SinkDevices](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::SinkDevices类 参考abstract

C++ API to provide device enumeration for sink plug-ins.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices.html#details)

`#include <SinkDevices.h>`

类 AK.Wwise::Plugin::V1::SinkDevices 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a3ede7a7c607eb7f307ce15c8fb41cbc5.html#a3ede7a7c607eb7f307ce15c8fb41cbc5a28368faeffd487e03acdfc604f174cc9) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SINK\_DEVICES } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a3ede7a7c607eb7f307ce15c8fb41cbc5.html#a3ede7a7c607eb7f307ce15c8fb41cbc5) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_af244f904e89579550c8f2f3aecfc8e30.html#af244f904e89579550c8f2f3aecfc8e30a188a61fa824c30c428c130f353377617) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_af244f904e89579550c8f2f3aecfc8e30.html#af244f904e89579550c8f2f3aecfc8e30) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a4171b2f7c8a0a4fa3aa5223e075342d2.html#a4171b2f7c8a0a4fa3aa5223e075342d2) = [CSinkDevices::Instance](structak__wwise__plugin__sink__devices__v1_aa5f405106aa1af9ef69f1c5093ebe2f4.html#aa5f405106aa1af9ef69f1c5093ebe2f4) |
|  | Base instance type for providing a device list for your custom sink through [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html "Device enumerator for sink plug-ins."). [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a4171b2f7c8a0a4fa3aa5223e075342d2.html#a4171b2f7c8a0a4fa3aa5223e075342d2) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a92a7daee78677be06b2e7e657a8f9a70.html#a92a7daee78677be06b2e7e657a8f9a70) () |
|  | |
| [CSinkDevices::Instance](structak__wwise__plugin__sink__devices__v1_aa5f405106aa1af9ef69f1c5093ebe2f4.html#aa5f405106aa1af9ef69f1c5093ebe2f4) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_aece4f835924444d2062a0d5ae0fa15b8.html#aece4f835924444d2062a0d5ae0fa15b8) () |
|  | |
| const [CSinkDevices::Instance](structak__wwise__plugin__sink__devices__v1_aa5f405106aa1af9ef69f1c5093ebe2f4.html#aa5f405106aa1af9ef69f1c5093ebe2f4) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_af5f552be978f2cd8240ef27230a61437.html#af5f552be978f2cd8240ef27230a61437) () const |
|  | |
|  | [SinkDevices](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a3162f7d4d104db711aa9a599a055a2fa.html#a3162f7d4d104db711aa9a599a055a2fa) () |
|  | |
| virtual | [~SinkDevices](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a91a5ff46f20230c5f963730b5a8b4d1f.html#a91a5ff46f20230c5f963730b5a8b4d1f) () |
|  | |
| virtual int | [GetCount](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_ab38c3a53717c426c667841e148e5fffe.html#ab38c3a53717c426c667841e148e5fffe) () const =0 |
|  | Get a count of the number of interfaces currently available. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_ab38c3a53717c426c667841e148e5fffe.html#ab38c3a53717c426c667841e148e5fffe) |
|  | |
| virtual const char \* | [GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_abe416b2abe47f16ef9368b7c18d8c159.html#abe416b2abe47f16ef9368b7c18d8c159) (int in\_num) const =0 |
|  | Get a user-presentable name for the device number in\_num. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_abe416b2abe47f16ef9368b7c18d8c159.html#abe416b2abe47f16ef9368b7c18d8c159) |
|  | |
| virtual uint32\_t | [GetDeviceID](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a0b5fb646510a4566363eb59a06917c67.html#a0b5fb646510a4566363eb59a06917c67) (int in\_num) const =0 |
|  | Get a device ID for the device number in\_num. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_a0b5fb646510a4566363eb59a06917c67.html#a0b5fb646510a4566363eb59a06917c67) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

C++ API to provide device enumeration for sink plug-ins.

Allows your plug-in to provide a list of up-to-date device IDs that can be used to instantiate a new Sound Engine sink.

This plug-in interface cannot be linked to a backend or a frontend plug-in, it must be standalone.

参见
:   - [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html) C interface
    - [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SINK\_DEVICES](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a821f9229a08f07baaf0783425ced53d1)

在文件 [SinkDevices.h](_sink_devices_8h_source.html) 第 [171](_sink_devices_8h_source.html#l00171) 行定义.