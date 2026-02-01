# ak_wwise_plugin_host_property_set_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__property__set__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_property\_set\_v1结构体 参考

Interface used to interact with property sets.
[更多...](structak__wwise__plugin__host__property__set__v1.html#details)

`#include <HostPropertySet.h>`

类 ak\_wwise\_plugin\_host\_property\_set\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__property__set__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__property__set__v1_a2f6cdb9c74adbd3ac44b679501ce733d.html#a2f6cdb9c74adbd3ac44b679501ce733d) = [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_property\_set\_v1](structak__wwise__plugin__host__property__set__v1.html "Interface used to interact with property sets."). [更多...](structak__wwise__plugin__host__property__set__v1_a2f6cdb9c74adbd3ac44b679501ce733d.html#a2f6cdb9c74adbd3ac44b679501ce733d) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_property\_set\_v1](structak__wwise__plugin__host__property__set__v1_a6cad4333cb4d64f5b77255ac80fc567a.html#a6cad4333cb4d64f5b77255ac80fc567a) (int version=1) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_a7d1ff21fd409fc7363077edecb25a85d.html#a7d1ff21fd409fc7363077edecb25a85d) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_aef726120a06d869829ad6ec67df4f2a4.html#aef726120a06d869829ad6ec67df4f2a4) () |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_acefd1ca37e4c88b6c792ec43953d3f9c.html#acefd1ca37e4c88b6c792ec43953d3f9c) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| bool(\* | [GetValue](structak__wwise__plugin__host__property__set__v1_acfb82bcfc80b332df01011e138031369.html#acfb82bcfc80b332df01011e138031369) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, AK::WwiseAuthoringAPI::AkVariantBase \*out\_varProperty) |
|  | Retrieves the value of a specific property as a variant. [更多...](structak__wwise__plugin__host__property__set__v1_acfb82bcfc80b332df01011e138031369.html#acfb82bcfc80b332df01011e138031369) |
|  | |
| bool(\* | [SetValue](structak__wwise__plugin__host__property__set__v1_a60e99b3b9188b8ce6bc8ee36eefcd512.html#a60e99b3b9188b8ce6bc8ee36eefcd512) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, const AK::WwiseAuthoringAPI::AkVariantBase \*in\_varProperty) |
|  | Modifies the value of a specific property as a variant. [更多...](structak__wwise__plugin__host__property__set__v1_a60e99b3b9188b8ce6bc8ee36eefcd512.html#a60e99b3b9188b8ce6bc8ee36eefcd512) |
|  | |
| bool(\* | [HasPropertyValue](structak__wwise__plugin__host__property__set__v1_a00d84b9564f37e4a501530ae1c35768d.html#a00d84b9564f37e4a501530ae1c35768d) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Returns true if the specified property exists. [更多...](structak__wwise__plugin__host__property__set__v1_a00d84b9564f37e4a501530ae1c35768d.html#a00d84b9564f37e4a501530ae1c35768d) |
|  | |
| bool(\* | [PropertyHasRTPC](structak__wwise__plugin__host__property__set__v1_a96ce459681d9ab1b02d7e3420a53de72.html#a96ce459681d9ab1b02d7e3420a53de72) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const char \*in\_pszPropertyName) |
|  | Get the RTPC binding status for the specified property. [更多...](structak__wwise__plugin__host__property__set__v1_a96ce459681d9ab1b02d7e3420a53de72.html#a96ce459681d9ab1b02d7e3420a53de72) |
|  | |
| bool(\* | [PropertyHasState](structak__wwise__plugin__host__property__set__v1_ac0c0fc707f64352dcddedae0ef03279e.html#ac0c0fc707f64352dcddedae0ef03279e) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const char \*in\_pszPropertyName) |
|  | Returns whether the specified property is bound to a state object. [更多...](structak__wwise__plugin__host__property__set__v1_ac0c0fc707f64352dcddedae0ef03279e.html#ac0c0fc707f64352dcddedae0ef03279e) |
|  | |
| bool(\* | [PropertyHasLinked](structak__wwise__plugin__host__property__set__v1_ae0bd17081d27da7159b72513414936b8.html#ae0bd17081d27da7159b72513414936b8) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const char \*in\_pszPropertyName) |
|  | Returns whether the specified property has at least some linked platforms. [更多...](structak__wwise__plugin__host__property__set__v1_ae0bd17081d27da7159b72513414936b8.html#ae0bd17081d27da7159b72513414936b8) |
|  | |
| bool(\* | [PropertyHasUnlinked](structak__wwise__plugin__host__property__set__v1_ae431ee81d9a6753ee0e6827c4a501e26.html#ae431ee81d9a6753ee0e6827c4a501e26) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const char \*in\_pszPropertyName) |
|  | Returns whether the specified property has at least some platforms that are not linked. [更多...](structak__wwise__plugin__host__property__set__v1_ae431ee81d9a6753ee0e6827c4a501e26.html#ae431ee81d9a6753ee0e6827c4a501e26) |
|  | |
| bool(\* | [PropertyPlatformIsLinked](structak__wwise__plugin__host__property__set__v1_a5d976442f9e4012e95f9000bd43cffe3.html#a5d976442f9e4012e95f9000bd43cffe3) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Returns whether the specified property's platform is linked. [更多...](structak__wwise__plugin__host__property__set__v1_a5d976442f9e4012e95f9000bd43cffe3.html#a5d976442f9e4012e95f9000bd43cffe3) |
|  | |
| const GUID \*(\* | [GetID](structak__wwise__plugin__host__property__set__v1_ad9e7102701e0d946bbff02db3e9a7888.html#ad9e7102701e0d946bbff02db3e9a7888) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this) |
|  | Returns the internal unique identifier of the corresponding object. [更多...](structak__wwise__plugin__host__property__set__v1_ad9e7102701e0d946bbff02db3e9a7888.html#ad9e7102701e0d946bbff02db3e9a7888) |
|  | |
| int(\* | [GetType](structak__wwise__plugin__host__property__set__v1_ad8c9effa998d46fcfa94262f72b48aed.html#ad8c9effa998d46fcfa94262f72b48aed) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Retrieves the type of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_ad8c9effa998d46fcfa94262f72b48aed.html#ad8c9effa998d46fcfa94262f72b48aed) |
|  | |
| bool(\* | [ClearValue](structak__wwise__plugin__host__property__set__v1_ae8795b0c2c1d3312fa5cec2996344357.html#ae8795b0c2c1d3312fa5cec2996344357) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Resets a property value to its default. [更多...](structak__wwise__plugin__host__property__set__v1_ae8795b0c2c1d3312fa5cec2996344357.html#ae8795b0c2c1d3312fa5cec2996344357) |
|  | |
| bool(\* | [SetValueString](structak__wwise__plugin__host__property__set__v1_a78eb67c8602584f5e6ec646680174ba7.html#a78eb67c8602584f5e6ec646680174ba7) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, const char \*in\_propertyValue) |
|  | Modifies a property to a string value. [更多...](structak__wwise__plugin__host__property__set__v1_a78eb67c8602584f5e6ec646680174ba7.html#a78eb67c8602584f5e6ec646680174ba7) |
|  | |
| bool(\* | [SetValueInt64](structak__wwise__plugin__host__property__set__v1_ad18a24232a845daef70a83cb38fedb4b.html#ad18a24232a845daef70a83cb38fedb4b) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int64\_t in\_propertyValue) |
|  | Modifies a property to a 64-bit signed integer value. [更多...](structak__wwise__plugin__host__property__set__v1_ad18a24232a845daef70a83cb38fedb4b.html#ad18a24232a845daef70a83cb38fedb4b) |
|  | |
| bool(\* | [SetValueInt32](structak__wwise__plugin__host__property__set__v1_ac09e6f98b57648b290e499512435a49a.html#ac09e6f98b57648b290e499512435a49a) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int32\_t in\_propertyValue) |
|  | Modifies a property to a 32-bit signed integer value. [更多...](structak__wwise__plugin__host__property__set__v1_ac09e6f98b57648b290e499512435a49a.html#ac09e6f98b57648b290e499512435a49a) |
|  | |
| bool(\* | [SetValueInt16](structak__wwise__plugin__host__property__set__v1_ab4d2c80fbbbfb5cbd794d55d277f0513.html#ab4d2c80fbbbfb5cbd794d55d277f0513) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int16\_t in\_propertyValue) |
|  | Modifies a property to a 16-bit signed integer value. [更多...](structak__wwise__plugin__host__property__set__v1_ab4d2c80fbbbfb5cbd794d55d277f0513.html#ab4d2c80fbbbfb5cbd794d55d277f0513) |
|  | |
| bool(\* | [SetValueInt8](structak__wwise__plugin__host__property__set__v1_ad4f44c8c43896348186c7eff4fb9990b.html#ad4f44c8c43896348186c7eff4fb9990b) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int8\_t in\_propertyValue) |
|  | Modifies a property to an 8-bit signed integer value. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_ad4f44c8c43896348186c7eff4fb9990b.html#ad4f44c8c43896348186c7eff4fb9990b) |
|  | |
| bool(\* | [SetValueUInt64](structak__wwise__plugin__host__property__set__v1_ad1048c1838d50c13b0fa614141723f63.html#ad1048c1838d50c13b0fa614141723f63) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint64\_t in\_propertyValue) |
|  | Modifies a property to a 64-bit unsigned integer value. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_ad1048c1838d50c13b0fa614141723f63.html#ad1048c1838d50c13b0fa614141723f63) |
|  | |
| bool(\* | [SetValueUInt32](structak__wwise__plugin__host__property__set__v1_a900439c5544c44a480c502212fd38da9.html#a900439c5544c44a480c502212fd38da9) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint32\_t in\_propertyValue) |
|  | Modifies a property to a 32-bit unsigned integer value. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_a900439c5544c44a480c502212fd38da9.html#a900439c5544c44a480c502212fd38da9) |
|  | |
| bool(\* | [SetValueUInt16](structak__wwise__plugin__host__property__set__v1_aa4c288212d318eb6091c61664919963a.html#aa4c288212d318eb6091c61664919963a) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint16\_t in\_propertyValue) |
|  | Modifies a property to a 16-bit unsigned integer value. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_aa4c288212d318eb6091c61664919963a.html#aa4c288212d318eb6091c61664919963a) |
|  | |
| bool(\* | [SetValueUInt8](structak__wwise__plugin__host__property__set__v1_ab89d058f21d33ccb164a200f3e5ddc8b.html#ab89d058f21d33ccb164a200f3e5ddc8b) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint8\_t in\_propertyValue) |
|  | Modifies a property to an 8-bit unsigned integer value. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_ab89d058f21d33ccb164a200f3e5ddc8b.html#ab89d058f21d33ccb164a200f3e5ddc8b) |
|  | |
| bool(\* | [SetValueReal64](structak__wwise__plugin__host__property__set__v1_a80aacd19b827bd4db6462b8475c8fe5a.html#a80aacd19b827bd4db6462b8475c8fe5a) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, double in\_propertyValue) |
|  | Modifies a property to a 64-bit floating point value. [更多...](structak__wwise__plugin__host__property__set__v1_a80aacd19b827bd4db6462b8475c8fe5a.html#a80aacd19b827bd4db6462b8475c8fe5a) |
|  | |
| bool(\* | [SetValueReal32](structak__wwise__plugin__host__property__set__v1_a817c166c01f5e74e46734a852ce6e6d7.html#a817c166c01f5e74e46734a852ce6e6d7) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, float in\_propertyValue) |
|  | Modifies a property to a 32-bit floating point value. [更多...](structak__wwise__plugin__host__property__set__v1_a817c166c01f5e74e46734a852ce6e6d7.html#a817c166c01f5e74e46734a852ce6e6d7) |
|  | |
| bool(\* | [SetValueBool](structak__wwise__plugin__host__property__set__v1_aa71b03b97a9138a634f6acab60921397.html#aa71b03b97a9138a634f6acab60921397) )(struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, bool in\_propertyValue) |
|  | Modifies a property to a boolean value. [更多...](structak__wwise__plugin__host__property__set__v1_aa71b03b97a9138a634f6acab60921397.html#aa71b03b97a9138a634f6acab60921397) |
|  | |
| bool(\* | [GetValueString](structak__wwise__plugin__host__property__set__v1_a805f9eb4ac7e3b08037b89c39a9b6a2e.html#a805f9eb4ac7e3b08037b89c39a9b6a2e) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, const char \*\*out\_propertyValue) |
|  | Retrieves the string value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_a805f9eb4ac7e3b08037b89c39a9b6a2e.html#a805f9eb4ac7e3b08037b89c39a9b6a2e) |
|  | |
| bool(\* | [GetValueInt64](structak__wwise__plugin__host__property__set__v1_aba8f5b5ad9475e34281b9aa559681ab7.html#aba8f5b5ad9475e34281b9aa559681ab7) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int64\_t \*out\_propertyValue) |
|  | Retrieves the 64-bit signed integer value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_aba8f5b5ad9475e34281b9aa559681ab7.html#aba8f5b5ad9475e34281b9aa559681ab7) |
|  | |
| bool(\* | [GetValueInt32](structak__wwise__plugin__host__property__set__v1_aa648ef55a305d3732a52665245b54d23.html#aa648ef55a305d3732a52665245b54d23) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int32\_t \*out\_propertyValue) |
|  | Retrieves the 32-bit signed integer value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_aa648ef55a305d3732a52665245b54d23.html#aa648ef55a305d3732a52665245b54d23) |
|  | |
| bool(\* | [GetValueInt16](structak__wwise__plugin__host__property__set__v1_a9751c0a08feade52210099b5d2427a83.html#a9751c0a08feade52210099b5d2427a83) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int16\_t \*out\_propertyValue) |
|  | Retrieves the 16-bit signed integer value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_a9751c0a08feade52210099b5d2427a83.html#a9751c0a08feade52210099b5d2427a83) |
|  | |
| bool(\* | [GetValueInt8](structak__wwise__plugin__host__property__set__v1_a812a5ac93e2a3f44490c64288444fddf.html#a812a5ac93e2a3f44490c64288444fddf) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, int8\_t \*out\_propertyValue) |
|  | Retrieves the 8-bit signed integer value of a specific property. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_a812a5ac93e2a3f44490c64288444fddf.html#a812a5ac93e2a3f44490c64288444fddf) |
|  | |
| bool(\* | [GetValueUInt64](structak__wwise__plugin__host__property__set__v1_ab542f075c8072678238a13163f85e5c7.html#ab542f075c8072678238a13163f85e5c7) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint64\_t \*out\_propertyValue) |
|  | Retrieves the 64-bit unsigned integer value of a specific property. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_ab542f075c8072678238a13163f85e5c7.html#ab542f075c8072678238a13163f85e5c7) |
|  | |
| bool(\* | [GetValueUInt32](structak__wwise__plugin__host__property__set__v1_a6934cb4d7824fb9123df787b6b9cd8de.html#a6934cb4d7824fb9123df787b6b9cd8de) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint32\_t \*out\_propertyValue) |
|  | Retrieves the 32-bit unsigned integer value of a specific property. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_a6934cb4d7824fb9123df787b6b9cd8de.html#a6934cb4d7824fb9123df787b6b9cd8de) |
|  | |
| bool(\* | [GetValueUInt16](structak__wwise__plugin__host__property__set__v1_ad3ec70d6d895d55b92f0d9876d93caf8.html#ad3ec70d6d895d55b92f0d9876d93caf8) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint16\_t \*out\_propertyValue) |
|  | Retrieves the 16-bit unsigned integer value of a specific property. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_ad3ec70d6d895d55b92f0d9876d93caf8.html#ad3ec70d6d895d55b92f0d9876d93caf8) |
|  | |
| bool(\* | [GetValueUInt8](structak__wwise__plugin__host__property__set__v1_ad94c8319a4e880c211ec90792bd72dd5.html#ad94c8319a4e880c211ec90792bd72dd5) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, uint8\_t \*out\_propertyValue) |
|  | Retrieves the 8-bit unsigned integer value of a specific property. (Future use) [更多...](structak__wwise__plugin__host__property__set__v1_ad94c8319a4e880c211ec90792bd72dd5.html#ad94c8319a4e880c211ec90792bd72dd5) |
|  | |
| bool(\* | [GetValueReal64](structak__wwise__plugin__host__property__set__v1_adbba9a0947c1d93ff8eb05aaa575d2a6.html#adbba9a0947c1d93ff8eb05aaa575d2a6) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, double \*out\_propertyValue) |
|  | Retrieves the 64-bit floating point value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_adbba9a0947c1d93ff8eb05aaa575d2a6.html#adbba9a0947c1d93ff8eb05aaa575d2a6) |
|  | |
| bool(\* | [GetValueReal32](structak__wwise__plugin__host__property__set__v1_a909222ae906a73eb5b900b05843cc9bd.html#a909222ae906a73eb5b900b05843cc9bd) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, float \*out\_propertyValue) |
|  | Retrieves the 32-bit floating point value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_a909222ae906a73eb5b900b05843cc9bd.html#a909222ae906a73eb5b900b05843cc9bd) |
|  | |
| bool(\* | [GetValueBool](structak__wwise__plugin__host__property__set__v1_aaf501cb71349f937ca87787056620167.html#aaf501cb71349f937ca87787056620167) )(const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName, bool \*out\_propertyValue) |
|  | Retrieves the boolean value of a specific property. [更多...](structak__wwise__plugin__host__property__set__v1_aaf501cb71349f937ca87787056620167.html#aaf501cb71349f937ca87787056620167) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Interface used to interact with property sets.

A property set is a dictionary of properties, as stored inside a user's Authoring project. Whenever a property name is specified, it corresponds to the property name as set in the plug-in's XML definition file.

By default, Authoring will provide a property set, as defined in the XML definition file. It is possible to have more than one property set by requesting [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html "Custom inner property set interface."), and adding `InnerTypes` in the XML definition file.

This interface supports both the unique default property set, as well as Object Store's inner property sets.

You can also subscribe to notifications through [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html) in order to be informed when some property set values changed.

The methods in this interface which use in\_guidPlatform as an input parameter assume that you have access to a Platform defined as a GUID, either provided by the caller function or retrieved through the Host interface.

You can retrieve GUIDs in the following ways:

- Use the in\_guidPlatform provided as an input parameter in [ak\_wwise\_plugin\_audio\_plugin\_v1::GetBankParameters](structak__wwise__plugin__audio__plugin__v1_abd584886ab95277158307efdf633af78.html#abd584886ab95277158307efdf633af78) or [ak\_wwise\_plugin\_custom\_data\_v1::GetPluginData](structak__wwise__plugin__custom__data__v1_ae2a50eda33df6c0c7da86b967751cf40.html#ae2a50eda33df6c0c7da86b967751cf40)
- Poll the currently-active platform from [ak\_wwise\_plugin\_host\_v1::GetCurrentPlatform](structak__wwise__plugin__host__v1_abb94fc626e520d00c4f77e9b8fab3adb.html#abb94fc626e520d00c4f77e9b8fab3adb) or [ak\_wwise\_plugin\_host\_v1::GetAuthoringPlaybackPlatform](structak__wwise__plugin__host__v1_a04c6938e999f9d1b3da2599155680e1f.html#a04c6938e999f9d1b3da2599155680e1f)

You can also provide GUID\_NULL as a parameter, which accesses data for all platforms at once as a linked value. However, GUID\_NULL only works when no platform-specific data is possible for a value. Using the current platform is always the preferred access method.

参见
:   - [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag)
    - [Property Set](plugin_backend_model.html#wwiseplugin_propertyset)
    - [ak\_wwise\_plugin\_notifications\_property\_set\_v1](structak__wwise__plugin__notifications__property__set__v1.html)
    - [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html)

在文件 [HostPropertySet.h](_v1_2_host_property_set_8h_source.html) 第 [75](_v1_2_host_property_set_8h_source.html#l00075) 行定义.