# GetDeviceDesc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [StreamMgr](namespace_a_k_1_1_stream_mgr.html)
- [IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555) | | [BatchRead](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a9bc325405bc17c0a5105d0a53981b186.html#a9bc325405bc17c0a5105d0a53981b186) | | [BatchWrite](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a8f5041a24e395784437a62cdd2140505.html#a8f5041a24e395784437a62cdd2140505) | | [Close](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a7a50a7a5fa624691d7bb7608753dc096.html#a7a50a7a5fa624691d7bb7608753dc096) | | [GetBlockSize](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a5018552d455ddc2a95b727fc543aac9e.html#a5018552d455ddc2a95b727fc543aac9e) | | [GetDeviceData](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a885d39fdd78da3748f78e176615fb6ea.html#a885d39fdd78da3748f78e176615fb6ea) | | [GetDeviceDesc](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a06860cb1211c2ebd5c49f4429cc66a0b.html#a06860cb1211c2ebd5c49f4429cc66a0b) | | [OutputSearchedPaths](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a40d53d28e4c8942d23ba011f1222d29a.html#a40d53d28e4c8942d23ba011f1222d29a) | | [~IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a35a38687a6a0fc6431c8dc8317f2434f.html#a35a38687a6a0fc6431c8dc8317f2434f) | | [◆](#a06860cb1211c2ebd5c49f4429cc66a0b)GetDeviceDesc() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual void AK::StreamMgr::IAkLowLevelIOHook::GetDeviceDesc | ( | [AkDeviceDesc](struct_ak_device_desc.html) & | *out\_deviceDesc* | ) |  | | pure virtual |  Returns a description for the streaming device above this low-level hook.  备注  For profiling purposes only. The Release configuration of the Stream Manager never calls it.  参数  |  |  | | --- | --- | | out\_deviceDesc | Device description. | |