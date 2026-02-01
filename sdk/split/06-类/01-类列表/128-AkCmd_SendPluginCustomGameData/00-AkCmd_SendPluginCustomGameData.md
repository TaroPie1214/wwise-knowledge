# AkCmd_SendPluginCustomGameData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___send_plugin_custom_game_data-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SendPluginCustomGameData结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [busID](struct_ak_cmd___send_plugin_custom_game_data_a71fdb1dcc2c8a4fd2792e5139d31e70a.html#a71fdb1dcc2c8a4fd2792e5139d31e70a) |
|  | Bus ID. For source plug-ins, specify AK\_INVALID\_UNIQUE\_ID. [更多...](struct_ak_cmd___send_plugin_custom_game_data_a71fdb1dcc2c8a4fd2792e5139d31e70a.html#a71fdb1dcc2c8a4fd2792e5139d31e70a) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___send_plugin_custom_game_data_a9f8b46260b490eebfb4880a5f5fa7985.html#a9f8b46260b490eebfb4880a5f5fa7985) |
|  | Game Object ID. Pass AK\_INVALID\_GAME\_OBJECT to send custom data with global scope. Game object scope supersedes global scope, as with RTPCs. [更多...](struct_ak_cmd___send_plugin_custom_game_data_a9f8b46260b490eebfb4880a5f5fa7985.html#a9f8b46260b490eebfb4880a5f5fa7985) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [pluginType](struct_ak_cmd___send_plugin_custom_game_data_a7918758575991f947573918e88751224.html#a7918758575991f947573918e88751224) |
|  | Plug-in type (for example, source or effect). See [AkPluginType](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4). [更多...](struct_ak_cmd___send_plugin_custom_game_data_a7918758575991f947573918e88751224.html#a7918758575991f947573918e88751224) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [companyID](struct_ak_cmd___send_plugin_custom_game_data_af804f1be0e0597d2fbea7a0d719b0941.html#af804f1be0e0597d2fbea7a0d719b0941) |
|  | Company identifier (as declared in the plug-in description XML file) [更多...](struct_ak_cmd___send_plugin_custom_game_data_af804f1be0e0597d2fbea7a0d719b0941.html#af804f1be0e0597d2fbea7a0d719b0941) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [pluginID](struct_ak_cmd___send_plugin_custom_game_data_ab8e5fc267b55d6eb05af85d9097f71c7.html#ab8e5fc267b55d6eb05af85d9097f71c7) |
|  | Plug-in identifier (as declared in the plug-in description XML file) [更多...](struct_ak_cmd___send_plugin_custom_game_data_ab8e5fc267b55d6eb05af85d9097f71c7.html#ab8e5fc267b55d6eb05af85d9097f71c7) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [dataSize](struct_ak_cmd___send_plugin_custom_game_data_a668271d0385277255bad659a019e554d.html#a668271d0385277255bad659a019e554d) |
|  | Size of data in bytes [更多...](struct_ak_cmd___send_plugin_custom_game_data_a668271d0385277255bad659a019e554d.html#a668271d0385277255bad659a019e554d) |
|  | |

## 详细描述

Sends custom game data to a plug-in that resides on a bus (effect plug-in) or a voice (source plug-in).

When `dataSize` is greater than 0, the Sound Engine expects binary data to follow this command. For example:

```
auto cmd = (AkCmd_SendPluginCustomGameData*)AK_CommandBuffer_Add(buffer, AkCmd_SendPluginCustomGameData);
cmd->busID = myBusID;
cmd->pluginType = AkPluginTypeEffect;
cmd->companyID = myCompanyID;
cmd->pluginID = myPluginID;
cmd->dataSize = plugin_data.size();
AK_CommandBuffer_AddArray(buffer, 1, plugin_data.size(), plugin_data.data());
```

Data will be copied and stored into a separate list. Previous entry is deleted when a new one is sent. Set `dataSize` to 0 to clear item from the list.

|  |  |
| --- | --- |
|  | **备注:** The plug-in type and ID are passed and matched with plugins set on the desired bus. This means that multiple instances of the same plug-in on a given bus' effect chain will always receive the same data. |

This command can fail for the following reasons:

- `AK_InvalidParameter:` `pluginID` is invalid, or there is less binary data following the command than what `dataSize` declares.
- `AK_InsufficientMemory:` Not enough memory to complete the operation.

参见
:   - [AkCommand\_SendPluginCustomGameData](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdabf0e7dc9ceb02348eeb4ebfea428b713 "See AkCmd_SendPluginCustomGameData")
    - [AK::SoundEngine::SendPluginCustomGameData](namespace_a_k_1_1_sound_engine_a25efe2a9b18ad130f4fc4c0c3599ec30.html#a25efe2a9b18ad130f4fc4c0c3599ec30)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1321](_ak_command_types_8h_source.html#l01321) 行定义.