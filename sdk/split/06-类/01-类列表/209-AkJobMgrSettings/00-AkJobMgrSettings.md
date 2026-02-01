# AkJobMgrSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_job_mgr_settings-members.html) |
[Public 类型](#pub-types) |
[Public 属性](#pub-attribs)

AkJobMgrSettings结构体 参考

Settings for the Sound Engine's internal job manager
[更多...](struct_ak_job_mgr_settings.html#details)

`#include <AkSoundEngine.h>`

|  |  |
| --- | --- |
| Public 类型 | |
| typedef void(\* | [FuncRequestJobWorker](struct_ak_job_mgr_settings_a425f817f8a59747148d5dd1b502daefe.html#a425f817f8a59747148d5dd1b502daefe)) ([AkJobWorkerFunc](_ak_sound_engine_8h_a8edd5fddd3dfdf6cc9b17f63ad23915c.html#a8edd5fddd3dfdf6cc9b17f63ad23915c) in\_fnJobWorker, [AkJobType](_ak_typedefs_8h_a1cc301d7b3b1af3e3051df12fb484e68.html#a1cc301d7b3b1af3e3051df12fb484e68) in\_jobType, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumWorkers, void \*in\_pClientData) |
|  | Callback function prototype definition used for handling requests from JobMgr for new workers to perform work. [更多...](struct_ak_job_mgr_settings_a425f817f8a59747148d5dd1b502daefe.html#a425f817f8a59747148d5dd1b502daefe) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [FuncRequestJobWorker](struct_ak_job_mgr_settings_a425f817f8a59747148d5dd1b502daefe.html#a425f817f8a59747148d5dd1b502daefe) | [fnRequestJobWorker](struct_ak_job_mgr_settings_a9a6278f869a1a10e613da6e77f343303.html#a9a6278f869a1a10e613da6e77f343303) |
|  | Function called by the job manager when a new worker needs to be requested. When null, all jobs will be executed on the same thread that calls [RenderAudio()](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1). [更多...](struct_ak_job_mgr_settings_a9a6278f869a1a10e613da6e77f343303.html#a9a6278f869a1a10e613da6e77f343303) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxActiveWorkers](struct_ak_job_mgr_settings_a5e216a01552c2d93d25eba4d4eff3350.html#a5e216a01552c2d93d25eba4d4eff3350) [[AK\_NUM\_JOB\_TYPES](_ak_constants_8h_a1b007bf841a40aacc6f7d533a940f32c.html#a1b007bf841a40aacc6f7d533a940f32c)] |
|  | The maximum number of concurrent workers that will be requested. Must be >= 1 for each jobType. [更多...](struct_ak_job_mgr_settings_a5e216a01552c2d93d25eba4d4eff3350.html#a5e216a01552c2d93d25eba4d4eff3350) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumMemorySlabs](struct_ak_job_mgr_settings_a857e4ffe8a85fc4d9a15e2a56dbf4bd1.html#a857e4ffe8a85fc4d9a15e2a56dbf4bd1) |
|  | Number of memory slabs to pre-allocate for job manager memory. At least one slab per worker thread should be pre-allocated. Default is 1. [更多...](struct_ak_job_mgr_settings_a857e4ffe8a85fc4d9a15e2a56dbf4bd1.html#a857e4ffe8a85fc4d9a15e2a56dbf4bd1) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMemorySlabSize](struct_ak_job_mgr_settings_ab2a8def39da063c40396d44186a67bf8.html#ab2a8def39da063c40396d44186a67bf8) |
|  | Size of each memory slab used for job manager memory. Must be a power of two. Default is 8K. [更多...](struct_ak_job_mgr_settings_ab2a8def39da063c40396d44186a67bf8.html#ab2a8def39da063c40396d44186a67bf8) |
|  | |
| void \* | [pClientData](struct_ak_job_mgr_settings_aa2b675afe703cb11ef7e884baeb401b6.html#aa2b675afe703cb11ef7e884baeb401b6) |
|  | Arbitrary data that will be passed back to the client when calling FuncRequestJobWorker [更多...](struct_ak_job_mgr_settings_aa2b675afe703cb11ef7e884baeb401b6.html#aa2b675afe703cb11ef7e884baeb401b6) |
|  | |

## 详细描述

Settings for the Sound Engine's internal job manager

在文件 [AkSoundEngine.h](_ak_sound_engine_8h_source.html) 第 [148](_ak_sound_engine_8h_source.html#l00148) 行定义.