# Release Notes 2017.1.1.6340.673

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.1.1.6340.673

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2017.1.0.6302.628 and the 2017.1.1.6340.673 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.15/4.16/4.17 - Wwise 2017.1.1.6340.673

- Added support for Unreal Engine 4.17
- Since Unreal 4.17, the Unreal audio system needs to be disabled on the Xbox One and Switch platforms. Please refer to [常见问题解答](using_faq.html) for more information.
- **WG-34098** (Mac) An `AkComponent` located at exactly the same position as a volume with an `AkRoomComponent` will be properly assigned to that room.
- **WG-34119** Fixed: Uninitialized listener ID value sent to SpatialAudio API via `SetEmitterAuxSendValues`.
- **WG-34368** Fixed: `FAkAudioDevice::PostEventAtLocation` does not register game object.
- **WG-34388** Fixed: Crash in Editor when resetting RTPC sequence name to default in Level Sequencer.