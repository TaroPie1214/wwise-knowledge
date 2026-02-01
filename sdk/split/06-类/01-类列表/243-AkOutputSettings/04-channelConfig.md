# channelConfig

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkOutputSettings](struct_ak_output_settings.html)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkOutputSettings](struct_ak_output_settings_a057960789c35740f5ab7a653d92fc6c0.html#a057960789c35740f5ab7a653d92fc6c0) | | [AkOutputSettings](struct_ak_output_settings_a62fe5204e9347724db24cc64399fdb48.html#a62fe5204e9347724db24cc64399fdb48) | | [audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535) | | [channelConfig](struct_ak_output_settings_a5b546b6116a91f422fc0f61615159c06.html#a5b546b6116a91f422fc0f61615159c06) | | [ePanningRule](struct_ak_output_settings_aaf1191276e3ac40828eeefb1db8767f7.html#aaf1191276e3ac40828eeefb1db8767f7) | | [idDevice](struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html#a0e145d97af362b7f3267b64ca0e38054) | | [◆](#a5b546b6116a91f422fc0f61615159c06)channelConfig |  | | --- | | struct [AkChannelConfig](struct_ak_channel_config.html) AkOutputSettings::channelConfig |  Channel configuration for this output. Call [AkChannelConfig::Clear()](struct_ak_channel_config_a79d3e6e29649aabb9b9cd82bdd127d70.html#a79d3e6e29649aabb9b9cd82bdd127d70 "Clear the channel config. Becomes \"invalid\" (IsValid() returns false).") to let the engine use the default output configuration.   Hardware might not support the selected configuration.  在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [245](_ak_sound_engine_types_8h_source.html#l00245) 行定义. |