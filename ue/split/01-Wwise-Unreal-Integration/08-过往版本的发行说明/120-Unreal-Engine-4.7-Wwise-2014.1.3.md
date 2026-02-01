# Unreal Engine 4.7 - Wwise 2014.1.3

|  |
| --- |
| Wwise Unreal Integration Documentation |

Unreal Engine 4.7 - Wwise 2014.1.3

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the Unreal Engine 4.7 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.7 - Wwise v2014.1.3

- Added support for the Android platform.
- Now including a new demonstration game, based on Epic's First Person Template. For more information, see [使用 Wwise Demo Game](using_samplegame.html).
- All Wwise Integration settings now have their page in the Unreal Project Settings window. No need to manually edit INI files anymore!
- **UI-157** Fixed: When generating the SoundBanks, add the Max Attenuation information to AkEvents. It can be retrieved via Blueprints.
- **UI-187** Fixed: Allow the preview of AkEvents from the Content Browser by pressing the space bar.
- **UI-188** Fixed: When an AkAmbientSound is about to be destroyed, cancel its event callback to avoid using a destroyed object in the callback.
- **UI-189** Fixed: Added an attenuation scaling factor to AkComponent, allowing to make each actor's attenuation radius unique.
- **UI-190** Fixed: Added a new Blueprint node that allows setting the exact list of loaded SoundBanks. 有关详细信息，请参阅 [已移除和已弃用的函数](features_blueprintsoundbanks.html#features_blueprintsoundbanks_removed) 章节。
- **UI-193** Fixed: Get the `UAkAudioEventFactory` directly when creating `UAkAudioEvents` by Drag & Drop.
- **UI-194** Fixed: Optimized the finding of `AkReverbVolumes` at a location.
- **UI-195** Fixed: Added [blueprint\_actor\_posteventbyname](features_blueprintactor.html#blueprint_actor_postevent), [features\_blueprintsoundbanks\_removed](features_blueprintsoundbanks.html#features_blueprintsoundbanks_removed), and [已移除和已弃用的函数](features_blueprintsoundbanks.html#features_blueprintsoundbanks_removed) Blueprint nodes.
- **UI-196** Fixed: Added a configuration parameter for the maximum number of concurrent Reverb Volumes applied on a sound.
- **UI-201** Fixed: Added an UAkAudioEvent to AkComponent, to bring it in sync with Unreal's AudioComponent. An AkComponent can by added in a Blueprint via drag & drop of a UAkAudioEvent. An actor with an attached AkComponent will also show its attenuation radius in the Editor.
- **UI-204** Fixed: Added code to unload auto-loaded SoundBanks.
- **UI-205** Fixed: Don't post events in a world that does not allow audio playback.
- **UI-208** Fixed: Fixed a potential crash when generating SoundBanks.