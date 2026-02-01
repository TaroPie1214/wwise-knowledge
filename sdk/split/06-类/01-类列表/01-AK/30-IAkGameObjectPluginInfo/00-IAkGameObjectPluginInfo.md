# IAkGameObjectPluginInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info.html)

[所有成员列表](class_a_k_1_1_i_ak_game_object_plugin_info-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkGameObjectPluginInfo类 参考abstract

Game object information available to plugins.
[更多...](class_a_k_1_1_i_ak_game_object_plugin_info.html#details)

`#include <IAkPlugin.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [GetGameObjectID](class_a_k_1_1_i_ak_game_object_plugin_info_ab9b76e3cbf8360809ad559b88498a940.html#ab9b76e3cbf8360809ad559b88498a940) () const =0 |
|  | Get the ID of the game object. [更多...](class_a_k_1_1_i_ak_game_object_plugin_info_ab9b76e3cbf8360809ad559b88498a940.html#ab9b76e3cbf8360809ad559b88498a940) |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNumEmitterListenerPairs](class_a_k_1_1_i_ak_game_object_plugin_info_ac7354b04e29343e78471c320bd85d48e.html#ac7354b04e29343e78471c320bd85d48e) () const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetEmitterListenerPair](class_a_k_1_1_i_ak_game_object_plugin_info_ac64ca233a93939f8d7d41f83a2ff8c27.html#ac64ca233a93939f8d7d41f83a2ff8c27) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uIndex, [AkEmitterListenerPair](class_ak_emitter_listener_pair.html) &out\_emitterListenerPair) const =0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetNumGameObjectPositions](class_a_k_1_1_i_ak_game_object_plugin_info_aadc5129ad1faf81790983f8d96b911fc.html#aadc5129ad1faf81790983f8d96b911fc) () const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetGameObjectPosition](class_a_k_1_1_i_ak_game_object_plugin_info_ac1962ffbbe7276ea6aaf88ee36c78996.html#ac1962ffbbe7276ea6aaf88ee36c78996) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uIndex, AkSoundPosition &out\_position) const =0 |
|  | |
| virtual [AkMultiPositionType](_ak_enums_8h_a751ba836dfd5edf52ceaab00cf74b6c1.html#a751ba836dfd5edf52ceaab00cf74b6c1) | [GetGameObjectMultiPositionType](class_a_k_1_1_i_ak_game_object_plugin_info_ae092b578bda8611d0fcb93ee7243dc70.html#ae092b578bda8611d0fcb93ee7243dc70) () const =0 |
|  | |
| virtual [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetGameObjectScaling](class_a_k_1_1_i_ak_game_object_plugin_info_ac50bfec9bb48a7ec7187cfb250591635.html#ac50bfec9bb48a7ec7187cfb250591635) () const =0 |
|  | |
| virtual bool | [GetListeners](class_a_k_1_1_i_ak_game_object_plugin_info_a4000e34b25c85c81dca34543072193b8.html#a4000e34b25c85c81dca34543072193b8) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) \*out\_aListenerIDs, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uSize) const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetListenerData](class_a_k_1_1_i_ak_game_object_plugin_info_ac6d05467e017f0334df784289a045ddf.html#ac6d05467e017f0334df784289a045ddf) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_uListener, [AkListener](struct_ak_listener.html) &out\_listener) const =0 |
|  | |
| virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [GetDistanceProbe](class_a_k_1_1_i_ak_game_object_plugin_info_ad0e5372b07eea66fd0d015ccf026dc6d.html#ad0e5372b07eea66fd0d015ccf026dc6d) ([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_uListener, [AkWorldTransform](struct_ak_world_transform.html) &out\_position) const =0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info_af907b08cfbb00730b4599668ad3ec23d.html#af907b08cfbb00730b4599668ad3ec23d) () |
|  | Virtual destructor on interface to avoid warnings. [更多...](class_a_k_1_1_i_ak_game_object_plugin_info_af907b08cfbb00730b4599668ad3ec23d.html#af907b08cfbb00730b4599668ad3ec23d) |
|  | |

## 详细描述

Game object information available to plugins.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [104](_i_ak_plugin_8h_source.html#l00104) 行定义.