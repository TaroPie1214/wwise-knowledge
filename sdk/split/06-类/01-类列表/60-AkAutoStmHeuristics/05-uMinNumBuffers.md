# uMinNumBuffers

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkAutoStmHeuristics](struct_ak_auto_stm_heuristics.html)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [fThroughput](struct_ak_auto_stm_heuristics_a4765f706b096765eb25dd6c06073d9af.html#a4765f706b096765eb25dd6c06073d9af) | | [priority](struct_ak_auto_stm_heuristics_a574352be21d197e2bbca4e87177a48ab.html#a574352be21d197e2bbca4e87177a48ab) | | [uLoopEnd](struct_ak_auto_stm_heuristics_a378d13e909830ce63e57782d9389506a.html#a378d13e909830ce63e57782d9389506a) | | [uLoopStart](struct_ak_auto_stm_heuristics_afe02155d1e487ebba5cf6b467c40f24d.html#afe02155d1e487ebba5cf6b467c40f24d) | | [uMinNumBuffers](struct_ak_auto_stm_heuristics_aeda0fa45777364065a470210b54bffea.html#aeda0fa45777364065a470210b54bffea) | | [◆](#aeda0fa45777364065a470210b54bffea)uMinNumBuffers |  | | --- | | [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) AkAutoStmHeuristics::uMinNumBuffers |  Minimum number of buffers if you plan to own more than one buffer at a time, 0 or 1 otherwise  备注  You should always release buffers as fast as possible, therefore this heuristic should be used only when dealing with special contraints, like drivers or hardware that require more than one buffer at a time.  Also, this is only a heuristic: it does not guarantee that data will be ready when calling [AK::IAkAutoStream::GetBuffer()](class_a_k_1_1_i_ak_auto_stream_aa8197d63b8e758acb075a437103e573c.html#aa8197d63b8e758acb075a437103e573c).  在文件 [IAkStreamMgr.h](_i_ak_stream_mgr_8h_source.html) 第 [99](_i_ak_stream_mgr_8h_source.html#l00099) 行定义. |