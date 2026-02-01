# AkIOCallback

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)
- [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  | | --- | | [AkFileOpenCallback](_ak_stream_mgr_module_8h_ae00967344e3fcd553d8cdf391ec7081e.html#ae00967344e3fcd553d8cdf391ec7081e) | | [AkIOCallback](_ak_stream_mgr_module_8h_a3e66cb4516ec856e0b7d3f6ba45994e0.html#a3e66cb4516ec856e0b7d3f6ba45994e0) | | [◆](#a3e66cb4516ec856e0b7d3f6ba45994e0)AkIOCallback |  | | --- | | typedef void( \* AkIOCallback) ([AkAsyncIOTransferInfo](struct_ak_async_i_o_transfer_info.html) \*in\_pTransferInfo, [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_eResult) |  Callback function prototype definition used for asynchronous I/O transfers between the Stream Manager and the Low-Level IO. Notes:   - If you pass in\_eResult of AK\_Fail, all streams awaiting for this transfer are marked as invalid and will stop. An "IO error" notification is posted to the capture log. - If the transfer was cancelled by the Stream Manager while it was in the Low-Level IO, you must return AK\_Success, whether you performed the operation or not. The Stream Manager knows that it was cancelled, so it will not try to use it after you call it back. 参见 - [AkAsyncIOTransferInfo](struct_ak_async_i_o_transfer_info.html) - [AK::StreamMgr::IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html)   在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [109](_ak_stream_mgr_module_8h_source.html#l00109) 行定义. |