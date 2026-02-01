# WriteBytes

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IWriteBytes](class_a_k_1_1_i_write_bytes.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Write](class_a_k_1_1_i_write_bytes_a4db16f8c3735f39903277bd1cd24d9e1.html#a4db16f8c3735f39903277bd1cd24d9e1) | | [Write](class_a_k_1_1_i_write_bytes_a94945a17afde7c787007c6d04f2ca92f.html#a94945a17afde7c787007c6d04f2ca92f) | | [WriteBytes](class_a_k_1_1_i_write_bytes_af52b6e689172d6ec3ac9288012436d65.html#af52b6e689172d6ec3ac9288012436d65) | | [◆](#af52b6e689172d6ec3ac9288012436d65)WriteBytes() |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual bool AK::IWriteBytes::WriteBytes | ( | const void \* | *in\_pData*, | |  |  | [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | *in\_cBytes*, | |  |  | [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) & | *out\_cWritten* | |  | ) |  |  | | pure virtual |  Writes some bytes from a buffer.  返回  True if the operation was successful, False otherwise  参数  |  |  | | --- | --- | | in\_pData | Pointer to a buffer | | in\_cBytes | Size of the buffer (in bytes) | | out\_cWritten | Returned number of written bytes |  在 [AK::WriteBytesBuffer](class_a_k_1_1_write_bytes_buffer_a0cc916c7a9fc72b18b43d8a5e8b1bba8.html#a0cc916c7a9fc72b18b43d8a5e8b1bba8), [AK::WriteBytesMem](class_a_k_1_1_write_bytes_mem_af688769e2ff35b29b6f3c701a3188eab.html#af688769e2ff35b29b6f3c701a3188eab) , 以及 [AK::WriteBytesCount](class_a_k_1_1_write_bytes_count_ab2b1cc4f5c9162b371504fff9b9a775c.html#ab2b1cc4f5c9162b371504fff9b9a775c) 内被实现.  被这些函数引用 [Write()](_i_bytes_8h_source.html#l00135). |