# Compute

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [FNVHash](class_a_k_1_1_f_n_v_hash.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Compute](class_a_k_1_1_f_n_v_hash_a907841bf37541824958d382686b1fb1f.html#a907841bf37541824958d382686b1fb1f) | | [Compute](class_a_k_1_1_f_n_v_hash_a9408dd90cf3836ce3ce39370638a144b.html#a9408dd90cf3836ce3ce39370638a144b) | | [ComputeLowerCase](class_a_k_1_1_f_n_v_hash_ac5d8db171c7e49452ff88bed5359b705.html#ac5d8db171c7e49452ff88bed5359b705) | | [FNVHash](class_a_k_1_1_f_n_v_hash_a9ee1906e8dbf95ff3b98708c1b755ecd.html#a9ee1906e8dbf95ff3b98708c1b755ecd) | | [Get](class_a_k_1_1_f_n_v_hash_a45e3387db9391c12c3d93e66ebe5755f.html#a45e3387db9391c12c3d93e66ebe5755f) | | [◆](#a907841bf37541824958d382686b1fb1f)Compute() [2/2] template<class HashParams >   |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | HashParams::HashType [AK::FNVHash](class_a_k_1_1_f_n_v_hash.html)< HashParams >::Compute | ( | const void \* | *in\_pData*, | |  |  | typename HashParams::SizeType | *in\_dataSize* | |  | ) |  |  | | inline |  Turn the provided data into a hash value. When [Wwise](namespace_a_k_1_1_wwise.html) uses this hash with strings, it always provides lower case strings only. Call this repeatedly on the same instance to build a hash incrementally.  在文件 [AkFNVHash.h](_ak_f_n_v_hash_8h_source.html) 第 [105](_ak_f_n_v_hash_8h_source.html#l00105) 行定义.  被这些函数引用 [AkHash()](_ak_string_8h_source.html#l00255) , 以及 [AK::GetAppLocalDeviceIdHash()](_ak_motion_sink_game_input_helpers_8h_source.html#l00044). |