# AkStreamRecord

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_stream_record-members.html) |
[Public 属性](#pub-attribs)

AkStreamRecord结构体 参考

Stream general information.
[更多...](struct_ak_stream_record.html#details)

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uStreamID](struct_ak_stream_record_aac7aa42ec003b0684aa1d39b20cba685.html#aac7aa42ec003b0684aa1d39b20cba685) |
|  | Unique stream identifier [更多...](struct_ak_stream_record_aac7aa42ec003b0684aa1d39b20cba685.html#aac7aa42ec003b0684aa1d39b20cba685) |
|  | |
| [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) | [deviceID](struct_ak_stream_record_a9292c912f11f11e5b88a413685319fb0.html#a9292c912f11f11e5b88a413685319fb0) |
|  | Device ID [更多...](struct_ak_stream_record_a9292c912f11f11e5b88a413685319fb0.html#a9292c912f11f11e5b88a413685319fb0) |
|  | |
| [AkUtf16](_platforms_2_windows_2_ak_types_8h_aa322c734de4000b9c01ce3c033b59089.html#aa322c734de4000b9c01ce3c033b59089) | [szStreamName](struct_ak_stream_record_a4067f8f74ded427269be5d13cee0b00a.html#a4067f8f74ded427269be5d13cee0b00a) [[AK\_MONITOR\_STREAMNAME\_MAXLENGTH](_i_ak_stream_mgr_8h_a202e0d60e7364c98e0b80dec959562c5.html#a202e0d60e7364c98e0b80dec959562c5)] |
|  | Stream name [更多...](struct_ak_stream_record_a4067f8f74ded427269be5d13cee0b00a.html#a4067f8f74ded427269be5d13cee0b00a) |
|  | |
| [AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) | [idFile](struct_ak_stream_record_aab2ddc0c85baa8bf31dbd2299995fdef.html#aab2ddc0c85baa8bf31dbd2299995fdef) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uStringSize](struct_ak_stream_record_a446ac6becb69ec511e7bd6ed4f9650b3.html#a446ac6becb69ec511e7bd6ed4f9650b3) |
|  | Stream name string's size (number of characters) [更多...](struct_ak_stream_record_a446ac6becb69ec511e7bd6ed4f9650b3.html#a446ac6becb69ec511e7bd6ed4f9650b3) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uFileSize](struct_ak_stream_record_a5f400548b2b599796adef423d4d53680.html#a5f400548b2b599796adef423d4d53680) |
|  | File size   [更多...](struct_ak_stream_record_a5f400548b2b599796adef423d4d53680.html#a5f400548b2b599796adef423d4d53680) |
|  | |
| bool | [bIsAutoStream](struct_ak_stream_record_a84f43ecf2c81b47ede10ebcff1e50d15.html#a84f43ecf2c81b47ede10ebcff1e50d15) |
|  | True for auto streams [更多...](struct_ak_stream_record_a84f43ecf2c81b47ede10ebcff1e50d15.html#a84f43ecf2c81b47ede10ebcff1e50d15) |
|  | |
| bool | [bIsCachingStream](struct_ak_stream_record_a4932a4e47f1bea2fa568e866c2b14aff.html#a4932a4e47f1bea2fa568e866c2b14aff) |
|  | True for caching streams [更多...](struct_ak_stream_record_a4932a4e47f1bea2fa568e866c2b14aff.html#a4932a4e47f1bea2fa568e866c2b14aff) |
|  | |

## 详细描述

Stream general information.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [155](_i_ak_stream_mgr_8h_source.html#l00155) 行定义.