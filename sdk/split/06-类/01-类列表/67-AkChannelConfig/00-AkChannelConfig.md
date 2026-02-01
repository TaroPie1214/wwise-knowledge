# AkChannelConfig

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_channel_config-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

AkChannelConfig结构体 参考

`#include <AkSpeakerConfig.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkChannelConfig](struct_ak_channel_config_affb931f09f5389d870ee26c20f56bba4.html#affb931f09f5389d870ee26c20f56bba4) () |
|  | Constructor. Clears / sets the channel config in "invalid" state ([IsValid()](struct_ak_channel_config_ab68295ed31a6156decb291ab7a6c07f3.html#ab68295ed31a6156decb291ab7a6c07f3 "Returns true if valid, false otherwise (as when it is constructed, or invalidated using Clear()).") returns false). [更多...](struct_ak_channel_config_affb931f09f5389d870ee26c20f56bba4.html#affb931f09f5389d870ee26c20f56bba4) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkChannelConfig](struct_ak_channel_config_a711b0912c0edb1d02132fd40a41aa8d8.html#a711b0912c0edb1d02132fd40a41aa8d8) (const [AkChannelConfig](struct_ak_channel_config.html) &rCopy) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkChannelConfig](struct_ak_channel_config_ac8430a418bc46084eb9567f2932d2348.html#ac8430a418bc46084eb9567f2932d2348) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelMask) |
|  | Constructor. Sets number of channels, and config type according to whether channel mask is defined or not. If defined, it must be consistent with the number of channels. [更多...](struct_ak_channel_config_ac8430a418bc46084eb9567f2932d2348.html#ac8430a418bc46084eb9567f2932d2348) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [operator!=](struct_ak_channel_config_ad561707700030c7c25ea91be32428dcb.html#ad561707700030c7c25ea91be32428dcb) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uBitField) |
|  | Operator != with a 32-bit word. [更多...](struct_ak_channel_config_ad561707700030c7c25ea91be32428dcb.html#ad561707700030c7c25ea91be32428dcb) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Clear](struct_ak_channel_config_a79d3e6e29649aabb9b9cd82bdd127d70.html#a79d3e6e29649aabb9b9cd82bdd127d70) () |
|  | Clear the channel config. Becomes "invalid" ([IsValid()](struct_ak_channel_config_ab68295ed31a6156decb291ab7a6c07f3.html#ab68295ed31a6156decb291ab7a6c07f3 "Returns true if valid, false otherwise (as when it is constructed, or invalidated using Clear()).") returns false). [更多...](struct_ak_channel_config_a79d3e6e29649aabb9b9cd82bdd127d70.html#a79d3e6e29649aabb9b9cd82bdd127d70) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelMask) |
|  | Set channel config as a standard configuration specified with given channel mask. [更多...](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetStandardOrAnonymous](struct_ak_channel_config_ae2ecde50aaf48e18a12cf1d8ce9cb881.html#ae2ecde50aaf48e18a12cf1d8ce9cb881) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelMask) |
|  | Set channel config as either a standard or an anonymous configuration, specified with both a given channel mask (0 if anonymous) and a number of channels (which must match the channel mask if standard). [更多...](struct_ak_channel_config_ae2ecde50aaf48e18a12cf1d8ce9cb881.html#ae2ecde50aaf48e18a12cf1d8ce9cb881) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetAnonymous](struct_ak_channel_config_ad01eb5a33d451da82346ea2f564e2218.html#ad01eb5a33d451da82346ea2f564e2218) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | Set channel config as an anonymous configuration specified with given number of channels. [更多...](struct_ak_channel_config_ad01eb5a33d451da82346ea2f564e2218.html#ad01eb5a33d451da82346ea2f564e2218) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetAmbisonic](struct_ak_channel_config_af284d807e5b3a18d25d629d307516e3f.html#af284d807e5b3a18d25d629d307516e3f) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | Set channel config as an ambisonic configuration specified with given number of channels. [更多...](struct_ak_channel_config_af284d807e5b3a18d25d629d307516e3f.html#af284d807e5b3a18d25d629d307516e3f) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetObject](struct_ak_channel_config_a8822cf194d89f4004e56e865a2ec61c0.html#a8822cf194d89f4004e56e865a2ec61c0) () |
|  | Set channel config as an object-based configuration (implies dynamic number of objects). [更多...](struct_ak_channel_config_a8822cf194d89f4004e56e865a2ec61c0.html#a8822cf194d89f4004e56e865a2ec61c0) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetSameAsMainMix](struct_ak_channel_config_ac9450f656af053116a5f12e061f27a62.html#ac9450f656af053116a5f12e061f27a62) () |
|  | Set channel config as the main mix channel configuration [更多...](struct_ak_channel_config_ac9450f656af053116a5f12e061f27a62.html#ac9450f656af053116a5f12e061f27a62) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetSameAsPassthrough](struct_ak_channel_config_a561db88b1004a317495e38258e6ac80a.html#a561db88b1004a317495e38258e6ac80a) () |
|  | Set channel config as the passthrough mix channel configuration [更多...](struct_ak_channel_config_a561db88b1004a317495e38258e6ac80a.html#a561db88b1004a317495e38258e6ac80a) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [IsValid](struct_ak_channel_config_ab68295ed31a6156decb291ab7a6c07f3.html#ab68295ed31a6156decb291ab7a6c07f3) () const |
|  | Returns true if valid, false otherwise (as when it is constructed, or invalidated using [Clear()](struct_ak_channel_config_a79d3e6e29649aabb9b9cd82bdd127d70.html#a79d3e6e29649aabb9b9cd82bdd127d70 "Clear the channel config. Becomes \"invalid\" (IsValid() returns false).")). [更多...](struct_ak_channel_config_ab68295ed31a6156decb291ab7a6c07f3.html#ab68295ed31a6156decb291ab7a6c07f3) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Serialize](struct_ak_channel_config_adfd0a8af9ca649feeed34dda727faf88.html#adfd0a8af9ca649feeed34dda727faf88) () const |
|  | Serialize channel config into a 32-bit word. [更多...](struct_ak_channel_config_adfd0a8af9ca649feeed34dda727faf88.html#adfd0a8af9ca649feeed34dda727faf88) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Deserialize](struct_ak_channel_config_ab5892ee08004394a8265068804a6b298.html#ab5892ee08004394a8265068804a6b298) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelConfig) |
|  | Deserialize channel config from a 32-bit word. [更多...](struct_ak_channel_config_ab5892ee08004394a8265068804a6b298.html#ab5892ee08004394a8265068804a6b298) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [RemoveLFE](struct_ak_channel_config_ab55c44b4ade2a0aca8ecaa4cc0b85426.html#ab55c44b4ade2a0aca8ecaa4cc0b85426) () const |
|  | Returns a new config based on 'this' with no LFE. [更多...](struct_ak_channel_config_ab55c44b4ade2a0aca8ecaa4cc0b85426.html#ab55c44b4ade2a0aca8ecaa4cc0b85426) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [RemoveCenter](struct_ak_channel_config_ab0971b5cf718f71e02122dd97a5d830a.html#ab0971b5cf718f71e02122dd97a5d830a) () const |
|  | Returns a new config based on 'this' with no Front Center channel. [更多...](struct_ak_channel_config_ab0971b5cf718f71e02122dd97a5d830a.html#ab0971b5cf718f71e02122dd97a5d830a) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [operator==](struct_ak_channel_config_af2b29fb3622a01473ab2e2f3aa605198.html#af2b29fb3622a01473ab2e2f3aa605198) (const [AkChannelConfig](struct_ak_channel_config.html) &in\_other) const |
|  | Operator == [更多...](struct_ak_channel_config_af2b29fb3622a01473ab2e2f3aa605198.html#af2b29fb3622a01473ab2e2f3aa605198) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [operator!=](struct_ak_channel_config_a033732a8babe01f701174d7689d3bbba.html#a033732a8babe01f701174d7689d3bbba) (const [AkChannelConfig](struct_ak_channel_config.html) &in\_other) const |
|  | Operator != [更多...](struct_ak_channel_config_a033732a8babe01f701174d7689d3bbba.html#a033732a8babe01f701174d7689d3bbba) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [HasLFE](struct_ak_channel_config_ae3cde5ab0c6d93f5ab6dc5445b991dd1.html#ae3cde5ab0c6d93f5ab6dc5445b991dd1) () const |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [HasCenter](struct_ak_channel_config_a8f6f92b93a6a3a3ed13d23ca746153e3.html#a8f6f92b93a6a3a3ed13d23ca746153e3) () const |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [Standard](struct_ak_channel_config_ac4b9efc271077943315791ce5fbb7b59.html#ac4b9efc271077943315791ce5fbb7b59) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uChannelMask) |
|  | Construct standard channel config from channel mask [更多...](struct_ak_channel_config_ac4b9efc271077943315791ce5fbb7b59.html#ac4b9efc271077943315791ce5fbb7b59) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [Anonymous](struct_ak_channel_config_a85063c6f4b594fd120e0c1d62cc35d26.html#a85063c6f4b594fd120e0c1d62cc35d26) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [Ambisonic](struct_ak_channel_config_a3a621efb948ec9458960841113b89d43.html#a3a621efb948ec9458960841113b89d43) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumChannels) |
|  | Construct ambisonic channel config from number of channels (NOT order) [更多...](struct_ak_channel_config_a3a621efb948ec9458960841113b89d43.html#a3a621efb948ec9458960841113b89d43) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelConfig](struct_ak_channel_config.html) | [Object](struct_ak_channel_config_a3e02da9f60c4279c3d50278df94ef1b4.html#a3e02da9f60c4279c3d50278df94ef1b4) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| union { |
| struct { |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)   [uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc): 8 |
|  | Number of channels. [更多...](struct_ak_channel_config_1_1_0d0_1_1_0d2_a8ebd5e942b2bc4d1b49480db614a0ee7.html#a8ebd5e942b2bc4d1b49480db614a0ee7) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)   [eConfigType](struct_ak_channel_config_a598c4a4489e9fb252e7022ae99135674.html#a598c4a4489e9fb252e7022ae99135674): 4 |
|  | Channel config type (AkChannelConfigType). [更多...](struct_ak_channel_config_1_1_0d0_1_1_0d2_aacfeabf1ecdff116477e078d9140677e.html#aacfeabf1ecdff116477e078d9140677e) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)   [uChannelMask](struct_ak_channel_config_a8fc646976d669b0b0bdf81371c2a2f76.html#a8fc646976d669b0b0bdf81371c2a2f76): 20 |
|  | Channel mask (configuration). [更多...](struct_ak_channel_config_1_1_0d0_1_1_0d2_a12219a02d857593bee019164f0820b58.html#a12219a02d857593bee019164f0820b58) |
|  | |
| } |  |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)   [uFullCfg](struct_ak_channel_config_af2ef29d52224a86d414db89604187b4f.html#af2ef29d52224a86d414db89604187b4f) |
|  | |
| }; |  |
|  | |

## 详细描述

Defines a channel configuration. Examples:

[AkChannelConfig](struct_ak_channel_config.html) cfg;

// Create a stereo configuration.

cfg.[SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)([AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894));

// Create a 7.1.4 configuration (7.1 plus 4 height channels).

cfg.[SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)([AK\_SPEAKER\_SETUP\_AURO\_11POINT1\_740](_ak_speaker_config_8h_ac3f7045b044654e66ea4e6a7cb181c30.html#ac3f7045b044654e66ea4e6a7cb181c30));

// or

cfg.[SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)([AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0));

// Create a 3rd order ambisonic configuration.

cfg.[SetAmbisonic](struct_ak_channel_config_af284d807e5b3a18d25d629d307516e3f.html#af284d807e5b3a18d25d629d307516e3f)(16); // pass in the number of spherical harmonics, (N+1)^2, where N is the ambisonics order.

// Invalidate (usually means "As Parent")

cfg.[Clear](struct_ak_channel_config_a79d3e6e29649aabb9b9cd82bdd127d70.html#a79d3e6e29649aabb9b9cd82bdd127d70)();

在文件 [AkSpeakerConfig.h](_ak_speaker_config_8h_source.html) 第 [435](_ak_speaker_config_8h_source.html#l00435) 行定义.

[AkChannelConfig](struct_ak_channel_config.html)

**Definition:** [AkSpeakerConfig.h:436](_ak_speaker_config_8h_source.html#l00435)

[AkChannelConfig::SetAmbisonic](struct_ak_channel_config_af284d807e5b3a18d25d629d307516e3f.html#af284d807e5b3a18d25d629d307516e3f)

AkForceInline void SetAmbisonic(AkUInt32 in\_uNumChannels)

Set channel config as an ambisonic configuration specified with given number of channels.

**Definition:** [AkSpeakerConfig.h:538](_ak_speaker_config_8h_source.html#l00538)

[AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0)

#define AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4

Dolby 7.1.4 setup channel mask

**Definition:** [AkSpeakerConfig.h:113](_ak_speaker_config_8h_source.html#l00113)

[AkChannelConfig::Clear](struct_ak_channel_config_a79d3e6e29649aabb9b9cd82bdd127d70.html#a79d3e6e29649aabb9b9cd82bdd127d70)

AkForceInline void Clear()

Clear the channel config. Becomes "invalid" (IsValid() returns false).

**Definition:** [AkSpeakerConfig.h:505](_ak_speaker_config_8h_source.html#l00505)

[AK\_SPEAKER\_SETUP\_AURO\_11POINT1\_740](_ak_speaker_config_8h_ac3f7045b044654e66ea4e6a7cb181c30.html#ac3f7045b044654e66ea4e6a7cb181c30)

#define AK\_SPEAKER\_SETUP\_AURO\_11POINT1\_740

Auro-11.1 (7+4) setup channel mask (7.1.4)

**Definition:** [AkSpeakerConfig.h:97](_ak_speaker_config_8h_source.html#l00097)

[AkChannelConfig::SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)

AkForceInline void SetStandard(AkUInt32 in\_uChannelMask)

Set channel config as a standard configuration specified with given channel mask.

**Definition:** [AkSpeakerConfig.h:511](_ak_speaker_config_8h_source.html#l00511)

[AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894)

#define AK\_SPEAKER\_SETUP\_STEREO

2.0 setup channel mask

**Definition:** [AkSpeakerConfig.h:66](_ak_speaker_config_8h_source.html#l00066)