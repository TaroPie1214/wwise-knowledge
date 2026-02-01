# kHashSizes

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)
- [AkHashList.h](_ak_hash_list_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AK\_HASH\_SIZE\_VERY\_SMALL](_ak_hash_list_8h_a93553137c136e12e13b27283b317e1e5.html#a93553137c136e12e13b27283b317e1e5) | | [AkDefaultHashListBarePolicy](_ak_hash_list_8h_add6e5990e83597cd7194b237de2f1c96.html#add6e5990e83597cd7194b237de2f1c96) | | [AkHash](_ak_hash_list_8h_a8b7677c6a6fa728a10f13d34e85335af.html#a8b7677c6a6fa728a10f13d34e85335af) | | [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) | | [kHashSizes](_ak_hash_list_8h_a0217cf461cf5b442bd30c557fe4a9a6e.html#a0217cf461cf5b442bd30c557fe4a9a6e) | | [kHashTableGrowthFactor](_ak_hash_list_8h_ac75bd58235b536b2a2b8fdeaac1d117b.html#ac75bd58235b536b2a2b8fdeaac1d117b) | | [kNumHashSizes](_ak_hash_list_8h_a6d37fff280ec5e5d2eba03dcbe3c40dd.html#a6d37fff280ec5e5d2eba03dcbe3c40dd) | | [◆](#a0217cf461cf5b442bd30c557fe4a9a6e)kHashSizes |  |  |  | | --- | --- | --- | | |  | | --- | | const [AK\_SELECTANY](_ak_platforms_8h_aace42721bf834d460bc43bf1c87c7c67.html#aace42721bf834d460bc43bf1c87c7c67) [AkHashType](_ak_hash_list_8h_a93e50723472a35369bc80e47c3bb09c9.html#a93e50723472a35369bc80e47c3bb09c9) kHashSizes[] = { 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741 } | | extern |  被这些函数引用 [AkHashList< AkUInt32, Entry, TAlloc >::Resize()](_ak_hash_list_8h_source.html#l00539) , 以及 [AkHashListBare< T\_KEY, T\_MAPSTRUCT, T\_ALLOC, KEY\_POLICY >::Resize()](_ak_hash_list_8h_source.html#l01114). |