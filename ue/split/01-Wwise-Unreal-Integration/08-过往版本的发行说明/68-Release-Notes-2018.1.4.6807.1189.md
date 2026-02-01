# Release Notes 2018.1.4.6807.1189

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.4.6807.1189

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.3.6784.1177 and the 2018.1.4.6807.1189 release of the integration (in addition to upgrading to the new Unreal build).

# Unreal Engine 4.19/4.20/4.21 - Wwise 2018.1.4.6807.1189

- **WG-39671**: Exposed `ExecuteActionOnEvent` to Blueprint.
- **WG-40333**: Ensured all `PostEvent` calls go through the Callback Manager.
- **WG-40344**: Exposed GetSpeakerAngles and SetSpeakerAngles in Blueprint.
- **WG-40365**: Changed SoundBank generation message to make it clearer that the SoundBank can be generated but still have errors.
- **WG-40380**: Prevented crash when calling `PostAkEventAndWaitForEnd` with an invalid AkEvent.