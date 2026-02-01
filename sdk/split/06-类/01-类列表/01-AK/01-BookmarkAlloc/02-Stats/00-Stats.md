# Stats

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [BookmarkAlloc](namespace_a_k_1_1_bookmark_alloc.html)
- [Stats](struct_a_k_1_1_bookmark_alloc_1_1_stats.html)

[所有成员列表](struct_a_k_1_1_bookmark_alloc_1_1_stats-members.html) |
[Public 属性](#pub-attribs)

AK::BookmarkAlloc::Stats结构体 参考

`#include <AkTempAllocDefs.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uRecentPeakMemUsed](struct_a_k_1_1_bookmark_alloc_1_1_stats_aac7e15c32ebf613e64b1b6f2a2cb9f75.html#aac7e15c32ebf613e64b1b6f2a2cb9f75) |
|  | Peak used memory in a single [BookmarkAlloc](namespace_a_k_1_1_bookmark_alloc.html) region since the last tick (in bytes). [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_aac7e15c32ebf613e64b1b6f2a2cb9f75.html#aac7e15c32ebf613e64b1b6f2a2cb9f75) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uRecentBlocksFetched](struct_a_k_1_1_bookmark_alloc_1_1_stats_afa04e0033565e5671592283b59f0f749.html#afa04e0033565e5671592283b59f0f749) |
|  | Number of times a block was fetched from the cache, not including the base block. High values here may indicate that block sizes need to be larger. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_afa04e0033565e5671592283b59f0f749.html#afa04e0033565e5671592283b59f0f749) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemAllocated](struct_a_k_1_1_bookmark_alloc_1_1_stats_affe5b5898848da7822c347cfb3e85cc6.html#affe5b5898848da7822c347cfb3e85cc6) |
|  | Currently allocated memory (in bytes). [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_affe5b5898848da7822c347cfb3e85cc6.html#affe5b5898848da7822c347cfb3e85cc6) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBlocksAllocated](struct_a_k_1_1_bookmark_alloc_1_1_stats_a0e6125fe8d4c3cd6cc3ed82b59ca549f.html#a0e6125fe8d4c3cd6cc3ed82b59ca549f) |
|  | Number of individual blocks currently allocated. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_a0e6125fe8d4c3cd6cc3ed82b59ca549f.html#a0e6125fe8d4c3cd6cc3ed82b59ca549f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakMemUsed](struct_a_k_1_1_bookmark_alloc_1_1_stats_aede98232fecfe3840a8061d25c1843ed.html#aede98232fecfe3840a8061d25c1843ed) |
|  | The peak value for uRecentPeakMemUsed since initialization. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_aede98232fecfe3840a8061d25c1843ed.html#aede98232fecfe3840a8061d25c1843ed) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakMemAllocated](struct_a_k_1_1_bookmark_alloc_1_1_stats_aa0228a6a918357448511c0540af54fea.html#aa0228a6a918357448511c0540af54fea) |
|  | The peak value for uMemAllocated since initialization. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_aa0228a6a918357448511c0540af54fea.html#aa0228a6a918357448511c0540af54fea) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakBlocksFetched](struct_a_k_1_1_bookmark_alloc_1_1_stats_a56479f5c381f5c4584105eaae74c3edd.html#a56479f5c381f5c4584105eaae74c3edd) |
|  | The peak value for uRecentBlocksFetched since initialization. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_a56479f5c381f5c4584105eaae74c3edd.html#a56479f5c381f5c4584105eaae74c3edd) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakBlocksAllocated](struct_a_k_1_1_bookmark_alloc_1_1_stats_a1455ae15cfac1dad78384d7274a29660.html#a1455ae15cfac1dad78384d7274a29660) |
|  | The peak value for uBlocksAllocated since initialization. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_a1455ae15cfac1dad78384d7274a29660.html#a1455ae15cfac1dad78384d7274a29660) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPeakBlockSize](struct_a_k_1_1_bookmark_alloc_1_1_stats_abdeea1b46a8f1cf3dead9934588a2e9f.html#abdeea1b46a8f1cf3dead9934588a2e9f) |
|  | The peak size of any single block since initialization. [更多...](struct_a_k_1_1_bookmark_alloc_1_1_stats_abdeea1b46a8f1cf3dead9934588a2e9f.html#abdeea1b46a8f1cf3dead9934588a2e9f) |
|  | |

## 详细描述

Bookmark-allocator memory statistics. Whenever these are fetched, they represent whatever happened since the last tick

备注
:   These statistics are not collected in the Release configuration of the memory mgr.

在文件 [AkTempAllocDefs.h](_ak_temp_alloc_defs_8h_source.html) 第 [117](_ak_temp_alloc_defs_8h_source.html#l00117) 行定义.