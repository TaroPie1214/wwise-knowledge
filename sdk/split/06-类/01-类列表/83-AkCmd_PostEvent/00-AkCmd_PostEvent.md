# AkCmd_PostEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___post_event-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_PostEvent结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___post_event_afd6138b4a6f412766540cedc8357482d.html#afd6138b4a6f412766540cedc8357482d) |
|  | Unique ID that will be associated with this playback. Use [AK\_SoundEngine\_GeneratePlayingID()](_ak_command_buffer_8h_a4d75a81be7be245c1e49cea34e32bfc3.html#a4d75a81be7be245c1e49cea34e32bfc3) to generate a new unique playing ID. [更多...](struct_ak_cmd___post_event_afd6138b4a6f412766540cedc8357482d.html#afd6138b4a6f412766540cedc8357482d) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [eventID](struct_ak_cmd___post_event_ac2f257b0dc6268b25c6dcb57075ff5a2.html#ac2f257b0dc6268b25c6dcb57075ff5a2) |
|  | Unique ID of the event [更多...](struct_ak_cmd___post_event_ac2f257b0dc6268b25c6dcb57075ff5a2.html#ac2f257b0dc6268b25c6dcb57075ff5a2) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___post_event_a2a1a6012ddf0620e9778d4ed52905e7e.html#a2a1a6012ddf0620e9778d4ed52905e7e) |
|  | Associated game object ID [更多...](struct_ak_cmd___post_event_a2a1a6012ddf0620e9778d4ed52905e7e.html#a2a1a6012ddf0620e9778d4ed52905e7e) |
|  | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [actionTargetPlayingID](struct_ak_cmd___post_event_a851418131024aef23feb4365383fb3de.html#a851418131024aef23feb4365383fb3de) |
|  | Filters the "Target" of actions in the event by a playing ID. Set to AK\_INVALID\_PLAYING\_ID to disable target filtering. Not all actions are affected by this; see AkActionOnEventType for the list of action types affected by this option. [更多...](struct_ak_cmd___post_event_a851418131024aef23feb4365383fb3de.html#a851418131024aef23feb4365383fb3de) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [flags](struct_ak_cmd___post_event_aa2f0adaa40744e91a817798b1640ac1e.html#aa2f0adaa40744e91a817798b1640ac1e) |
|  | (optional) Bitmask: see [AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) [更多...](struct_ak_cmd___post_event_aa2f0adaa40744e91a817798b1640ac1e.html#aa2f0adaa40744e91a817798b1640ac1e) |
|  | |
| [AkEventCallbackFunc](_ak_callback_types_8h_a276c9e8420fee177debd0838b664d7c7.html#a276c9e8420fee177debd0838b664d7c7) | [callback](struct_ak_cmd___post_event_a717b82e877eef07dbda23ec1f9af1b4a.html#a717b82e877eef07dbda23ec1f9af1b4a) |
|  | (optional) Callback function [更多...](struct_ak_cmd___post_event_a717b82e877eef07dbda23ec1f9af1b4a.html#a717b82e877eef07dbda23ec1f9af1b4a) |
|  | |
| void \* | [callbackCookie](struct_ak_cmd___post_event_afea65a6d78378883d7da55d63494e52f.html#afea65a6d78378883d7da55d63494e52f) |
|  | (optional) Callback cookie [更多...](struct_ak_cmd___post_event_afea65a6d78378883d7da55d63494e52f.html#afea65a6d78378883d7da55d63494e52f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [numExternalSources](struct_ak_cmd___post_event_a5572fa3bb9d905f3b4e334aee3bb6a08.html#a5572fa3bb9d905f3b4e334aee3bb6a08) |
|  | (optional) Number of elements in `externalSources` array [更多...](struct_ak_cmd___post_event_a5572fa3bb9d905f3b4e334aee3bb6a08.html#a5572fa3bb9d905f3b4e334aee3bb6a08) |
|  | |

## 详细描述

Posts an event. When this command is executed, the actions referenced in the event will be executed. The user is responsible for providing a new unique playingID value for every instance of this command. Re-using the same playing ID will cause actions in this event to be associated with an existing playback.

If `numExternalSources` is set to a value higher than 0, then the client is expected to call AK\_CommandBuffer\_AddExternalSources after the command:

```
auto cmd = (AkCmd_PostEvent*)AK_CommandBuffer_Add(buffer, AkCommand_PostEvent);
// Fill out the command...
cmd->numExternalSources = myExternalSourcesArray.size();
AK_CommandBuffer_AddExternalSources(buffer, myExternalSourcesArray.size(), myExternalSourcesArray.data());
```

This command can fail for the following reasons:

- AK\_InvalidParameter: `eventID` is not valid or `numExternalSources` is higher than 0 and not enough external sources were added after the command.
- AK\_InsufficientMemory: Failed to allocate memory necessary to begin processing the command
- AK\_ResourceInUse: `playingID` was already used in a previous post event command. Use `AK_SoundEngine_GeneratePlayingID()` to ensure that a unique ID is generated for each post event command.
- AK\_IDNotFound: Event ID not found.
- AK\_PartialSuccess: When connected to the Wwise Profiler, command has been delayed to a later frame until Wwise synchronizes the event.
- AK\_MaxReached: Event Cooldown parameters for eventID did not allow the event to play.

参见
:   - [AkCommand\_PostEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf20e9790432e3db005cd602adcf4d962 "See AkCmd_PostEvent")
    - [AK\_CommandBuffer\_AddExternalSources](_ak_command_buffer_8h_ad436cc2841e8ed9bd0a45cb5a5b28bdd.html#ad436cc2841e8ed9bd0a45cb5a5b28bdd)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [160](_ak_command_types_8h_source.html#l00160) 行定义.