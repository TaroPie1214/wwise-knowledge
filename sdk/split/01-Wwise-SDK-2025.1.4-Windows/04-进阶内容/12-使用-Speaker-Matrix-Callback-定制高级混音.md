# 使用 Speaker Matrix Callback 定制高级混音

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

使用 Speaker Matrix Callback 定制高级混音

某些游戏对信号通路和声像平移有非常特殊的要求，而 Wwise 中可能无法满足这些要求。解决此限制的一种方法是注册到“Speaker Matrix Callback”（扬声器矩阵回调）。当 voice（声部）或总线将混入到另一条总线时，将调用此回调。通过此回调，您可以更改全局的和声道专用的声部或总线电平，从而修改混音或声像平移。

下面示例显示您可以如何为声部注册到此回调。注册是在发送播放此声部的事件时完成的。

[‘AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)( AK::EVENTS::PLAY\_HELLO, GAME\_OBJECT\_HUMAN, [AK\_SpeakerVolumeMatrix](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a398dd4133debe48731389d00ac8335fe), VoiceCallback );

VoiceCallback 回调描述如何识别输出总线，更改声部混入输出总线时的基础音量，以及更改声像平移音量来模拟不同的入射角。AkSpeakerVolumeMatrixCallbackInfo::pContext 暴露出声部相关信息，而 [AkSpeakerVolumeMatrixCallbackInfo::pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5 "Output mixing bus context. Use it to access a few useful panning and mixing services,...") 暴露出声部混入的总线相关信息（干信号的输出总线或辅助发送）。

static void VoiceCallback(

[AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) in\_eType, // Callback type.

[AkCallbackInfo](struct_ak_callback_info.html)\* in\_pCallbackInfo // 包含所需信息的结构。根据回调类型，您可以将它转换为适当的子类型。

)

{

// 我们知道这是扬声器音量矩阵回调。转换到适当的子类型。

[AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)( in\_eType == [AK\_SpeakerVolumeMatrix](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a398dd4133debe48731389d00ac8335fe) );

[AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html)\* pVolumeCallbackInfo = ([AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html)\*)in\_pCallbackInfo;

// 事件、游戏对象和播放 ID 对应于传递给 PostEvent() 以及 PostEvent() 返回的 ID。

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) eventID = pVolumeCallbackInfo->eventID;

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) objID = pVolumeCallbackInfo->gameObjID;

[AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) playingID = pVolumeCallbackInfo->playingID;

[AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)( eventID == AK::EVENTS::PLAY\_HELLO );

// This callback gets called for each bus into which the voice is routed. 在本例中，我们只希望定制混音到“My\_Dry\_Bus”总线。

if ( pVolumeCallbackInfo->[pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5)->GetBusID() != [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)( "My\_Dry\_Bus" ) )

return;

// 随便更改一下“基本”音量（即通用于所有声道）。

// ---------------------------------------------------------------------------------

// Double the volume (+6dB) of the voice into "My\_Dry\_Bus".

\*pVolumeCallbackInfo->[pfBaseVolume](struct_ak_speaker_volume_matrix_callback_info_a98f33fbc94ccda839e1069f549ded36e.html#a98f33fbc94ccda839e1069f549ded36e) \*= 2.f;

// Undo distance attenuation of the voice into "My\_Dry\_Bus" (in the single position case).

\*pVolumeCallbackInfo->[pfEmitterListenerVolume](struct_ak_speaker_volume_matrix_callback_info_a1e3f15191739f523ec8955e7e025cf7c.html#a1e3f15191739f523ec8955e7e025cf7c) = 1.f;

// Change panning of the voice into "My\_Dry\_Bus". 假设声音使用3D定位。

// ---------------------------------------------------------------------------------

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uNumPosition = pVolumeCallbackInfo->[pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)->[GetNum3DPositions](class_a_k_1_1_i_ak_mixer_input_context_a8d99842f211d766d9d7fc6479902facf.html#a8d99842f211d766d9d7fc6479902facf)();

// 3D声音可具有多个位置（请参阅AK::SoundEngine::SetMultiplePositions()）。在本例中，只考虑第一个位置。

if ( uNumPosition > 0 )

{

// 查询听者位置。通常，声部混音所用总线会与听者绑定。藉此，将游戏对象与混音器关联。

[AkTransform](struct_ak_transform.html) posListener;

[AK::IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info.html) \* pBusObject = pVolumeCallbackInfo->[pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5)->[GetGameObjectInfo](class_a_k_1_1_i_ak_plugin_context_base_a4c26b12664c7a9b73b6efc363a74a2e3.html#a4c26b12664c7a9b73b6efc363a74a2e3)();

if (pBusObject)

{

pBusObject->[GetGameObjectPosition](class_a_k_1_1_i_ak_game_object_plugin_info_ac1962ffbbe7276ea6aaf88ee36c78996.html#ac1962ffbbe7276ea6aaf88ee36c78996)(0, posListener);

// 颠倒听者位置，看有什么效果。

[AkVector](struct_ak_vector.html) listenerTop = posListener.[OrientationTop](struct_ak_transform_a3fb8ed7b29d03c5e365b5c06320ca24e.html#a3fb8ed7b29d03c5e365b5c06320ca24e)();

listenerTop.[X](struct_ak_vector_ad976d2990ff1acc75d10051a7035baea.html#ad976d2990ff1acc75d10051a7035baea) = -listenerTop.[X](struct_ak_vector_ad976d2990ff1acc75d10051a7035baea.html#ad976d2990ff1acc75d10051a7035baea);

listenerTop.[Y](struct_ak_vector_a7d00da14f7e9d326592ba82a28d7bc0f.html#a7d00da14f7e9d326592ba82a28d7bc0f) = -listenerTop.[Y](struct_ak_vector_a7d00da14f7e9d326592ba82a28d7bc0f.html#a7d00da14f7e9d326592ba82a28d7bc0f);

listenerTop.[Z](struct_ak_vector_ae29b396901bdb7592f010b36bee9c868.html#ae29b396901bdb7592f010b36bee9c868) = -listenerTop.[Z](struct_ak_vector_ae29b396901bdb7592f010b36bee9c868.html#ae29b396901bdb7592f010b36bee9c868);

posListener.[SetOrientation](struct_ak_transform_a9bb03962057cebf8d48a3f6f62cedcb6.html#a9bb03962057cebf8d48a3f6f62cedcb6)(posListener.[OrientationFront](struct_ak_transform_a3bd22931409f0dc23578631a2a6d50c1.html#a3bd22931409f0dc23578631a2a6d50c1)(), listenerTop);

// 获取“发声体”游戏对象位置。

[AkTransform](struct_ak_transform.html) posEmitter;

pVolumeCallbackInfo->[pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)->[GetVoiceInfo](class_a_k_1_1_i_ak_mixer_input_context_afff91983cd78acdd305fd224b26501ee.html#afff91983cd78acdd305fd224b26501ee)()->GetGameObjectPosition(0, posEmitter);

// 使用总线/混音器的混音服务计算新的声像平移音量。

pVolumeCallbackInfo->[pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5)->[Compute3DPositioning](class_a_k_1_1_i_ak_mixer_plugin_context_aa3aebb0cd836c0dcab14e3d862e13626.html#aa3aebb0cd836c0dcab14e3d862e13626)(

posEmitter, // Emitter transform.

posListener, // 听者的变换。

pVolumeCallbackInfo->[pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)->[GetCenterPerc](class_a_k_1_1_i_ak_mixer_input_context_ad4e9e9d4667099f24dcc8820dbc62e05.html#ad4e9e9d4667099f24dcc8820dbc62e05)(), // 中置百分比。仅将单声道输入应用于带中置的输出。

pVolumeCallbackInfo->[pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)->[GetSpread](class_a_k_1_1_i_ak_mixer_input_context_a4c1d6a4163b0a1d64ee70486d0c81be5.html#a4c1d6a4163b0a1d64ee70486d0c81be5)(0), // 散布（Spread）。

pVolumeCallbackInfo->[pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)->[GetFocus](class_a_k_1_1_i_ak_mixer_input_context_ad32391f2f5dba6d7eb2f34dd9d604a31.html#ad32391f2f5dba6d7eb2f34dd9d604a31)(0), // 聚焦（Focus）。

pVolumeCallbackInfo->[inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f), // 输入的声道配置。

pVolumeCallbackInfo->[inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f).[uChannelMask](struct_ak_channel_config_a8fc646976d669b0b0bdf81371c2a2f76.html#a8fc646976d669b0b0bdf81371c2a2f76), // 声像摆位选用的输入声道掩码（被排除的输入声道将不会作用于输出）。

pVolumeCallbackInfo->[outputConfig](struct_ak_speaker_volume_matrix_callback_info_afd0b0f3ada00da404ddf2f3a8d269017.html#afd0b0f3ada00da404ddf2f3a8d269017), // 所需输出配置。

pVolumeCallbackInfo->[pVolumes](struct_ak_speaker_volume_matrix_callback_info_a8939707c798dfb3687a80a00db8a8c74.html#a8939707c798dfb3687a80a00db8a8c74) // 返回的音量矩阵。Must be preallocated using AK::SpeakerVolumes::Matrix::GetRequiredSize() (see AK::SpeakerVolumes::Matrix services).

);

}

}

}

以下示例显示如何注册到总线回调。在本例中，AkSpeakerVolumeMatrixCallbackInfo::pContext 暴露出总线相关信息，我们要将("My\_Bus")注册到这条总线，而 [AkSpeakerVolumeMatrixCallbackInfo::pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5 "Output mixing bus context. Use it to access a few useful panning and mixing services,...") 也对总线的父总线（或信号链中的下一条混音总线）暴露出总线相关信息，该总线是要将信号混音进去的总线。

[AK::SoundEngine::RegisterBusVolumeCallback](namespace_a_k_1_1_sound_engine_adc878481e54793302e90f59d1c90202f.html#adc878481e54793302e90f59d1c90202f)( [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)( "My\_Bus" ), BusCallback );

static void BusCallback(

[AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html)\* in\_pCallbackInfo // Structure containing desired bus information.

)

{

// 从总线调用：无法关联到播放 ID（playing ID）。

[AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)( in\_pCallbackInfo->playingID == [AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360) );

// Change panning volumes of the mixdown signal at the output of this bus before it gets mixed into its parent;

// Using mixing services, transmix input into a 3-stereo configuration, and silence out contribution to all other channels of the parent bus.

// 分配音量矩阵以获取转混增益（input\_config -> 3-stereo）。

[AkChannelConfig](struct_ak_channel_config.html) cfgThreeStereo;

cfgThreeStereo.[SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)( [AK\_SPEAKER\_SETUP\_3STEREO](_ak_speaker_config_8h_af7e4b223543b8464b7f39603f912308e.html#af7e4b223543b8464b7f39603f912308e) );

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uSize = [AK::SpeakerVolumes::Matrix::GetRequiredSize](namespace_a_k_1_1_speaker_volumes_1_1_matrix_a59458aba2b1be3fa678021a3aea813b9.html#a59458aba2b1be3fa678021a3aea813b9)( in\_pCallbackInfo->[inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f).[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc), cfgThreeStereo.[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc) );

[AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074) mxTransmix = ([AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074))AkAlloca( uSize );

in\_pCallbackInfo->[pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5)->[ComputeSpeakerVolumesDirect](class_a_k_1_1_i_ak_mixer_plugin_context_ab9131df4725689003defce52077eb72f.html#ab9131df4725689003defce52077eb72f)(

in\_pCallbackInfo->[inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f), // 输入的声道配置。

cfgThreeStereo, // 混音器输出的声道配置。

in\_pCallbackInfo->[pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)->[GetCenterPerc](class_a_k_1_1_i_ak_mixer_input_context_ad4e9e9d4667099f24dcc8820dbc62e05.html#ad4e9e9d4667099f24dcc8820dbc62e05)(),// Center%：使用 Wwise 计算的 center% 值。

mxTransmix );

// 将结果复制到真正的混音矩阵，并清除后置声道和 LFE（如适用的话）。

// 警告：我们不能假定混音总线有中置声道，因此我们需要证实一下。

[AkChannelConfig](struct_ak_channel_config.html) cfgThreeStereoANDBus;

cfgThreeStereoANDBus.[SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)( [AK\_SPEAKER\_SETUP\_3STEREO](_ak_speaker_config_8h_af7e4b223543b8464b7f39603f912308e.html#af7e4b223543b8464b7f39603f912308e) & in\_pCallbackInfo->[outputConfig](struct_ak_speaker_volume_matrix_callback_info_afd0b0f3ada00da404ddf2f3a8d269017.html#afd0b0f3ada00da404ddf2f3a8d269017).[uChannelMask](struct_ak_channel_config_a8fc646976d669b0b0bdf81371c2a2f76.html#a8fc646976d669b0b0bdf81371c2a2f76) );

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uNumOutputChannelsToCopy = cfgThreeStereoANDBus.[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc);

for ( [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uChanIn = 0; uChanIn < in\_pCallbackInfo->[inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f).[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc); uChanIn++ )

{

// 为各个输入声道获取输出音量向量。

[AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) vTransmixOut = [AK::SpeakerVolumes::Matrix::GetChannel](namespace_a_k_1_1_speaker_volumes_1_1_matrix_a77aabf10ae35e9ccd346662e29fba169.html#a77aabf10ae35e9ccd346662e29fba169)( mxTransmix, uChanIn, cfgThreeStereo.[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc) );

[AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa) vMixOut = [AK::SpeakerVolumes::Matrix::GetChannel](namespace_a_k_1_1_speaker_volumes_1_1_matrix_a77aabf10ae35e9ccd346662e29fba169.html#a77aabf10ae35e9ccd346662e29fba169)( in\_pCallbackInfo->[pVolumes](struct_ak_speaker_volume_matrix_callback_info_a8939707c798dfb3687a80a00db8a8c74.html#a8939707c798dfb3687a80a00db8a8c74), uChanIn, in\_pCallbackInfo->[outputConfig](struct_ak_speaker_volume_matrix_callback_info_afd0b0f3ada00da404ddf2f3a8d269017.html#afd0b0f3ada00da404ddf2f3a8d269017).[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc) );

// 将声像平移复制到前声道。

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uChanOut = 0;

while ( uChanOut < uNumOutputChannelsToCopy )

{

vMixOut[uChanOut] = vTransmixOut[uChanOut];

++uChanOut;

}

// 清除其他声道。

while ( uChanOut < in\_pCallbackInfo->outputConfig.uNumChannels )

{

vMixOut[uChanOut] = 0;

++uChanOut;

}

}

}

下一示例显示如何注册到总线以查询它的电平表数据。

// 注册到总线电平表。注意：注册到电平表特别是 True Peak（真峰值）和 K-Weighted Power（K加权功率电平表）需要相当大的性能消耗。

[AK::SoundEngine::RegisterBusMeteringCallback](namespace_a_k_1_1_sound_engine_a4935dbc8c375c82c03475a1dbde37a51.html#a4935dbc8c375c82c03475a1dbde37a51)( [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)( "My\_Bus" ), MeterCallback, ([AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729))( [AK\_EnableBusMeter\_TruePeak](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729a441c6538c4043ea68fb6df31c2a2d858) | [AK\_EnableBusMeter\_KPower](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729a3b13dfeeef85751ae9e6cf0b1852de1b) ) );

static void MeterCallback(

[AK::AkMetering](struct_a_k_1_1_ak_metering.html) \* in\_pMetering, // AK::AkMetering 结构体包含电平表信息。

[AkChannelConfig](struct_ak_channel_config.html) in\_channelConfig, // 总线的声道配置。

[AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729) in\_eMeteringFlags // RegisterBusMeteringCallback() 中请求的电平表标识。您只可从 in\_pMeteringInfo 获取相应的电平表值。尝试获取不对应的参数将失败。

)

{

// 由于我们注册了此回调，所以必须启用至少 True Peak 和 K-Weighted Power 电平表。

[AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)( ( in\_eMeteringFlags & [AK\_EnableBusMeter\_TruePeak](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729a441c6538c4043ea68fb6df31c2a2d858) ) && ( in\_eMeteringFlags & [AK\_EnableBusMeter\_KPower](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729a3b13dfeeef85751ae9e6cf0b1852de1b) ) );

// Get K-weighted power and do something with it.

[AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fPower = in\_pMetering->GetKWeightedPower();

// 获取 True Peak，并使用它执行某项操作。

// 每个声道有一个值。

[AK::SpeakerVolumes::ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064) vTruePeak = in\_pMetering->GetTruePeak();

for ( [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uChannel = 0; uChannel < in\_channelConfig.[uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc); uChannel++ )

{

[AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fChannelPeak = vTruePeak[uChannel];

...

}

...

}

[AkSpeakerVolumeMatrixCallbackInfo::pVolumes](struct_ak_speaker_volume_matrix_callback_info_a8939707c798dfb3687a80a00db8a8c74.html#a8939707c798dfb3687a80a00db8a8c74)

AkSpeakerVolumesMatrixPtr pVolumes

Pointer to volume matrix describing the contribution of each source channel to destination channels....

**Definition:** [AkCallbackTypes.h:228](_ak_callback_types_8h_source.html#l00228)

[AkSpeakerVolumeMatrixCallbackInfo::inputConfig](struct_ak_speaker_volume_matrix_callback_info_a30e81ba08ad7b60f475ab431af67587f.html#a30e81ba08ad7b60f475ab431af67587f)

struct AkChannelConfig inputConfig

Channel configuration of the voice/bus.

**Definition:** [AkCallbackTypes.h:229](_ak_callback_types_8h_source.html#l00228)

[AkSpeakerVolumeMatrixCallbackInfo::outputConfig](struct_ak_speaker_volume_matrix_callback_info_afd0b0f3ada00da404ddf2f3a8d269017.html#afd0b0f3ada00da404ddf2f3a8d269017)

struct AkChannelConfig outputConfig

Channel configuration of the output bus.

**Definition:** [AkCallbackTypes.h:230](_ak_callback_types_8h_source.html#l00228)

[AK::IAkMixerInputContext::GetSpread](class_a_k_1_1_i_ak_mixer_input_context_a4c1d6a4163b0a1d64ee70486d0c81be5.html#a4c1d6a4163b0a1d64ee70486d0c81be5)

virtual AkReal32 GetSpread(AkUInt32 in\_uIndex)=0

[AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729)

AkMeteringFlags

Metering flags. Used for specifying bus metering, through AK::SoundEngine::RegisterBusVolumeCallback(...

**Definition:** [AkEnums.h:265](_ak_enums_8h_source.html#l00264)

[AkSpeakerVolumeMatrixCallbackInfo::pfBaseVolume](struct_ak_speaker_volume_matrix_callback_info_a98f33fbc94ccda839e1069f549ded36e.html#a98f33fbc94ccda839e1069f549ded36e)

AkReal32 \* pfBaseVolume

Base volume, common to all channels.

**Definition:** [AkCallbackTypes.h:231](_ak_callback_types_8h_source.html#l00231)

[AkSpeakerVolumeMatrixCallbackInfo::pMixerContext](struct_ak_speaker_volume_matrix_callback_info_ac1e8922ff3762c07e99ba3acb98f0bb5.html#ac1e8922ff3762c07e99ba3acb98f0bb5)

AkMixerPluginContextPtr pMixerContext

Output mixing bus context. Use it to access a few useful panning and mixing services,...

**Definition:** [AkCallbackTypes.h:235](_ak_callback_types_8h_source.html#l00235)

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AK::SoundEngine::RegisterBusVolumeCallback](namespace_a_k_1_1_sound_engine_adc878481e54793302e90f59d1c90202f.html#adc878481e54793302e90f59d1c90202f)

AKSOUNDENGINE\_API AKRESULT RegisterBusVolumeCallback(AkUniqueID in\_busID, AkBusCallbackFunc in\_pfnCallback, void \*in\_pCookie=NULL)

[AkCallbackInfo](struct_ak_callback_info.html)

**Definition:** [AkCallbackTypes.h:273](_ak_callback_types_8h_source.html#l00272)

[AkChannelConfig::uNumChannels](struct_ak_channel_config_af86d291ad68bcc75d3a47e4582dc69fc.html#af86d291ad68bcc75d3a47e4582dc69fc)

AkUInt32 uNumChannels

Number of channels.

**Definition:** [AkSpeakerConfig.h:444](_ak_speaker_config_8h_source.html#l00444)

[AkChannelConfig](struct_ak_channel_config.html)

**Definition:** [AkSpeakerConfig.h:436](_ak_speaker_config_8h_source.html#l00435)

[AkChannelConfig::uChannelMask](struct_ak_channel_config_a8fc646976d669b0b0bdf81371c2a2f76.html#a8fc646976d669b0b0bdf81371c2a2f76)

AkUInt32 uChannelMask

Channel mask (configuration).

**Definition:** [AkSpeakerConfig.h:446](_ak_speaker_config_8h_source.html#l00446)

[AK\_SpeakerVolumeMatrix](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a398dd4133debe48731389d00ac8335fe)

@ AK\_SpeakerVolumeMatrix

Callback triggered at each frame, letting the client modify the speaker volume matrix....

**Definition:** [AkCallbackTypes.h:67](_ak_callback_types_8h_source.html#l00067)

[AK::SpeakerVolumes::Matrix::GetRequiredSize](namespace_a_k_1_1_speaker_volumes_1_1_matrix_a59458aba2b1be3fa678021a3aea813b9.html#a59458aba2b1be3fa678021a3aea813b9)

AkForceInline AkUInt32 GetRequiredSize(AkUInt32 in\_uNumChannelsIn, AkUInt32 in\_uNumChannelsOut)

**Definition:** [AkSpeakerVolumes.h:303](_ak_speaker_volumes_8h_source.html#l00303)

[AkTransform::OrientationTop](struct_ak_transform_a3fb8ed7b29d03c5e365b5c06320ca24e.html#a3fb8ed7b29d03c5e365b5c06320ca24e)

const AkVector & OrientationTop() const

Get orientation top vector.

**Definition:** [Ak3DObjects.h:275](_ak3_d_objects_8h_source.html#l00275)

[AkSpeakerVolumeMatrixCallbackInfo::pContext](struct_ak_speaker_volume_matrix_callback_info_a6930688e64bad2ce4019fc4c19de7962.html#a6930688e64bad2ce4019fc4c19de7962)

AkMixerInputContextPtr pContext

Context of the current voice/bus about to be mixed into the output bus with specified base volume and...

**Definition:** [AkCallbackTypes.h:234](_ak_callback_types_8h_source.html#l00234)

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc)

AkUInt32 AkUniqueID

Unique 32-bit ID

**Definition:** [AkTypedefs.h:31](_ak_typedefs_8h_source.html#l00031)

[AkTransform](struct_ak_transform.html)

Position and orientation of objects in a "local" space

**Definition:** [Ak3DObjects.h:255](_ak3_d_objects_8h_source.html#l00254)

[AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)

float AkReal32

32-bit floating point

**Definition:** [AkNumeralTypes.h:43](_ak_numeral_types_8h_source.html#l00043)

[AK::IAkGameObjectPluginInfo::GetGameObjectPosition](class_a_k_1_1_i_ak_game_object_plugin_info_ac1962ffbbe7276ea6aaf88ee36c78996.html#ac1962ffbbe7276ea6aaf88ee36c78996)

virtual AKRESULT GetGameObjectPosition(AkUInt32 in\_uIndex, AkSoundPosition &out\_position) const =0

[AK::IAkMixerInputContext::GetVoiceInfo](class_a_k_1_1_i_ak_mixer_input_context_afff91983cd78acdd305fd224b26501ee.html#afff91983cd78acdd305fd224b26501ee)

virtual IAkVoicePluginInfo \* GetVoiceInfo()=0

[AkVector::Y](struct_ak_vector_a7d00da14f7e9d326592ba82a28d7bc0f.html#a7d00da14f7e9d326592ba82a28d7bc0f)

AkReal32 Y

Y Position

**Definition:** [Ak3DObjects.h:128](_ak3_d_objects_8h_source.html#l00128)

[AK::IAkMixerInputContext::GetFocus](class_a_k_1_1_i_ak_mixer_input_context_ad32391f2f5dba6d7eb2f34dd9d604a31.html#ad32391f2f5dba6d7eb2f34dd9d604a31)

virtual AkReal32 GetFocus(AkUInt32 in\_uIndex)=0

[AkVector::X](struct_ak_vector_ad976d2990ff1acc75d10051a7035baea.html#ad976d2990ff1acc75d10051a7035baea)

AkReal32 X

X Position

**Definition:** [Ak3DObjects.h:127](_ak3_d_objects_8h_source.html#l00127)

[AK::SpeakerVolumes::Matrix::GetChannel](namespace_a_k_1_1_speaker_volumes_1_1_matrix_a77aabf10ae35e9ccd346662e29fba169.html#a77aabf10ae35e9ccd346662e29fba169)

AkForceInline VectorPtr GetChannel(MatrixPtr in\_pVolumeMx, AkUInt32 in\_uIdxChannelIn, AkUInt32 in\_uNumChannelsOut)

**Definition:** [AkSpeakerVolumes.h:313](_ak_speaker_volumes_8h_source.html#l00313)

[AK\_SPEAKER\_SETUP\_3STEREO](_ak_speaker_config_8h_af7e4b223543b8464b7f39603f912308e.html#af7e4b223543b8464b7f39603f912308e)

#define AK\_SPEAKER\_SETUP\_3STEREO

3.0 setup channel mask

**Definition:** [AkSpeakerConfig.h:68](_ak_speaker_config_8h_source.html#l00068)

[AK::IAkMixerInputContext::GetNum3DPositions](class_a_k_1_1_i_ak_mixer_input_context_a8d99842f211d766d9d7fc6479902facf.html#a8d99842f211d766d9d7fc6479902facf)

virtual AkUInt32 GetNum3DPositions()=0

[AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)

#define AKASSERT(Condition)

**Definition:** [AkAssert.h:69](_ak_assert_8h_source.html#l00069)

[AkTransform::SetOrientation](struct_ak_transform_a9bb03962057cebf8d48a3f6f62cedcb6.html#a9bb03962057cebf8d48a3f6f62cedcb6)

void SetOrientation(const AkVector &in\_orientationFront, const AkVector &in\_orientationTop)

Set orientation. Orientation front and top should be orthogonal and normalized.

**Definition:** [Ak3DObjects.h:341](_ak3_d_objects_8h_source.html#l00341)

[AK::SpeakerVolumes::MatrixPtr](namespace_a_k_1_1_speaker_volumes_a57e0ce3a8225a58dd886853164554074.html#a57e0ce3a8225a58dd886853164554074)

AkSpeakerVolumesVectorPtr MatrixPtr

**Definition:** [AkTypedefs.h:96](_ak_typedefs_8h_source.html#l00096)

[AK\_INVALID\_PLAYING\_ID](_ak_constants_8h_a5141397d9cce5d9656f58931596d8360.html#a5141397d9cce5d9656f58931596d8360)

static const AkPlayingID AK\_INVALID\_PLAYING\_ID

Invalid playing ID

**Definition:** [AkConstants.h:36](_ak_constants_8h_source.html#l00036)

[AkTransform::OrientationFront](struct_ak_transform_a3bd22931409f0dc23578631a2a6d50c1.html#a3bd22931409f0dc23578631a2a6d50c1)

const AkVector & OrientationFront() const

Get orientation front vector.

**Definition:** [Ak3DObjects.h:269](_ak3_d_objects_8h_source.html#l00269)

[AkVector::Z](struct_ak_vector_ae29b396901bdb7592f010b36bee9c868.html#ae29b396901bdb7592f010b36bee9c868)

AkReal32 Z

Z Position

**Definition:** [Ak3DObjects.h:129](_ak3_d_objects_8h_source.html#l00129)

[AkSpeakerVolumeMatrixCallbackInfo](struct_ak_speaker_volume_matrix_callback_info.html)

**Definition:** [AkCallbackTypes.h:227](_ak_callback_types_8h_source.html#l00226)

[AK::SoundEngine::RegisterBusMeteringCallback](namespace_a_k_1_1_sound_engine_a4935dbc8c375c82c03475a1dbde37a51.html#a4935dbc8c375c82c03475a1dbde37a51)

AKSOUNDENGINE\_API AKRESULT RegisterBusMeteringCallback(AkUniqueID in\_busID, AkBusMeteringCallbackFunc in\_pfnCallback, AkMeteringFlags in\_eMeteringFlags, void \*in\_pCookie=NULL)

[AkSpeakerVolumeMatrixCallbackInfo::pfEmitterListenerVolume](struct_ak_speaker_volume_matrix_callback_info_a1e3f15191739f523ec8955e7e025cf7c.html#a1e3f15191739f523ec8955e7e025cf7c)

AkReal32 \* pfEmitterListenerVolume

Emitter-listener pair-specific gain. When there are multiple emitter-listener pairs,...

**Definition:** [AkCallbackTypes.h:232](_ak_callback_types_8h_source.html#l00232)

[AK::IAkMixerPluginContext::Compute3DPositioning](class_a_k_1_1_i_ak_mixer_plugin_context_aa3aebb0cd836c0dcab14e3d862e13626.html#aa3aebb0cd836c0dcab14e3d862e13626)

virtual AKRESULT Compute3DPositioning(AkReal32 in\_fAngle, AkReal32 in\_fElevation, AkReal32 in\_fSpread, AkReal32 in\_fFocus, AkChannelConfig in\_inputConfig, AkChannelMask in\_uInputChanSel, AkChannelConfig in\_outputConfig, AkReal32 in\_fCenterPerc, AK::SpeakerVolumes::MatrixPtr out\_mxVolumes)=0

[AK::AkMetering](struct_a_k_1_1_ak_metering.html)

Struct containing metering information about a buffer. Depending on when this struct is generated,...

**Definition:** [AkCommonDefs.h:193](_ak_common_defs_8h_source.html#l00192)

[AK::SpeakerVolumes::ConstVectorPtr](namespace_a_k_1_1_speaker_volumes_a095cabe0d4b9f1339e578eeb8a348064.html#a095cabe0d4b9f1339e578eeb8a348064)

AkSpeakerVolumesConstVectorPtr ConstVectorPtr

**Definition:** [AkTypedefs.h:97](_ak_typedefs_8h_source.html#l00097)

[AK::IAkMixerPluginContext::ComputeSpeakerVolumesDirect](class_a_k_1_1_i_ak_mixer_plugin_context_ab9131df4725689003defce52077eb72f.html#ab9131df4725689003defce52077eb72f)

virtual AKRESULT ComputeSpeakerVolumesDirect(AkChannelConfig in\_inputConfig, AkChannelConfig in\_outputConfig, AkReal32 in\_fCenterPerc, AK::SpeakerVolumes::MatrixPtr out\_mxVolumes)=0

[AK\_EnableBusMeter\_TruePeak](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729a441c6538c4043ea68fb6df31c2a2d858)

@ AK\_EnableBusMeter\_TruePeak

Enable computation of true peak metering (most CPU and memory intensive).

**Definition:** [AkEnums.h:268](_ak_enums_8h_source.html#l00268)

[AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)

AKSOUNDENGINE\_API AkUInt32 GetIDFromString(const char \*in\_pszString)

[AK\_EnableBusMeter\_KPower](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729a3b13dfeeef85751ae9e6cf0b1852de1b)

@ AK\_EnableBusMeter\_KPower

Enable computation of K-weighted power metering (used as a basis for computing loudness,...

**Definition:** [AkEnums.h:271](_ak_enums_8h_source.html#l00271)

[AK::IAkPluginContextBase::GetGameObjectInfo](class_a_k_1_1_i_ak_plugin_context_base_a4c26b12664c7a9b73b6efc363a74a2e3.html#a4c26b12664c7a9b73b6efc363a74a2e3)

virtual IAkGameObjectPluginInfo \* GetGameObjectInfo()=0

[AkChannelConfig::SetStandard](struct_ak_channel_config_a4c0f4b3d39608a10c9b330c1ef8281a7.html#a4c0f4b3d39608a10c9b330c1ef8281a7)

AkForceInline void SetStandard(AkUInt32 in\_uChannelMask)

Set channel config as a standard configuration specified with given channel mask.

**Definition:** [AkSpeakerConfig.h:511](_ak_speaker_config_8h_source.html#l00511)

[AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732)

AkCallbackType

Type of callback. Used as a bitfield in methods AK::SoundEngine::PostEvent() and AK::SoundEngine::Dyn...

**Definition:** [AkCallbackTypes.h:61](_ak_callback_types_8h_source.html#l00060)

[AK::IAkMixerInputContext::GetCenterPerc](class_a_k_1_1_i_ak_mixer_input_context_ad4e9e9d4667099f24dcc8820dbc62e05.html#ad4e9e9d4667099f24dcc8820dbc62e05)

virtual AkReal32 GetCenterPerc()=0

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AK::IAkGameObjectPluginInfo](class_a_k_1_1_i_ak_game_object_plugin_info.html)

Game object information available to plugins.

**Definition:** [IAkPlugin.h:105](_i_ak_plugin_8h_source.html#l00104)

[AkVector](struct_ak_vector.html)

3D vector for some operations in 3D space. Typically intended only for localized calculations due to ...

**Definition:** [Ak3DObjects.h:71](_ak3_d_objects_8h_source.html#l00070)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)

[AK::SpeakerVolumes::VectorPtr](namespace_a_k_1_1_speaker_volumes_ad437e8acf5a9509d22a2d13629502afa.html#ad437e8acf5a9509d22a2d13629502afa)

AkSpeakerVolumesMatrixPtr VectorPtr

**Definition:** [AkTypedefs.h:95](_ak_typedefs_8h_source.html#l00095)

[AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3)

AkUInt32 AkPlayingID

A unique identifier generated whenever a PostEvent is called (or when a Dynamic Sequence is created)....

**Definition:** [AkTypedefs.h:34](_ak_typedefs_8h_source.html#l00034)