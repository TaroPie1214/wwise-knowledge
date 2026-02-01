# Release Notes 2017.2.0.6500.836

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2017.2.0.6500.836

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the 2017.2.0.6500.836 release of the integration (in addition to upgrading to the new Unreal build).

[Migration Notes 2017.2.0.6500.836](migrationnotes_2017_2_0.html)

# Unreal Engine 4.17/4.18 - Wwise 2017.2.0.6500.836

- Improved listener handling while in the Editor. See [Using the Editor Listener](features_editor_listener.html) for more information.
- Added a new WAAPI-enabled Wwise picker. See [Using Waapi Features](features_editor_wwise_browser.html#features_editor_waapi_picker) for more information.
- Improved Sequencer integration with scrubbing and 'play from anywhere' support. See [Using the Level Sequencer](using_features_sequencer.html) for more information.
- Added WAAPI-enabled waveform rendering to AkAudioEventSection Sequencer sections. See [Using the Level Sequencer](using_features_sequencer.html) for more information.
- Exposed WAAPI to Blueprint.
- Added WAAPI-enabled widgets for use in UMG. See [WAAPI 小组件](pg_features_objects__w_a_a_p_i.html) for more information.
- **WG-30009** Fixed: Added support for multiple listeners via Blueprint.
- **WG-30010** Fixed: [`SetMultiplePositions`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad63431938ab1e605a1f6e7fb013c0128.html) is now exposed in Blueprint.
- **WG-33932** Fixed: Removed the experimental alternate occlusion feature.
- **WG-34745** Fixed: Reduced Lower Engine memory pool size on mobile platforms.
- **WG-34879** Fixed: Exposed the collision channel used for the occlusion line trace in AkComponent's properties.
- **WG-35104** Fixed: Fixed listeners to be properly handled in a multiplayer scenario.
- **WG-35307** Fixed: Added more configurations to the Set Bus Config Blueprint node.
- **WG-35614** Fixed: Removed coordinates conversion. 有关详细信息，请参阅 [迁移到新的坐标系](migrationnotes_2017_2_0.html#migration_to_new_coord_system) 章节。