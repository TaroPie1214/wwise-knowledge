# AkBytesMem.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces)

AkBytesMem.h 文件参考

`#include <AK/IBytes.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`  
`#include <AK/Tools/Common/AkBankReadHelpers.h>`

[浏览源代码.](_ak_bytes_mem_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK::ReadBytesMem](class_a_k_1_1_read_bytes_mem.html) |
|  | |
| class | [AK::WriteBytesMem](class_a_k_1_1_write_bytes_mem.html) |
|  | |
| class | [AK::WriteBytesBuffer](class_a_k_1_1_write_bytes_buffer.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

## 详细描述

IReadBytes / IWriteBytes implementation on a growing memory buffer. This version uses the [AK::MemoryMgr](namespace_a_k_1_1_memory_mgr.html) allocator.

在文件 [AkBytesMem.h](_ak_bytes_mem_8h_source.html) 中定义.