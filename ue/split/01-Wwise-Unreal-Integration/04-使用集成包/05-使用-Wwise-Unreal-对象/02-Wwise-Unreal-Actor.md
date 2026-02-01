# Wwise Unreal Actor

|  |
| --- |
| Wwise Unreal Integration Documentation |

Wwise Unreal Actor

### 目录

- [AkAmbientSound](#features_akambientsound)
- [AkReverbVolume](#features_akreverbvolume)

# AkAmbientSound

`AkAmbientSound` 是一个 `AActor` 类，其使用方式与 Unreal Audio 系统配套提供的 `AAmbientSound` 对象相同。您可以通过其自有对象 Blueprint 函数或使用 Start All Ambient Sounds 和 Stop All Ambient Sounds 全局辅助函数来控制其播放行为。同时，`AkAmbientSound` 还包含 [AkComponent](pg_features_objects_components.html#features_akcomponent) （具有自己的属性）。

属性：

- **Stop When Owner Is Destroyed**：在销毁 AkAmbientSound 时自动停止 Event。
- **Auto Post**：在 BeginPlay 时自动发送关联的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。

Blueprint 函数：

- **Start All Ambient Sounds**：开始播放所有环境声。
- **Start Ambient Sound**：开始播放所选环境声。
- **Stop All Ambient Sounds**：停止播放所有环境声。
- **Stop Ambient Sound**：停止播放所选环境声。

# AkReverbVolume

`AkReverbVolume` 是一个 `AVolume` 类，其使用方式与 Unreal Audio 系统配套提供的 `AReverbVolume` 对象相同。它可以通过 Editor 中的任何 `Brush` 生成。通过 [AkLateReverbComponent](pg_features_objects_components.html#features_aklatereverbcomponent) 来获得混响效果。