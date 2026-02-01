# Release Notes 2018.1.0.6714.1065

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.0.6714.1065

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2018.1.0.6714.1065 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.19/4.20 - Wwise 2018.1.0.6714.1065

- Added support for Unreal Engine 4.20.
- **WG-30002** Added support for audio input using the Wwise Audio Input plug-in. 请参阅 [Providing Audio Input to Wwise](using_features_audioinput.html) 。
- **WG-33507** Exposed Event and SoundBank callbacks to Blueprint. See [在 Blueprint 中使用回调](features_blueprintcallback.html) for more information.
- **WG-34570** Added ability to register to the global callback via delegates.
- **WG-35615** At sound engine initialization time the floor plane can be set using a new value in `AkInitSettings`. The Audiokinetic Unreal integration sets this value, in AkAudioDevice.cpp, to use X-Y as the floor plane.
- **WG-38608** Added experimental support for Lumin.
- **WG-38676** Fixed: Changing Spatial Audio Volume shape makes Unreal Editor freeze.