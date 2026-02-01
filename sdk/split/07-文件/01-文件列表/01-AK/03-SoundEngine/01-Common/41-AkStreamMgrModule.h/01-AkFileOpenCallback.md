# AkFileOpenCallback

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)
- [AkStreamMgrModule.h](_ak_stream_mgr_module_8h.html)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  | | --- | | [AkFileOpenCallback](_ak_stream_mgr_module_8h_ae00967344e3fcd553d8cdf391ec7081e.html#ae00967344e3fcd553d8cdf391ec7081e) | | [AkIOCallback](_ak_stream_mgr_module_8h_a3e66cb4516ec856e0b7d3f6ba45994e0.html#a3e66cb4516ec856e0b7d3f6ba45994e0) | | [◆](#ae00967344e3fcd553d8cdf391ec7081e)AkFileOpenCallback |  | | --- | | typedef void( \* AkFileOpenCallback) ([AkAsyncFileOpenData](struct_ak_async_file_open_data.html) \*in\_pOpenInfo, [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_eResult) |  Callback signature for the notification of completion of the asynchronous Open operation.  参见  - [AkAsyncFileOpenData](struct_ak_async_file_open_data.html) - [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555)  在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 第 [133](_ak_stream_mgr_module_8h_source.html#l00133) 行定义. |