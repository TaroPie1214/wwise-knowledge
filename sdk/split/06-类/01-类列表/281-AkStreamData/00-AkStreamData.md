# AkStreamData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_stream_data-members.html) |
[Public 属性](#pub-attribs)

AkStreamData结构体 参考

Stream statistics.
[更多...](struct_ak_stream_data.html#details)

`#include <IAkStreamMgr.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uStreamID](struct_ak_stream_data_a652fea59ea1bcfda44cd382aed609663.html#a652fea59ea1bcfda44cd382aed609663) |
|  | Unique stream identifier [更多...](struct_ak_stream_data_a652fea59ea1bcfda44cd382aed609663.html#a652fea59ea1bcfda44cd382aed609663) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPriority](struct_ak_stream_data_ac5f6b997a21d6739ebbf9bfb57847410.html#ac5f6b997a21d6739ebbf9bfb57847410) |
|  | Stream priority [更多...](struct_ak_stream_data_ac5f6b997a21d6739ebbf9bfb57847410.html#ac5f6b997a21d6739ebbf9bfb57847410) |
|  | |
| [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) | [uFilePosition](struct_ak_stream_data_a9272e0f82d556ce4ebdb54fe9ca43f3b.html#a9272e0f82d556ce4ebdb54fe9ca43f3b) |
|  | Current position [更多...](struct_ak_stream_data_a9272e0f82d556ce4ebdb54fe9ca43f3b.html#a9272e0f82d556ce4ebdb54fe9ca43f3b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uTargetBufferingSize](struct_ak_stream_data_ae99cae76c8a5700ee0827474fcd45129.html#ae99cae76c8a5700ee0827474fcd45129) |
|  | Total stream buffer size (specific to IAkAutoStream) [更多...](struct_ak_stream_data_ae99cae76c8a5700ee0827474fcd45129.html#ae99cae76c8a5700ee0827474fcd45129) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uVirtualBufferingSize](struct_ak_stream_data_a5c90c3704839cc9297a0cfd3f7cd5997.html#a5c90c3704839cc9297a0cfd3f7cd5997) |
|  | Size of available data including requested data (specific to IAkAutoStream) [更多...](struct_ak_stream_data_a5c90c3704839cc9297a0cfd3f7cd5997.html#a5c90c3704839cc9297a0cfd3f7cd5997) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBufferedSize](struct_ak_stream_data_a2e6897fdfc3fb85b8ed0fa04bd4d621d.html#a2e6897fdfc3fb85b8ed0fa04bd4d621d) |
|  | Size of available data (specific to IAkAutoStream) [更多...](struct_ak_stream_data_a2e6897fdfc3fb85b8ed0fa04bd4d621d.html#a2e6897fdfc3fb85b8ed0fa04bd4d621d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumBytesTransfered](struct_ak_stream_data_a83c675cc254fe780eed722a35b291362.html#a83c675cc254fe780eed722a35b291362) |
|  | Transfered amount since last query (Accumulate/Reset) [更多...](struct_ak_stream_data_a83c675cc254fe780eed722a35b291362.html#a83c675cc254fe780eed722a35b291362) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumBytesTransferedLowLevel](struct_ak_stream_data_ae8ddd549368bff6b6ae60e0d03effa67.html#ae8ddd549368bff6b6ae60e0d03effa67) |
|  | Transfered amount (from low-level IO only) since last query (Accumulate/Reset) [更多...](struct_ak_stream_data_ae8ddd549368bff6b6ae60e0d03effa67.html#ae8ddd549368bff6b6ae60e0d03effa67) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemoryReferenced](struct_ak_stream_data_a9fbdbb868ac2414212d1aa6832ca4706.html#a9fbdbb868ac2414212d1aa6832ca4706) |
|  | Amount of streaming memory referenced by this stream [更多...](struct_ak_stream_data_a9fbdbb868ac2414212d1aa6832ca4706.html#a9fbdbb868ac2414212d1aa6832ca4706) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fEstimatedThroughput](struct_ak_stream_data_ab0b5b48902d09548af23413fb31377d7.html#ab0b5b48902d09548af23413fb31377d7) |
|  | Estimated throughput heuristic [更多...](struct_ak_stream_data_ab0b5b48902d09548af23413fb31377d7.html#ab0b5b48902d09548af23413fb31377d7) |
|  | |
| bool | [bActive](struct_ak_stream_data_ae6fb479d60a096e81be8c37ed079de29.html#ae6fb479d60a096e81be8c37ed079de29) |
|  | True if this stream has been active (that is, was ready for I/O or had at least one pending I/O transfer, uncached or not) in the previous frame [更多...](struct_ak_stream_data_ae6fb479d60a096e81be8c37ed079de29.html#ae6fb479d60a096e81be8c37ed079de29) |
|  | |

## 详细描述

Stream statistics.

在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [168](_i_ak_stream_mgr_8h_source.html#l00168) 行定义.