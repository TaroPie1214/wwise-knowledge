# PropertySet

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html)
- [PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V2::PropertySet类 参考

Interface used to interact with property sets.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html#details)

`#include <HostPropertySet.h>`

类 AK.Wwise::Plugin::V2::PropertySet 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_aa12cd298737efd68e0e1cb20a852a2e3.html#aa12cd298737efd68e0e1cb20a852a2e3) = [CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_adadefb669a14a661a38960b441d2de02.html#adadefb669a14a661a38960b441d2de02) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a034f7a4639a0dafa880d6eee5f0b1708.html#a034f7a4639a0dafa880d6eee5f0b1708) = [CHostPropertySet::Instance](structak__wwise__plugin__host__property__set__v2_a91bf99c38eb6ac7299d9465390816171.html#a91bf99c38eb6ac7299d9465390816171) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::PropertySetBase< CHostPropertySet, 2 >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base.html) | |
| enum |  |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0877c249e51b5c527fee4a36f1a90902.html#a0877c249e51b5c527fee4a36f1a90902) |
|  | |
| enum |  |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a5dd47669a21a294e6a81a41f6f0ea67a.html#a5dd47669a21a294e6a81a41f6f0ea67a) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a1d1a2dac78243d98058e050a27384307.html#a1d1a2dac78243d98058e050a27384307) = [CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a977c67b76548703aa34a942c0afd0e58.html#a977c67b76548703aa34a942c0afd0e58) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostPropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostPropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a485c72db20c02ae9f16af1baca14bde4.html#a485c72db20c02ae9f16af1baca14bde4) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | [OpenBraces](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a639f4f509cdc7e21a55ee6e267628c1a.html#a639f4f509cdc7e21a55ee6e267628c1a) ([ak\_wwise\_plugin\_property\_set\_braces](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) in\_bracesToOpen) |
|  | Open one or more brace that denotes the start of a change [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a639f4f509cdc7e21a55ee6e267628c1a.html#a639f4f509cdc7e21a55ee6e267628c1a) |
|  | |
| void | [CloseBraces](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ac789793b55569eb816c76a18749d62d6.html#ac789793b55569eb816c76a18749d62d6) ([ak\_wwise\_plugin\_property\_set\_braces](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) in\_bracesToClose) |
|  | Close one or more brace that denotes the end of a change [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ac789793b55569eb816c76a18749d62d6.html#ac789793b55569eb816c76a18749d62d6) |
|  | |
| [ak\_wwise\_plugin\_property\_set\_braces](group__global_ga9e89de3693d568e58c5ef76bda84afbe.html#ga9e89de3693d568e58c5ef76bda84afbe) | [GetOpenedBraces](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a7ac9a5d0cd54d92fc65781dfc988d6d3.html#a7ac9a5d0cd54d92fc65781dfc988d6d3) () const |
|  | Retrieve the currently open braces [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a7ac9a5d0cd54d92fc65781dfc988d6d3.html#a7ac9a5d0cd54d92fc65781dfc988d6d3) |
|  | |
| bool | [GetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a4879a9fbf7e867f060630b0f8cb7743a.html#a4879a9fbf7e867f060630b0f8cb7743a) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, AK::WwiseAuthoringAPI::AkVariantBase &out\_varProperty) const |
|  | |
| bool | [GetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a4879a9fbf7e867f060630b0f8cb7743a.html#a4879a9fbf7e867f060630b0f8cb7743a) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, AK::WwiseAuthoringAPI::AkVariantBase &out\_varProperty) const |
|  | |
| bool | [SetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ac0382163b5d3fa6c5e351a6b87c0d774.html#ac0382163b5d3fa6c5e351a6b87c0d774) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, const AK::WwiseAuthoringAPI::AkVariantBase &in\_varProperty) |
|  | |
| bool | [HasPropertyValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_abdd8a2d040ee86583eb97226fada8345.html#abdd8a2d040ee86583eb97226fada8345) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| bool | [PropertyHasRTPC](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_acdf38fe0c2fdecf272e8c5e3fd720ad0.html#acdf38fe0c2fdecf272e8c5e3fd720ad0) (const char \*in\_pszPropertyName) const |
|  | |
| bool | [PropertyHasState](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a197f25fbbf713e298293e55a026896be.html#a197f25fbbf713e298293e55a026896be) (const char \*in\_pszPropertyName) const |
|  | |
| bool | [PropertyHasLinked](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a72b02662b0f939ad2937b51286f31111.html#a72b02662b0f939ad2937b51286f31111) (const char \*in\_pszPropertyName) const |
|  | |
| bool | [PropertyHasUnlinked](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a1a8f45296b57f8ae01df176ab6312904.html#a1a8f45296b57f8ae01df176ab6312904) (const char \*in\_pszPropertyName) const |
|  | |
| bool | [PropertyPlatformIsLinked](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a82c8cf7b94d848375580cee1a3db634d.html#a82c8cf7b94d848375580cee1a3db634d) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| const GUID \* | [GetID](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a7bc29d5d5342b761707a67cd2493964d.html#a7bc29d5d5342b761707a67cd2493964d) () const |
|  | |
| int | [GetType](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a9b8c8d355208cd2e3b61f64fa79a9de4.html#a9b8c8d355208cd2e3b61f64fa79a9de4) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| bool | [ClearValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a6f7d4cf5a6815be8b73cbf53f95fe2ad.html#a6f7d4cf5a6815be8b73cbf53f95fe2ad) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | |
| bool | [SetValueString](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ae7eec55a46f459d0c74088dd3a6f5c4e.html#ae7eec55a46f459d0c74088dd3a6f5c4e) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, const char \*in\_propertyValue) |
|  | |
| bool | [SetValueInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a8703218c34a5913e755237d66715052e.html#a8703218c34a5913e755237d66715052e) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int64\_t in\_propertyValue) |
|  | |
| bool | [SetValueInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a45d7955b5a8d477580ea0674786330af.html#a45d7955b5a8d477580ea0674786330af) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int32\_t in\_propertyValue) |
|  | |
| bool | [SetValueInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a450f132ad91e15a906b3074d7e3580da.html#a450f132ad91e15a906b3074d7e3580da) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int16\_t in\_propertyValue) |
|  | |
| bool | [SetValueInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ac7261e82b25f43585078344dfb4673b2.html#ac7261e82b25f43585078344dfb4673b2) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int8\_t in\_propertyValue) |
|  | |
| bool | [SetValueUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a60d23c93c53a1daf4a7ab83d970d2270.html#a60d23c93c53a1daf4a7ab83d970d2270) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint64\_t in\_propertyValue) |
|  | |
| bool | [SetValueUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_aad77d167b3aaaa1e70559163ff2ec00f.html#aad77d167b3aaaa1e70559163ff2ec00f) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint32\_t in\_propertyValue) |
|  | |
| bool | [SetValueUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a6863ed5619603c92dce4344a815271cf.html#a6863ed5619603c92dce4344a815271cf) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint16\_t in\_propertyValue) |
|  | |
| bool | [SetValueUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_afdded3e171e6750a1f410ca9bf022e02.html#afdded3e171e6750a1f410ca9bf022e02) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint8\_t in\_propertyValue) |
|  | |
| bool | [SetValueReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a7a1bd104264076046d011c60805d4f95.html#a7a1bd104264076046d011c60805d4f95) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, double in\_propertyValue) |
|  | |
| bool | [SetValueReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_af12543e9eb0552ee648b83d9c4c8a6c0.html#af12543e9eb0552ee648b83d9c4c8a6c0) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, float in\_propertyValue) |
|  | |
| bool | [SetValueBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a18d5c83201c617a41bc9c4dde3a77b62.html#a18d5c83201c617a41bc9c4dde3a77b62) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, bool in\_propertyValue) |
|  | |
| bool | [GetValueString](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_acfaa499af5dce6de2a1dde351267ba76.html#acfaa499af5dce6de2a1dde351267ba76) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, const char \*&out\_propertyValue) const |
|  | |
| bool | [GetValueInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a7ee3dfc436d14edaa53652b6a3ee8e94.html#a7ee3dfc436d14edaa53652b6a3ee8e94) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int64\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a4ff3190eaa2d57e78bf3fadde29d24d6.html#a4ff3190eaa2d57e78bf3fadde29d24d6) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int32\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a4b0b2452a3260c9a7bd7e1e1aa524eb4.html#a4b0b2452a3260c9a7bd7e1e1aa524eb4) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int16\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a75d2682ff3f7e3780f54c0f021335190.html#a75d2682ff3f7e3780f54c0f021335190) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int8\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_acc865979b00e89bea556af021bd0d26c.html#acc865979b00e89bea556af021bd0d26c) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint64\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a5108e0ff1875df20c0191edbabe72f9e.html#a5108e0ff1875df20c0191edbabe72f9e) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint32\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a76eaf020ecd307c610bd6f4ad86ff56b.html#a76eaf020ecd307c610bd6f4ad86ff56b) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint16\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a41bac3c08a395ff9482f6b25bfa20e37.html#a41bac3c08a395ff9482f6b25bfa20e37) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint8\_t &out\_propertyValue) const |
|  | |
| bool | [GetValueReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a4b8205b17171ce8eec061b4b6c99942a.html#a4b8205b17171ce8eec061b4b6c99942a) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, double &out\_propertyValue) const |
|  | |
| bool | [GetValueReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a69f6ec36d736519cc1bcb58a3773b7e1.html#a69f6ec36d736519cc1bcb58a3773b7e1) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, float &out\_propertyValue) const |
|  | |
| bool | [GetValueBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_acf6570c7cdbcee258eca45c523fa21c6.html#acf6570c7cdbcee258eca45c523fa21c6) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, bool &out\_propertyValue) const |
|  | |
| const char \* | [GetString](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a60012b10b49cde637e344b26d851f975.html#a60012b10b49cde637e344b26d851f975) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| int64\_t | [GetInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a64ef477c36768b47372b394a7b6231ad.html#a64ef477c36768b47372b394a7b6231ad) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| int32\_t | [GetInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a146d72ec556ebf75c91179b793dff00c.html#a146d72ec556ebf75c91179b793dff00c) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| int16\_t | [GetInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a6dbc03ddee27c6a5aeef8f7c89c1e3ce.html#a6dbc03ddee27c6a5aeef8f7c89c1e3ce) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| int8\_t | [GetInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a74e4cfe43c66d20aff0330ed87da7b8e.html#a74e4cfe43c66d20aff0330ed87da7b8e) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| uint64\_t | [GetUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a3b6f80d6ed56921d9a85ca51fc56b64c.html#a3b6f80d6ed56921d9a85ca51fc56b64c) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| uint32\_t | [GetUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a4b5845f13838734e0f4f45eb0635b08a.html#a4b5845f13838734e0f4f45eb0635b08a) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| uint16\_t | [GetUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ac9ff5cd17cfae220a1a2ee71f91c2c50.html#ac9ff5cd17cfae220a1a2ee71f91c2c50) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| uint8\_t | [GetUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_ab9e615c1bc4c454d37e8a22d9e91890a.html#ab9e615c1bc4c454d37e8a22d9e91890a) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| double | [GetReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a95ea7b497c6f07dd3a0d13901c800fad.html#a95ea7b497c6f07dd3a0d13901c800fad) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| float | [GetReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a78fe18ba20af4b3b8e087276ace4f780.html#a78fe18ba20af4b3b8e087276ace4f780) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| bool | [GetBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set_a2b98cbc5e293709ca27e6ffe8b98878b.html#a2b98cbc5e293709ca27e6ffe8b98878b) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::PropertySetBase< CHostPropertySet, 2 >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base.html) | |
| bool | [GetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a13a395f67a5cb50d0de259db2f7e68e9.html#a13a395f67a5cb50d0de259db2f7e68e9) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, AK::WwiseAuthoringAPI::AkVariantBase &out\_varProperty) const |
|  | Retrieves the value of a specific property as a variant. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a13a395f67a5cb50d0de259db2f7e68e9.html#a13a395f67a5cb50d0de259db2f7e68e9) |
|  | |
| bool | [SetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0ad377dfbc2d0fe2d76d25637a1da659.html#a0ad377dfbc2d0fe2d76d25637a1da659) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, const AK::WwiseAuthoringAPI::AkVariantBase &in\_varProperty) |
|  | Modifies the value of a specific property as a variant. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0ad377dfbc2d0fe2d76d25637a1da659.html#a0ad377dfbc2d0fe2d76d25637a1da659) |
|  | |
| bool | [HasPropertyValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ae7fd5d49114e1fba1057b495e0f7fe88.html#ae7fd5d49114e1fba1057b495e0f7fe88) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns true if the specified property exists. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ae7fd5d49114e1fba1057b495e0f7fe88.html#ae7fd5d49114e1fba1057b495e0f7fe88) |
|  | |
| bool | [PropertyHasRTPC](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a62e045af1c4842dd5605467a08a40df9.html#a62e045af1c4842dd5605467a08a40df9) (const char \*in\_pszPropertyName) const |
|  | Get the RTPC binding status for the specified property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a62e045af1c4842dd5605467a08a40df9.html#a62e045af1c4842dd5605467a08a40df9) |
|  | |
| bool | [PropertyHasState](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ad9fdb2385bdc900fee2169784b9e1d7b.html#ad9fdb2385bdc900fee2169784b9e1d7b) (const char \*in\_pszPropertyName) const |
|  | Returns whether the specified property is bound to a state object. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ad9fdb2385bdc900fee2169784b9e1d7b.html#ad9fdb2385bdc900fee2169784b9e1d7b) |
|  | |
| bool | [PropertyHasLinked](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a7702728ffc547dc3118eebea3f19c9aa.html#a7702728ffc547dc3118eebea3f19c9aa) (const char \*in\_pszPropertyName) const |
|  | Returns whether the specified property has at least some linked platforms. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a7702728ffc547dc3118eebea3f19c9aa.html#a7702728ffc547dc3118eebea3f19c9aa) |
|  | |
| bool | [PropertyHasUnlinked](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a4f69e73647e10164258e93c97732b533.html#a4f69e73647e10164258e93c97732b533) (const char \*in\_pszPropertyName) const |
|  | Returns whether the specified property has at least some platforms that are not linked. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a4f69e73647e10164258e93c97732b533.html#a4f69e73647e10164258e93c97732b533) |
|  | |
| bool | [PropertyPlatformIsLinked](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0e0c3b2069116d64494f8bc1d23aece3.html#a0e0c3b2069116d64494f8bc1d23aece3) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns whether the specified property's platform is linked. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0e0c3b2069116d64494f8bc1d23aece3.html#a0e0c3b2069116d64494f8bc1d23aece3) |
|  | |
| const GUID \* | [GetID](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a608360ae9a40884889f3e292b10d3dd3.html#a608360ae9a40884889f3e292b10d3dd3) () const |
|  | Returns the internal unique identifier of the corresponding object. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a608360ae9a40884889f3e292b10d3dd3.html#a608360ae9a40884889f3e292b10d3dd3) |
|  | |
| int | [GetType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab9eaf8ec88e6c2aa1514d3feee3ca131.html#ab9eaf8ec88e6c2aa1514d3feee3ca131) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Retrieves the type of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab9eaf8ec88e6c2aa1514d3feee3ca131.html#ab9eaf8ec88e6c2aa1514d3feee3ca131) |
|  | |
| bool | [ClearValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_abbf56eb0c0d3106311edce7d57389bd0.html#abbf56eb0c0d3106311edce7d57389bd0) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Resets a property value to its default. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_abbf56eb0c0d3106311edce7d57389bd0.html#abbf56eb0c0d3106311edce7d57389bd0) |
|  | |
| bool | [SetValueString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a743d61712d234117b288011deba14e76.html#a743d61712d234117b288011deba14e76) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, const char \*in\_propertyValue) |
|  | Modifies a property to a string value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a743d61712d234117b288011deba14e76.html#a743d61712d234117b288011deba14e76) |
|  | |
| bool | [SetValueInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a203736ad843f5814d25f1f92f54cf8b0.html#a203736ad843f5814d25f1f92f54cf8b0) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int64\_t in\_propertyValue) |
|  | Modifies a property to a 64-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a203736ad843f5814d25f1f92f54cf8b0.html#a203736ad843f5814d25f1f92f54cf8b0) |
|  | |
| bool | [SetValueInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab82c20c6927e03f83de2a0449b808b76.html#ab82c20c6927e03f83de2a0449b808b76) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int32\_t in\_propertyValue) |
|  | Modifies a property to a 32-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab82c20c6927e03f83de2a0449b808b76.html#ab82c20c6927e03f83de2a0449b808b76) |
|  | |
| bool | [SetValueInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_abd6ab8e1ece437a790279b5eccb14069.html#abd6ab8e1ece437a790279b5eccb14069) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int16\_t in\_propertyValue) |
|  | Modifies a property to a 16-bit signed integer value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_abd6ab8e1ece437a790279b5eccb14069.html#abd6ab8e1ece437a790279b5eccb14069) |
|  | |
| bool | [SetValueInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a15114bf05e110341e09c3b9f17d9d67f.html#a15114bf05e110341e09c3b9f17d9d67f) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int8\_t in\_propertyValue) |
|  | Modifies a property to an 8-bit signed integer value. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a15114bf05e110341e09c3b9f17d9d67f.html#a15114bf05e110341e09c3b9f17d9d67f) |
|  | |
| bool | [SetValueUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a18866903826ef76fc0f93fbf8aab0258.html#a18866903826ef76fc0f93fbf8aab0258) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint64\_t in\_propertyValue) |
|  | Modifies a property to a 64-bit unsigned integer value. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a18866903826ef76fc0f93fbf8aab0258.html#a18866903826ef76fc0f93fbf8aab0258) |
|  | |
| bool | [SetValueUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a96cf86cb46ecf2c8d6f9ce46bd2c6c8c.html#a96cf86cb46ecf2c8d6f9ce46bd2c6c8c) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint32\_t in\_propertyValue) |
|  | Modifies a property to a 32-bit unsigned integer value. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a96cf86cb46ecf2c8d6f9ce46bd2c6c8c.html#a96cf86cb46ecf2c8d6f9ce46bd2c6c8c) |
|  | |
| bool | [SetValueUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aaa10b4fabe6849e5aefd26fca9630f54.html#aaa10b4fabe6849e5aefd26fca9630f54) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint16\_t in\_propertyValue) |
|  | Modifies a property to a 16-bit unsigned integer value. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aaa10b4fabe6849e5aefd26fca9630f54.html#aaa10b4fabe6849e5aefd26fca9630f54) |
|  | |
| bool | [SetValueUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a477942a422e4b4f2279cdf51666c8a2e.html#a477942a422e4b4f2279cdf51666c8a2e) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint8\_t in\_propertyValue) |
|  | Modifies a property to an 8-bit unsigned integer value. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a477942a422e4b4f2279cdf51666c8a2e.html#a477942a422e4b4f2279cdf51666c8a2e) |
|  | |
| bool | [SetValueReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a494c92aa82960491c4cb7bda1d3ff3b9.html#a494c92aa82960491c4cb7bda1d3ff3b9) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, double in\_propertyValue) |
|  | Modifies a property to a 64-bit floating point value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a494c92aa82960491c4cb7bda1d3ff3b9.html#a494c92aa82960491c4cb7bda1d3ff3b9) |
|  | |
| bool | [SetValueReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a69924c090f1f6cd6e30b4487670662ce.html#a69924c090f1f6cd6e30b4487670662ce) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, float in\_propertyValue) |
|  | Modifies a property to a 32-bit floating point value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a69924c090f1f6cd6e30b4487670662ce.html#a69924c090f1f6cd6e30b4487670662ce) |
|  | |
| bool | [SetValueBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a3b2aefc388c05b6e4202816481312de6.html#a3b2aefc388c05b6e4202816481312de6) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, bool in\_propertyValue) |
|  | Modifies a property to a boolean value. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a3b2aefc388c05b6e4202816481312de6.html#a3b2aefc388c05b6e4202816481312de6) |
|  | |
| bool | [GetValueString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a9102df1be0eda0d5e4aee30517d8e2d8.html#a9102df1be0eda0d5e4aee30517d8e2d8) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, const char \*&out\_propertyValue) const |
|  | Retrieves the string value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a9102df1be0eda0d5e4aee30517d8e2d8.html#a9102df1be0eda0d5e4aee30517d8e2d8) |
|  | |
| bool | [GetValueInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab8881742aaa2b384b6d9b014503c9c9f.html#ab8881742aaa2b384b6d9b014503c9c9f) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int64\_t &out\_propertyValue) const |
|  | Retrieves the 64-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab8881742aaa2b384b6d9b014503c9c9f.html#ab8881742aaa2b384b6d9b014503c9c9f) |
|  | |
| bool | [GetValueInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0d580ae264aca798734f9966cf9bf917.html#a0d580ae264aca798734f9966cf9bf917) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int32\_t &out\_propertyValue) const |
|  | Retrieves the 32-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0d580ae264aca798734f9966cf9bf917.html#a0d580ae264aca798734f9966cf9bf917) |
|  | |
| bool | [GetValueInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a14cde5a5cf17ab0020ef598681f85c71.html#a14cde5a5cf17ab0020ef598681f85c71) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int16\_t &out\_propertyValue) const |
|  | Retrieves the 16-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a14cde5a5cf17ab0020ef598681f85c71.html#a14cde5a5cf17ab0020ef598681f85c71) |
|  | |
| bool | [GetValueInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a540e1afacc99a4d3c25c38a36e197d3f.html#a540e1afacc99a4d3c25c38a36e197d3f) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, int8\_t &out\_propertyValue) const |
|  | Retrieves the 8-bit signed integer value of a specific property. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a540e1afacc99a4d3c25c38a36e197d3f.html#a540e1afacc99a4d3c25c38a36e197d3f) |
|  | |
| bool | [GetValueUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab1df6f0e3917af006af844c2f9b7c86f.html#ab1df6f0e3917af006af844c2f9b7c86f) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint64\_t &out\_propertyValue) const |
|  | Retrieves the 64-bit unsigned integer value of a specific property. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ab1df6f0e3917af006af844c2f9b7c86f.html#ab1df6f0e3917af006af844c2f9b7c86f) |
|  | |
| bool | [GetValueUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aae6580a0bf76c04c2d058ae0df64a08c.html#aae6580a0bf76c04c2d058ae0df64a08c) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint32\_t &out\_propertyValue) const |
|  | Retrieves the 32-bit unsigned integer value of a specific property. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aae6580a0bf76c04c2d058ae0df64a08c.html#aae6580a0bf76c04c2d058ae0df64a08c) |
|  | |
| bool | [GetValueUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aba3916720afa5246ccfb87c29cfb2d31.html#aba3916720afa5246ccfb87c29cfb2d31) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint16\_t &out\_propertyValue) const |
|  | Retrieves the 16-bit unsigned integer value of a specific property. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aba3916720afa5246ccfb87c29cfb2d31.html#aba3916720afa5246ccfb87c29cfb2d31) |
|  | |
| bool | [GetValueUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a7a6980d96e24b9091fe236a9ebfc8f52.html#a7a6980d96e24b9091fe236a9ebfc8f52) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, uint8\_t &out\_propertyValue) const |
|  | Retrieves the 8-bit unsigned integer value of a specific property. (Future use) [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a7a6980d96e24b9091fe236a9ebfc8f52.html#a7a6980d96e24b9091fe236a9ebfc8f52) |
|  | |
| bool | [GetValueReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ad735ca1e90efe0f42e2d1191cdfd5e66.html#ad735ca1e90efe0f42e2d1191cdfd5e66) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, double &out\_propertyValue) const |
|  | Retrieves the 64-bit floating point value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ad735ca1e90efe0f42e2d1191cdfd5e66.html#ad735ca1e90efe0f42e2d1191cdfd5e66) |
|  | |
| bool | [GetValueReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0e52ad85a03ee9a133aeb48ca4679a5a.html#a0e52ad85a03ee9a133aeb48ca4679a5a) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, float &out\_propertyValue) const |
|  | Retrieves the 32-bit floating point value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a0e52ad85a03ee9a133aeb48ca4679a5a.html#a0e52ad85a03ee9a133aeb48ca4679a5a) |
|  | |
| bool | [GetValueBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a24a4fd6b5b0c259d731d2b6d10df38ed.html#a24a4fd6b5b0c259d731d2b6d10df38ed) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName, bool &out\_propertyValue) const |
|  | Retrieves the boolean value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a24a4fd6b5b0c259d731d2b6d10df38ed.html#a24a4fd6b5b0c259d731d2b6d10df38ed) |
|  | |
| const char \* | [GetString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a9b538d96158349c6b8b6909beea07a7d.html#a9b538d96158349c6b8b6909beea07a7d) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Retrieves the string value of a specific property and returns the value as a temporary pointer. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a9b538d96158349c6b8b6909beea07a7d.html#a9b538d96158349c6b8b6909beea07a7d) |
|  | |
| int64\_t | [GetInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a01141e329d211778ebb33374c1ea1004.html#a01141e329d211778ebb33374c1ea1004) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 64-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a01141e329d211778ebb33374c1ea1004.html#a01141e329d211778ebb33374c1ea1004) |
|  | |
| int32\_t | [GetInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a6afc2379f9c14b93d93ba9104f57c2e3.html#a6afc2379f9c14b93d93ba9104f57c2e3) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 32-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a6afc2379f9c14b93d93ba9104f57c2e3.html#a6afc2379f9c14b93d93ba9104f57c2e3) |
|  | |
| int16\_t | [GetInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a7c65df4ddaec4515200f811709ca8aba.html#a7c65df4ddaec4515200f811709ca8aba) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 16-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a7c65df4ddaec4515200f811709ca8aba.html#a7c65df4ddaec4515200f811709ca8aba) |
|  | |
| int8\_t | [GetInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ae250df4988f09fbd937e37aa5701cd60.html#ae250df4988f09fbd937e37aa5701cd60) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 8-bit signed integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_ae250df4988f09fbd937e37aa5701cd60.html#ae250df4988f09fbd937e37aa5701cd60) |
|  | |
| uint64\_t | [GetUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a1eabe588442726b006ac1434c1bf3add.html#a1eabe588442726b006ac1434c1bf3add) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 64-bit unsigned integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a1eabe588442726b006ac1434c1bf3add.html#a1eabe588442726b006ac1434c1bf3add) |
|  | |
| uint32\_t | [GetUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a20cb4532fb5c0672353620672c4b2d53.html#a20cb4532fb5c0672353620672c4b2d53) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 32-bit unsigned integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a20cb4532fb5c0672353620672c4b2d53.html#a20cb4532fb5c0672353620672c4b2d53) |
|  | |
| uint16\_t | [GetUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aa60b360321b6889b07a55c7ca1047cd2.html#aa60b360321b6889b07a55c7ca1047cd2) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 16-bit unsigned integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aa60b360321b6889b07a55c7ca1047cd2.html#aa60b360321b6889b07a55c7ca1047cd2) |
|  | |
| uint8\_t | [GetUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a4209073f988ee90cccefa5954022be9b.html#a4209073f988ee90cccefa5954022be9b) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 8-bit unsigned integer value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a4209073f988ee90cccefa5954022be9b.html#a4209073f988ee90cccefa5954022be9b) |
|  | |
| double | [GetReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a192bae4f9198dc173b984b2ddd2cb9ba.html#a192bae4f9198dc173b984b2ddd2cb9ba) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 64-bit floating point value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a192bae4f9198dc173b984b2ddd2cb9ba.html#a192bae4f9198dc173b984b2ddd2cb9ba) |
|  | |
| float | [GetReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a898b063a8a7d2e4a3a37495b6e8c467f.html#a898b063a8a7d2e4a3a37495b6e8c467f) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the 32-bit floating point value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_a898b063a8a7d2e4a3a37495b6e8c467f.html#a898b063a8a7d2e4a3a37495b6e8c467f) |
|  | |
| bool | [GetBool](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aeb62d8a62b678e42e7d3bd538c340a8b.html#aeb62d8a62b678e42e7d3bd538c340a8b) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) const |
|  | Returns the boolean value of a specific property. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_property_set_base_aeb62d8a62b678e42e7d3bd538c340a8b.html#aeb62d8a62b678e42e7d3bd538c340a8b) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostPropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

Interface used to interact with property sets.

A property set is a dictionary of properties, as stored inside a user's Authoring project. Whenever a property name is specified, it corresponds to the property name as set in the plug-in's XML definition file.

By default, Authoring will provide a property set, as defined in the XML definition file. It is possible to have more than one property set by requesting [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html "Custom inner property set interface."), and adding `InnerTypes` in the XML definition file.

This interface supports both the unique default property set, as well as Object Store's inner property sets.

You can also subscribe to notifications through [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) in order to be informed when some property set values changed.

The methods in this interface which use in\_guidPlatform as an input parameter assume that you have access to a Platform defined as a GUID, either provided by the caller function or retrieved through the [Host](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html "API to request host's current state and services.") interface.

You can retrieve GUIDs in the following ways:

- Use the in\_guidPlatform provided as an input parameter in [ak\_wwise\_plugin\_audio\_plugin\_v1::GetBankParameters](structak__wwise__plugin__audio__plugin__v1_abd584886ab95277158307efdf633af78.html#abd584886ab95277158307efdf633af78) or [ak\_wwise\_plugin\_custom\_data\_v1::GetPluginData](structak__wwise__plugin__custom__data__v1_ae2a50eda33df6c0c7da86b967751cf40.html#ae2a50eda33df6c0c7da86b967751cf40)
- Poll the currently-active platform from [ak\_wwise\_plugin\_host\_v1::GetCurrentPlatform](structak__wwise__plugin__host__v1_abb94fc626e520d00c4f77e9b8fab3adb.html#abb94fc626e520d00c4f77e9b8fab3adb) or [ak\_wwise\_plugin\_host\_v1::GetAuthoringPlaybackPlatform](structak__wwise__plugin__host__v1_a04c6938e999f9d1b3da2599155680e1f.html#a04c6938e999f9d1b3da2599155680e1f)

You can also provide GUID\_NULL as a parameter, which accesses data for all platforms at once as a linked value. However, GUID\_NULL only works when no platform-specific data is possible for a value. Using the current platform is always the preferred access method.

参见
:   - [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag)
    - [Property Set](plugin_backend_model.html#wwiseplugin_propertyset)
    - [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html)
    - [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html)

在文件 [HostPropertySet.h](_host_property_set_8h_source.html) 第 [91](_host_property_set_8h_source.html#l00091) 行定义.