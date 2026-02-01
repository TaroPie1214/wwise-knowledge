# NotifyCurrentPlatformChanged

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1_a2b38d9090ee45f780177974b5dda8d93.html#a2b38d9090ee45f780177974b5dda8d93) | | [Instance](structak__wwise__plugin__notifications__host__v1_a2be163bb727db442e2a06b70ce45dcd0.html#a2be163bb727db442e2a06b70ce45dcd0) | | [NotifyCurrentPlatformChanged](structak__wwise__plugin__notifications__host__v1_a5906b30c4623ca87f4d1caecf9bfebbe.html#a5906b30c4623ca87f4d1caecf9bfebbe) | | [◆](#a5906b30c4623ca87f4d1caecf9bfebbe)NotifyCurrentPlatformChanged |  | | --- | | void(\* ak\_wwise\_plugin\_notifications\_host\_v1::NotifyCurrentPlatformChanged) (struct [ak\_wwise\_plugin\_notifications\_host\_instance\_v1](structak__wwise__plugin__notifications__host__instance__v1.html) \*in\_this, const GUID \*in\_guidCurrentPlatform) |  Received when the current platform changes.  参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. | | [in] | in\_guidCurrentPlatform | The unique ID of the new platform. |  参见  - [音频设计师更改当前平台](wwiseplugin_frontend.html#wwiseplugin_platformchange)  在文件 [Host.h](_v1_2_host_8h_source.html) 第 [213](_v1_2_host_8h_source.html#l00213) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V1::Notifications::Host\_::Interface::Interface()](_v1_2_host_8h_source.html#l00426). |