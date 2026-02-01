# AkCmd_ControlOfflineRendering

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___control_offline_rendering-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_ControlOfflineRendering结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [isEnabled](struct_ak_cmd___control_offline_rendering_a114c72c096cc3c84dd18ad735f76249b.html#a114c72c096cc3c84dd18ad735f76249b) |
|  | Whether offline rendering should be activated or not. [更多...](struct_ak_cmd___control_offline_rendering_a114c72c096cc3c84dd18ad735f76249b.html#a114c72c096cc3c84dd18ad735f76249b) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [frameTimeInSeconds](struct_ak_cmd___control_offline_rendering_a27acb08303f887da798ee98e5d0eec26.html#a27acb08303f887da798ee98e5d0eec26) |
|  | Frame time in seconds used during offline rendering. Set to 0 to leave the frame time the same as the last time it was set. [更多...](struct_ak_cmd___control_offline_rendering_a27acb08303f887da798ee98e5d0eec26.html#a27acb08303f887da798ee98e5d0eec26) |
|  | |

## 详细描述

Enable/disable offline rendering, and control the size of each audio frame when offline rendering is enabled.

Offline rendering disconnects the Sound Engine from hardware audio output. Instead, the Sound Engine renders one frame of audio every time [AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1) is called. This audio frame is not audible, but it can be captured to a file using Output Capture (see `AkCmd_ControlOutputCapture`).

参见
:   - [AkCommand\_ControlOfflineRendering](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab86dae96b811481c1afdab0901ee2f8f "See AkCmd_ControlOfflineRendering")
    - [AK::SoundEngine::SetOfflineRendering](namespace_a_k_1_1_sound_engine_a609347e86f41f68638fc318d18248ca2.html#a609347e86f41f68638fc318d18248ca2)
    - [AK::SoundEngine::SetOfflineRenderingFrameTime](namespace_a_k_1_1_sound_engine_a2239ac58b4276815dab0645476905150.html#a2239ac58b4276815dab0645476905150)
    - [AkCmd\_ControlOutputCapture](struct_ak_cmd___control_output_capture.html)
    - [利用 Wwise 进行离线渲染](goingfurther_offlinerendering.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1200](_ak_command_types_8h_source.html#l01200) 行定义.