# kHashTableGrowthFactor

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)
- [AkHashList.h](_ak_hash_list_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AK\_HASH\_SIZE\_VERY\_SMALL](_ak_hash_list_8h_a93553137c136e12e13b27283b317e1e5.html#a93553137c136e12e13b27283b317e1e5) | | [AkDefaultHashListBarePolicy](_ak_hash_list_8h_add6e5990e83597cd7194b237de2f1c96.html#add6e5990e83597cd7194b237de2f1c96) | | [AkHash](_ak_hash_list_8h_a8b7677c6a6fa728a10f13d34e85335af.html#a8b7677c6a6fa728a10f13d34e85335af) | | [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | | [kHashSizes](_ak_hash_list_8h_a0217cf461cf5b442bd30c557fe4a9a6e.html#a0217cf461cf5b442bd30c557fe4a9a6e) | | [kHashTableGrowthFactor](_ak_hash_list_8h_ac75bd58235b536b2a2b8fdeaac1d117b.html#ac75bd58235b536b2a2b8fdeaac1d117b) | | [kNumHashSizes](_ak_hash_list_8h_a6d37fff280ec5e5d2eba03dcbe3c40dd.html#a6d37fff280ec5e5d2eba03dcbe3c40dd) | | [◆](#ac75bd58235b536b2a2b8fdeaac1d117b)kHashTableGrowthFactor |  |  |  | | --- | --- | --- | | |  | | --- | | constexpr [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) kHashTableGrowthFactor = 0.9f | | constexpr |  在文件 [AkHashList.h](_ak_hash_list_8h_source.html) 第 [46](_ak_hash_list_8h_source.html#l00046) 行定义.  被这些函数引用 [AkHashList< AkUInt32, Entry, TAlloc >::CheckSize()](_ak_hash_list_8h_source.html#l00597), [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY >::CheckSize()](_ak_hash_list_8h_source.html#l01173), [AkHashList< AkUInt32, Entry, TAlloc >::Reserve()](_ak_hash_list_8h_source.html#l00531) , 以及 [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY >::Reserve()](_ak_hash_list_8h_source.html#l01106). |