# idDevice

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkDeviceDescription](struct_ak_device_description.html)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [deviceName](struct_ak_device_description_a92fab106652fec366709aaee87383e5f.html#a92fab106652fec366709aaee87383e5f) | | [deviceStateMask](struct_ak_device_description_ac0acc1661266c664aae7d9fd983315eb.html#ac0acc1661266c664aae7d9fd983315eb) | | [idDevice](struct_ak_device_description_a5e1be4d07a51040ccc6ff04a38e7d47c.html#a5e1be4d07a51040ccc6ff04a38e7d47c) | | [isDefaultDevice](struct_ak_device_description_aff286ff755788f1997fc4bf34846824f.html#aff286ff755788f1997fc4bf34846824f) | | [◆](#a5e1be4d07a51040ccc6ff04a38e7d47c)idDevice |  | | --- | | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) AkDeviceDescription::idDevice |  Device ID for Wwise. This is the same as what is returned from [AK::GetDeviceID](namespace_a_k_a84b3896b7b5b223c72b5ea826fae6bd8.html#a84b3896b7b5b223c72b5ea826fae6bd8) and [AK::GetDeviceIDFromName](namespace_a_k_a8609f19bc85d9ea8266c2fdd79ac5084.html#a8609f19bc85d9ea8266c2fdd79ac5084). Use it to specify the main device in AkPlatformInitSettings.idAudioDevice or in AK::SoundEngine::AddSecondaryOutput.  在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [58](_ak_sound_engine_types_8h_source.html#l00058) 行定义. |