# Unreal Engine 4.8 - Wwise 2014.1.5

|  |
| --- |
| Wwise Unreal Integration Documentation |

Unreal Engine 4.8 - Wwise 2014.1.5

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the Unreal Engine 4.8 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.8 - Wwise v2014.1.5

- **UI-206** Fixed: Sounds with an attenuation can now be heard when an animation window is opened.
- **UI-212** Fixed: Added a "Load Init Bank" Blueprint node.
- **UI-213** Fixed: Added null checks in Blueprint nodes, preventing crashes.
- **UI-214** Fixed: No crash when saving an output capture to disk.
- **UI-215** Fixed: No issue with the Attenuation Scaling Factor of an AkComponent not being set when attached to an actor.
- **UI-217** Fixed: Made AkReverbVolume's collision settings visible in the details panel.
- **UI-220** Fixed: Fixed the occlusion fade behavior for sounds that a spawn occluded.
- **UI-223** Fixed: The gathering of the max attenuations for AkEvent does not halt when the parsing of one SoundBank fails.
- **UI-226** Fixed: SoundBank generation is now performed by the 32-bit WwiseCLI.exe when the 64-bit WwiseCLI.exe is missing.
- **UI-230** Fixed: Now using `OnComponentDestroyed` instead of `FinishDestroy` to unregister Wwise Game Objects, which had caused some Game Objects to be registered for too long.
- **UI-233** Fixed: Added validity checks on actors in the GetGameObjectID function.
- **UI-234** Fixed: Multiple viewports in the SetListener function are properly handled. This fixes a crash in AkAudioDevice.cpp.
- **UI-236** Fixed: The Location Type given to the GetAkComponent Blueprint node is properly handled.
- **UI-239** Fixed: No crash at engine shutdown as a result of the Bank Manager unloading SoundBanks that might already have been destroyed.
- Added a "Follow" check box to the AnimNotify\_AkEvent. Leaving it unchecked will post the AkEvent at a specific location, instead of attaching to the parent.
- Added a new AnimNotify: AnimNotify\_AkEventByName, allowing to post events using their name as a string.
- Added Debugging tools to Blueprints. For more information, see [Debug Blueprint 函数](features_blueprintdebug.html)