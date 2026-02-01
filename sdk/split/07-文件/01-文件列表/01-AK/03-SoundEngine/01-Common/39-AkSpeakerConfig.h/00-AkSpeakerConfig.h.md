# AkSpeakerConfig.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[枚举](#enum-members) |
[函数](#func-members)

AkSpeakerConfig.h 文件参考

`#include <AK/SoundEngine/Common/AkNumeralTypes.h>`  
`#include <AK/SoundEngine/Common/AkTypedefs.h>`  
`#include <AK/SoundEngine/Common/AkEnums.h>`  
`#include <AK/Tools/Common/AkBitFuncs.h>`

[浏览源代码.](_ak_speaker_config_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkChannelConfig](struct_ak_channel_config.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_SPEAKER\_FRONT\_LEFT](_ak_speaker_config_8h_aa9dc5afd59709444ca24c974c54b08b3.html#aa9dc5afd59709444ca24c974c54b08b3)   0x1 |
|  | Standard speakers (channel mask): [更多...](_ak_speaker_config_8h_aa9dc5afd59709444ca24c974c54b08b3.html#aa9dc5afd59709444ca24c974c54b08b3) |
|  | |
| #define | [AK\_SPEAKER\_FRONT\_RIGHT](_ak_speaker_config_8h_a2bf48d2a4c5235e0d5a42d1caa7edd16.html#a2bf48d2a4c5235e0d5a42d1caa7edd16)   0x2 |
|  | Front right speaker bit mask [更多...](_ak_speaker_config_8h_a2bf48d2a4c5235e0d5a42d1caa7edd16.html#a2bf48d2a4c5235e0d5a42d1caa7edd16) |
|  | |
| #define | [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906)   0x4 |
|  | Front center speaker bit mask [更多...](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906) |
|  | |
| #define | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)   0x8 |
|  | Low-frequency speaker bit mask [更多...](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) |
|  | |
| #define | [AK\_SPEAKER\_BACK\_LEFT](_ak_speaker_config_8h_a5d7dbd0352851bdc06b23b1b4f83f1a5.html#a5d7dbd0352851bdc06b23b1b4f83f1a5)   0x10 |
|  | Rear left speaker bit mask [更多...](_ak_speaker_config_8h_a5d7dbd0352851bdc06b23b1b4f83f1a5.html#a5d7dbd0352851bdc06b23b1b4f83f1a5) |
|  | |
| #define | [AK\_SPEAKER\_BACK\_RIGHT](_ak_speaker_config_8h_a097104505e8284e45e017722c398e815.html#a097104505e8284e45e017722c398e815)   0x20 |
|  | Rear right speaker bit mask [更多...](_ak_speaker_config_8h_a097104505e8284e45e017722c398e815.html#a097104505e8284e45e017722c398e815) |
|  | |
| #define | [AK\_SPEAKER\_BACK\_CENTER](_ak_speaker_config_8h_ab5aaf461d5cabcf9f03f7830337a0e91.html#ab5aaf461d5cabcf9f03f7830337a0e91)   0x100 |
|  | Rear center speaker ("surround speaker") bit mask [更多...](_ak_speaker_config_8h_ab5aaf461d5cabcf9f03f7830337a0e91.html#ab5aaf461d5cabcf9f03f7830337a0e91) |
|  | |
| #define | [AK\_SPEAKER\_SIDE\_LEFT](_ak_speaker_config_8h_af5b7859eec3d8b46915b09f2edbf47d6.html#af5b7859eec3d8b46915b09f2edbf47d6)   0x200 |
|  | Side left speaker bit mask [更多...](_ak_speaker_config_8h_af5b7859eec3d8b46915b09f2edbf47d6.html#af5b7859eec3d8b46915b09f2edbf47d6) |
|  | |
| #define | [AK\_SPEAKER\_SIDE\_RIGHT](_ak_speaker_config_8h_a2d1d64b4c244fab01feeda53a0c856e7.html#a2d1d64b4c244fab01feeda53a0c856e7)   0x400 |
|  | Side right speaker bit mask [更多...](_ak_speaker_config_8h_a2d1d64b4c244fab01feeda53a0c856e7.html#a2d1d64b4c244fab01feeda53a0c856e7) |
|  | |
| #define | [AK\_SPEAKER\_TOP](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47)   0x800 |
|  | "Height" speakers. [更多...](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580)   0x1000 |
|  | Top front left speaker bit mask [更多...](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_FRONT\_CENTER](_ak_speaker_config_8h_a26bed61f5c560fcca91eeae5befee945.html#a26bed61f5c560fcca91eeae5befee945)   0x2000 |
|  | Top front center speaker bit mask [更多...](_ak_speaker_config_8h_a26bed61f5c560fcca91eeae5befee945.html#a26bed61f5c560fcca91eeae5befee945) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b)   0x4000 |
|  | Top front right speaker bit mask [更多...](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62)   0x8000 |
|  | Top rear left speaker bit mask [更多...](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_BACK\_CENTER](_ak_speaker_config_8h_a549caf0c2a9c944ba058a09720167786.html#a549caf0c2a9c944ba058a09720167786)   0x10000 |
|  | Top rear center speaker bit mask [更多...](_ak_speaker_config_8h_a549caf0c2a9c944ba058a09720167786.html#a549caf0c2a9c944ba058a09720167786) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f)   0x20000 |
|  | Top rear right speaker bit mask [更多...](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_SIDE\_LEFT](_ak_speaker_config_8h_a33a581ae293361f094ab4138b02f0475.html#a33a581ae293361f094ab4138b02f0475)   0x40000 |
|  | Top side left speaker bit mask [更多...](_ak_speaker_config_8h_a33a581ae293361f094ab4138b02f0475.html#a33a581ae293361f094ab4138b02f0475) |
|  | |
| #define | [AK\_SPEAKER\_HEIGHT\_SIDE\_RIGHT](_ak_speaker_config_8h_ac88dd93d57cfeb29d2587a718996c249.html#ac88dd93d57cfeb29d2587a718996c249)   0x80000 |
|  | Top side right speaker bit mask [更多...](_ak_speaker_config_8h_ac88dd93d57cfeb29d2587a718996c249.html#ac88dd93d57cfeb29d2587a718996c249) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_MONO](_ak_speaker_config_8h_a15b620987b17cea4c8dca72443f3ac96.html#a15b620987b17cea4c8dca72443f3ac96)   [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906) |
|  | 1.0 setup channel mask [更多...](_ak_speaker_config_8h_a15b620987b17cea4c8dca72443f3ac96.html#a15b620987b17cea4c8dca72443f3ac96) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_0POINT1](_ak_speaker_config_8h_ab8cf216c7e084f3aa07abf7834b220a3.html#ab8cf216c7e084f3aa07abf7834b220a3)   [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) |
|  | 0.1 setup channel mask [更多...](_ak_speaker_config_8h_ab8cf216c7e084f3aa07abf7834b220a3.html#ab8cf216c7e084f3aa07abf7834b220a3) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_1POINT1](_ak_speaker_config_8h_a0ab2f95eda607bf022fcf3edbdcb6e32.html#a0ab2f95eda607bf022fcf3edbdcb6e32)   ([AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 1.1 setup channel mask [更多...](_ak_speaker_config_8h_a0ab2f95eda607bf022fcf3edbdcb6e32.html#a0ab2f95eda607bf022fcf3edbdcb6e32) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894)   ([AK\_SPEAKER\_FRONT\_LEFT](_ak_speaker_config_8h_aa9dc5afd59709444ca24c974c54b08b3.html#aa9dc5afd59709444ca24c974c54b08b3) | [AK\_SPEAKER\_FRONT\_RIGHT](_ak_speaker_config_8h_a2bf48d2a4c5235e0d5a42d1caa7edd16.html#a2bf48d2a4c5235e0d5a42d1caa7edd16)) |
|  | 2.0 setup channel mask [更多...](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_2POINT1](_ak_speaker_config_8h_a38ac2122986c32d45a3de34877ffee5d.html#a38ac2122986c32d45a3de34877ffee5d)   ([AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 2.1 setup channel mask [更多...](_ak_speaker_config_8h_a38ac2122986c32d45a3de34877ffee5d.html#a38ac2122986c32d45a3de34877ffee5d) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_3STEREO](_ak_speaker_config_8h_af7e4b223543b8464b7f39603f912308e.html#af7e4b223543b8464b7f39603f912308e)   ([AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894) | [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906)) |
|  | 3.0 setup channel mask [更多...](_ak_speaker_config_8h_af7e4b223543b8464b7f39603f912308e.html#af7e4b223543b8464b7f39603f912308e) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_3POINT1](_ak_speaker_config_8h_a67b971821c86b263ccb2625af1b32fd5.html#a67b971821c86b263ccb2625af1b32fd5)   ([AK\_SPEAKER\_SETUP\_3STEREO](_ak_speaker_config_8h_af7e4b223543b8464b7f39603f912308e.html#af7e4b223543b8464b7f39603f912308e) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 3.1 setup channel mask [更多...](_ak_speaker_config_8h_a67b971821c86b263ccb2625af1b32fd5.html#a67b971821c86b263ccb2625af1b32fd5) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_4](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7)   ([AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894) | [AK\_SPEAKER\_SIDE\_LEFT](_ak_speaker_config_8h_af5b7859eec3d8b46915b09f2edbf47d6.html#af5b7859eec3d8b46915b09f2edbf47d6) | [AK\_SPEAKER\_SIDE\_RIGHT](_ak_speaker_config_8h_a2d1d64b4c244fab01feeda53a0c856e7.html#a2d1d64b4c244fab01feeda53a0c856e7)) |
|  | 4.0 setup channel mask [更多...](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_4POINT1](_ak_speaker_config_8h_a1afad61d2fd6a3dfcb9af2166371ca33.html#a1afad61d2fd6a3dfcb9af2166371ca33)   ([AK\_SPEAKER\_SETUP\_4](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 4.1 setup channel mask [更多...](_ak_speaker_config_8h_a1afad61d2fd6a3dfcb9af2166371ca33.html#a1afad61d2fd6a3dfcb9af2166371ca33) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_5](_ak_speaker_config_8h_af181b7b2236165b1e43fc8d54f5dee9d.html#af181b7b2236165b1e43fc8d54f5dee9d)   ([AK\_SPEAKER\_SETUP\_4](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7) | [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906)) |
|  | 5.0 setup channel mask [更多...](_ak_speaker_config_8h_af181b7b2236165b1e43fc8d54f5dee9d.html#af181b7b2236165b1e43fc8d54f5dee9d) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_5POINT1](_ak_speaker_config_8h_a666b8c74f7cca22244ae5d96b6a665e0.html#a666b8c74f7cca22244ae5d96b6a665e0)   ([AK\_SPEAKER\_SETUP\_5](_ak_speaker_config_8h_af181b7b2236165b1e43fc8d54f5dee9d.html#af181b7b2236165b1e43fc8d54f5dee9d) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 5.1 setup channel mask [更多...](_ak_speaker_config_8h_a666b8c74f7cca22244ae5d96b6a665e0.html#a666b8c74f7cca22244ae5d96b6a665e0) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_6](_ak_speaker_config_8h_a84fe0119ee9267e7b81357b6816333c1.html#a84fe0119ee9267e7b81357b6816333c1)   ([AK\_SPEAKER\_SETUP\_4](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7) | [AK\_SPEAKER\_BACK\_LEFT](_ak_speaker_config_8h_a5d7dbd0352851bdc06b23b1b4f83f1a5.html#a5d7dbd0352851bdc06b23b1b4f83f1a5) | [AK\_SPEAKER\_BACK\_RIGHT](_ak_speaker_config_8h_a097104505e8284e45e017722c398e815.html#a097104505e8284e45e017722c398e815)) |
|  | 6.0 setup channel mask [更多...](_ak_speaker_config_8h_a84fe0119ee9267e7b81357b6816333c1.html#a84fe0119ee9267e7b81357b6816333c1) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_6POINT1](_ak_speaker_config_8h_a008245a635a79cf8c7c2e9e9931cf923.html#a008245a635a79cf8c7c2e9e9931cf923)   ([AK\_SPEAKER\_SETUP\_6](_ak_speaker_config_8h_a84fe0119ee9267e7b81357b6816333c1.html#a84fe0119ee9267e7b81357b6816333c1) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 6.1 setup channel mask [更多...](_ak_speaker_config_8h_a008245a635a79cf8c7c2e9e9931cf923.html#a008245a635a79cf8c7c2e9e9931cf923) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_7](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17)   ([AK\_SPEAKER\_SETUP\_6](_ak_speaker_config_8h_a84fe0119ee9267e7b81357b6816333c1.html#a84fe0119ee9267e7b81357b6816333c1) | [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906)) |
|  | 7.0 setup channel mask [更多...](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_7POINT1](_ak_speaker_config_8h_a0220ffe73c82eefb927458d83bdf75b2.html#a0220ffe73c82eefb927458d83bdf75b2)   ([AK\_SPEAKER\_SETUP\_7](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | 7.1 setup channel mask [更多...](_ak_speaker_config_8h_a0220ffe73c82eefb927458d83bdf75b2.html#a0220ffe73c82eefb927458d83bdf75b2) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_SURROUND](_ak_speaker_config_8h_a69fc7735b94fbcff2bd2dd01ac5f9433.html#a69fc7735b94fbcff2bd2dd01ac5f9433)   ([AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894) | [AK\_SPEAKER\_BACK\_CENTER](_ak_speaker_config_8h_ab5aaf461d5cabcf9f03f7830337a0e91.html#ab5aaf461d5cabcf9f03f7830337a0e91)) |
|  | Legacy surround setup channel mask [更多...](_ak_speaker_config_8h_a69fc7735b94fbcff2bd2dd01ac5f9433.html#a69fc7735b94fbcff2bd2dd01ac5f9433) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_HEIGHT\_2](_ak_speaker_config_8h_acf576972d6270d9c03ca7c39041e19cc.html#acf576972d6270d9c03ca7c39041e19cc)   ([AK\_SPEAKER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580) | [AK\_SPEAKER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b)) |
|  | 2 speaker height layer. [更多...](_ak_speaker_config_8h_acf576972d6270d9c03ca7c39041e19cc.html#acf576972d6270d9c03ca7c39041e19cc) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_HEIGHT\_4](_ak_speaker_config_8h_a854ab32248261d7a544b7f14b2498354.html#a854ab32248261d7a544b7f14b2498354)   ([AK\_SPEAKER\_SETUP\_HEIGHT\_2](_ak_speaker_config_8h_acf576972d6270d9c03ca7c39041e19cc.html#acf576972d6270d9c03ca7c39041e19cc) | [AK\_SPEAKER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62) | [AK\_SPEAKER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f)) |
|  | 4 speaker height layer. [更多...](_ak_speaker_config_8h_a854ab32248261d7a544b7f14b2498354.html#a854ab32248261d7a544b7f14b2498354) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_HEIGHT\_5](_ak_speaker_config_8h_a0df8788e9fbdeae657b7204f757fb0f9.html#a0df8788e9fbdeae657b7204f757fb0f9)   ([AK\_SPEAKER\_SETUP\_HEIGHT\_4](_ak_speaker_config_8h_a854ab32248261d7a544b7f14b2498354.html#a854ab32248261d7a544b7f14b2498354) | [AK\_SPEAKER\_HEIGHT\_FRONT\_CENTER](_ak_speaker_config_8h_a26bed61f5c560fcca91eeae5befee945.html#a26bed61f5c560fcca91eeae5befee945)) |
|  | 5 speaker height layer. [更多...](_ak_speaker_config_8h_a0df8788e9fbdeae657b7204f757fb0f9.html#a0df8788e9fbdeae657b7204f757fb0f9) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_HEIGHT\_ALL](_ak_speaker_config_8h_ab588f767c4528ca4465f567a2f8dd8f4.html#ab588f767c4528ca4465f567a2f8dd8f4)   ([AK\_SPEAKER\_SETUP\_HEIGHT\_5](_ak_speaker_config_8h_a0df8788e9fbdeae657b7204f757fb0f9.html#a0df8788e9fbdeae657b7204f757fb0f9) | [AK\_SPEAKER\_HEIGHT\_BACK\_CENTER](_ak_speaker_config_8h_a549caf0c2a9c944ba058a09720167786.html#a549caf0c2a9c944ba058a09720167786)) |
|  | All height speaker layer. [更多...](_ak_speaker_config_8h_ab588f767c4528ca4465f567a2f8dd8f4.html#ab588f767c4528ca4465f567a2f8dd8f4) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_HEIGHT\_4\_TOP](_ak_speaker_config_8h_a7f72a10d2dd4b029d81ff03d725e6639.html#a7f72a10d2dd4b029d81ff03d725e6639)   ([AK\_SPEAKER\_SETUP\_HEIGHT\_4](_ak_speaker_config_8h_a854ab32248261d7a544b7f14b2498354.html#a854ab32248261d7a544b7f14b2498354) | [AK\_SPEAKER\_TOP](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47)) |
|  | 4 speaker height layer + top. [更多...](_ak_speaker_config_8h_a7f72a10d2dd4b029d81ff03d725e6639.html#a7f72a10d2dd4b029d81ff03d725e6639) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_HEIGHT\_5\_TOP](_ak_speaker_config_8h_a2ba12fbcde523a32e388923fa0b534cf.html#a2ba12fbcde523a32e388923fa0b534cf)   ([AK\_SPEAKER\_SETUP\_HEIGHT\_5](_ak_speaker_config_8h_a0df8788e9fbdeae657b7204f757fb0f9.html#a0df8788e9fbdeae657b7204f757fb0f9) | [AK\_SPEAKER\_TOP](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47)) |
|  | 5 speaker height layer + top. [更多...](_ak_speaker_config_8h_a2ba12fbcde523a32e388923fa0b534cf.html#a2ba12fbcde523a32e388923fa0b534cf) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_222](_ak_speaker_config_8h_a26415c97a80190a24e9b920ed8f2da24.html#a26415c97a80190a24e9b920ed8f2da24)   ([AK\_SPEAKER\_SETUP\_4](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7) | [AK\_SPEAKER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580) | [AK\_SPEAKER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b)) |
|  | Auro-222 setup channel mask (4.0.2) [更多...](_ak_speaker_config_8h_a26415c97a80190a24e9b920ed8f2da24.html#a26415c97a80190a24e9b920ed8f2da24) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_8](_ak_speaker_config_8h_aa22eeddd73dd120e026c566aa794ebd6.html#aa22eeddd73dd120e026c566aa794ebd6)   ([AK\_SPEAKER\_SETUP\_AURO\_222](_ak_speaker_config_8h_a26415c97a80190a24e9b920ed8f2da24.html#a26415c97a80190a24e9b920ed8f2da24) | [AK\_SPEAKER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62) | [AK\_SPEAKER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f)) |
|  | Auro-8 setup channel mask (4.0.4) [更多...](_ak_speaker_config_8h_aa22eeddd73dd120e026c566aa794ebd6.html#aa22eeddd73dd120e026c566aa794ebd6) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_9](_ak_speaker_config_8h_a7c4a354e165d844da19c4e8bc8fe6040.html#a7c4a354e165d844da19c4e8bc8fe6040)   ([AK\_SPEAKER\_SETUP\_AURO\_8](_ak_speaker_config_8h_aa22eeddd73dd120e026c566aa794ebd6.html#aa22eeddd73dd120e026c566aa794ebd6) | [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906)) |
|  | Auro-9.0 setup channel mask (5.0.4) [更多...](_ak_speaker_config_8h_a7c4a354e165d844da19c4e8bc8fe6040.html#a7c4a354e165d844da19c4e8bc8fe6040) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_9POINT1](_ak_speaker_config_8h_ac0cd8b462b65a8a4ef8f0b813473dc24.html#ac0cd8b462b65a8a4ef8f0b813473dc24)   ([AK\_SPEAKER\_SETUP\_AURO\_9](_ak_speaker_config_8h_a7c4a354e165d844da19c4e8bc8fe6040.html#a7c4a354e165d844da19c4e8bc8fe6040) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | Auro-9.1 setup channel mask (5.1.4) [更多...](_ak_speaker_config_8h_ac0cd8b462b65a8a4ef8f0b813473dc24.html#ac0cd8b462b65a8a4ef8f0b813473dc24) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_10](_ak_speaker_config_8h_a7749a1218fb5b6ea72010731ee49aa4e.html#a7749a1218fb5b6ea72010731ee49aa4e)   ([AK\_SPEAKER\_SETUP\_AURO\_9](_ak_speaker_config_8h_a7c4a354e165d844da19c4e8bc8fe6040.html#a7c4a354e165d844da19c4e8bc8fe6040) | [AK\_SPEAKER\_TOP](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47)) |
|  | Auro-10.0 setup channel mask (5.0.4+top) [更多...](_ak_speaker_config_8h_a7749a1218fb5b6ea72010731ee49aa4e.html#a7749a1218fb5b6ea72010731ee49aa4e) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_10POINT1](_ak_speaker_config_8h_ae529d430f1ecc2e088fe4ba34a5c4ff8.html#ae529d430f1ecc2e088fe4ba34a5c4ff8)   ([AK\_SPEAKER\_SETUP\_AURO\_10](_ak_speaker_config_8h_a7749a1218fb5b6ea72010731ee49aa4e.html#a7749a1218fb5b6ea72010731ee49aa4e) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | Auro-10.1 setup channel mask (5.1.4+top) [更多...](_ak_speaker_config_8h_ae529d430f1ecc2e088fe4ba34a5c4ff8.html#ae529d430f1ecc2e088fe4ba34a5c4ff8) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_11](_ak_speaker_config_8h_a6cbd9d8b47388090ff89df8e45f2ccd3.html#a6cbd9d8b47388090ff89df8e45f2ccd3)   ([AK\_SPEAKER\_SETUP\_AURO\_10](_ak_speaker_config_8h_a7749a1218fb5b6ea72010731ee49aa4e.html#a7749a1218fb5b6ea72010731ee49aa4e) | [AK\_SPEAKER\_HEIGHT\_FRONT\_CENTER](_ak_speaker_config_8h_a26bed61f5c560fcca91eeae5befee945.html#a26bed61f5c560fcca91eeae5befee945)) |
|  | Auro-11.0 setup channel mask (5.0.5+top) [更多...](_ak_speaker_config_8h_a6cbd9d8b47388090ff89df8e45f2ccd3.html#a6cbd9d8b47388090ff89df8e45f2ccd3) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_11POINT1](_ak_speaker_config_8h_ab52b3ab3ef41cb8bd21d4523b0dd9758.html#ab52b3ab3ef41cb8bd21d4523b0dd9758)   ([AK\_SPEAKER\_SETUP\_AURO\_11](_ak_speaker_config_8h_a6cbd9d8b47388090ff89df8e45f2ccd3.html#a6cbd9d8b47388090ff89df8e45f2ccd3) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | Auro-11.1 setup channel mask (5.1.5+top) [更多...](_ak_speaker_config_8h_ab52b3ab3ef41cb8bd21d4523b0dd9758.html#ab52b3ab3ef41cb8bd21d4523b0dd9758) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_11\_740](_ak_speaker_config_8h_a9b78908be87ee5bac8a6ec7636386f58.html#a9b78908be87ee5bac8a6ec7636386f58)   ([AK\_SPEAKER\_SETUP\_7](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17) | [AK\_SPEAKER\_SETUP\_HEIGHT\_4](_ak_speaker_config_8h_a854ab32248261d7a544b7f14b2498354.html#a854ab32248261d7a544b7f14b2498354)) |
|  | Auro-11.0 (7+4) setup channel mask (7.0.4) [更多...](_ak_speaker_config_8h_a9b78908be87ee5bac8a6ec7636386f58.html#a9b78908be87ee5bac8a6ec7636386f58) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_11POINT1\_740](_ak_speaker_config_8h_ac3f7045b044654e66ea4e6a7cb181c30.html#ac3f7045b044654e66ea4e6a7cb181c30)   ([AK\_SPEAKER\_SETUP\_AURO\_11\_740](_ak_speaker_config_8h_a9b78908be87ee5bac8a6ec7636386f58.html#a9b78908be87ee5bac8a6ec7636386f58) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | Auro-11.1 (7+4) setup channel mask (7.1.4) [更多...](_ak_speaker_config_8h_ac3f7045b044654e66ea4e6a7cb181c30.html#ac3f7045b044654e66ea4e6a7cb181c30) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_13\_751](_ak_speaker_config_8h_a2cbe0ea6fcb972aab50261617284aa53.html#a2cbe0ea6fcb972aab50261617284aa53)   ([AK\_SPEAKER\_SETUP\_7](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17) | [AK\_SPEAKER\_SETUP\_HEIGHT\_5](_ak_speaker_config_8h_a0df8788e9fbdeae657b7204f757fb0f9.html#a0df8788e9fbdeae657b7204f757fb0f9) | [AK\_SPEAKER\_TOP](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47)) |
|  | Auro-13.0 setup channel mask (7.0.5+top) [更多...](_ak_speaker_config_8h_a2cbe0ea6fcb972aab50261617284aa53.html#a2cbe0ea6fcb972aab50261617284aa53) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_AURO\_13POINT1\_751](_ak_speaker_config_8h_a036bd10b96a01e2be0e0016fd920fcbc.html#a036bd10b96a01e2be0e0016fd920fcbc)   ([AK\_SPEAKER\_SETUP\_AURO\_13\_751](_ak_speaker_config_8h_a2cbe0ea6fcb972aab50261617284aa53.html#a2cbe0ea6fcb972aab50261617284aa53) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90)) |
|  | Auro-13.1 setup channel mask (7.1.5+top) [更多...](_ak_speaker_config_8h_a036bd10b96a01e2be0e0016fd920fcbc.html#a036bd10b96a01e2be0e0016fd920fcbc) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_5\_0\_2](_ak_speaker_config_8h_a58d2cc25b432a97f0c0514e67c7aca78.html#a58d2cc25b432a97f0c0514e67c7aca78)   ([AK\_SPEAKER\_SETUP\_5](_ak_speaker_config_8h_af181b7b2236165b1e43fc8d54f5dee9d.html#af181b7b2236165b1e43fc8d54f5dee9d) | [AK\_SPEAKER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580) | [AK\_SPEAKER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b) ) |
|  | Dolby 5.0.2 setup channel mask [更多...](_ak_speaker_config_8h_a58d2cc25b432a97f0c0514e67c7aca78.html#a58d2cc25b432a97f0c0514e67c7aca78) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_5\_1\_2](_ak_speaker_config_8h_aea2a3a9b9043077257fd8b224b5529f1.html#aea2a3a9b9043077257fd8b224b5529f1)   ([AK\_SPEAKER\_SETUP\_DOLBY\_5\_0\_2](_ak_speaker_config_8h_a58d2cc25b432a97f0c0514e67c7aca78.html#a58d2cc25b432a97f0c0514e67c7aca78) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | Dolby 5.1.2 setup channel mask [更多...](_ak_speaker_config_8h_aea2a3a9b9043077257fd8b224b5529f1.html#aea2a3a9b9043077257fd8b224b5529f1) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_5\_0\_4](_ak_speaker_config_8h_aa8f3f391d552ea990ce4e7ab93d6c973.html#aa8f3f391d552ea990ce4e7ab93d6c973)   ([AK\_SPEAKER\_SETUP\_DOLBY\_5\_0\_2](_ak_speaker_config_8h_a58d2cc25b432a97f0c0514e67c7aca78.html#a58d2cc25b432a97f0c0514e67c7aca78) | [AK\_SPEAKER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62) | [AK\_SPEAKER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f) ) |
|  | Dolby 5.0.4 setup channel mask [更多...](_ak_speaker_config_8h_aa8f3f391d552ea990ce4e7ab93d6c973.html#aa8f3f391d552ea990ce4e7ab93d6c973) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_5\_1\_4](_ak_speaker_config_8h_a01562b667f2df72943f4e2465d218f18.html#a01562b667f2df72943f4e2465d218f18)   ([AK\_SPEAKER\_SETUP\_DOLBY\_5\_0\_4](_ak_speaker_config_8h_aa8f3f391d552ea990ce4e7ab93d6c973.html#aa8f3f391d552ea990ce4e7ab93d6c973) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | Dolby 5.1.4 setup channel mask [更多...](_ak_speaker_config_8h_a01562b667f2df72943f4e2465d218f18.html#a01562b667f2df72943f4e2465d218f18) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_6\_0\_2](_ak_speaker_config_8h_a51357fa0ba8e34b17bd9056f344af44c.html#a51357fa0ba8e34b17bd9056f344af44c)   ([AK\_SPEAKER\_SETUP\_6](_ak_speaker_config_8h_a84fe0119ee9267e7b81357b6816333c1.html#a84fe0119ee9267e7b81357b6816333c1) | [AK\_SPEAKER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580) | [AK\_SPEAKER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b) ) |
|  | Dolby 6.0.2 setup channel mask [更多...](_ak_speaker_config_8h_a51357fa0ba8e34b17bd9056f344af44c.html#a51357fa0ba8e34b17bd9056f344af44c) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_6\_1\_2](_ak_speaker_config_8h_a71cfc4a1d7c922df3af15eb7507b3524.html#a71cfc4a1d7c922df3af15eb7507b3524)   ([AK\_SPEAKER\_SETUP\_DOLBY\_6\_0\_2](_ak_speaker_config_8h_a51357fa0ba8e34b17bd9056f344af44c.html#a51357fa0ba8e34b17bd9056f344af44c) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | Dolby 6.1.2 setup channel mask [更多...](_ak_speaker_config_8h_a71cfc4a1d7c922df3af15eb7507b3524.html#a71cfc4a1d7c922df3af15eb7507b3524) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_6\_0\_4](_ak_speaker_config_8h_a43c5f68eaff995fb2d5422909c1293b9.html#a43c5f68eaff995fb2d5422909c1293b9)   ([AK\_SPEAKER\_SETUP\_DOLBY\_6\_0\_2](_ak_speaker_config_8h_a51357fa0ba8e34b17bd9056f344af44c.html#a51357fa0ba8e34b17bd9056f344af44c) | [AK\_SPEAKER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62) | [AK\_SPEAKER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f) ) |
|  | Dolby 6.0.4 setup channel mask [更多...](_ak_speaker_config_8h_a43c5f68eaff995fb2d5422909c1293b9.html#a43c5f68eaff995fb2d5422909c1293b9) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_6\_1\_4](_ak_speaker_config_8h_ab90a99f35f2c891a8d3ae27c3a6df73d.html#ab90a99f35f2c891a8d3ae27c3a6df73d)   ([AK\_SPEAKER\_SETUP\_DOLBY\_6\_0\_4](_ak_speaker_config_8h_a43c5f68eaff995fb2d5422909c1293b9.html#a43c5f68eaff995fb2d5422909c1293b9) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | Dolby 6.1.4 setup channel mask [更多...](_ak_speaker_config_8h_ab90a99f35f2c891a8d3ae27c3a6df73d.html#ab90a99f35f2c891a8d3ae27c3a6df73d) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_7\_0\_2](_ak_speaker_config_8h_a02b502aa7d9ed0c224bfc4f2d508b44e.html#a02b502aa7d9ed0c224bfc4f2d508b44e)   ([AK\_SPEAKER\_SETUP\_7](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17) | [AK\_SPEAKER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_a148bb823a96a5fde25f758ac8479f580.html#a148bb823a96a5fde25f758ac8479f580) | [AK\_SPEAKER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a1df9fc004739a44f1f5aa1f0437cc00b.html#a1df9fc004739a44f1f5aa1f0437cc00b) ) |
|  | Dolby 7.0.2 setup channel mask [更多...](_ak_speaker_config_8h_a02b502aa7d9ed0c224bfc4f2d508b44e.html#a02b502aa7d9ed0c224bfc4f2d508b44e) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_2](_ak_speaker_config_8h_aff46dc2cb25d2a231a7cff72cb5b73d9.html#aff46dc2cb25d2a231a7cff72cb5b73d9)   ([AK\_SPEAKER\_SETUP\_DOLBY\_7\_0\_2](_ak_speaker_config_8h_a02b502aa7d9ed0c224bfc4f2d508b44e.html#a02b502aa7d9ed0c224bfc4f2d508b44e) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | Dolby 7.1.2 setup channel mask [更多...](_ak_speaker_config_8h_aff46dc2cb25d2a231a7cff72cb5b73d9.html#aff46dc2cb25d2a231a7cff72cb5b73d9) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_7\_0\_4](_ak_speaker_config_8h_a59c6277d9f419f218855df35d86b67d0.html#a59c6277d9f419f218855df35d86b67d0)   ([AK\_SPEAKER\_SETUP\_DOLBY\_7\_0\_2](_ak_speaker_config_8h_a02b502aa7d9ed0c224bfc4f2d508b44e.html#a02b502aa7d9ed0c224bfc4f2d508b44e) | [AK\_SPEAKER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_a85c4c1bdce87db6afbc38592c23e5d62.html#a85c4c1bdce87db6afbc38592c23e5d62) | [AK\_SPEAKER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a3243d9ee881ebd44a0f1219adc91952f.html#a3243d9ee881ebd44a0f1219adc91952f) ) |
|  | Dolby 7.0.4 setup channel mask [更多...](_ak_speaker_config_8h_a59c6277d9f419f218855df35d86b67d0.html#a59c6277d9f419f218855df35d86b67d0) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0)   ([AK\_SPEAKER\_SETUP\_DOLBY\_7\_0\_4](_ak_speaker_config_8h_a59c6277d9f419f218855df35d86b67d0.html#a59c6277d9f419f218855df35d86b67d0) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | Dolby 7.1.4 setup channel mask [更多...](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_ALL\_SPEAKERS](_ak_speaker_config_8h_aa1245a2c77e336be3e18af169b514ca2.html#aa1245a2c77e336be3e18af169b514ca2)   ([AK\_SPEAKER\_SETUP\_7POINT1](_ak_speaker_config_8h_a0220ffe73c82eefb927458d83bdf75b2.html#a0220ffe73c82eefb927458d83bdf75b2) | [AK\_SPEAKER\_BACK\_CENTER](_ak_speaker_config_8h_ab5aaf461d5cabcf9f03f7830337a0e91.html#ab5aaf461d5cabcf9f03f7830337a0e91) | [AK\_SPEAKER\_SETUP\_HEIGHT\_ALL](_ak_speaker_config_8h_ab588f767c4528ca4465f567a2f8dd8f4.html#ab588f767c4528ca4465f567a2f8dd8f4) | [AK\_SPEAKER\_TOP](_ak_speaker_config_8h_adcb895daade7e0a21b7ad4402cb7fb47.html#adcb895daade7e0a21b7ad4402cb7fb47)) |
|  | All speakers. [更多...](_ak_speaker_config_8h_aa1245a2c77e336be3e18af169b514ca2.html#aa1245a2c77e336be3e18af169b514ca2) |
|  | |
| #define | [AK\_IDX\_SETUP\_FRONT\_LEFT](_ak_speaker_config_8h_a03cf045848926571fc748fadf2bbdd52.html#a03cf045848926571fc748fadf2bbdd52)   (0) |
|  | Index of front-left channel in all configurations. [更多...](_ak_speaker_config_8h_a03cf045848926571fc748fadf2bbdd52.html#a03cf045848926571fc748fadf2bbdd52) |
|  | |
| #define | [AK\_IDX\_SETUP\_FRONT\_RIGHT](_ak_speaker_config_8h_a2d599ee7fae56f2f34d6e1bf10e06c6c.html#a2d599ee7fae56f2f34d6e1bf10e06c6c)   (1) |
|  | Index of front-right channel in all configurations. [更多...](_ak_speaker_config_8h_a2d599ee7fae56f2f34d6e1bf10e06c6c.html#a2d599ee7fae56f2f34d6e1bf10e06c6c) |
|  | |
| #define | [AK\_IDX\_SETUP\_CENTER](_ak_speaker_config_8h_a41a4cdd766ba3a7461e4f6844f3926ba.html#a41a4cdd766ba3a7461e4f6844f3926ba)   (2) |
|  | Index of front-center channel in all configurations. [更多...](_ak_speaker_config_8h_a41a4cdd766ba3a7461e4f6844f3926ba.html#a41a4cdd766ba3a7461e4f6844f3926ba) |
|  | |
| #define | [AK\_IDX\_SETUP\_NOCENTER\_BACK\_LEFT](_ak_speaker_config_8h_a33e85624ac15a7ba7838d38ad5bf38ad.html#a33e85624ac15a7ba7838d38ad5bf38ad)   (2) |
|  | Index of back-left channel in configurations with no front-center channel. [更多...](_ak_speaker_config_8h_a33e85624ac15a7ba7838d38ad5bf38ad.html#a33e85624ac15a7ba7838d38ad5bf38ad) |
|  | |
| #define | [AK\_IDX\_SETUP\_NOCENTER\_BACK\_RIGHT](_ak_speaker_config_8h_a0a5eb77c394e1dc2c381cc582515cfcf.html#a0a5eb77c394e1dc2c381cc582515cfcf)   (3) |
|  | Index of back-right channel in configurations with no front-center channel. [更多...](_ak_speaker_config_8h_a0a5eb77c394e1dc2c381cc582515cfcf.html#a0a5eb77c394e1dc2c381cc582515cfcf) |
|  | |
| #define | [AK\_IDX\_SETUP\_NOCENTER\_SIDE\_LEFT](_ak_speaker_config_8h_a84a6900ee4d044f67e1a274604db316e.html#a84a6900ee4d044f67e1a274604db316e)   (4) |
|  | Index of side-left channel in configurations with no front-center channel. [更多...](_ak_speaker_config_8h_a84a6900ee4d044f67e1a274604db316e.html#a84a6900ee4d044f67e1a274604db316e) |
|  | |
| #define | [AK\_IDX\_SETUP\_NOCENTER\_SIDE\_RIGHT](_ak_speaker_config_8h_afdb1b9a37394fafa9ce23b171eba99bf.html#afdb1b9a37394fafa9ce23b171eba99bf)   (5) |
|  | Index of side-right channel in configurations with no front-center channel. [更多...](_ak_speaker_config_8h_afdb1b9a37394fafa9ce23b171eba99bf.html#afdb1b9a37394fafa9ce23b171eba99bf) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_BACK\_LEFT](_ak_speaker_config_8h_a4d13003b109a75a8f8253f3dc24e8fe8.html#a4d13003b109a75a8f8253f3dc24e8fe8)   (3) |
|  | Index of back-left channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_a4d13003b109a75a8f8253f3dc24e8fe8.html#a4d13003b109a75a8f8253f3dc24e8fe8) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_BACK\_RIGHT](_ak_speaker_config_8h_a8fca9f479caf83e0cd69cc82b9829dee.html#a8fca9f479caf83e0cd69cc82b9829dee)   (4) |
|  | Index of back-right channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_a8fca9f479caf83e0cd69cc82b9829dee.html#a8fca9f479caf83e0cd69cc82b9829dee) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_SIDE\_LEFT](_ak_speaker_config_8h_a0ddcb1856d38c3e3e7900177b223b91d.html#a0ddcb1856d38c3e3e7900177b223b91d)   (5) |
|  | Index of side-left channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_a0ddcb1856d38c3e3e7900177b223b91d.html#a0ddcb1856d38c3e3e7900177b223b91d) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_SIDE\_RIGHT](_ak_speaker_config_8h_a86010a2eb1a36f2214c18c798e3db304.html#a86010a2eb1a36f2214c18c798e3db304)   (6) |
|  | Index of side-right channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_a86010a2eb1a36f2214c18c798e3db304.html#a86010a2eb1a36f2214c18c798e3db304) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_HEIGHT\_FRONT\_LEFT](_ak_speaker_config_8h_abf93592dcee1e718d24b65a805b8e90a.html#abf93592dcee1e718d24b65a805b8e90a)   (7) |
|  | Index of height-front-left channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_abf93592dcee1e718d24b65a805b8e90a.html#abf93592dcee1e718d24b65a805b8e90a) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_HEIGHT\_FRONT\_RIGHT](_ak_speaker_config_8h_a0055b7ce5d12a63847ca65296a63e816.html#a0055b7ce5d12a63847ca65296a63e816)   (8) |
|  | Index of height-front-right channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_a0055b7ce5d12a63847ca65296a63e816.html#a0055b7ce5d12a63847ca65296a63e816) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_HEIGHT\_BACK\_LEFT](_ak_speaker_config_8h_ad2ef4a740ce7753e52b3a2f577460818.html#ad2ef4a740ce7753e52b3a2f577460818)   (9) |
|  | Index of height-back-left channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_ad2ef4a740ce7753e52b3a2f577460818.html#ad2ef4a740ce7753e52b3a2f577460818) |
|  | |
| #define | [AK\_IDX\_SETUP\_WITHCENTER\_HEIGHT\_BACK\_RIGHT](_ak_speaker_config_8h_a7244d8d258fadbae84f1a9b61d551a0b.html#a7244d8d258fadbae84f1a9b61d551a0b)   (10) |
|  | Index of height-back-right channel in configurations with a front-center channel. [更多...](_ak_speaker_config_8h_a7244d8d258fadbae84f1a9b61d551a0b.html#a7244d8d258fadbae84f1a9b61d551a0b) |
|  | |
| #define | [AK\_IDX\_SETUP\_0\_LFE](_ak_speaker_config_8h_a9ed4062f4915248c736579dee34ee3c6.html#a9ed4062f4915248c736579dee34ee3c6)   (0) |
|  | Index of low-frequency channel in 0.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a9ed4062f4915248c736579dee34ee3c6.html#a9ed4062f4915248c736579dee34ee3c6) |
|  | |
| #define | [AK\_IDX\_SETUP\_1\_CENTER](_ak_speaker_config_8h_af6e6c1cef336f60076e6c7698047c2f4.html#af6e6c1cef336f60076e6c7698047c2f4)   (0) |
|  | Index of center channel in 1.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_af6e6c1cef336f60076e6c7698047c2f4.html#af6e6c1cef336f60076e6c7698047c2f4) |
|  | |
| #define | [AK\_IDX\_SETUP\_1\_LFE](_ak_speaker_config_8h_ab89fccf88bc5ea30d551c52a2fe57b90.html#ab89fccf88bc5ea30d551c52a2fe57b90)   (1) |
|  | Index of low-frequency channel in 1.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ab89fccf88bc5ea30d551c52a2fe57b90.html#ab89fccf88bc5ea30d551c52a2fe57b90) |
|  | |
| #define | [AK\_IDX\_SETUP\_2\_LEFT](_ak_speaker_config_8h_a2be51b449043d3f046d3077e2696a18c.html#a2be51b449043d3f046d3077e2696a18c)   (0) |
|  | Index of left channel in 2.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a2be51b449043d3f046d3077e2696a18c.html#a2be51b449043d3f046d3077e2696a18c) |
|  | |
| #define | [AK\_IDX\_SETUP\_2\_RIGHT](_ak_speaker_config_8h_a66ef38f6c733086f6b6aed8379eab0b1.html#a66ef38f6c733086f6b6aed8379eab0b1)   (1) |
|  | Index of right channel in 2.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a66ef38f6c733086f6b6aed8379eab0b1.html#a66ef38f6c733086f6b6aed8379eab0b1) |
|  | |
| #define | [AK\_IDX\_SETUP\_2\_LFE](_ak_speaker_config_8h_aba394705de67a503b1270010358baf0b.html#aba394705de67a503b1270010358baf0b)   (2) |
|  | Index of low-frequency channel in 2.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aba394705de67a503b1270010358baf0b.html#aba394705de67a503b1270010358baf0b) |
|  | |
| #define | [AK\_IDX\_SETUP\_3\_LEFT](_ak_speaker_config_8h_ae48330580d6640a392674cc7cadb06ee.html#ae48330580d6640a392674cc7cadb06ee)   (0) |
|  | Index of left channel in 3.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ae48330580d6640a392674cc7cadb06ee.html#ae48330580d6640a392674cc7cadb06ee) |
|  | |
| #define | [AK\_IDX\_SETUP\_3\_RIGHT](_ak_speaker_config_8h_aae2076113dd30a2ad75489dd8c5f9a13.html#aae2076113dd30a2ad75489dd8c5f9a13)   (1) |
|  | Index of right channel in 3.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aae2076113dd30a2ad75489dd8c5f9a13.html#aae2076113dd30a2ad75489dd8c5f9a13) |
|  | |
| #define | [AK\_IDX\_SETUP\_3\_CENTER](_ak_speaker_config_8h_aa1b1ab7c35f9dd11b6985f68ab6c8bd9.html#aa1b1ab7c35f9dd11b6985f68ab6c8bd9)   (2) |
|  | Index of center channel in 3.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aa1b1ab7c35f9dd11b6985f68ab6c8bd9.html#aa1b1ab7c35f9dd11b6985f68ab6c8bd9) |
|  | |
| #define | [AK\_IDX\_SETUP\_3\_LFE](_ak_speaker_config_8h_aa7003116ec1b368972f9f3d8d6a5c1c4.html#aa7003116ec1b368972f9f3d8d6a5c1c4)   (3) |
|  | Index of low-frequency channel in 3.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aa7003116ec1b368972f9f3d8d6a5c1c4.html#aa7003116ec1b368972f9f3d8d6a5c1c4) |
|  | |
| #define | [AK\_IDX\_SETUP\_4\_FRONTLEFT](_ak_speaker_config_8h_a2cf8a52cb2bc562409e0192b4738b5ae.html#a2cf8a52cb2bc562409e0192b4738b5ae)   (0) |
|  | Index of front left channel in 4.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a2cf8a52cb2bc562409e0192b4738b5ae.html#a2cf8a52cb2bc562409e0192b4738b5ae) |
|  | |
| #define | [AK\_IDX\_SETUP\_4\_FRONTRIGHT](_ak_speaker_config_8h_ae89be437e01f2544ad377a5c97120b80.html#ae89be437e01f2544ad377a5c97120b80)   (1) |
|  | Index of front right channel in 4.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ae89be437e01f2544ad377a5c97120b80.html#ae89be437e01f2544ad377a5c97120b80) |
|  | |
| #define | [AK\_IDX\_SETUP\_4\_REARLEFT](_ak_speaker_config_8h_af8ade802dd307ea211adfc0ee4df4dcd.html#af8ade802dd307ea211adfc0ee4df4dcd)   (2) |
|  | Index of rear left channel in 4.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_af8ade802dd307ea211adfc0ee4df4dcd.html#af8ade802dd307ea211adfc0ee4df4dcd) |
|  | |
| #define | [AK\_IDX\_SETUP\_4\_REARRIGHT](_ak_speaker_config_8h_a478afbe71c152285b6f1dd68783d7925.html#a478afbe71c152285b6f1dd68783d7925)   (3) |
|  | Index of rear right channel in 4.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a478afbe71c152285b6f1dd68783d7925.html#a478afbe71c152285b6f1dd68783d7925) |
|  | |
| #define | [AK\_IDX\_SETUP\_4\_LFE](_ak_speaker_config_8h_a854868ddce1f35c082d7c841e0b13139.html#a854868ddce1f35c082d7c841e0b13139)   (4) |
|  | Index of low-frequency channel in 4.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a854868ddce1f35c082d7c841e0b13139.html#a854868ddce1f35c082d7c841e0b13139) |
|  | |
| #define | [AK\_IDX\_SETUP\_5\_FRONTLEFT](_ak_speaker_config_8h_adf640a5037af2f21511c6b30f41013bd.html#adf640a5037af2f21511c6b30f41013bd)   (0) |
|  | Index of front left channel in 5.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_adf640a5037af2f21511c6b30f41013bd.html#adf640a5037af2f21511c6b30f41013bd) |
|  | |
| #define | [AK\_IDX\_SETUP\_5\_FRONTRIGHT](_ak_speaker_config_8h_a7406602f495312a9432d9ede8fadf0ab.html#a7406602f495312a9432d9ede8fadf0ab)   (1) |
|  | Index of front right channel in 5.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a7406602f495312a9432d9ede8fadf0ab.html#a7406602f495312a9432d9ede8fadf0ab) |
|  | |
| #define | [AK\_IDX\_SETUP\_5\_CENTER](_ak_speaker_config_8h_a2639ea7a4d6c2a1a0fa9368ef9d15f33.html#a2639ea7a4d6c2a1a0fa9368ef9d15f33)   (2) |
|  | Index of center channel in 5.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a2639ea7a4d6c2a1a0fa9368ef9d15f33.html#a2639ea7a4d6c2a1a0fa9368ef9d15f33) |
|  | |
| #define | [AK\_IDX\_SETUP\_5\_REARLEFT](_ak_speaker_config_8h_ab8c3c92e9f5f601723a56b9709c52f36.html#ab8c3c92e9f5f601723a56b9709c52f36)   (3) |
|  | Index of rear left channel in 5.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ab8c3c92e9f5f601723a56b9709c52f36.html#ab8c3c92e9f5f601723a56b9709c52f36) |
|  | |
| #define | [AK\_IDX\_SETUP\_5\_REARRIGHT](_ak_speaker_config_8h_a579e6a7b350a96375d71949ec6b42c02.html#a579e6a7b350a96375d71949ec6b42c02)   (4) |
|  | Index of rear right channel in 5.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a579e6a7b350a96375d71949ec6b42c02.html#a579e6a7b350a96375d71949ec6b42c02) |
|  | |
| #define | [AK\_IDX\_SETUP\_5\_LFE](_ak_speaker_config_8h_a9d21fa58fb7b09a0133d96e8c53eb69a.html#a9d21fa58fb7b09a0133d96e8c53eb69a)   (5) |
|  | Index of low-frequency channel in 5.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a9d21fa58fb7b09a0133d96e8c53eb69a.html#a9d21fa58fb7b09a0133d96e8c53eb69a) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_FRONTLEFT](_ak_speaker_config_8h_a6eaaf36e06dd92f20678c83faa1113a7.html#a6eaaf36e06dd92f20678c83faa1113a7)   (0) |
|  | Index of front left channel in 6.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a6eaaf36e06dd92f20678c83faa1113a7.html#a6eaaf36e06dd92f20678c83faa1113a7) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_FRONTRIGHT](_ak_speaker_config_8h_ac9ad8b6f672faafbb04e8427fcb11fed.html#ac9ad8b6f672faafbb04e8427fcb11fed)   (1) |
|  | Index of front right channel in 6x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ac9ad8b6f672faafbb04e8427fcb11fed.html#ac9ad8b6f672faafbb04e8427fcb11fed) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_REARLEFT](_ak_speaker_config_8h_aa1371bd9e44fb08dc3568f62c4494d23.html#aa1371bd9e44fb08dc3568f62c4494d23)   (2) |
|  | Index of rear left channel in 6.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aa1371bd9e44fb08dc3568f62c4494d23.html#aa1371bd9e44fb08dc3568f62c4494d23) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_REARRIGHT](_ak_speaker_config_8h_aef66ac3e5cba422ae58799f83352154a.html#aef66ac3e5cba422ae58799f83352154a)   (3) |
|  | Index of rear right channel in 6.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aef66ac3e5cba422ae58799f83352154a.html#aef66ac3e5cba422ae58799f83352154a) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_SIDELEFT](_ak_speaker_config_8h_a9e55a2df949bb1e3f95b069d7a184eb8.html#a9e55a2df949bb1e3f95b069d7a184eb8)   (4) |
|  | Index of side left channel in 6.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a9e55a2df949bb1e3f95b069d7a184eb8.html#a9e55a2df949bb1e3f95b069d7a184eb8) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_SIDERIGHT](_ak_speaker_config_8h_acbc163c2dfefef020e5e574e9db40a2a.html#acbc163c2dfefef020e5e574e9db40a2a)   (5) |
|  | Index of side right channel in 6.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_acbc163c2dfefef020e5e574e9db40a2a.html#acbc163c2dfefef020e5e574e9db40a2a) |
|  | |
| #define | [AK\_IDX\_SETUP\_6\_LFE](_ak_speaker_config_8h_a1afa73df636fd0bc5cb094b313ee1979.html#a1afa73df636fd0bc5cb094b313ee1979)   (6) |
|  | Index of low-frequency channel in 6.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a1afa73df636fd0bc5cb094b313ee1979.html#a1afa73df636fd0bc5cb094b313ee1979) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_FRONTLEFT](_ak_speaker_config_8h_ad07f5173844b0d79287e36059fe4afcb.html#ad07f5173844b0d79287e36059fe4afcb)   (0) |
|  | Index of front left channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ad07f5173844b0d79287e36059fe4afcb.html#ad07f5173844b0d79287e36059fe4afcb) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_FRONTRIGHT](_ak_speaker_config_8h_ad832dcdea5076a8961b098aa0d9190ed.html#ad832dcdea5076a8961b098aa0d9190ed)   (1) |
|  | Index of front right channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_ad832dcdea5076a8961b098aa0d9190ed.html#ad832dcdea5076a8961b098aa0d9190ed) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_CENTER](_ak_speaker_config_8h_a4e26d50d96d0c67b56061847ed665dfc.html#a4e26d50d96d0c67b56061847ed665dfc)   (2) |
|  | Index of center channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a4e26d50d96d0c67b56061847ed665dfc.html#a4e26d50d96d0c67b56061847ed665dfc) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_REARLEFT](_ak_speaker_config_8h_a564d5ff714e8cc8e333df3a204ce45d9.html#a564d5ff714e8cc8e333df3a204ce45d9)   (3) |
|  | Index of rear left channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a564d5ff714e8cc8e333df3a204ce45d9.html#a564d5ff714e8cc8e333df3a204ce45d9) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_REARRIGHT](_ak_speaker_config_8h_add4433784b76b010350f2e3757f21e49.html#add4433784b76b010350f2e3757f21e49)   (4) |
|  | Index of rear right channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_add4433784b76b010350f2e3757f21e49.html#add4433784b76b010350f2e3757f21e49) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_SIDELEFT](_ak_speaker_config_8h_aa40ccb30966b46822fa3c189201f884f.html#aa40ccb30966b46822fa3c189201f884f)   (5) |
|  | Index of side left channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_aa40ccb30966b46822fa3c189201f884f.html#aa40ccb30966b46822fa3c189201f884f) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_SIDERIGHT](_ak_speaker_config_8h_a09fa3a9b9c98770ce0d6359a2b3b8ea3.html#a09fa3a9b9c98770ce0d6359a2b3b8ea3)   (6) |
|  | Index of side right channel in 7.x setups (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a09fa3a9b9c98770ce0d6359a2b3b8ea3.html#a09fa3a9b9c98770ce0d6359a2b3b8ea3) |
|  | |
| #define | [AK\_IDX\_SETUP\_7\_LFE](_ak_speaker_config_8h_a72ce9160c9c6ae1a5d45ac258fb76987.html#a72ce9160c9c6ae1a5d45ac258fb76987)   (7) |
|  | Index of low-frequency channel in 7.1 setup (use with [AkAudioBuffer::GetChannel()](class_ak_audio_buffer_ad2bc3b8ddd61eaa0c111798d5f9e8c9c.html#ad2bc3b8ddd61eaa0c111798d5f9e8c9c)) [更多...](_ak_speaker_config_8h_a72ce9160c9c6ae1a5d45ac258fb76987.html#a72ce9160c9c6ae1a5d45ac258fb76987) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_0\_1](_ak_speaker_config_8h_a2c9f3806994b7ad0ae9fc25da2ff342d.html#a2c9f3806994b7ad0ae9fc25da2ff342d)   ( [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_1\_0\_CENTER](_ak_speaker_config_8h_a1a8221ddbfc9b8531f2ac3c8b5856389.html#a1a8221ddbfc9b8531f2ac3c8b5856389)   ( [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_1\_1\_CENTER](_ak_speaker_config_8h_a398c27d882ae2777c1b6ac1d34cb6227.html#a398c27d882ae2777c1b6ac1d34cb6227)   ( [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_2\_0](_ak_speaker_config_8h_aa4a5d597adddae7f3eba39046a422a20.html#aa4a5d597adddae7f3eba39046a422a20)   ( [AK\_SPEAKER\_FRONT\_LEFT](_ak_speaker_config_8h_aa9dc5afd59709444ca24c974c54b08b3.html#aa9dc5afd59709444ca24c974c54b08b3) | [AK\_SPEAKER\_FRONT\_RIGHT](_ak_speaker_config_8h_a2bf48d2a4c5235e0d5a42d1caa7edd16.html#a2bf48d2a4c5235e0d5a42d1caa7edd16) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_2\_1](_ak_speaker_config_8h_a946ec923d8113b98fde913df523ae4d9.html#a946ec923d8113b98fde913df523ae4d9)   ( [AK\_SPEAKER\_FRONT\_LEFT](_ak_speaker_config_8h_aa9dc5afd59709444ca24c974c54b08b3.html#aa9dc5afd59709444ca24c974c54b08b3) | [AK\_SPEAKER\_FRONT\_RIGHT](_ak_speaker_config_8h_a2bf48d2a4c5235e0d5a42d1caa7edd16.html#a2bf48d2a4c5235e0d5a42d1caa7edd16) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_3\_0](_ak_speaker_config_8h_aab2857823761c88cf0f72d75e31a3ae1.html#aab2857823761c88cf0f72d75e31a3ae1)   ( [AK\_SPEAKER\_FRONT\_LEFT](_ak_speaker_config_8h_aa9dc5afd59709444ca24c974c54b08b3.html#aa9dc5afd59709444ca24c974c54b08b3) | [AK\_SPEAKER\_FRONT\_RIGHT](_ak_speaker_config_8h_a2bf48d2a4c5235e0d5a42d1caa7edd16.html#a2bf48d2a4c5235e0d5a42d1caa7edd16) | [AK\_SPEAKER\_FRONT\_CENTER](_ak_speaker_config_8h_a28805dfa2f63a4ca0174e94ea5113906.html#a28805dfa2f63a4ca0174e94ea5113906) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_3\_1](_ak_speaker_config_8h_a81d15689227a5710dc61d3142d201768.html#a81d15689227a5710dc61d3142d201768)   ( [AK\_SPEAKER\_SETUP\_3\_0](_ak_speaker_config_8h_aab2857823761c88cf0f72d75e31a3ae1.html#aab2857823761c88cf0f72d75e31a3ae1) | [AK\_SPEAKER\_LOW\_FREQUENCY](_ak_speaker_config_8h_a16ecab62413c630ef5d6998a679f4c90.html#a16ecab62413c630ef5d6998a679f4c90) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_FRONT](_ak_speaker_config_8h_a7dc04d1b85313ef9d777fc20f45d50e7.html#a7dc04d1b85313ef9d777fc20f45d50e7)   ( [AK\_SPEAKER\_SETUP\_3\_0](_ak_speaker_config_8h_aab2857823761c88cf0f72d75e31a3ae1.html#aab2857823761c88cf0f72d75e31a3ae1) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_4\_0](_ak_speaker_config_8h_a5ed9bc8d0ea19be71affe2ca5c95bcbc.html#a5ed9bc8d0ea19be71affe2ca5c95bcbc)   ( [AK\_SPEAKER\_SETUP\_4](_ak_speaker_config_8h_ac059469ced9a652f7b16d333b37dd3e7.html#ac059469ced9a652f7b16d333b37dd3e7) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_4\_1](_ak_speaker_config_8h_a90793ff5ab2cdb1016149acb7184bb93.html#a90793ff5ab2cdb1016149acb7184bb93)   ( [AK\_SPEAKER\_SETUP\_4POINT1](_ak_speaker_config_8h_a1afad61d2fd6a3dfcb9af2166371ca33.html#a1afad61d2fd6a3dfcb9af2166371ca33) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_5\_0](_ak_speaker_config_8h_a41e914a7edbd3136753f598934732e9c.html#a41e914a7edbd3136753f598934732e9c)   ( [AK\_SPEAKER\_SETUP\_5](_ak_speaker_config_8h_af181b7b2236165b1e43fc8d54f5dee9d.html#af181b7b2236165b1e43fc8d54f5dee9d) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_5\_1](_ak_speaker_config_8h_af31a62fd1aaec068c10fc05aeda75a7a.html#af31a62fd1aaec068c10fc05aeda75a7a)   ( [AK\_SPEAKER\_SETUP\_5POINT1](_ak_speaker_config_8h_a666b8c74f7cca22244ae5d96b6a665e0.html#a666b8c74f7cca22244ae5d96b6a665e0) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_6\_0](_ak_speaker_config_8h_a3a5b0bc52f5e6f2d5aef4705bebbaa39.html#a3a5b0bc52f5e6f2d5aef4705bebbaa39)   ( [AK\_SPEAKER\_SETUP\_6](_ak_speaker_config_8h_a84fe0119ee9267e7b81357b6816333c1.html#a84fe0119ee9267e7b81357b6816333c1) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_6\_1](_ak_speaker_config_8h_aea2712ca884e3c15c84a819671a56a16.html#aea2712ca884e3c15c84a819671a56a16)   ( [AK\_SPEAKER\_SETUP\_6POINT1](_ak_speaker_config_8h_a008245a635a79cf8c7c2e9e9931cf923.html#a008245a635a79cf8c7c2e9e9931cf923) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_7\_0](_ak_speaker_config_8h_a441d7f29694aac538ea13250b0ea60b9.html#a441d7f29694aac538ea13250b0ea60b9)   ( [AK\_SPEAKER\_SETUP\_7](_ak_speaker_config_8h_ad5760c337a405189f5c005bc9fa83a17.html#ad5760c337a405189f5c005bc9fa83a17) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_7\_1](_ak_speaker_config_8h_a69b5f93e12513edd50b60f5fe763dfd5.html#a69b5f93e12513edd50b60f5fe763dfd5)   ( [AK\_SPEAKER\_SETUP\_7POINT1](_ak_speaker_config_8h_a0220ffe73c82eefb927458d83bdf75b2.html#a0220ffe73c82eefb927458d83bdf75b2) ) |
|  | |
| #define | [AK\_SPEAKER\_SETUP\_DEFAULT\_PLANE](_ak_speaker_config_8h_aa7d7e0237b8c6cfc1ffcdd8e09f1fc59.html#aa7d7e0237b8c6cfc1ffcdd8e09f1fc59)   ([AK\_SPEAKER\_SETUP\_7POINT1](_ak_speaker_config_8h_a0220ffe73c82eefb927458d83bdf75b2.html#a0220ffe73c82eefb927458d83bdf75b2)) |
|  | All speakers on the plane, supported on this platform. [更多...](_ak_speaker_config_8h_aa7d7e0237b8c6cfc1ffcdd8e09f1fc59.html#aa7d7e0237b8c6cfc1ffcdd8e09f1fc59) |
|  | |
| #define | [AK\_SUPPORTED\_STANDARD\_CHANNEL\_MASK](_ak_speaker_config_8h_abb059b9491d28bf5dffd6483bdc2318b.html#abb059b9491d28bf5dffd6483bdc2318b)   ([AK\_SPEAKER\_SETUP\_ALL\_SPEAKERS](_ak_speaker_config_8h_aa1245a2c77e336be3e18af169b514ca2.html#aa1245a2c77e336be3e18af169b514ca2)) |
|  | Platform supports all standard channels. [更多...](_ak_speaker_config_8h_abb059b9491d28bf5dffd6483bdc2318b.html#abb059b9491d28bf5dffd6483bdc2318b) |
|  | |
| #define | [AK\_STANDARD\_MAX\_NUM\_CHANNELS](_ak_speaker_config_8h_af0e6a750b8bd1a2e7dae860a6ab09a08.html#af0e6a750b8bd1a2e7dae860a6ab09a08)   (8) |
|  | Legacy: Platform supports at least 7.1 [更多...](_ak_speaker_config_8h_af0e6a750b8bd1a2e7dae860a6ab09a08.html#af0e6a750b8bd1a2e7dae860a6ab09a08) |
|  | |
| #define | [AK\_MAX\_AMBISONICS\_ORDER](_ak_speaker_config_8h_a6c96b719bb9bccce02e996f97ecc87f0.html#a6c96b719bb9bccce02e996f97ecc87f0)   (5) |
|  | |
| #define | [AK\_DEFAULT\_HEIGHT\_ANGLE](_ak_speaker_config_8h_a0f974c4ff1591d13bf71f302f1bb47ef.html#a0f974c4ff1591d13bf71f302f1bb47ef)   (30.0f) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AK::AkChannelOrdering](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42) {     [AK::ChannelOrdering\_Standard](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42a16ee50f4a4d9625cd070c73544128d6b) = 0, [AK::ChannelOrdering\_Film](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42a71cfc9c9bbb51e58a7305d44d80f26c3), [AK::ChannelOrdering\_FuMa](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42aac59473ce77179f3c651358d13112bd2), [AK::ChannelOrdering\_RunTime](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42a67e706d42068d98a0096313952f0d1be),     [AK::ChannelOrdering\_Last](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42a7723c48c3630d9fc9b05b69f6d51b511)   } |
|  | Channel ordering type. [更多...](namespace_a_k_a96a4d4c0205f609855344ad8365d5e42.html#a96a4d4c0205f609855344ad8365d5e42) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| void | [AK\_SPEAKER\_SETUP\_FIX\_LEFT\_TO\_CENTER](_ak_speaker_config_8h_a63c4fc9ad705ae1f419a3cd459c304d7.html#a63c4fc9ad705ae1f419a3cd459c304d7) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uChannelMask) |
|  | |
| void | [AK\_SPEAKER\_SETUP\_FIX\_REAR\_TO\_SIDE](_ak_speaker_config_8h_ada5bbd27fdefef9d4a2fd51216e82e58.html#ada5bbd27fdefef9d4a2fd51216e82e58) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uChannelMask) |
|  | |
| void | [AK\_SPEAKER\_SETUP\_CONVERT\_TO\_SUPPORTED](_ak_speaker_config_8h_a0e54b2f6cb60334b7e20029018487e2d.html#a0e54b2f6cb60334b7e20029018487e2d) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uChannelMask) |
|  | |
| static [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AK::ChannelMaskToNumChannels](namespace_a_k_a114edb0e4fb01adc0e8280a29e66934c.html#a114edb0e4fb01adc0e8280a29e66934c) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | Returns the number of channels of a given channel configuration. [更多...](namespace_a_k_a114edb0e4fb01adc0e8280a29e66934c.html#a114edb0e4fb01adc0e8280a29e66934c) |
|  | |
| static [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) | [AK::ChannelMaskFromNumChannels](namespace_a_k_a09698cb92a160345e844a0464ea9aaa7.html#a09698cb92a160345e844a0464ea9aaa7) (unsigned int in\_uNumChannels) |
|  | |
| static [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AK::ChannelBitToIndex](namespace_a_k_afe697b2eb4579c071fe31fc9fbab5f92.html#afe697b2eb4579c071fe31fc9fbab5f92) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelBit, [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AK::HasLFE](namespace_a_k_ad484b7e2eca0bdebecc4e4ebfa555ca6.html#ad484b7e2eca0bdebecc4e4ebfa555ca6) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AK::HasCenter](namespace_a_k_ab07695065a6017f7975e5db3a47cf081.html#ab07695065a6017f7975e5db3a47cf081) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK::GetNumberOfAnglesForConfig](namespace_a_k_a0a2881da1ba78c206bbc4f35dd281ac0.html#a0a2881da1ba78c206bbc4f35dd281ac0) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AK::HasSurroundChannels](namespace_a_k_ac9ad6ad649ece19e284071d87d71192e.html#ac9ad6ad649ece19e284071d87d71192e) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AK::HasStrictlyOnePairOfSurroundChannels](namespace_a_k_a93dbd13821bd2b3d9a7c28b51ce98161.html#a93dbd13821bd2b3d9a7c28b51ce98161) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AK::HasSideAndRearChannels](namespace_a_k_abd454ee9de4ce7673572f19f5705b060.html#abd454ee9de4ce7673572f19f5705b060) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) bool | [AK::HasHeightChannels](namespace_a_k_a1e54efe3945cf79913ce12d746b1dbb2.html#a1e54efe3945cf79913ce12d746b1dbb2) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | Returns true if standard configuration represented by channel mask has at least one "height" channel (above the plane). [更多...](namespace_a_k_a1e54efe3945cf79913ce12d746b1dbb2.html#a1e54efe3945cf79913ce12d746b1dbb2) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) | [AK::BackToSideChannels](namespace_a_k_ae8802614b6c166b523c61314bd726ab6.html#ae8802614b6c166b523c61314bd726ab6) ([AkChannelMask](_ak_typedefs_8h_a55aa4d20f0df920eb82ec5d293a6afac.html#a55aa4d20f0df920eb82ec5d293a6afac) in\_uChannelMask) |
|  | |