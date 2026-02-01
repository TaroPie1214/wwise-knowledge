# AkComponent Blueprint 函数

|  |
| --- |
| Wwise Unreal Integration Documentation |

AkComponent Blueprint 函数

您可以针对 [AkComponent](pg_features_objects_components.html#features_akcomponent) 场景组件执行多个 Wwise 函数。在 Ak Component 类别中可以找到这些函数。

# Get Attenuation Radius

返回此 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的有效衰减半径 (ScalingFactor \* MaxAttenuation)。

# Post Ak Event

发送 Wwise 中指定的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。

# Post Ak Event Async

发送 Wwise 中指定的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。异步版本会等到加载媒体之后再发送 Event。

# Post Ak Event and Wait for End

该 Blueprint 隐藏节点会发送 Wwise 中指定的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) ，并在 Event 结束后继续执行流程图的后续节点。

# Post Ak Event and Wait for End Async

该 Blueprint 隐藏节点会发送 Wwise 中指定的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) ，并在 Event 结束后继续执行流程图的后续节点。异步版本会等到加载媒体之后再发送 Event。

# Post Associated Ak Event

发送 Wwise 中此 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的内部 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。

# Post Associated Ak Event Async

发送 Wwise 中此 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的内部 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。异步版本会等到加载媒体之后再发送 Event。

# Post Associated Ak Event and Wait for End

该 Blueprint 隐藏节点会发送 Wwise 中此 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的内部 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) ，并在 Event 结束后继续执行流程图的后续节点。

# Post Associated Ak Event and Wait for End Async

该 Blueprint 隐藏节点会发送 Wwise 中此 [AkComponent](pg_features_objects_components.html#features_akcomponent) 的内部 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) ，并在 Event 结束后继续执行流程图的后续节点。异步版本会等到加载媒体之后再发送 Event。

# Post Trigger

针对关联 [AkComponent](pg_features_objects_components.html#features_akcomponent) 发送 Trigger。

# Set Listeners

针对 [AkComponent](pg_features_objects_components.html#features_akcomponent) 设置听者。

# Get Collision Channel

Gets the collision channel used when doing line of sight traces for obstruction/occlusion calculations.

# Set Output Bus Volume

设置给定游戏对象的直达声输出总线音量。Bus Volume 的取值范围为 0.0f ~ 1.0f。

# Get RTPC Value

针对关联 [AkComponent](pg_features_objects_components.html#features_akcomponent) 获取 Game Parameter 值。

# Set RTPC Value

针对关联 [AkComponent](pg_features_objects_components.html#features_akcomponent) 设置 Game Parameter 值。

# Set Stop when Owner Destroyed

针对相应 [AkComponent](pg_features_objects_components.html#features_akcomponent) 设置 StopWhenOwnerDestroyed 值。

# Set Switch

针对关联 [AkComponent](pg_features_objects_components.html#features_akcomponent) 将 Switch Group 设为给定 Switch。

# Stop

停止播放与 [AkComponent](pg_features_objects_components.html#features_akcomponent) 关联的 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 。

# Use Reverb Volumes

设置 [AkComponent](pg_features_objects_components.html#features_akcomponent) 是否受 [AkReverbVolume](pg_features_objects_actors.html#features_akreverbvolume) 影响。

# Set GameObject Radius

通过调用 [AK:SpatialAudio::SetGameObjectRadius()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a8c2e8f50769b6ae29dcbcb636e9c33f2.html) 来设置游戏对象的内外半径并将其发送到 Spatial Audio。