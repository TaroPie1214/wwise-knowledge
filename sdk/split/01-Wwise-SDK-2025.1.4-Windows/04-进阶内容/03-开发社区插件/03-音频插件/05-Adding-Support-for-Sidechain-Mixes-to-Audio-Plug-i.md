# Adding Support for Sidechain Mixes to Audio Plug-ins

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Adding Support for Sidechain Mixes to Audio Plug-ins

This topic explains how to add support for Sidechain Mixes to custom Effect plug-ins. For information about how to use Sidechain Mixes with built-in Wwise plug-ins, see [Using Sidechain Mixes with Effects](https://www.audiokinetic.com/library/edge/?source=Help&id=using_sidechain_mixes_with_effects).

# Defining Sidechain Mixes in Wwise Authoring

In the Authoring part of an audio plug-in, you must configure a Sidechain Mix as a Reference element, as described in [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag). The following sample code demonstrates how to add a Sidechain Mix Reference element to the `Properties` element of the plug-in's XML description.

<EffectPlugin Name="MySidechainPlugin">

<Properties>

<Property Name="Gain" [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="Real32" SupportRTPCType="Additive">

<AudioEnginePropertyID>0</AudioEnginePropertyID>

<Restrictions>

<ValueRestriction>

<Range [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="Real32">

<[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>-96.3</[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>

<[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>0</[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>

</Range>

</ValueRestriction>

</Restrictions>

</Property>

<Reference Name="SidechainRef" DisplayName="Sidechain Mix Source">

<AudioEnginePropertyID>1</AudioEnginePropertyID>

<Restrictions>

<TypeEnumerationRestriction>

<[Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) Name="SidechainMix" />

</TypeEnumerationRestriction>

</Restrictions>

</Reference>

</Properties>

</EffectPlugin>

In order to read the Reference, your plug-in backend must derive from `AK::Wwise::Plugin::RequestReferenceSet`, which provides an `m_referenceSet` member to your class, through which you can access services that read the object ShortIDs of any References.

class MySidechainPlugin

: public [AK::Wwise::Plugin::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html)

, public [AK::Wwise::Plugin::RequestReferenceSet](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4.html)

{

public:

MySidechainPlugin() {}

// AK::Wwise::Plugin::AudioPlugin

virtual bool [GetBankParameters](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539)(const GUID& in\_guidPlatform, [AK::Wwise::Plugin::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html)& in\_dataWriter) const override

{

in\_dataWriter.[WriteReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8d9b58e2ecba7f95721d4b89b7f9630f.html#a8d9b58e2ecba7f95721d4b89b7f9630f)(m\_propertySet.GetReal32(in\_guidPlatform, szGain));

in\_dataWriter.[WriteInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9626e22ea3ba15a71d2cf51ac2332693.html#a9626e22ea3ba15a71d2cf51ac2332693)(m\_referenceSet.GetReferenceShortId(in\_guidPlatform, szSidechainRef));

return true;

}

};

The `m_referenceSet` includes functions that read additional information from referenced objects, as described in `ak_wwise_plugin_host_reference_set_v1`. However, for Sidechain Mixes, the most important function is `ak_wwise_plugin_host_reference_set_v1::GetReferenceShortId` because it retrieves the Short ID of the referenced object. The Short ID is what other APIs in the sound engine use to interact with Sidechain Mixes, so that data must be included during SoundBank serialization.

|  |  |
| --- | --- |
|  | **备注:** The Short ID of a Reference is also sent to the sound engine runtime through `IAkPluginParam::SetParam`, using the `AudioEnginePropertyID` as the `in_lParamID` parameter, when Wwise Authoring is connected to a runtime and live editing of the Effect is performed. |

# Using Sidechain Mixes in the Sound Engine

To interact with Sidechain Mixes during Effect plug-in execution, use the following APIs:

- `IAkEffectPluginContext::GetSidechainMixChannelConfig`
- `IAkEffectPluginContext::SendToSidechainMix`
- `IAkEffectPluginContext::ReceiveFromSidechainMix`

Channel configuration can change without notice during sound engine execution, either through modifications to the Sidechain Mix during live editing or through other sound engine systems such as calls to `AK::SoundEngine::SetSidechainMixConfig`. Therefore, we recommend that you always call `AkEffectPluginContext::GetSidechainMixChannelConfig` to read the channel configuration before you send to or receive from the Sidechain Mix.

To send to or receive from a Sidechain mix, you must do the following:

- Initialize an `AkAudioBuffer`.
- Provide the ShortID of the Sidechain Mix as a parameter.
- Provide an additional, 64-bit identifier as a scope for the Sidechain Mix.

You can use the scope to constrain a Sidechain Mix to a specific listener even if you use the definition across multiple listeners. Built-in Wwise plug-ins define the scope as either the Game Object ID of the voice or bus the plug-in is running on `IAkEffectPluginContext::GetGameObjectInfo`, or use a value of 0 for a Global scope.

To ensure interoperability with other plug-ins, we recommend that you follow this pattern, although it is not required to do so. For example, you might want to design a custom plug-in to allow a sound designer to target a remote Game Object ID, instead of the voice or bus's local Game Object ID.

Sending to and receiving from a Sidechain Mix also requires an `AkAudioBuffer` to be properly initialized in order for the operation to succeed.

To send to a Sidechain Mix, the `AkAudioBuffer::channelConfig` must match the Sidechain Mix's channel configuration and `AkAudioBuffer::uMaxFrames` must match the sound engine's audio granularity, such as the buffer length returned by `IAkGlobalPluginContext::GetMaxBufferLength`. After you call `IAkEffectPluginContext::SendToSidechainMix`, you can immediately destroy the `AkAudioBuffer` and `AkAudioBuffer::pData`. `IAkEffectPluginContext::SendToSidechainMix` internally copies all of the audio data provided, so the audio buffer does not have to stay allocated indefinitely.

Receiving from a Sidechain Mix has similar restrictions on `AkAudioBuffer::channelConfig` and `AkAudioBuffer::uMaxFrames`. You must also provide an appropriate memory allocation for `AkAudioBuffer::pData` before you call `IAkEffectPluginContext::ReceiveFromSidechainMix`. Calling `IAkEffectPluginContext::ReceiveFromSidechainMix` copies the Sidechain Mix's audio data to `AkAudioBuffer::pData` and replaces any existing data. It might be necessary to handle the `AK_IDNotFound` result because it can be returned if the Sidechain Mix ID is not loaded or registered by the sound engine, or if no data was sent to the Sidechain Mix in a previous sound engine frame. For example, you could zero out the audio buffer and continue with normal execution of the Effect.

[AK.Wwise::Plugin::V1::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html)

Interface used to write data during sound bank generation.

**Definition:** [HostDataWriter.h:245](_host_data_writer_8h_source.html#l00244)

[AK::SpeakerVolumes::Vector::Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)

AkForceInline void Max(AkReal32 \*in\_pVolumesDst, const AkReal32 \*in\_pVolumesSrc, AkUInt32 in\_uNumChannels)

**Definition:** [AkSpeakerVolumes.h:283](_ak_speaker_volumes_8h_source.html#l00283)

[AK.Wwise::Plugin::V1::DataWriter::WriteReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8d9b58e2ecba7f95721d4b89b7f9630f.html#a8d9b58e2ecba7f95721d4b89b7f9630f)

bool WriteReal32(float in\_value)

Writes a 32-bit, single-precision floating point value.

**Definition:** [HostDataWriter.h:427](_host_data_writer_8h_source.html#l00427)

[AK::TempAlloc::Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)

Type

IDs of temporary memory pools used by the sound engine.

**Definition:** [AkTempAllocDefs.h:63](_ak_temp_alloc_defs_8h_source.html#l00062)

[AK.Wwise::Plugin::V1::DataWriter::WriteInt32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a9626e22ea3ba15a71d2cf51ac2332693.html#a9626e22ea3ba15a71d2cf51ac2332693)

bool WriteInt32(int32\_t in\_value)

Writes a 32-bit signed integer value.

**Definition:** [HostDataWriter.h:323](_host_data_writer_8h_source.html#l00323)

[AK.Wwise::Plugin::V1::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html)

Wwise API for general Audio Plug-in's backend.

**Definition:** [AudioPlugin.h:133](_audio_plugin_8h_source.html#l00130)

[AK.Wwise::Plugin::RequestedHostInterface< ReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_reference_set_01_4.html)

**Definition:** [HostReferenceSet.h:536](_host_reference_set_8h_source.html#l00536)

[AK.Wwise::Plugin::V1::AudioPlugin::GetBankParameters](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539)

virtual bool GetBankParameters(const GUID &in\_guidPlatform, DataWriter &in\_dataWriter) const

Obtains parameters that will be written to a bank.

**Definition:** [AudioPlugin.h:228](_audio_plugin_8h_source.html#l00228)

[AK::SpeakerVolumes::Vector::Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)

AkForceInline void Min(AkReal32 \*in\_pVolumesDst, const AkReal32 \*in\_pVolumesSrc, AkUInt32 in\_uNumChannels)

**Definition:** [AkSpeakerVolumes.h:291](_ak_speaker_volumes_8h_source.html#l00291)