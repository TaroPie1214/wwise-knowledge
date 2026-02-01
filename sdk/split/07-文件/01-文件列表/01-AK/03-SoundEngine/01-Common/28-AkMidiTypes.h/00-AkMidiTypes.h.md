# AkMidiTypes.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[变量](#var-members)

AkMidiTypes.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_midi_types_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkMIDIGen](struct_ak_m_i_d_i_gen.html) |
|  | |
| struct | [AkMIDINote](struct_ak_m_i_d_i_note.html) |
|  | |
| struct | [AkMIDICC](struct_ak_m_i_d_i_c_c.html) |
|  | |
| struct | [AkMIDIPitchbend](struct_ak_m_i_d_i_pitchbend.html) |
|  | |
| struct | [AkMIDINoteAftertouch](struct_ak_m_i_d_i_note_aftertouch.html) |
|  | |
| struct | [AkMIDIChannelAftertouch](struct_ak_m_i_d_i_channel_aftertouch.html) |
|  | |
| struct | [AkMIDIProgramChange](struct_ak_m_i_d_i_program_change.html) |
|  | |
| struct | [AkMIDIWwiseCmd](struct_ak_m_i_d_i_wwise_cmd.html) |
|  | |
| struct | [AkMIDIEvent](struct_ak_m_i_d_i_event.html) |
|  | |
| struct | [AkMIDIPost](struct_ak_m_i_d_i_post.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_INVALID](_ak_midi_types_8h_ab7eba7b4063dd66219b9c92ad66ba332.html#ab7eba7b4063dd66219b9c92ad66ba332)   0x00 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_NOTE\_OFF](_ak_midi_types_8h_a4e80b2ac02932beebf56df69d409b072.html#a4e80b2ac02932beebf56df69d409b072)   0x80 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_NOTE\_ON](_ak_midi_types_8h_ab12db90c72e49a3514ad0e77b296fa5e.html#ab12db90c72e49a3514ad0e77b296fa5e)   0x90 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_NOTE\_AFTERTOUCH](_ak_midi_types_8h_abfa64b516eddbc43c695a2e02bb9a158.html#abfa64b516eddbc43c695a2e02bb9a158)   0xa0 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_CONTROLLER](_ak_midi_types_8h_a1590bc4bb3ea12ef9ef15c705f08b6fc.html#a1590bc4bb3ea12ef9ef15c705f08b6fc)   0xb0 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_PROGRAM\_CHANGE](_ak_midi_types_8h_ad8b850fdd702ef2275428f4b32615ddb.html#ad8b850fdd702ef2275428f4b32615ddb)   0xc0 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_CHANNEL\_AFTERTOUCH](_ak_midi_types_8h_ac275234d6f92b28addbbae5e70497dc4.html#ac275234d6f92b28addbbae5e70497dc4)   0xd0 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_PITCH\_BEND](_ak_midi_types_8h_a8af9e8d3cef234551d0443a75e92b6db.html#a8af9e8d3cef234551d0443a75e92b6db)   0xe0 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_SYSEX](_ak_midi_types_8h_a58fc4ee22d50eead08fb635d03e2b675.html#a58fc4ee22d50eead08fb635d03e2b675)   0xf0 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_ESCAPE](_ak_midi_types_8h_a80557eeec9313b2e4142f4221066aecc.html#a80557eeec9313b2e4142f4221066aecc)   0xf7 |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_WWISE\_CMD](_ak_midi_types_8h_af2798a84c1f017cd6859dc4f6ab82482.html#af2798a84c1f017cd6859dc4f6ab82482)   0xfe |
|  | |
| #define | [AK\_MIDI\_EVENT\_TYPE\_META](_ak_midi_types_8h_ae5b718c19d163184c73f03d7f7e15ae6.html#ae5b718c19d163184c73f03d7f7e15ae6)   0xff |
|  | |
| #define | [AK\_MIDI\_CC\_BANK\_SELECT\_COARSE](_ak_midi_types_8h_a486900125f1145e3e7e150b6663c9c30.html#a486900125f1145e3e7e150b6663c9c30)   0 |
|  | |
| #define | [AK\_MIDI\_CC\_MOD\_WHEEL\_COARSE](_ak_midi_types_8h_a8ea7742821a372063afe70d568426eb5.html#a8ea7742821a372063afe70d568426eb5)   1 |
|  | |
| #define | [AK\_MIDI\_CC\_BREATH\_CTRL\_COARSE](_ak_midi_types_8h_a3167db977f5e43b1567d0baf33d68989.html#a3167db977f5e43b1567d0baf33d68989)   2 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_3\_COARSE](_ak_midi_types_8h_ad6ca19cac64e7b8ae6720d83ca3ffacd.html#ad6ca19cac64e7b8ae6720d83ca3ffacd)   3 |
|  | |
| #define | [AK\_MIDI\_CC\_FOOT\_PEDAL\_COARSE](_ak_midi_types_8h_a3f7d07c8c68451ae5e00b151538ef9b3.html#a3f7d07c8c68451ae5e00b151538ef9b3)   4 |
|  | |
| #define | [AK\_MIDI\_CC\_PORTAMENTO\_COARSE](_ak_midi_types_8h_a9f3664d9ff631b6761e34f05c2b3e78e.html#a9f3664d9ff631b6761e34f05c2b3e78e)   5 |
|  | |
| #define | [AK\_MIDI\_CC\_DATA\_ENTRY\_COARSE](_ak_midi_types_8h_ad954ec1c10fd8b2ecda296a664773710.html#ad954ec1c10fd8b2ecda296a664773710)   6 |
|  | |
| #define | [AK\_MIDI\_CC\_VOLUME\_COARSE](_ak_midi_types_8h_a85e5d17dfef525d3ace224edad582074.html#a85e5d17dfef525d3ace224edad582074)   7 |
|  | |
| #define | [AK\_MIDI\_CC\_BALANCE\_COARSE](_ak_midi_types_8h_a32bfb53957bec86bd7c401a9e86fd278.html#a32bfb53957bec86bd7c401a9e86fd278)   8 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_9\_COARSE](_ak_midi_types_8h_a30b87f6298cca9b335bc5309cada62dc.html#a30b87f6298cca9b335bc5309cada62dc)   9 |
|  | |
| #define | [AK\_MIDI\_CC\_PAN\_POSITION\_COARSE](_ak_midi_types_8h_a563a03c57a2a0d7e6c826ff23684dec5.html#a563a03c57a2a0d7e6c826ff23684dec5)   10 |
|  | |
| #define | [AK\_MIDI\_CC\_EXPRESSION\_COARSE](_ak_midi_types_8h_a77895e7b4fb00be493ee689768943e83.html#a77895e7b4fb00be493ee689768943e83)   11 |
|  | |
| #define | [AK\_MIDI\_CC\_EFFECT\_CTRL\_1\_COARSE](_ak_midi_types_8h_a45715d770195e25ad59a435298a60de9.html#a45715d770195e25ad59a435298a60de9)   12 |
|  | |
| #define | [AK\_MIDI\_CC\_EFFECT\_CTRL\_2\_COARSE](_ak_midi_types_8h_a3e2c16e46303033fc658e018740c9ac4.html#a3e2c16e46303033fc658e018740c9ac4)   13 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_14\_COARSE](_ak_midi_types_8h_a6622557fc967e61edc5b3516cc44a7b1.html#a6622557fc967e61edc5b3516cc44a7b1)   14 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_15\_COARSE](_ak_midi_types_8h_adffbb9362c47aa06091a3850f619afea.html#adffbb9362c47aa06091a3850f619afea)   15 |
|  | |
| #define | [AK\_MIDI\_CC\_GEN\_SLIDER\_1](_ak_midi_types_8h_a5ca5b99d63c1c2fdbf13239dadafe1b9.html#a5ca5b99d63c1c2fdbf13239dadafe1b9)   16 |
|  | |
| #define | [AK\_MIDI\_CC\_GEN\_SLIDER\_2](_ak_midi_types_8h_a6b4d9c041eeb7fce1a149a3ef0b0803a.html#a6b4d9c041eeb7fce1a149a3ef0b0803a)   17 |
|  | |
| #define | [AK\_MIDI\_CC\_GEN\_SLIDER\_3](_ak_midi_types_8h_a9d08a59bc7d09f6908c3dacb5bc06894.html#a9d08a59bc7d09f6908c3dacb5bc06894)   18 |
|  | |
| #define | [AK\_MIDI\_CC\_GEN\_SLIDER\_4](_ak_midi_types_8h_a826e4a95a056efad9f4c74f623e4a37e.html#a826e4a95a056efad9f4c74f623e4a37e)   19 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_20\_COARSE](_ak_midi_types_8h_a1cce3f62d5bfee980bb7438eb17e2613.html#a1cce3f62d5bfee980bb7438eb17e2613)   20 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_21\_COARSE](_ak_midi_types_8h_abe6674c3342b10713a610949832b41e2.html#abe6674c3342b10713a610949832b41e2)   21 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_22\_COARSE](_ak_midi_types_8h_a6a2fc300931bde2c07bef8646ae48893.html#a6a2fc300931bde2c07bef8646ae48893)   22 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_23\_COARSE](_ak_midi_types_8h_a4e0cb9d559a513969d4518cf66bbe23c.html#a4e0cb9d559a513969d4518cf66bbe23c)   23 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_24\_COARSE](_ak_midi_types_8h_ab6557e6454f10a71e3a073d89a9f8e76.html#ab6557e6454f10a71e3a073d89a9f8e76)   24 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_25\_COARSE](_ak_midi_types_8h_a888b06778ae4adf2c04f7f440a218b7a.html#a888b06778ae4adf2c04f7f440a218b7a)   25 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_26\_COARSE](_ak_midi_types_8h_aed8dd606225a351254d6f0873ebc278a.html#aed8dd606225a351254d6f0873ebc278a)   26 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_27\_COARSE](_ak_midi_types_8h_a162d1984e70da18f11a74846d4905af1.html#a162d1984e70da18f11a74846d4905af1)   27 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_28\_COARSE](_ak_midi_types_8h_a6b8235e74f07286b56cd497b8bd69aaf.html#a6b8235e74f07286b56cd497b8bd69aaf)   28 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_29\_COARSE](_ak_midi_types_8h_a90c3a84356e799a8987341edbadaf142.html#a90c3a84356e799a8987341edbadaf142)   29 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_30\_COARSE](_ak_midi_types_8h_af0bb45cbece4dd79b89ef07b7de5b129.html#af0bb45cbece4dd79b89ef07b7de5b129)   30 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_31\_COARSE](_ak_midi_types_8h_ab1b3627896f6514d8659500931cbb1a5.html#ab1b3627896f6514d8659500931cbb1a5)   31 |
|  | |
| #define | [AK\_MIDI\_CC\_BANK\_SELECT\_FINE](_ak_midi_types_8h_aea21db0bfe29824042691a1cfec7fc8d.html#aea21db0bfe29824042691a1cfec7fc8d)   32 |
|  | |
| #define | [AK\_MIDI\_CC\_MOD\_WHEEL\_FINE](_ak_midi_types_8h_a3db1fbc7ae26b6f21c8947a724d32132.html#a3db1fbc7ae26b6f21c8947a724d32132)   33 |
|  | |
| #define | [AK\_MIDI\_CC\_BREATH\_CTRL\_FINE](_ak_midi_types_8h_a43e3d932373047a498fb5e60205886a1.html#a43e3d932373047a498fb5e60205886a1)   34 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_3\_FINE](_ak_midi_types_8h_a6051c6cf5ca4b5580deb8828210f6658.html#a6051c6cf5ca4b5580deb8828210f6658)   35 |
|  | |
| #define | [AK\_MIDI\_CC\_FOOT\_PEDAL\_FINE](_ak_midi_types_8h_aba9595259418e8d6ece30589cc84b6a5.html#aba9595259418e8d6ece30589cc84b6a5)   36 |
|  | |
| #define | [AK\_MIDI\_CC\_PORTAMENTO\_FINE](_ak_midi_types_8h_a4a068efac4bee9fff7db505abb2c5fe3.html#a4a068efac4bee9fff7db505abb2c5fe3)   37 |
|  | |
| #define | [AK\_MIDI\_CC\_DATA\_ENTRY\_FINE](_ak_midi_types_8h_acb7d79f769d825d42ea71a8d1442afc7.html#acb7d79f769d825d42ea71a8d1442afc7)   38 |
|  | |
| #define | [AK\_MIDI\_CC\_VOLUME\_FINE](_ak_midi_types_8h_af7cbdceea913354e832db0e4f2bb0db5.html#af7cbdceea913354e832db0e4f2bb0db5)   39 |
|  | |
| #define | [AK\_MIDI\_CC\_BALANCE\_FINE](_ak_midi_types_8h_a1342e10e797e78777b151455e3419ce9.html#a1342e10e797e78777b151455e3419ce9)   40 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_9\_FINE](_ak_midi_types_8h_af3e2aea15876c0c5d746c3143c5ca943.html#af3e2aea15876c0c5d746c3143c5ca943)   41 |
|  | |
| #define | [AK\_MIDI\_CC\_PAN\_POSITION\_FINE](_ak_midi_types_8h_aa71291bba0b0325ae5a4bc57ea3aa70c.html#aa71291bba0b0325ae5a4bc57ea3aa70c)   42 |
|  | |
| #define | [AK\_MIDI\_CC\_EXPRESSION\_FINE](_ak_midi_types_8h_a43e3865bd7cde60042b649ec7627f507.html#a43e3865bd7cde60042b649ec7627f507)   43 |
|  | |
| #define | [AK\_MIDI\_CC\_EFFECT\_CTRL\_1\_FINE](_ak_midi_types_8h_abee7418c9f5c9a3e2f58ee56edcf452b.html#abee7418c9f5c9a3e2f58ee56edcf452b)   44 |
|  | |
| #define | [AK\_MIDI\_CC\_EFFECT\_CTRL\_2\_FINE](_ak_midi_types_8h_aff348584e17610340b444f9444621023.html#aff348584e17610340b444f9444621023)   45 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_14\_FINE](_ak_midi_types_8h_ae9ece4d9d6ae57bd3ebfa6fd67b17834.html#ae9ece4d9d6ae57bd3ebfa6fd67b17834)   46 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_15\_FINE](_ak_midi_types_8h_acc4aa798c80d1409dd38611dad7299f8.html#acc4aa798c80d1409dd38611dad7299f8)   47 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_20\_FINE](_ak_midi_types_8h_a5648ac2113cf17c3fdcb66ef9b102e85.html#a5648ac2113cf17c3fdcb66ef9b102e85)   52 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_21\_FINE](_ak_midi_types_8h_ae8d42472e6ff9c5152a54fc43e6eea58.html#ae8d42472e6ff9c5152a54fc43e6eea58)   53 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_22\_FINE](_ak_midi_types_8h_a403a4541e1bbeaadd3b9a79791fe3778.html#a403a4541e1bbeaadd3b9a79791fe3778)   54 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_23\_FINE](_ak_midi_types_8h_ad273c6d3fc6c35b74f30c4d855aabe74.html#ad273c6d3fc6c35b74f30c4d855aabe74)   55 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_24\_FINE](_ak_midi_types_8h_a3548f57f23e71f4cd0d5383794de1bfe.html#a3548f57f23e71f4cd0d5383794de1bfe)   56 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_25\_FINE](_ak_midi_types_8h_a98584f7d91ef03b9e0a4488723265bac.html#a98584f7d91ef03b9e0a4488723265bac)   57 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_26\_FINE](_ak_midi_types_8h_a4223ad4749c454bb2b2088f6b62b7415.html#a4223ad4749c454bb2b2088f6b62b7415)   58 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_27\_FINE](_ak_midi_types_8h_ab136a42ea1fa88fedbf610879cd1df9a.html#ab136a42ea1fa88fedbf610879cd1df9a)   59 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_28\_FINE](_ak_midi_types_8h_a418f27b04436b05da924568c188e7818.html#a418f27b04436b05da924568c188e7818)   60 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_29\_FINE](_ak_midi_types_8h_acba937f5288d7aa4be5d8cb85be14961.html#acba937f5288d7aa4be5d8cb85be14961)   61 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_30\_FINE](_ak_midi_types_8h_a505846bc5ecb17230f2a50573f869292.html#a505846bc5ecb17230f2a50573f869292)   62 |
|  | |
| #define | [AK\_MIDI\_CC\_CTRL\_31\_FINE](_ak_midi_types_8h_abc7f5611ccc503173bcc81d5c444fd5d.html#abc7f5611ccc503173bcc81d5c444fd5d)   63 |
|  | |
| #define | [AK\_MIDI\_CC\_HOLD\_PEDAL](_ak_midi_types_8h_af78bb97626ab7c2a8a7437565b724caf.html#af78bb97626ab7c2a8a7437565b724caf)   64 |
|  | |
| #define | [AK\_MIDI\_CC\_PORTAMENTO\_ON\_OFF](_ak_midi_types_8h_a36e5506ecf9c63047c593e44ddbf91e7.html#a36e5506ecf9c63047c593e44ddbf91e7)   65 |
|  | |
| #define | [AK\_MIDI\_CC\_SUSTENUTO\_PEDAL](_ak_midi_types_8h_acb79e401df3d6ca9cf9648ae8faa8e2d.html#acb79e401df3d6ca9cf9648ae8faa8e2d)   66 |
|  | |
| #define | [AK\_MIDI\_CC\_SOFT\_PEDAL](_ak_midi_types_8h_a7f3bb5325c0cbff786ed91a61644096c.html#a7f3bb5325c0cbff786ed91a61644096c)   67 |
|  | |
| #define | [AK\_MIDI\_CC\_LEGATO\_PEDAL](_ak_midi_types_8h_af550878aa36b3145db8b0f838696cfc3.html#af550878aa36b3145db8b0f838696cfc3)   68 |
|  | |
| #define | [AK\_MIDI\_CC\_HOLD\_PEDAL\_2](_ak_midi_types_8h_a53b22524cdd0bb4c885613dac1de5b6e.html#a53b22524cdd0bb4c885613dac1de5b6e)   69 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_VARIATION](_ak_midi_types_8h_a6261bbdb80c8e35b9cc323e1a7a2fa77.html#a6261bbdb80c8e35b9cc323e1a7a2fa77)   70 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_TIMBRE](_ak_midi_types_8h_a8ceddf782756152ecdbe7f36ffa70b24.html#a8ceddf782756152ecdbe7f36ffa70b24)   71 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_RELEASE\_TIME](_ak_midi_types_8h_a0bba995121bb7668c820aa0af9c9d79e.html#a0bba995121bb7668c820aa0af9c9d79e)   72 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_ATTACK\_TIME](_ak_midi_types_8h_a70c4aafb1895af5113732e2c4c2e6754.html#a70c4aafb1895af5113732e2c4c2e6754)   73 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_BRIGHTNESS](_ak_midi_types_8h_ab214f6788251b23b5f30c5c7e9e494b1.html#ab214f6788251b23b5f30c5c7e9e494b1)   74 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_CTRL\_6](_ak_midi_types_8h_a634e0c3e10c99df3c23f6f315af54ee5.html#a634e0c3e10c99df3c23f6f315af54ee5)   75 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_CTRL\_7](_ak_midi_types_8h_a7a3a7c980d7a0e2db588a1fbc670f4b4.html#a7a3a7c980d7a0e2db588a1fbc670f4b4)   76 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_CTRL\_8](_ak_midi_types_8h_a8b38e1a3cde927b24ad81c8da4abfe1c.html#a8b38e1a3cde927b24ad81c8da4abfe1c)   77 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_CTRL\_9](_ak_midi_types_8h_a8a67b7e9638962619add38a9732e2194.html#a8a67b7e9638962619add38a9732e2194)   78 |
|  | |
| #define | [AK\_MIDI\_CC\_SOUND\_CTRL\_10](_ak_midi_types_8h_ab6fab777c34485bed581407dadce8ec1.html#ab6fab777c34485bed581407dadce8ec1)   79 |
|  | |
| #define | [AK\_MIDI\_CC\_GENERAL\_BUTTON\_1](_ak_midi_types_8h_a149d51ecfb6ca7a33a2d999b46de98f4.html#a149d51ecfb6ca7a33a2d999b46de98f4)   80 |
|  | |
| #define | [AK\_MIDI\_CC\_GENERAL\_BUTTON\_2](_ak_midi_types_8h_a805292d7430431b275ef2da75fccf1c9.html#a805292d7430431b275ef2da75fccf1c9)   81 |
|  | |
| #define | [AK\_MIDI\_CC\_GENERAL\_BUTTON\_3](_ak_midi_types_8h_aa1b55d44523e5cab62da5251839c0dc3.html#aa1b55d44523e5cab62da5251839c0dc3)   82 |
|  | |
| #define | [AK\_MIDI\_CC\_GENERAL\_BUTTON\_4](_ak_midi_types_8h_a58a2f9873c0591399560e7359e7fbcd3.html#a58a2f9873c0591399560e7359e7fbcd3)   83 |
|  | |
| #define | [AK\_MIDI\_CC\_REVERB\_LEVEL](_ak_midi_types_8h_a768762e640340ebe58b0e2bb36d1d0a6.html#a768762e640340ebe58b0e2bb36d1d0a6)   91 |
|  | |
| #define | [AK\_MIDI\_CC\_TREMOLO\_LEVEL](_ak_midi_types_8h_a6d33aef2221ff9d13e90f988904699da.html#a6d33aef2221ff9d13e90f988904699da)   92 |
|  | |
| #define | [AK\_MIDI\_CC\_CHORUS\_LEVEL](_ak_midi_types_8h_a3d178a008afa2b57c127f7f714193805.html#a3d178a008afa2b57c127f7f714193805)   93 |
|  | |
| #define | [AK\_MIDI\_CC\_CELESTE\_LEVEL](_ak_midi_types_8h_a05abf22534ed2ac2d4fd0f7f6e7db148.html#a05abf22534ed2ac2d4fd0f7f6e7db148)   94 |
|  | |
| #define | [AK\_MIDI\_CC\_PHASER\_LEVEL](_ak_midi_types_8h_a80888025204152b5321a0de17d63b054.html#a80888025204152b5321a0de17d63b054)   95 |
|  | |
| #define | [AK\_MIDI\_CC\_DATA\_BUTTON\_P1](_ak_midi_types_8h_a11199c5999a807b40ee68bfbafcc34d7.html#a11199c5999a807b40ee68bfbafcc34d7)   96 |
|  | |
| #define | [AK\_MIDI\_CC\_DATA\_BUTTON\_M1](_ak_midi_types_8h_ae5681583fdece0e95f1833bf2be253ab.html#ae5681583fdece0e95f1833bf2be253ab)   97 |
|  | |
| #define | [AK\_MIDI\_CC\_NON\_REGISTER\_COARSE](_ak_midi_types_8h_a2d2c9db2672823a7a62ce81aba71b3b7.html#a2d2c9db2672823a7a62ce81aba71b3b7)   98 |
|  | |
| #define | [AK\_MIDI\_CC\_NON\_REGISTER\_FINE](_ak_midi_types_8h_adcff06e0dfeec0944aed4bc13767f8ba.html#adcff06e0dfeec0944aed4bc13767f8ba)   99 |
|  | |
| #define | [AK\_MIDI\_CC\_ALL\_SOUND\_OFF](_ak_midi_types_8h_a89a039b1e73edbbf8f5d3af3c4f39e37.html#a89a039b1e73edbbf8f5d3af3c4f39e37)   120 |
|  | |
| #define | [AK\_MIDI\_CC\_ALL\_CONTROLLERS\_OFF](_ak_midi_types_8h_a773631d2ed5b332db350d1be3cba5544.html#a773631d2ed5b332db350d1be3cba5544)   121 |
|  | |
| #define | [AK\_MIDI\_CC\_LOCAL\_KEYBOARD](_ak_midi_types_8h_abc95e3afe9ae51b1ff61f1494da5bfb9.html#abc95e3afe9ae51b1ff61f1494da5bfb9)   122 |
|  | |
| #define | [AK\_MIDI\_CC\_ALL\_NOTES\_OFF](_ak_midi_types_8h_a2f3df49090748c840c8ec3d1c96ddb12.html#a2f3df49090748c840c8ec3d1c96ddb12)   123 |
|  | |
| #define | [AK\_MIDI\_CC\_OMNI\_MODE\_OFF](_ak_midi_types_8h_a93e8cbc52f823744ecc9831b00c6cb6a.html#a93e8cbc52f823744ecc9831b00c6cb6a)   124 |
|  | |
| #define | [AK\_MIDI\_CC\_OMNI\_MODE\_ON](_ak_midi_types_8h_a3492b10fe7650817f1cf79908358ac7f.html#a3492b10fe7650817f1cf79908358ac7f)   125 |
|  | |
| #define | [AK\_MIDI\_CC\_OMNI\_MONOPHONIC\_ON](_ak_midi_types_8h_a6749fb2d7afdcaf91d87b30e24f2ffd9.html#a6749fb2d7afdcaf91d87b30e24f2ffd9)   126 |
|  | |
| #define | [AK\_MIDI\_CC\_OMNI\_POLYPHONIC\_ON](_ak_midi_types_8h_a2ffc18777e095b529ec0b359710edd80.html#a2ffc18777e095b529ec0b359710edd80)   127 |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkMidiChannelNo](_ak_midi_types_8h_a04087ee2bce0372883d5e328c7314639.html#a04087ee2bce0372883d5e328c7314639) |
|  | MIDI channel number, usually 0-15.   [更多...](_ak_midi_types_8h_a04087ee2bce0372883d5e328c7314639.html#a04087ee2bce0372883d5e328c7314639) |
|  | |
| typedef [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [AkMidiNoteNo](_ak_midi_types_8h_a83e69ea8c28e2e860bfc352a91b7f8aa.html#a83e69ea8c28e2e860bfc352a91b7f8aa) |
|  | MIDI note number.   [更多...](_ak_midi_types_8h_a83e69ea8c28e2e860bfc352a91b7f8aa.html#a83e69ea8c28e2e860bfc352a91b7f8aa) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| static const [AkMidiChannelNo](_ak_midi_types_8h_a04087ee2bce0372883d5e328c7314639.html#a04087ee2bce0372883d5e328c7314639) | [AK\_INVALID\_MIDI\_CHANNEL](_ak_midi_types_8h_a047e9251918d8cfa3b845333f37c0819.html#a047e9251918d8cfa3b845333f37c0819) = ([AkMidiChannelNo](_ak_midi_types_8h_a04087ee2bce0372883d5e328c7314639.html#a04087ee2bce0372883d5e328c7314639))-1 |
|  | Not a valid midi channel [更多...](_ak_midi_types_8h_a047e9251918d8cfa3b845333f37c0819.html#a047e9251918d8cfa3b845333f37c0819) |
|  | |
| static const [AkMidiNoteNo](_ak_midi_types_8h_a83e69ea8c28e2e860bfc352a91b7f8aa.html#a83e69ea8c28e2e860bfc352a91b7f8aa) | [AK\_INVALID\_MIDI\_NOTE](_ak_midi_types_8h_a619b065d9fd214f195c0042ac04f30a6.html#a619b065d9fd214f195c0042ac04f30a6) = ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270))-1 |
|  | Not a valid midi note [更多...](_ak_midi_types_8h_a619b065d9fd214f195c0042ac04f30a6.html#a619b065d9fd214f195c0042ac04f30a6) |
|  | |

## 详细描述

Data type definitions.

在文件 [AkMidiTypes.h](_ak_midi_types_8h_source.html) 中定义.