# ReadBytes

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IReadBytes](class_a_k_1_1_i_read_bytes.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Read](class_a_k_1_1_i_read_bytes_a965ac2f82d5cecf138e0a00e48eb57b6.html#a965ac2f82d5cecf138e0a00e48eb57b6) | | [Read](class_a_k_1_1_i_read_bytes_af309b2ebf268abdbe56a7f2c7416c94b.html#af309b2ebf268abdbe56a7f2c7416c94b) | | [Read](class_a_k_1_1_i_read_bytes_a9c5de86288182bdc144ca72f40957fb9.html#a9c5de86288182bdc144ca72f40957fb9) | | [ReadBytes](class_a_k_1_1_i_read_bytes_a9814c15733b485b2b0443b2097b8ce91.html#a9814c15733b485b2b0443b2097b8ce91) | | [◆](#a9814c15733b485b2b0443b2097b8ce91)ReadBytes() |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual bool AK::IReadBytes::ReadBytes | ( | void \* | *in\_pData*, | |  |  | [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | *in\_cBytes*, | |  |  | [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) & | *out\_cRead* | |  | ) |  |  | | pure virtual |  Reads some bytes into a buffer.  返回  True if the operation was successful, False otherwise  参数  |  |  | | --- | --- | | in\_pData | Pointer to a buffer | | in\_cBytes | Size of the buffer (in bytes) | | out\_cRead | Returned number of read bytes |  在 [AK::ReadBytesMem](class_a_k_1_1_read_bytes_mem_a76acdbe78ec318c6447db6f103d3634e.html#a76acdbe78ec318c6447db6f103d3634e) , 以及 [AK::ReadBytesSkip](class_a_k_1_1_read_bytes_skip_ae7b81d58afc301b7c43b235700218364.html#ae7b81d58afc301b7c43b235700218364) 内被实现.  被这些函数引用 [Read()](_i_bytes_8h_source.html#l00069). |