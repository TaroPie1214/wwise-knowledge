# AkBehavioralPositioningData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_behavioral_positioning_data-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkBehavioralPositioningData结构体 参考

Positioning data inherited from sound structures and mix busses.
[更多...](struct_ak_behavioral_positioning_data.html#details)

`#include <AkCommonDefs.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkBehavioralPositioningData](struct_ak_behavioral_positioning_data_ad3827d4b10856d8baf250bf14c1e9546.html#ad3827d4b10856d8baf250bf14c1e9546) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [center](struct_ak_behavioral_positioning_data_a20342d48002d5f00ea6f484d196d52f1.html#a20342d48002d5f00ea6f484d196d52f1) |
|  | Center percentage [0,1] [更多...](struct_ak_behavioral_positioning_data_a20342d48002d5f00ea6f484d196d52f1.html#a20342d48002d5f00ea6f484d196d52f1) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [panLR](struct_ak_behavioral_positioning_data_ae7b760df50ad31c2402081b8003eb8ce.html#ae7b760df50ad31c2402081b8003eb8ce) |
|  | Pan left-right [-1,1] [更多...](struct_ak_behavioral_positioning_data_ae7b760df50ad31c2402081b8003eb8ce.html#ae7b760df50ad31c2402081b8003eb8ce) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [panBF](struct_ak_behavioral_positioning_data_a90a8e2f2ed884ebc89b596b6be88387b.html#a90a8e2f2ed884ebc89b596b6be88387b) |
|  | Pan back-front [-1,1] [更多...](struct_ak_behavioral_positioning_data_a90a8e2f2ed884ebc89b596b6be88387b.html#a90a8e2f2ed884ebc89b596b6be88387b) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [panDU](struct_ak_behavioral_positioning_data_a78d587528f6aef49fde677b581ba513d.html#a78d587528f6aef49fde677b581ba513d) |
|  | Pan down-up [-1,1] [更多...](struct_ak_behavioral_positioning_data_a78d587528f6aef49fde677b581ba513d.html#a78d587528f6aef49fde677b581ba513d) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [panSpatMix](struct_ak_behavioral_positioning_data_a0f9dd890531840a4fca32a521c8f8d4a.html#a0f9dd890531840a4fca32a521c8f8d4a) |
|  | Panning vs 3D spatialization mix ([0,1], 1 being 100% spatialized). [更多...](struct_ak_behavioral_positioning_data_a0f9dd890531840a4fca32a521c8f8d4a.html#a0f9dd890531840a4fca32a521c8f8d4a) |
|  | |
| [Ak3DSpatializationMode](_ak_enums_8h_a2091df555ad6110b01ce6905325a3a14.html#a2091df555ad6110b01ce6905325a3a14) | [spatMode](struct_ak_behavioral_positioning_data_a135aef56c3da0d202058e13af30ff950.html#a135aef56c3da0d202058e13af30ff950) |
|  | 3D spatialization mode. [更多...](struct_ak_behavioral_positioning_data_a135aef56c3da0d202058e13af30ff950.html#a135aef56c3da0d202058e13af30ff950) |
|  | |
| [AkSpeakerPanningType](_ak_enums_8h_a229e1503503cb92fbca8a437196b283f.html#a229e1503503cb92fbca8a437196b283f) | [panType](struct_ak_behavioral_positioning_data_a25d7fcf642c76a8b16becbfe723ae3c1.html#a25d7fcf642c76a8b16becbfe723ae3c1) |
|  | Speaker panning type. [更多...](struct_ak_behavioral_positioning_data_a25d7fcf642c76a8b16becbfe723ae3c1.html#a25d7fcf642c76a8b16becbfe723ae3c1) |
|  | |
| bool | [enableHeightSpread](struct_ak_behavioral_positioning_data_adc1441b1252511352564a41769392244.html#adc1441b1252511352564a41769392244) |
|  | When true, audio objects 3D spatialized onto a planar channel configuration will be given a minimum spread value based on their elevation angle, equal to sin(elevation)\*\*2. [更多...](struct_ak_behavioral_positioning_data_adc1441b1252511352564a41769392244.html#adc1441b1252511352564a41769392244) |
|  | |

## 详细描述

Positioning data inherited from sound structures and mix busses.

在文件 [AkCommonDefs.h](_ak_common_defs_8h_source.html) 第 [253](_ak_common_defs_8h_source.html#l00253) 行定义.