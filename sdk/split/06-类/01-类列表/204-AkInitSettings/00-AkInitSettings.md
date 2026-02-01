# AkInitSettings

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_init_settings-members.html) |
[Public 属性](#pub-attribs)

AkInitSettings结构体 参考

`#include <AkSoundEngine.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkAssertHook](_ak_sound_engine_8h_a828f993c08d2b2736616e6962c8680f1.html#a828f993c08d2b2736616e6962c8680f1) | [pfnAssertHook](struct_ak_init_settings_a7c467af52c93a8b47450d09d23cf776a.html#a7c467af52c93a8b47450d09d23cf776a) |
|  | External assertion handling function (optional) [更多...](struct_ak_init_settings_a7c467af52c93a8b47450d09d23cf776a.html#a7c467af52c93a8b47450d09d23cf776a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxNumPaths](struct_ak_init_settings_aa8137dca0d7b55c06900371c17ce6c8e.html#aa8137dca0d7b55c06900371c17ce6c8e) |
|  | Maximum number of paths for positioning [更多...](struct_ak_init_settings_aa8137dca0d7b55c06900371c17ce6c8e.html#aa8137dca0d7b55c06900371c17ce6c8e) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCommandQueueSize](struct_ak_init_settings_afd6ada0769c6316e7950961c38cc09d0.html#afd6ada0769c6316e7950961c38cc09d0) |
|  | Size of the command queue, in bytes [更多...](struct_ak_init_settings_afd6ada0769c6316e7950961c38cc09d0.html#afd6ada0769c6316e7950961c38cc09d0) |
|  | |
| bool | [bEnableGameSyncPreparation](struct_ak_init_settings_a65a86ebc5f0f7c6e3612a70e102f1cfd.html#a65a86ebc5f0f7c6e3612a70e102f1cfd) |
|  | Sets to true to enable AK::SoundEngine::PrepareGameSync usage. [更多...](struct_ak_init_settings_a65a86ebc5f0f7c6e3612a70e102f1cfd.html#a65a86ebc5f0f7c6e3612a70e102f1cfd) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uContinuousPlaybackLookAhead](struct_ak_init_settings_a2baedc80c64280eb0db21f94fe7ed78f.html#a2baedc80c64280eb0db21f94fe7ed78f) |
|  | Default is 1 audio quantum, also known as an audio frame. Its size is equal to [AkInitSettings::uNumSamplesPerFrame](struct_ak_init_settings_a2438a18ece872c83175f70d7f70d659b.html#a2438a18ece872c83175f70d7f70d659b "Number of samples per audio frame (256, 512, 1024, or 2048).") / [AkPlatformInitSettings::uSampleRate](struct_ak_platform_init_settings_a2bf6f000f256b146d6cd36401a234b85.html#a2bf6f000f256b146d6cd36401a234b85 "Sampling Rate. Default is 48000 Hz. Use 24000hz for low quality. Any positive reasonable sample rate ..."). For many platforms the default values - which can be overridden - are respectively 1,024 samples and 48 kHz. This gives a default 21.3 ms for an audio quantum, which is adequate if you have a RAM-based streaming device that completes transfers within 20 ms. With 1 look-ahead quantum, voices spawned by continuous containers are more likely to be ready when they are required to play, thereby improving the overall precision of sound scheduling. If your device completes transfers in 30 ms instead, you might consider increasing this value to 2 because it will grant new voices 2 audio quanta (~43 ms) to fetch data. [更多...](struct_ak_init_settings_a2baedc80c64280eb0db21f94fe7ed78f.html#a2baedc80c64280eb0db21f94fe7ed78f) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fStreamingLookAheadRatio](struct_ak_init_settings_acc428dbb2c934110d37dbfcab10436ce.html#acc428dbb2c934110d37dbfcab10436ce) |
|  | Multiplication factor for all streaming look-ahead heuristic values, for music streams. [更多...](struct_ak_init_settings_acc428dbb2c934110d37dbfcab10436ce.html#acc428dbb2c934110d37dbfcab10436ce) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumSamplesPerFrame](struct_ak_init_settings_a2438a18ece872c83175f70d7f70d659b.html#a2438a18ece872c83175f70d7f70d659b) |
|  | Number of samples per audio frame (256, 512, 1024, or 2048). [更多...](struct_ak_init_settings_a2438a18ece872c83175f70d7f70d659b.html#a2438a18ece872c83175f70d7f70d659b) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMonitorQueuePoolSize](struct_ak_init_settings_acdb64f2cf024ac17b7db878eb135c523.html#acdb64f2cf024ac17b7db878eb135c523) |
|  | Size of the monitoring queue, in bytes. This parameter is not used in Release build. [更多...](struct_ak_init_settings_acdb64f2cf024ac17b7db878eb135c523.html#acdb64f2cf024ac17b7db878eb135c523) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCpuMonitorQueueMaxSize](struct_ak_init_settings_a57c294b2de0ad7d01cab1d6020c95f45.html#a57c294b2de0ad7d01cab1d6020c95f45) |
|  | Maximum size of the CPU monitoring queue, per thread, in bytes. This parameter is not used in Release build. [更多...](struct_ak_init_settings_a57c294b2de0ad7d01cab1d6020c95f45.html#a57c294b2de0ad7d01cab1d6020c95f45) |
|  | |
| [AkOutputSettings](struct_ak_output_settings.html) | [settingsMainOutput](struct_ak_init_settings_a9c5254abf13a5c3bf60ddd27c48db4d7.html#a9c5254abf13a5c3bf60ddd27c48db4d7) |
|  | Main output device settings. [更多...](struct_ak_init_settings_a9c5254abf13a5c3bf60ddd27c48db4d7.html#a9c5254abf13a5c3bf60ddd27c48db4d7) |
|  | |
| [AkJobMgrSettings](struct_ak_job_mgr_settings.html) | [settingsJobManager](struct_ak_init_settings_a78895b2daaf2215e77b890ea2c072223.html#a78895b2daaf2215e77b890ea2c072223) |
|  | Settings to configure the behavior of the Sound Engine's internal job manager [更多...](struct_ak_init_settings_a78895b2daaf2215e77b890ea2c072223.html#a78895b2daaf2215e77b890ea2c072223) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uMaxHardwareTimeoutMs](struct_ak_init_settings_aa0453c32f6038f634408e6c3a25a570b.html#aa0453c32f6038f634408e6c3a25a570b) |
|  | Amount of time to wait for HW devices to trigger an audio interrupt. If there is no interrupt after that time, the sound engine will revert to silent mode and continue operating until the HW finally comes back. Default value: 2000 (2 seconds) [更多...](struct_ak_init_settings_aa0453c32f6038f634408e6c3a25a570b.html#aa0453c32f6038f634408e6c3a25a570b) |
|  | |
| bool | [bUseSoundBankMgrThread](struct_ak_init_settings_a3f9f40766762c100b829467ffaa31b24.html#a3f9f40766762c100b829467ffaa31b24) |
|  | Use a Wwise-owned thread for loading sound banks. If set to false, bank-loading will occur only inside a call to [AK::SoundEngine::ProcessBanks()](namespace_a_k_1_1_sound_engine_a1bb80e2fe3b8051fb9ece6dc9bb1fbb6.html#a1bb80e2fe3b8051fb9ece6dc9bb1fbb6). [更多...](struct_ak_init_settings_a3f9f40766762c100b829467ffaa31b24.html#a3f9f40766762c100b829467ffaa31b24) |
|  | |
| bool | [bUseLEngineThread](struct_ak_init_settings_a31218fafe5dea9bca79b979cfb1e6fb2.html#a31218fafe5dea9bca79b979cfb1e6fb2) |
|  | Use a Wwise-owned thread for processing audio. If set to false, audio processing will occur only inside a call to [AK::SoundEngine::RenderAudio()](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1). [更多...](struct_ak_init_settings_a31218fafe5dea9bca79b979cfb1e6fb2.html#a31218fafe5dea9bca79b979cfb1e6fb2) |
|  | |
| [AkBackgroundMusicChangeCallbackFunc](_ak_sound_engine_8h_ad8c63f34a7148171febdbcf5ead5431b.html#ad8c63f34a7148171febdbcf5ead5431b) | [BGMCallback](struct_ak_init_settings_a071653afbe490f1c9b5169d0a47ad6f5.html#a071653afbe490f1c9b5169d0a47ad6f5) |
|  | Application-defined audio source change event callback function. [更多...](struct_ak_init_settings_a071653afbe490f1c9b5169d0a47ad6f5.html#a071653afbe490f1c9b5169d0a47ad6f5) |
|  | |
| void \* | [BGMCallbackCookie](struct_ak_init_settings_a0a913fbc474686e2a18420498e31e174.html#a0a913fbc474686e2a18420498e31e174) |
|  | Application-defined user data for the audio source change event callback function. [更多...](struct_ak_init_settings_a0a913fbc474686e2a18420498e31e174.html#a0a913fbc474686e2a18420498e31e174) |
|  | |
| const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* | [szPluginDLLPath](struct_ak_init_settings_a381f6978151d3e205f3b493523ed3b57.html#a381f6978151d3e205f3b493523ed3b57) |
|  | When using DLLs for plugins, specify their path. Leave NULL if DLLs are in the same folder as the game executable. [更多...](struct_ak_init_settings_a381f6978151d3e205f3b493523ed3b57.html#a381f6978151d3e205f3b493523ed3b57) |
|  | |
| [AkFloorPlane](_ak_sound_engine_8h_a225b928d2b96fc2fd205ec5e0126d0f4.html#a225b928d2b96fc2fd205ec5e0126d0f4) | [eFloorPlane](struct_ak_init_settings_a27a65e61a3a2e55f537ae434a0f84549.html#a27a65e61a3a2e55f537ae434a0f84549) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fGameUnitsToMeters](struct_ak_init_settings_acbb4594e7634edbe91adec361e2cf111.html#acbb4594e7634edbe91adec361e2cf111) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uBankReadBufferSize](struct_ak_init_settings_ae4c40fd9bab28527705d43b2247bbe21.html#ae4c40fd9bab28527705d43b2247bbe21) |
|  | The number of bytes read by the BankReader when new data needs to be loaded from disk during serialization. Increasing this trades memory usage for larger, but fewer, file-read events during bank loading. [更多...](struct_ak_init_settings_ae4c40fd9bab28527705d43b2247bbe21.html#ae4c40fd9bab28527705d43b2247bbe21) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDebugOutOfRangeLimit](struct_ak_init_settings_ad6232de3514945186432d688f9b1083d.html#ad6232de3514945186432d688f9b1083d) |
|  | Debug setting: Only used when bDebugOutOfRangeCheckEnabled is true. This defines the maximum values samples can have. Normal audio must be contained within +1/-1. This limit should be set higher to allow temporary or short excursions out of range. Default is 16. [更多...](struct_ak_init_settings_ad6232de3514945186432d688f9b1083d.html#ad6232de3514945186432d688f9b1083d) |
|  | |
| bool | [bDebugOutOfRangeCheckEnabled](struct_ak_init_settings_a0ffc62cdbb07d0c8ebb2440fd177625b.html#a0ffc62cdbb07d0c8ebb2440fd177625b) |
|  | Debug setting: Enable checks for out-of-range (and NAN) floats in the processing code. This incurs a small performance hit, but can be enabled in most scenarios. Will print error messages in the log if invalid values are found at various point in the pipeline. Contact [AK](namespace_a_k.html "Definition of data structures for AkAudioObject") Support with the new error messages for more information. [更多...](struct_ak_init_settings_a0ffc62cdbb07d0c8ebb2440fd177625b.html#a0ffc62cdbb07d0c8ebb2440fd177625b) |
|  | |
| bool | [bOfflineRendering](struct_ak_init_settings_a9f19aeb735f8b75d7332eb5a64323ce3.html#a9f19aeb735f8b75d7332eb5a64323ce3) |
|  | Enables/disables offline rendering. [利用 Wwise 进行离线渲染](goingfurther_offlinerendering.html) [更多...](struct_ak_init_settings_a9f19aeb735f8b75d7332eb5a64323ce3.html#a9f19aeb735f8b75d7332eb5a64323ce3) |
|  | |
| [AkProfilerPushTimerFunc](_ak_sound_engine_8h_a565822e94507ed0826247173f6c5a144.html#a565822e94507ed0826247173f6c5a144) | [fnProfilerPushTimer](struct_ak_init_settings_a71783c4575cbf9410ecd8c7c5703c8d2.html#a71783c4575cbf9410ecd8c7c5703c8d2) |
|  | External (optional) function for tracking performance of the sound engine that is called when a timer starts. (only called in Debug and Profile binaries; this is not called in Release) [更多...](struct_ak_init_settings_a71783c4575cbf9410ecd8c7c5703c8d2.html#a71783c4575cbf9410ecd8c7c5703c8d2) |
|  | |
| [AkProfilerPopTimerFunc](_ak_sound_engine_8h_a7ea191d14466c20ddcfa300aa5a11f9c.html#a7ea191d14466c20ddcfa300aa5a11f9c) | [fnProfilerPopTimer](struct_ak_init_settings_a3d1f3008d52cdc3ead4e7497386e9dd7.html#a3d1f3008d52cdc3ead4e7497386e9dd7) |
|  | External (optional) function for tracking performance of the sound engine that is called when a timer stops. (only called in Debug and Profile binaries; this is not called in Release) [更多...](struct_ak_init_settings_a3d1f3008d52cdc3ead4e7497386e9dd7.html#a3d1f3008d52cdc3ead4e7497386e9dd7) |
|  | |
| [AkProfilerPostMarkerFunc](_ak_sound_engine_8h_afd663bf69bb434a594a61f185b1e1c52.html#afd663bf69bb434a594a61f185b1e1c52) | [fnProfilerPostMarker](struct_ak_init_settings_afee08f27130b3fdf479d15fb06f15b12.html#afee08f27130b3fdf479d15fb06f15b12) |
|  | External (optional) function for tracking significant events in the sound engine, to act as a marker or bookmark. (only called in Debug and Profile binaries; this is not called in Release) [更多...](struct_ak_init_settings_afee08f27130b3fdf479d15fb06f15b12.html#afee08f27130b3fdf479d15fb06f15b12) |
|  | |

## 详细描述

Platform-independent initialization settings of the sound engine

参见
:   - `AK::SoundEngine::Init()`
    - `AK::SoundEngine::GetDefaultInitSettings()`
    - [高级声音引擎集成](soundengine_integration_init_advanced.html)

在文件 [AkSoundEngine.h](_ak_sound_engine_8h_source.html) 第 [192](_ak_sound_engine_8h_source.html#l00192) 行定义.