# DataWriter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::DataWriter类 参考

Interface used to write data during sound bank generation.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html#details)

`#include <HostDataWriter.h>`

类 AK.Wwise::Plugin::V1::DataWriter 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9d73e140f317121ffef7fb44585604d0.html#a9d73e140f317121ffef7fb44585604d0a514333d0521168d99efddc2bc701abb9) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_DATA\_WRITER } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9d73e140f317121ffef7fb44585604d0.html#a9d73e140f317121ffef7fb44585604d0) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9be5f7cda5e80f599096ee2bd4bea7ed.html#a9be5f7cda5e80f599096ee2bd4bea7eda70679507eee556bf59843fc530e9f00b) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9be5f7cda5e80f599096ee2bd4bea7ed.html#a9be5f7cda5e80f599096ee2bd4bea7ed) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_aa51699e60e807c52b9824a158883453a.html#aa51699e60e807c52b9824a158883453a) = [CHostDataWriter](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_afd451009f6669cae2d5f092544a15f96.html#afd451009f6669cae2d5f092544a15f96) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostDataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostDataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostDataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a57477155e587be4bb9216ede425ea93e.html#a57477155e587be4bb9216ede425ea93e) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | [WriteData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a51b1f851263102a7b7eb914dcf4a730e.html#a51b1f851263102a7b7eb914dcf4a730e) (const void \*in\_pData, uint32\_t in\_cBytes, uint32\_t &out\_cWritten) |
|  | Writes a block of data. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a51b1f851263102a7b7eb914dcf4a730e.html#a51b1f851263102a7b7eb914dcf4a730e) |
|  | |
| bool | [WriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_af3924f7f2777b5bdf09ef379bc1bd124.html#af3924f7f2777b5bdf09ef379bc1bd124) (const char \*in\_szString) |
|  | Writes a string. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_af3924f7f2777b5bdf09ef379bc1bd124.html#af3924f7f2777b5bdf09ef379bc1bd124) |
|  | |
| bool | [WriteInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a3918434218fa705d507e2bb80aafb68b.html#a3918434218fa705d507e2bb80aafb68b) (int64\_t in\_value) |
|  | Writes a 64-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a3918434218fa705d507e2bb80aafb68b.html#a3918434218fa705d507e2bb80aafb68b) |
|  | |
| bool | [WriteInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9626e22ea3ba15a71d2cf51ac2332693.html#a9626e22ea3ba15a71d2cf51ac2332693) (int32\_t in\_value) |
|  | Writes a 32-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9626e22ea3ba15a71d2cf51ac2332693.html#a9626e22ea3ba15a71d2cf51ac2332693) |
|  | |
| bool | [WriteInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_ad74b965ff97aae6f93921633066299f1.html#ad74b965ff97aae6f93921633066299f1) (int16\_t in\_value) |
|  | Writes a 16-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_ad74b965ff97aae6f93921633066299f1.html#ad74b965ff97aae6f93921633066299f1) |
|  | |
| bool | [WriteInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a0118d55597fa01bae9126ef2d90c9483.html#a0118d55597fa01bae9126ef2d90c9483) (int8\_t in\_value) |
|  | Writes an 8-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a0118d55597fa01bae9126ef2d90c9483.html#a0118d55597fa01bae9126ef2d90c9483) |
|  | |
| bool | [WriteUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a2cde4eb02d99eb32ee5df9a5bc4f5c38.html#a2cde4eb02d99eb32ee5df9a5bc4f5c38) (uint64\_t in\_value) |
|  | Writes a 64-bit unsigned integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a2cde4eb02d99eb32ee5df9a5bc4f5c38.html#a2cde4eb02d99eb32ee5df9a5bc4f5c38) |
|  | |
| bool | [WriteUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_ad7b44a9cfd9992e441695bde4f1d8a8a.html#ad7b44a9cfd9992e441695bde4f1d8a8a) (uint32\_t in\_value) |
|  | Writes a 32-bit unsigned integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_ad7b44a9cfd9992e441695bde4f1d8a8a.html#ad7b44a9cfd9992e441695bde4f1d8a8a) |
|  | |
| bool | [WriteUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a87f10a02f84c39ba94956389b7d3b5a4.html#a87f10a02f84c39ba94956389b7d3b5a4) (uint16\_t in\_value) |
|  | Writes a 16-bit unsigned integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a87f10a02f84c39ba94956389b7d3b5a4.html#a87f10a02f84c39ba94956389b7d3b5a4) |
|  | |
| bool | [WriteUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a20745ddc468acf1a04fd9ab6039057a8.html#a20745ddc468acf1a04fd9ab6039057a8) (uint8\_t in\_value) |
|  | Writes an 8-bit unsigned integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a20745ddc468acf1a04fd9ab6039057a8.html#a20745ddc468acf1a04fd9ab6039057a8) |
|  | |
| bool | [WriteReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a3e62df4ee8fdbb1b3b65c64cd81aacf4.html#a3e62df4ee8fdbb1b3b65c64cd81aacf4) (double in\_value) |
|  | Writes a 64-bit, double-precision floating point value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a3e62df4ee8fdbb1b3b65c64cd81aacf4.html#a3e62df4ee8fdbb1b3b65c64cd81aacf4) |
|  | |
| bool | [WriteReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8d9b58e2ecba7f95721d4b89b7f9630f.html#a8d9b58e2ecba7f95721d4b89b7f9630f) (float in\_value) |
|  | Writes a 32-bit, single-precision floating point value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8d9b58e2ecba7f95721d4b89b7f9630f.html#a8d9b58e2ecba7f95721d4b89b7f9630f) |
|  | |
| bool | [WriteBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8f256236c51d1c4d9173b46952c74ca9.html#a8f256236c51d1c4d9173b46952c74ca9) (bool in\_value) |
|  | Writes a boolean value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8f256236c51d1c4d9173b46952c74ca9.html#a8f256236c51d1c4d9173b46952c74ca9) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostDataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Interface used to write data during sound bank generation.

|  |  |
| --- | --- |
|  | **备注:** All functions perform the appropriate platform-specific byte reordering, except where noted. |

参见
:   - [生成声音包](wwiseplugin_backend.html#wwiseplugin_bank)
    - AK::Wwise::Plugin::Plugin::GetBankParameters()

在文件 [HostDataWriter.h](_host_data_writer_8h_source.html) 第 [244](_host_data_writer_8h_source.html#l00244) 行定义.