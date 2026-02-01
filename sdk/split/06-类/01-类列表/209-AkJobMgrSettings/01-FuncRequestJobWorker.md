# FuncRequestJobWorker

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkJobMgrSettings](struct_ak_job_mgr_settings.html)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [fnRequestJobWorker](struct_ak_job_mgr_settings_a9a6278f869a1a10e613da6e77f343303.html#a9a6278f869a1a10e613da6e77f343303) | | [FuncRequestJobWorker](struct_ak_job_mgr_settings_a425f817f8a59747148d5dd1b502daefe.html#a425f817f8a59747148d5dd1b502daefe) | | [pClientData](struct_ak_job_mgr_settings_aa2b675afe703cb11ef7e884baeb401b6.html#aa2b675afe703cb11ef7e884baeb401b6) | | [uMaxActiveWorkers](struct_ak_job_mgr_settings_a5e216a01552c2d93d25eba4d4eff3350.html#a5e216a01552c2d93d25eba4d4eff3350) | | [uMemorySlabSize](struct_ak_job_mgr_settings_ab2a8def39da063c40396d44186a67bf8.html#ab2a8def39da063c40396d44186a67bf8) | | [uNumMemorySlabs](struct_ak_job_mgr_settings_a857e4ffe8a85fc4d9a15e2a56dbf4bd1.html#a857e4ffe8a85fc4d9a15e2a56dbf4bd1) | | [◆](#a425f817f8a59747148d5dd1b502daefe)FuncRequestJobWorker |  | | --- | | typedef void( \* AkJobMgrSettings::FuncRequestJobWorker) ([AkJobWorkerFunc](_ak_sound_engine_8h_a8edd5fddd3dfdf6cc9b17f63ad23915c.html#a8edd5fddd3dfdf6cc9b17f63ad23915c) in\_fnJobWorker, [AkJobType](_ak_typedefs_8h_a1cc301d7b3b1af3e3051df12fb484e68.html#a1cc301d7b3b1af3e3051df12fb484e68) in\_jobType, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumWorkers, void \*in\_pClientData) |  Callback function prototype definition used for handling requests from JobMgr for new workers to perform work.  在文件 [AkSoundEngine.h](_ak_sound_engine_8h_source.html) 第 [151](_ak_sound_engine_8h_source.html#l00151) 行定义. |