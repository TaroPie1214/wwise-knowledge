# IReadWriteProperties

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [IReadWriteProperties](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::IReadWriteProperties类 参考abstract

`#include <PluginDef.h>`

类 AK.Wwise::Plugin::IReadWriteProperties 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual bool | [SetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a009c0da2bbe3490229ffe50c7d5f4935.html#a009c0da2bbe3490229ffe50c7d5f4935) (const char \*in\_szPropertyName, const AK::WwiseAuthoringAPI::AkVariantBase &in\_rValue)=0 |
|  | |
| virtual bool | [ClearValue](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_aacb4cf9ee20e85cf8fc808ed190b8b7f.html#aacb4cf9ee20e85cf8fc808ed190b8b7f) (const char \*in\_pszPropertyName)=0 |
|  | |
| virtual bool | [SetValueString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a83499bc66d4c9d2469c9ed5f8c7d8754.html#a83499bc66d4c9d2469c9ed5f8c7d8754) (const char \*in\_pszPropertyName, const char \*in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a6ddfd2fdf3361f1e8102e0489842dcaa.html#a6ddfd2fdf3361f1e8102e0489842dcaa) (const char \*in\_pszPropertyName, int64\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_af703743ff9b9ca7d2e4f95a242c0fc74.html#af703743ff9b9ca7d2e4f95a242c0fc74) (const char \*in\_pszPropertyName, int32\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a97d6bdd2e99c260728436e50cc55b603.html#a97d6bdd2e99c260728436e50cc55b603) (const char \*in\_pszPropertyName, int16\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a2bf9f251e16707e6270125cf36a3d5fa.html#a2bf9f251e16707e6270125cf36a3d5fa) (const char \*in\_pszPropertyName, int8\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a6b0846e9a37afff28a12720931dfa093.html#a6b0846e9a37afff28a12720931dfa093) (const char \*in\_pszPropertyName, uint64\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a2a74eaf5e6a93b64d66761720c0af78e.html#a2a74eaf5e6a93b64d66761720c0af78e) (const char \*in\_pszPropertyName, uint32\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a32b3e0cbf1bef14db4c1b475c3374d61.html#a32b3e0cbf1bef14db4c1b475c3374d61) (const char \*in\_pszPropertyName, uint16\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a8d805e15ae052141d99780fe1724e3c5.html#a8d805e15ae052141d99780fe1724e3c5) (const char \*in\_pszPropertyName, uint8\_t in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_a125534bb41b99fdc5f61a1a645be7141.html#a125534bb41b99fdc5f61a1a645be7141) (const char \*in\_pszPropertyName, double in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_ae07c1c9ffb26e5ff9b0376d48420334e.html#ae07c1c9ffb26e5ff9b0376d48420334e) (const char \*in\_pszPropertyName, float in\_varProperty)=0 |
|  | |
| virtual bool | [SetValueBool](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_write_properties_afd1fed6dbe9e88acd59ad7d461a2b643.html#afd1fed6dbe9e88acd59ad7d461a2b643) (const char \*in\_pszPropertyName, bool in\_varProperty)=0 |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::IReadOnlyProperties](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties.html) | |
| virtual bool | [GetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a88cb09b1625f2ed114aebeb76ae6d5ad.html#a88cb09b1625f2ed114aebeb76ae6d5ad) (const char \*in\_szPropertyName, AK::WwiseAuthoringAPI::AkVariantBase &out\_rValue) const =0 |
|  | |
| virtual int | [GetType](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_aef8e984e56afe68c37a1341ac0f03f49.html#aef8e984e56afe68c37a1341ac0f03f49) (const char \*in\_pszPropertyName) const =0 |
|  | |
| virtual bool | [GetValueString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a257b65af5f5b5494dd948b4701bcfe00.html#a257b65af5f5b5494dd948b4701bcfe00) (const char \*in\_pszPropertyName, const char \*&out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a8eb744a50403c3fe28b16166e0c03463.html#a8eb744a50403c3fe28b16166e0c03463) (const char \*in\_pszPropertyName, int64\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a56bf8e310ff26023b1a09f480fbfdc60.html#a56bf8e310ff26023b1a09f480fbfdc60) (const char \*in\_pszPropertyName, int32\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a778584425bd06e790b61a088361b4798.html#a778584425bd06e790b61a088361b4798) (const char \*in\_pszPropertyName, int16\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a19a06e5b177af0728c2946aeba312be0.html#a19a06e5b177af0728c2946aeba312be0) (const char \*in\_pszPropertyName, int8\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a46c9794fd168c7f4dadbfda07b885dfd.html#a46c9794fd168c7f4dadbfda07b885dfd) (const char \*in\_pszPropertyName, uint64\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a3e64e781dd2c78acc6f979ffdd097bde.html#a3e64e781dd2c78acc6f979ffdd097bde) (const char \*in\_pszPropertyName, uint32\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a6bce3af88d1a727f8cb98be76427bc8b.html#a6bce3af88d1a727f8cb98be76427bc8b) (const char \*in\_pszPropertyName, uint16\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_ada67d6103ca7f5ad2d3533139e669002.html#ada67d6103ca7f5ad2d3533139e669002) (const char \*in\_pszPropertyName, uint8\_t &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a2a47ae65777ba975ba58d759224c30d9.html#a2a47ae65777ba975ba58d759224c30d9) (const char \*in\_pszPropertyName, double &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a937defc5333747c636a1ad71c20a4cca.html#a937defc5333747c636a1ad71c20a4cca) (const char \*in\_pszPropertyName, float &out\_varProperty) const =0 |
|  | |
| virtual bool | [GetValueBool](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_abba03a3c5550e7e1981113f3bfeb4063.html#abba03a3c5550e7e1981113f3bfeb4063) (const char \*in\_pszPropertyName, bool &out\_varProperty) const =0 |
|  | |
| const char \* | [GetString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a0229f190f47c27cef9083f06b3d3f265.html#a0229f190f47c27cef9083f06b3d3f265) (const char \*in\_pszPropertyName) const |
|  | |
| int64\_t | [GetInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_ab6238d3748c3b02580abcefd6794f9be.html#ab6238d3748c3b02580abcefd6794f9be) (const char \*in\_pszPropertyName) const |
|  | |
| int32\_t | [GetInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a5e7056560e52e1d4be3265d986b98f3b.html#a5e7056560e52e1d4be3265d986b98f3b) (const char \*in\_pszPropertyName) const |
|  | |
| int16\_t | [GetInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a0ffc024efb076cc367df3112ba62c9f9.html#a0ffc024efb076cc367df3112ba62c9f9) (const char \*in\_pszPropertyName) const |
|  | |
| int8\_t | [GetInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_af5fb9266315e25ea66a2ecc20df01439.html#af5fb9266315e25ea66a2ecc20df01439) (const char \*in\_pszPropertyName) const |
|  | |
| uint64\_t | [GetUInt64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_ae5e4a95220f8f65694606ab51431a2fb.html#ae5e4a95220f8f65694606ab51431a2fb) (const char \*in\_pszPropertyName) const |
|  | |
| uint32\_t | [GetUInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a44d0f1b84219bef18a59f72d55dd480d.html#a44d0f1b84219bef18a59f72d55dd480d) (const char \*in\_pszPropertyName) const |
|  | |
| uint16\_t | [GetUInt16](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a153253c7abc9dd160fe52600e715dd5e.html#a153253c7abc9dd160fe52600e715dd5e) (const char \*in\_pszPropertyName) const |
|  | |
| uint8\_t | [GetUInt8](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_afe428b5ff11b40d75e61c6dcfaad2a87.html#afe428b5ff11b40d75e61c6dcfaad2a87) (const char \*in\_pszPropertyName) const |
|  | |
| double | [GetReal64](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_ac51e609f924d2c3c317a2fdbdb0a2895.html#ac51e609f924d2c3c317a2fdbdb0a2895) (const char \*in\_pszPropertyName) const |
|  | |
| float | [GetReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a3f9427bc6d7b1bbed37703db8a44bdf1.html#a3f9427bc6d7b1bbed37703db8a44bdf1) (const char \*in\_pszPropertyName) const |
|  | |
| bool | [GetBool](class_a_k_1_1_wwise_1_1_plugin_1_1_i_read_only_properties_a9c1dd5a64011855fb1952deefe4bfd7a.html#a9c1dd5a64011855fb1952deefe4bfd7a) (const char \*in\_pszPropertyName) const |
|  | |

## 详细描述

在文件 [PluginDef.h](_plugin_def_8h_source.html) 第 [365](_plugin_def_8h_source.html#l00365) 行定义.