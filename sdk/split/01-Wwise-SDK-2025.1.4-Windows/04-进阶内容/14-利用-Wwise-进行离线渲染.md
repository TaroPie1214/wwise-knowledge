# 利用 Wwise 进行离线渲染

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

利用 Wwise 进行离线渲染

# 离线渲染

Wwise 声音引擎提供离线渲染功能以便实现计算量大的非实时音频生成以及音频处理和计算量大的视频生成之间的同步。

|  |  |
| --- | --- |
|  | **注意:** 在使用同步 `AK::SoundEngine::LoadBank` 和 `AK::SoundEngine::UnloadBank` API 的应用中启用离线渲染时须格外小心。有关详细信息，请参阅 [音频渲染线程](goingfurther_eventmgrthread.html#eventmgrthread) 章节。 |

可使用 `AK::SoundEngine::RegisterCaptureCallback` 来注册音频捕获回调，以便借助相应机制来访问经过渲染的音频缓冲区。

下面举例阐释了如何实现离线渲染：

/// Video capture services accessible in the game code

namespace VideoCaptureServices

{

/// Possibly allocates buffers for video capture

void Initialize();

/// Possibly outputs captured video and audio as a movie file

void Finalize();

/// 可将单个视频帧缓冲区捕获到对应文件中。

void CaptureSingleFrame();

}

/// 可在游戏代码中访问音频捕获服务

namespace AudioCaptureServices

{

/// 分配缓冲区或打开文件以最终捕获音频样本。

void Initialize(unsigned in\_uSampleRate, unsigned in\_uChannels);

/// 一旦完成音频帧捕获，即释放缓冲区或文件句柄。

void Finalize();

/// 将音频样本添加到分配的缓冲区

void CaptureInterleavedSamples(float\* in\_pfSamples, unsigned in\_uSampleCount);

}

class GameInterface

{

// ...

public:

/// 每一游戏帧调用一次函数

virtual void UpdateCallback(float deltaTime //< 经过的实时时钟时间，与离线模式下所需的帧率相对

) = 0;

};

class Game : public GameInterface

{

// ...

private:

/// 在启用离线渲染时为 true。

bool m\_bIsOfflineRendering{ false };

/// 使用输出设备 ID 来注册/注销捕获回调。

[AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) m\_defaultOutputDeviceId{ [AK\_INVALID\_OUTPUT\_DEVICE\_ID](_ak_constants_8h_a10906a6c67e9c74df9aeb174aee77ec4.html#a10906a6c67e9c74df9aeb174aee77ec4) };

/// Wwise 音频捕获回调。

static void CaptureCallback([AkAudioBuffer](class_ak_audio_buffer.html)& in\_CaptureBuffer, [AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd) /\*in\_idOutput\*/, void\* /\*in\_pCookie\*/)

{

const unsigned uSampleCount = static\_cast<unsigned>(in\_CaptureBuffer.[uValidFrames](class_ak_audio_buffer_ab7f90fd99119b56e92e4cbf3559f98cd.html#ab7f90fd99119b56e92e4cbf3559f98cd)) \* in\_CaptureBuffer.[NumChannels](class_ak_audio_buffer_a4523322478ec9a0f9de0c7c72e65df2f.html#a4523322478ec9a0f9de0c7c72e65df2f)();

if (!uSampleCount)

return;

AudioCaptureServices::CaptureInterleavedSamples(in\_CaptureBuffer.[GetInterleavedData](class_ak_audio_buffer_a8b3f75d4e95d5ce9af0b4573fae87510.html#a8b3f75d4e95d5ce9af0b4573fae87510)(), uSampleCount);

}

public:

/// 通过调用函数来启用/禁用离线渲染

void [SetOfflineRendering](namespace_a_k_1_1_sound_engine_a609347e86f41f68638fc318d18248ca2.html#a609347e86f41f68638fc318d18248ca2)(bool bIsOfflineRendering //< true 表示离线渲染，false 表示实时渲染

)

{

const bool bWasOfflineRendering{ m\_bIsOfflineRendering };

m\_bIsOfflineRendering = bIsOfflineRendering;

// 在消息队列中发送消息来启用/禁用离线渲染。

[AK::SoundEngine::SetOfflineRendering](namespace_a_k_1_1_sound_engine_a609347e86f41f68638fc318d18248ca2.html#a609347e86f41f68638fc318d18248ca2)(m\_bIsOfflineRendering);

if (m\_bIsOfflineRendering == bWasOfflineRendering)

return;

// 在消息队列中发送消息来将离线渲染帧时间设为零，确保后续对 RenderAudio() 的调用不会生成更多音频样本。

[AK::SoundEngine::SetOfflineRenderingFrameTime](namespace_a_k_1_1_sound_engine_a2239ac58b4276815dab0645476905150.html#a2239ac58b4276815dab0645476905150)(0.0f);

// 调用 RenderAudio() 来刷新消息队列。在此调用之后，将启用/禁用离线渲染。

[AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1)();

if (m\_bIsOfflineRendering)

{

VideoCaptureServices::Initialize();

// 在实施离线渲染时，输出配置将默认切换为 Stereo 输出

// 为了渲染为不同的输出扬声器布局，将输出替换为以显式方式定义的输出。

// 在本例中，将切换为 7.1.4

[AkChannelConfig](struct_ak_channel_config.html) surroundConfig;

surroundConfig.[SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)([AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0));

// 发送消息来替换输出设备。

[AkOutputSettings](struct_ak_output_settings.html) newSettings;

newSettings.[audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535) = AK::AUDIO\_DEVICES::SYSTEM;

newSettings.[idDevice](struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html#a0e145d97af362b7f3267b64ca0e38054) = 0;

newSettings.[ePanningRule](struct_ak_output_settings_aaf1191276e3ac40828eeefb1db8767f7.html#aaf1191276e3ac40828eeefb1db8767f7) = [AkPanningRule\_Speakers](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112a136f30c9cc3bc0be7afbe6223012131b);

newSettings.[channelConfig](struct_ak_output_settings_a5b546b6116a91f422fc0f61615159c06.html#a5b546b6116a91f422fc0f61615159c06) = surroundConfig;

[AK::SoundEngine::ReplaceOutput](namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html#a81521a4611d3891c499ec9c5eb421ac2)(newSettings, 0, &m\_defaultOutputDeviceId);

// Flush the message queue again to make sure ReplaceOutput is processed, before registering the capture callback on the offline device

[AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1)(true);

const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSampleRate{ [AK::SoundEngine::GetSampleRate](namespace_a_k_1_1_sound_engine_ad008c85c2aa438f16f2272fd494ecd84.html#ad008c85c2aa438f16f2272fd494ecd84)() };

// 提供采样率和声道数以便分配相应的缓冲区。

AudioCaptureServices::Initialize(uSampleRate, surroundConfig.[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc));

[AK::SoundEngine::RegisterCaptureCallback](namespace_a_k_1_1_sound_engine_a25dabf28198a55f9c11ab74e640be331.html#a25dabf28198a55f9c11ab74e640be331)(&CaptureCallback, m\_defaultOutputDeviceId, this);

}

else

{

[AK::SoundEngine::UnregisterCaptureCallback](namespace_a_k_1_1_sound_engine_acc0738332d393048d352d1ca6d92b355.html#acc0738332d393048d352d1ca6d92b355)(&CaptureCallback, m\_defaultOutputDeviceId, this);

AudioCaptureServices::Finalize();

VideoCaptureServices::Finalize();

}

}

void UpdateCallback(float deltaTime) override

{

if (m\_bIsOfflineRendering)

[AK::SoundEngine::SetOfflineRenderingFrameTime](namespace_a_k_1_1_sound_engine_a2239ac58b4276815dab0645476905150.html#a2239ac58b4276815dab0645476905150)(deltaTime);

[AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1)();

if (m\_bIsOfflineRendering)

VideoCaptureServices::CaptureSingleFrame();

}

};

[AK::SoundEngine::GetSampleRate](namespace_a_k_1_1_sound_engine_ad008c85c2aa438f16f2272fd494ecd84.html#ad008c85c2aa438f16f2272fd494ecd84)

AKSOUNDENGINE\_API AkUInt32 GetSampleRate()

[AK\_INVALID\_OUTPUT\_DEVICE\_ID](_ak_constants_8h_a10906a6c67e9c74df9aeb174aee77ec4.html#a10906a6c67e9c74df9aeb174aee77ec4)

static const AkUInt32 AK\_INVALID\_OUTPUT\_DEVICE\_ID

Invalid Device ID

**Definition:** [AkConstants.h:47](_ak_constants_8h_source.html#l00047)

[AkOutputSettings::ePanningRule](struct_ak_output_settings_aaf1191276e3ac40828eeefb1db8767f7.html#aaf1191276e3ac40828eeefb1db8767f7)

enum AkPanningRule ePanningRule

**Definition:** [AkSoundEngineTypes.h:250](_ak_sound_engine_types_8h_source.html#l00245)

[AkChannelConfig::uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc)

AkUInt32 uNumChannels

Number of channels.

**Definition:** [AkSpeakerConfig.h:444](_ak_speaker_config_8h_source.html#l00444)

[AkAudioBuffer::NumChannels](class_ak_audio_buffer_a4523322478ec9a0f9de0c7c72e65df2f.html#a4523322478ec9a0f9de0c7c72e65df2f)

AkForceInline AkUInt32 NumChannels() const

Get the number of channels.

**Definition:** [AkCommonDefs.h:337](_ak_common_defs_8h_source.html#l00337)

[AkChannelConfig](struct_ak_channel_config.html)

**Definition:** [AkSpeakerConfig.h:436](_ak_speaker_config_8h_source.html#l00435)

[AkOutputSettings](struct_ak_output_settings.html)

Platform-independent initialization settings of output devices.

**Definition:** [AkSoundEngineTypes.h:219](_ak_sound_engine_types_8h_source.html#l00218)

[AK::SoundEngine::SetOfflineRenderingFrameTime](namespace_a_k_1_1_sound_engine_a2239ac58b4276815dab0645476905150.html#a2239ac58b4276815dab0645476905150)

AKSOUNDENGINE\_API AKRESULT SetOfflineRenderingFrameTime(AkReal32 in\_fFrameTimeInSeconds)

[AkPanningRule\_Speakers](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112a136f30c9cc3bc0be7afbe6223012131b)

@ AkPanningRule\_Speakers

Left and right positioned 60 degrees apart (by default - see AK::SoundEngine::GetSpeakerAngles()).

**Definition:** [AkEnums.h:244](_ak_enums_8h_source.html#l00244)

[AK::SoundEngine::ReplaceOutput](namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html#a81521a4611d3891c499ec9c5eb421ac2)

AKSOUNDENGINE\_API AKRESULT ReplaceOutput(const AkOutputSettings &in\_Settings, AkOutputDeviceID in\_outputDeviceId, AkOutputDeviceID \*out\_pOutputDeviceId=NULL)

[AkAudioBuffer::uValidFrames](class_ak_audio_buffer_ab7f90fd99119b56e92e4cbf3559f98cd.html#ab7f90fd99119b56e92e4cbf3559f98cd)

AkUInt16 uValidFrames

Number of valid sample frames in the audio buffer

**Definition:** [AkCommonDefs.h:502](_ak_common_defs_8h_source.html#l00502)

[AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0)

#define AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4

Dolby 7.1.4 setup channel mask

**Definition:** [AkSpeakerConfig.h:113](_ak_speaker_config_8h_source.html#l00113)

[AK::SoundEngine::RegisterCaptureCallback](namespace_a_k_1_1_sound_engine_a25dabf28198a55f9c11ab74e640be331.html#a25dabf28198a55f9c11ab74e640be331)

AKSOUNDENGINE\_API AKRESULT RegisterCaptureCallback(AkCaptureCallbackFunc in\_pfnCallback, AkOutputDeviceID in\_idOutput=AK\_INVALID\_OUTPUT\_DEVICE\_ID, void \*in\_pCookie=NULL)

[AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1)

AKSOUNDENGINE\_API AKRESULT RenderAudio(bool in\_bAllowSyncRender=true)

[AK::SoundEngine::UnregisterCaptureCallback](namespace_a_k_1_1_sound_engine_acc0738332d393048d352d1ca6d92b355.html#acc0738332d393048d352d1ca6d92b355)

AKSOUNDENGINE\_API AKRESULT UnregisterCaptureCallback(AkCaptureCallbackFunc in\_pfnCallback, AkOutputDeviceID in\_idOutput=AK\_INVALID\_OUTPUT\_DEVICE\_ID, void \*in\_pCookie=NULL)

[AkOutputSettings::channelConfig](struct_ak_output_settings_a5b546b6116a91f422fc0f61615159c06.html#a5b546b6116a91f422fc0f61615159c06)

struct AkChannelConfig channelConfig

**Definition:** [AkSoundEngineTypes.h:254](_ak_sound_engine_types_8h_source.html#l00245)

[AK::SoundEngine::SetOfflineRendering](namespace_a_k_1_1_sound_engine_a609347e86f41f68638fc318d18248ca2.html#a609347e86f41f68638fc318d18248ca2)

AKSOUNDENGINE\_API AKRESULT SetOfflineRendering(bool in\_bEnableOfflineRendering)

[AkOutputSettings::idDevice](struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html#a0e145d97af362b7f3267b64ca0e38054)

AkUInt32 idDevice

**Definition:** [AkSoundEngineTypes.h:245](_ak_sound_engine_types_8h_source.html#l00245)

[AkChannelConfig::SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)

AkForceInline void SetStandard(AkUInt32 in\_uChannelMask)

Set channel config as a standard configuration specified with given channel mask.

**Definition:** [AkSpeakerConfig.h:511](_ak_speaker_config_8h_source.html#l00511)

[AkOutputSettings::audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535)

AkUniqueID audioDeviceShareset

**Definition:** [AkSoundEngineTypes.h:241](_ak_sound_engine_types_8h_source.html#l00241)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AkAudioBuffer](class_ak_audio_buffer.html)

**Definition:** [AkCommonDefs.h:310](_ak_common_defs_8h_source.html#l00309)

[AkAudioBuffer::GetInterleavedData](class_ak_audio_buffer_a8b3f75d4e95d5ce9af0b4573fae87510.html#a8b3f75d4e95d5ce9af0b4573fae87510)

AkForceInline void \* GetInterleavedData()

**Definition:** [AkCommonDefs.h:359](_ak_common_defs_8h_source.html#l00359)

[AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd)

AkUInt64 AkOutputDeviceID

Audio Output device ID

**Definition:** [AkTypedefs.h:64](_ak_typedefs_8h_source.html#l00064)