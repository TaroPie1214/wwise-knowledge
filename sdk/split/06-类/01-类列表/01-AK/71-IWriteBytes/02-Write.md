# Write

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IWriteBytes](class_a_k_1_1_i_write_bytes.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Write](class_a_k_1_1_i_write_bytes_a4db16f8c3735f39903277bd1cd24d9e1.html#a4db16f8c3735f39903277bd1cd24d9e1) | | [Write](class_a_k_1_1_i_write_bytes_a94945a17afde7c787007c6d04f2ca92f.html#a94945a17afde7c787007c6d04f2ca92f) | | [WriteBytes](class_a_k_1_1_i_write_bytes_af52b6e689172d6ec3ac9288012436d65.html#af52b6e689172d6ec3ac9288012436d65) | | [◆](#a4db16f8c3735f39903277bd1cd24d9e1)Write() [2/2] template<class T >   |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | bool AK::IWriteBytes::Write | ( | const T & | *in\_data* | ) |  | | inline |  Writes a simple type or struct.  警告  Not for object serialization.  返回  True if the operation was successful, False otherwise  参数  |  |  | | --- | --- | | in\_data | Data to be written |  在文件 [IBytes.h](_i_bytes_8h_source.html) 第 [135](_i_bytes_8h_source.html#l00135) 行定义.  引用了 [WriteBytes()](class_a_k_1_1_i_write_bytes_af52b6e689172d6ec3ac9288012436d65.html#af52b6e689172d6ec3ac9288012436d65). |