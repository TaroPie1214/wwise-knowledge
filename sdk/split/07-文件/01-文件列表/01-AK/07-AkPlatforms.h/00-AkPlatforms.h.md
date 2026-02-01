# AkPlatforms.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)

[宏定义](#define-members)

AkPlatforms.h 文件参考

[浏览源代码.](_ak_platforms_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_ALIGN](_ak_platforms_8h_a51602f641089d986e226ed0ba0097d04.html#a51602f641089d986e226ed0ba0097d04)(\_declaration\_, \_alignment\_)   \_declaration\_ \_\_attribute\_\_( ( aligned( \_alignment\_ ) ) ) |
|  | |
| #define | [AK\_ALIGN\_TO\_NEXT\_BOUNDARY](_ak_platforms_8h_aeea979ecc1d2b33bff7a49def566a87c.html#aeea979ecc1d2b33bff7a49def566a87c)(\_\_num\_\_, \_\_boundary\_\_)   (((\_\_num\_\_) + ((\_\_boundary\_\_)-1)) & ~((\_\_boundary\_\_)-1)) |
|  | |
| #define | [AK\_IS\_POWER\_OF\_TWO](_ak_platforms_8h_ab696f456053547e7d983bcc6cadecae6.html#ab696f456053547e7d983bcc6cadecae6)(\_\_num\_\_)   (((\_\_num\_\_) & ((\_\_num\_\_) - 1)) == 0) |
|  | |
| #define | [AK\_ENDIANNESS\_LITTLE](_ak_platforms_8h_a43129f33569a64905954068e93781a77.html#a43129f33569a64905954068e93781a77) |
|  | |
| #define | [AK\_UNALIGNED](_ak_platforms_8h_acead03f1e665d8ec282067b72db8e7b6.html#acead03f1e665d8ec282067b72db8e7b6) |
|  | AK\_UNALIGNED refers to the \_\_unaligned compilation flag available on some platforms. Note that so far, on the tested platform this should always be placed before the pointer symbol \*. [更多...](_ak_platforms_8h_acead03f1e665d8ec282067b72db8e7b6.html#acead03f1e665d8ec282067b72db8e7b6) |
|  | |
| #define | [AK\_SELECTANY](_ak_platforms_8h_aace42721bf834d460bc43bf1c87c7c67.html#aace42721bf834d460bc43bf1c87c7c67) |
|  | |
| #define | [AK\_NODISCARD](_ak_platforms_8h_afdad98a324f1b63271ac05b0730074de.html#afdad98a324f1b63271ac05b0730074de)   [[nodiscard]] |
|  | |
| #define | [AK\_POINTER\_64](_ak_platforms_8h_a30feac218b1f7cd4084906e12a7a2bdf.html#a30feac218b1f7cd4084906e12a7a2bdf) |
|  | |
| #define | [AK\_UNUSEDVAR](_ak_platforms_8h_a8480b535dbd765ff758a7b80d8f2bc4e.html#a8480b535dbd765ff758a7b80d8f2bc4e)(x)   ((void)(x)) |
|  | |
| #define | [AK\_THREAD\_LOCAL](_ak_platforms_8h_ab570f541b59332b92a43b8a9b7b43d4e.html#ab570f541b59332b92a43b8a9b7b43d4e) |
|  | |
| #define | [AkAllocaTypedArray](_ak_platforms_8h_a1830b75eb0a32b6bfaed6930bf528238.html#a1830b75eb0a32b6bfaed6930bf528238)(\_type\_, \_count\_)   ( (\_type\_\*)AkAlloca(sizeof(\_type\_) \* \_count\_) ) |
|  | Stack allocation helpers [更多...](_ak_platforms_8h_a1830b75eb0a32b6bfaed6930bf528238.html#a1830b75eb0a32b6bfaed6930bf528238) |
|  | |

## 详细描述

Audiokinetic platform checks. This is where we detect which platform is being compiled, and where we define the corresponding AK-specific symbols.

在文件 [AkPlatforms.h](_ak_platforms_8h_source.html) 中定义.

[AkAudioMarker](struct_ak_audio_marker.html)

Defines the parameters of a marker.

**Definition:** [AkAudioMarker.h:16](_ak_audio_marker_8h_source.html#l00015)

[AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005)

AkEventCallbackFunc AkCallbackFunc

**Definition:** [AkCallbackTypes.h:350](_ak_callback_types_8h_source.html#l00350)

[AK::SoundEngine::GetSampleRate](namespace_a_k_1_1_sound_engine_ad008c85c2aa438f16f2272fd494ecd84.html#ad008c85c2aa438f16f2272fd494ecd84)

AKSOUNDENGINE\_API AkUInt32 GetSampleRate()

[AK](namespace_a_k.html)

Definition of data structures for AkAudioObject

**Definition:** [AkWwiseSDKVersion.cs:31](_ak_wwise_s_d_k_version_8cs_source.html#l00030)

[AK::IAkEffectPlugin](class_a_k_1_1_i_ak_effect_plugin.html)

Software effect plug-in interface (see 创建声音引擎效果器插件).

**Definition:** [IAkPlugin.h:848](_i_ak_plugin_8h_source.html#l00847)

[AkEventCallbackInfo](struct_ak_event_callback_info.html)

**Definition:** [AkCallbackTypes.h:159](_ak_callback_types_8h_source.html#l00158)

[AK::IAkSourcePlugin](class_a_k_1_1_i_ak_source_plugin.html)

Wwise sound engine source plug-in interface (see 创建声音引擎源插件).

**Definition:** [IAkPlugin.h:1309](_i_ak_plugin_8h_source.html#l01308)

[AkOutputSettings::ePanningRule](struct_ak_output_settings_aaf1191276e3ac40828eeefb1db8767f7.html#aaf1191276e3ac40828eeefb1db8767f7)

enum AkPanningRule ePanningRule

**Definition:** [AkSoundEngineTypes.h:250](_ak_sound_engine_types_8h_source.html#l00245)

[AkAudioMarker::dwIdentifier](struct_ak_audio_marker_adef1428c7f4476db4dbeee707eec8984.html#adef1428c7f4476db4dbeee707eec8984)

AkUInt32 dwIdentifier

Identifier.

**Definition:** [AkAudioMarker.h:17](_ak_audio_marker_8h_source.html#l00017)

[AkMarkerCallbackInfo](struct_ak_marker_callback_info.html)

**Definition:** [AkCallbackTypes.h:180](_ak_callback_types_8h_source.html#l00179)

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AkCallbackInfo](struct_ak_callback_info.html)

**Definition:** [AkCallbackTypes.h:273](_ak_callback_types_8h_source.html#l00272)

[AK.Wwise::Plugin::ConversionSuccess](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a292220d538f5f5381f6f0514c782059f)

@ ConversionSuccess

**Definition:** [PluginDef.h:149](_plugin_def_8h_source.html#l00149)

[AkChannelConfig::uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc)

AkUInt32 uNumChannels

Number of channels.

**Definition:** [AkSpeakerConfig.h:444](_ak_speaker_config_8h_source.html#l00444)

[AkChannelConfig](struct_ak_channel_config.html)

**Definition:** [AkSpeakerConfig.h:436](_ak_speaker_config_8h_source.html#l00435)

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)

AKSOUNDENGINE\_API AKRESULT RegisterGameObj(AkGameObjectID in\_gameObjectID)

[AkAudioMarker::dwLabelSize](struct_ak_audio_marker_aa1c572e31ad099fb92d0bae6cf1e15f7.html#aa1c572e31ad099fb92d0bae6cf1e15f7)

AkUInt32 dwLabelSize

Length of label read the from the file + terminating null character.

**Definition:** [AkAudioMarker.h:20](_ak_audio_marker_8h_source.html#l00020)

[AK::GetDeviceID](namespace_a_k_a84b3896b7b5b223c72b5ea826fae6bd8.html#a84b3896b7b5b223c72b5ea826fae6bd8)

AKSOUNDENGINE\_API AkUInt32 GetDeviceID(IMMDevice \*in\_pDevice)

[AkOutputSettings](struct_ak_output_settings.html)

Platform-independent initialization settings of output devices.

**Definition:** [AkSoundEngineTypes.h:219](_ak_sound_engine_types_8h_source.html#l00218)

[AK::FNVHash](class_a_k_1_1_f_n_v_hash.html)

**Definition:** [AkFNVHash.h:74](_ak_f_n_v_hash_8h_source.html#l00073)

[AK::SoundEngine::SetOfflineRenderingFrameTime](namespace_a_k_1_1_sound_engine_a2239ac58b4276815dab0645476905150.html#a2239ac58b4276815dab0645476905150)

AKSOUNDENGINE\_API AKRESULT SetOfflineRenderingFrameTime(AkReal32 in\_fFrameTimeInSeconds)

[AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270)

uint8\_t AkUInt8

Unsigned 8-bit integer

**Definition:** [AkNumeralTypes.h:34](_ak_numeral_types_8h_source.html#l00034)

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc)

AkUInt32 AkUniqueID

Unique 32-bit ID

**Definition:** [AkTypedefs.h:31](_ak_typedefs_8h_source.html#l00031)

[AK::Comm::Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)

AKSOUNDENGINE\_API AKRESULT Init(const AkCommSettings &in\_settings)

[AK\_EndOfEvent](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a5ad7a62bfb83e7450cc685b3e51f767a)

@ AK\_EndOfEvent

Callback triggered when reaching the end of an event. No additional callback information.

**Definition:** [AkCallbackTypes.h:62](_ak_callback_types_8h_source.html#l00062)

[AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)

float AkReal32

32-bit floating point

**Definition:** [AkNumeralTypes.h:43](_ak_numeral_types_8h_source.html#l00043)

[AkPanningRule\_Speakers](_ak_enums_8h_a6a7a16f5e74370707bb7bff7fb29a112.html#a6a7a16f5e74370707bb7bff7fb29a112a136f30c9cc3bc0be7afbe6223012131b)

@ AkPanningRule\_Speakers

Left and right positioned 60 degrees apart (by default - see AK::SoundEngine::GetSpeakerAngles()).

**Definition:** [AkEnums.h:244](_ak_enums_8h_source.html#l00244)

[AK::SoundEngine::ReplaceOutput](namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html#a81521a4611d3891c499ec9c5eb421ac2)

AKSOUNDENGINE\_API AKRESULT ReplaceOutput(const AkOutputSettings &in\_Settings, AkOutputDeviceID in\_outputDeviceId, AkOutputDeviceID \*out\_pOutputDeviceId=NULL)

[AK.Wwise::Plugin::PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823)

CPluginInfo PluginInfo

**Definition:** [PluginInstanceTypes.h:537](_plugin_instance_types_8h_source.html#l00537)

[AK\_Marker](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ad3d6fcbeb177c536da8eb74d0f132827)

@ AK\_Marker

Callback triggered when encountering a marker during playback. Callback info can be cast to AkMarkerC...

**Definition:** [AkCallbackTypes.h:64](_ak_callback_types_8h_source.html#l00064)

[AK.Wwise::Plugin::V1::MediaConverter::ConvertFile](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter_a4324f69ea75774cbb8270c01bf607dd7.html#a4324f69ea75774cbb8270c01bf607dd7)

virtual ConversionResult ConvertFile(const GUID &in\_guidPlatform, const BasePlatformID &in\_basePlatform, const AkOSChar \*in\_szSourceFile, const AkOSChar \*in\_szDestFile, AkUInt32 in\_uSampleRate, AkUInt32 in\_uBlockLength, IProgress \*in\_pProgress, IWriteString \*io\_pError) const =0

Converts a file.

[AK::Comm::Term](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f)

AKSOUNDENGINE\_API void Term()

[AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24)

AkInt32 AkTimeMs

Time in ms

**Definition:** [AkTypedefs.h:35](_ak_typedefs_8h_source.html#l00035)

[AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4](_ak_speaker_config_8h_aa900d4eb858c3c0d2b2caa9fbf28a2d0.html#aa900d4eb858c3c0d2b2caa9fbf28a2d0)

#define AK\_SPEAKER\_SETUP\_DOLBY\_7\_1\_4

Dolby 7.1.4 setup channel mask

**Definition:** [AkSpeakerConfig.h:113](_ak_speaker_config_8h_source.html#l00113)

[PlatformID::PS5](namespace_platform_i_d_a7bf4c6443044f5e48210d3d09cc32a64.html#a7bf4c6443044f5e48210d3d09cc32a64)

AK\_ID\_DECLARE BasePlatformID PS5

**Definition:** [PlatformID.h:106](_platform_i_d_8h_source.html#l00106)

[PlatformID::Windows](namespace_platform_i_d_a21b4bdace04cb72145c4c7eb72761486.html#a21b4bdace04cb72145c4c7eb72761486)

AK\_ID\_DECLARE BasePlatformID Windows

**Definition:** [PlatformID.h:94](_platform_i_d_8h_source.html#l00094)

[AK.Wwise::Plugin::V1::MediaConverter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_media_converter.html)

**Definition:** [MediaConverter.h:125](_media_converter_8h_source.html#l00124)

[AK::SoundEngine::RegisterCaptureCallback](namespace_a_k_1_1_sound_engine_a25dabf28198a55f9c11ab74e640be331.html#a25dabf28198a55f9c11ab74e640be331)

AKSOUNDENGINE\_API AKRESULT RegisterCaptureCallback(AkCaptureCallbackFunc in\_pfnCallback, AkOutputDeviceID in\_idOutput=AK\_INVALID\_OUTPUT\_DEVICE\_ID, void \*in\_pCookie=NULL)

[AK::IAkSourcePluginContext](class_a_k_1_1_i_ak_source_plugin_context.html)

**Definition:** [IAkPlugin.h:460](_i_ak_plugin_8h_source.html#l00459)

[AK::SoundEngine::RenderAudio](namespace_a_k_1_1_sound_engine_afe54af0f5be38be061e8a3c7d7642bb1.html#afe54af0f5be38be061e8a3c7d7642bb1)

AKSOUNDENGINE\_API AKRESULT RenderAudio(bool in\_bAllowSyncRender=true)

[AK.Wwise::Plugin::V1::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html)

Wwise API for general Audio Plug-in's backend.

**Definition:** [AudioPlugin.h:133](_audio_plugin_8h_source.html#l00130)

[AK.Wwise::Plugin::V1::ObjectMedia::SetMediaSource](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media_aecc2d90460e0c684e027504f9fffe647.html#aecc2d90460e0c684e027504f9fffe647)

bool SetMediaSource(const AkOSChar \*in\_pszFilePathToImport, unsigned int in\_Index, bool in\_bReplace)

Requests to set the specified file as a data input file.

**Definition:** [HostObjectMedia.h:347](_host_object_media_8h_source.html#l00347)

[AK::SoundEngine::UnregisterCaptureCallback](namespace_a_k_1_1_sound_engine_acc0738332d393048d352d1ca6d92b355.html#acc0738332d393048d352d1ca6d92b355)

AKSOUNDENGINE\_API AKRESULT UnregisterCaptureCallback(AkCaptureCallbackFunc in\_pfnCallback, AkOutputDeviceID in\_idOutput=AK\_INVALID\_OUTPUT\_DEVICE\_ID, void \*in\_pCookie=NULL)

[AK.Wwise::Plugin::ConversionResult](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3)

ConversionResult

Conversion error code.

**Definition:** [PluginDef.h:148](_plugin_def_8h_source.html#l00147)

[AK::IAkPluginServiceMarkers::CreateMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_adc860123c5af8918edcc787a8459d65b.html#adc860123c5af8918edcc787a8459d65b)

virtual IAkMarkerNotificationService \* CreateMarkerNotificationService(IAkSourcePluginContext \*in\_pSourcePluginContext)=0

[AK\_Fail](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a904c9822fd2d40bb0ea6bfad9ead659b)

@ AK\_Fail

The operation failed.

**Definition:** [AkEnums.h:35](_ak_enums_8h_source.html#l00035)

[AkOutputSettings::channelConfig](struct_ak_output_settings_a5b546b6116a91f422fc0f61615159c06.html#a5b546b6116a91f422fc0f61615159c06)

struct AkChannelConfig channelConfig

**Definition:** [AkSoundEngineTypes.h:254](_ak_sound_engine_types_8h_source.html#l00245)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AK::SoundEngine::SetOfflineRendering](namespace_a_k_1_1_sound_engine_a609347e86f41f68638fc318d18248ca2.html#a609347e86f41f68638fc318d18248ca2)

AKSOUNDENGINE\_API AKRESULT SetOfflineRendering(bool in\_bEnableOfflineRendering)

[AK.Wwise::Plugin::RequestedHostInterface< Host >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4.html)

**Definition:** [Host.h:164](_host_8h_source.html#l00164)

[AK::SoundEngine::AddOutput](namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html#a15ab79f954a307902f529d8ccde8ad48)

AKSOUNDENGINE\_API AKRESULT AddOutput(const AkOutputSettings &in\_Settings, AkOutputDeviceID \*out\_pDeviceID=NULL, const AkGameObjectID \*in\_pListenerIDs=NULL, AkUInt32 in\_uNumListeners=0)

[AK::GetDeviceIDFromName](namespace_a_k_a8609f19bc85d9ea8266c2fdd79ac5084.html#a8609f19bc85d9ea8266c2fdd79ac5084)

AKSOUNDENGINE\_API AkUInt32 GetDeviceIDFromName(wchar\_t \*in\_szToken)

[AkOutputSettings::idDevice](struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html#a0e145d97af362b7f3267b64ca0e38054)

AkUInt32 idDevice

**Definition:** [AkSoundEngineTypes.h:245](_ak_sound_engine_types_8h_source.html#l00245)

[AkChannelConfig::SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)

AkForceInline void SetStandard(AkUInt32 in\_uChannelMask)

Set channel config as a standard configuration specified with given channel mask.

**Definition:** [AkSpeakerConfig.h:511](_ak_speaker_config_8h_source.html#l00511)

[AkAudioMarker::strLabel](struct_ak_audio_marker_aee87f10b0ad8d8bb5d226221479720a6.html#aee87f10b0ad8d8bb5d226221479720a6)

const char \* strLabel

Label of the marker taken from the file.

**Definition:** [AkAudioMarker.h:19](_ak_audio_marker_8h_source.html#l00019)

[AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732)

AkCallbackType

Type of callback. Used as a bitfield in methods AK::SoundEngine::PostEvent() and AK::SoundEngine::Dyn...

**Definition:** [AkCallbackTypes.h:61](_ak_callback_types_8h_source.html#l00060)

[AK.Wwise::Plugin::ConversionFailed](namespace_a_k_1_1_wwise_1_1_plugin_a63998463d5dba5bfb0df9321dbe3e5c3.html#a63998463d5dba5bfb0df9321dbe3e5c3a067c828fdfd88765697e4914fa192efc)

@ ConversionFailed

**Definition:** [PluginDef.h:151](_plugin_def_8h_source.html#l00151)

[AkOutputSettings::audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535)

AkUniqueID audioDeviceShareset

**Definition:** [AkSoundEngineTypes.h:241](_ak_sound_engine_types_8h_source.html#l00241)

[AK\_GET\_PLUGIN\_SERVICE\_MARKERS](_i_ak_plugin_8h_aca83a0bac8086bebd99fd3b1290926b5.html#aca83a0bac8086bebd99fd3b1290926b5)

#define AK\_GET\_PLUGIN\_SERVICE\_MARKERS(plugin\_ctx)

**Definition:** [IAkPlugin.h:1988](_i_ak_plugin_8h_source.html#l01988)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AkAudioBuffer](class_ak_audio_buffer.html)

**Definition:** [AkCommonDefs.h:310](_ak_common_defs_8h_source.html#l00309)

[AK::FNVHash::Compute](class_a_k_1_1_f_n_v_hash_a907841bf37541824958d382686b1fb1f.html#a907841bf37541824958d382686b1fb1f)

HashParams::HashType Compute(const void \*in\_pData, typename HashParams::SizeType in\_dataSize)

**Definition:** [AkFNVHash.h:105](_ak_f_n_v_hash_8h_source.html#l00105)

[AkAudioMarker::dwPosition](struct_ak_audio_marker_a614e69d4179a70b5d096b1812b3bd876.html#a614e69d4179a70b5d096b1812b3bd876)

AkUInt32 dwPosition

Position in the audio data in sample frames.

**Definition:** [AkAudioMarker.h:18](_ak_audio_marker_8h_source.html#l00018)

[AK\_SPEAKER\_SETUP\_STEREO](_ak_speaker_config_8h_a472757ac65daebc42373c503d4c3c894.html#a472757ac65daebc42373c503d4c3c894)

#define AK\_SPEAKER\_SETUP\_STEREO

2.0 setup channel mask

**Definition:** [AkSpeakerConfig.h:66](_ak_speaker_config_8h_source.html#l00066)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)

[AK::IAkPluginParam::ALL\_PLUGIN\_DATA\_ID](class_a_k_1_1_i_ak_plugin_param_a7d4422a73ca832f64edc0465e59be771.html#a7d4422a73ca832f64edc0465e59be771)

static const AkPluginParamID ALL\_PLUGIN\_DATA\_ID

**Definition:** [IAkPlugin.h:773](_i_ak_plugin_8h_source.html#l00773)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)

[AkAudioFormat](struct_ak_audio_format.html)

Defines the parameters of an audio buffer format.

**Definition:** [AkCommonDefs.h:61](_ak_common_defs_8h_source.html#l00060)

[AK.Wwise::Plugin::V1::ObjectMedia](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_media.html)

**Definition:** [HostObjectMedia.h:299](_host_object_media_8h_source.html#l00298)

[AK.Wwise::Plugin::MonitorData](struct_a_k_1_1_wwise_1_1_plugin_1_1_monitor_data.html)

**Definition:** [PluginDef.h:90](_plugin_def_8h_source.html#l00089)

[AkOutputDeviceID](_ak_typedefs_8h_ab608859e8c575f46ce18433e32aa2ccd.html#ab608859e8c575f46ce18433e32aa2ccd)

AkUInt64 AkOutputDeviceID

Audio Output device ID

**Definition:** [AkTypedefs.h:64](_ak_typedefs_8h_source.html#l00064)

[AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3)

AkUInt32 AkPlayingID

A unique identifier generated whenever a PostEvent is called (or when a Dynamic Sequence is created)....

**Definition:** [AkTypedefs.h:34](_ak_typedefs_8h_source.html#l00034)

[AkAudioBuffer::MaxFrames](class_ak_audio_buffer_a537445dce6e3ed09dd2c337fd73c6b41.html#a537445dce6e3ed09dd2c337fd73c6b41)

AkForceInline AkUInt16 MaxFrames() const

**Definition:** [AkCommonDefs.h:489](_ak_common_defs_8h_source.html#l00489)