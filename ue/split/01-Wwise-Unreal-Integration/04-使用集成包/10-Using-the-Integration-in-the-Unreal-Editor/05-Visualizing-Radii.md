# Visualizing Radii

|  |
| --- |
| Wwise Unreal Integration Documentation |

Visualizing Radii

When you select an [AkAmbientSound](pg_features_objects_actors.html#features_akambientsound), the relevant asset radii are drawn. If you modify the assets in Wwise Authoring while a WAAPI connection is enabled, the radii are updated in real time.

To update an asset radius:

1. In the Unreal Actor Browser, select an [AkAmbientSound](pg_features_objects_actors.html#features_akambientsound).
2. In Wwise Authoring, change any object associated with the Event assigned to the [AkAmbientSound](pg_features_objects_actors.html#features_akambientsound).
3. 若未启用 WAAPI，请重新生成 SoundBank。
4. Select the [AkAmbientSound](pg_features_objects_actors.html#features_akambientsound) again. The size of the corresponding sphere in the Unreal Editor changes at the same time.

若未启用 WAAPI，将从生成的 SoundBank 获取 **Max Attenuation**。 In your Wwise Project Settings, under the SoundBanks tab, ensure that **Generate Per Bank Metadata File**, **Generate JSON Metadata**, and **Max Attenuation** are selected. The next time you generate SoundBanks in the Unreal Editor, the Max Attenuation information is added to all `UAkAudioEvents`, and the attenuation spheres are visible in your level viewport.