# uDiscoveryBroadcast

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkCommSettings](struct_ak_comm_settings.html)
- [Ports](struct_ak_comm_settings_1_1_ports.html)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Ports](struct_ak_comm_settings_1_1_ports_a04376f3823460eb29d46983ba40bf3c3.html#a04376f3823460eb29d46983ba40bf3c3) | | [uCommand](struct_ak_comm_settings_1_1_ports_a2980cfef40f976dd403f8f48c0789265.html#a2980cfef40f976dd403f8f48c0789265) | | [uDiscoveryBroadcast](struct_ak_comm_settings_1_1_ports_ac18f3080b45b5eba2634527d5d27e75c.html#ac18f3080b45b5eba2634527d5d27e75c) | | [◆](#ac18f3080b45b5eba2634527d5d27e75c)uDiscoveryBroadcast |  | | --- | | [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) AkCommSettings::Ports::uDiscoveryBroadcast |  This is where the authoring application broadcasts "Game Discovery" requests to discover games running on the network. Default value: 24024.  警告  Unlike the other port in this structure, this port cannot be dynamic: setting it to 0 will disable discovery. See [一个固定端口：Discovery Broadcast](workingwithsdks_initialization.html#initialization_comm_ports_discovery_broadcast) for more details.  在文件 [AkCommunication.h](_ak_communication_8h_source.html) 第 [81](_ak_communication_8h_source.html#l00081) 行定义. |