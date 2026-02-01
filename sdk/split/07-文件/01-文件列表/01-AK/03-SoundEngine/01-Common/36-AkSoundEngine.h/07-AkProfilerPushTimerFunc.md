# AkProfilerPushTimerFunc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)
- [AkSoundEngine.h](_ak_sound_engine_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AK\_ASSERT\_HOOK](_ak_sound_engine_8h_a4be2a10f389cda83d9646f431ddadb86.html#a4be2a10f389cda83d9646f431ddadb86) | | [AkAssertHook](_ak_sound_engine_8h_a828f993c08d2b2736616e6962c8680f1.html#a828f993c08d2b2736616e6962c8680f1) | | [AkBackgroundMusicChangeCallbackFunc](_ak_sound_engine_8h_ad8c63f34a7148171febdbcf5ead5431b.html#ad8c63f34a7148171febdbcf5ead5431b) | | [AkFloorPlane](_ak_sound_engine_8h_a225b928d2b96fc2fd205ec5e0126d0f4.html#a225b928d2b96fc2fd205ec5e0126d0f4) | | [AkJobWorkerFunc](_ak_sound_engine_8h_a8edd5fddd3dfdf6cc9b17f63ad23915c.html#a8edd5fddd3dfdf6cc9b17f63ad23915c) | | [AkProfilerPopTimerFunc](_ak_sound_engine_8h_a7ea191d14466c20ddcfa300aa5a11f9c.html#a7ea191d14466c20ddcfa300aa5a11f9c) | | [AkProfilerPostMarkerFunc](_ak_sound_engine_8h_afd663bf69bb434a594a61f185b1e1c52.html#afd663bf69bb434a594a61f185b1e1c52) | | [AkProfilerPushTimerFunc](_ak_sound_engine_8h_a565822e94507ed0826247173f6c5a144.html#a565822e94507ed0826247173f6c5a144) | | [◆](#a565822e94507ed0826247173f6c5a144)AkProfilerPushTimerFunc |  | | --- | | typedef void( \* AkProfilerPushTimerFunc) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) in\_uPluginID, const char \*in\_pszZoneName) |  External (optional) callback for tracking performance of the sound engine that is called when a timer starts. (only called in Debug and Profile binaries; this is not called in Release) in\_uPluginID may be non-zero when this function is called, to provide extra data about what context this Timer was started in. in\_pszZoneName will point to a static string, so the pointer can be stored for later use, not just the contents of the string itself.  在文件 [AkSoundEngine.h](_ak_sound_engine_8h_source.html) 第 [171](_ak_sound_engine_8h_source.html#l00171) 行定义. |