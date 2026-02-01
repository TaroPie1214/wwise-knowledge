# Occlusion

|  |
| --- |
| Wwise Unreal Integration Documentation |

Occlusion

`AkOcclusionObstructionService::SetOcclusionObstruction()` 中暴露了基本的声障设置。You can use this service with or without Spatial Audio Rooms. This section describes how the service works without Spatial Audio, and the following [Occlusion and Spatial Audio](using_features_occlusion.html#using_features_occlusion_spatialaudio) section describes how it works with Spatial Audio.

您可以使用 Blueprint Editor 中的 **Set Occlusion Refresh Interval** 函数来针对 Actor 启用声障。另外，还可调节 UAkComponent 的设置。若将刷新间隔设为 0，将禁用声障。

To determine whether a listener is occluded from a source, a simple line of sight check is sufficient. Use the line trace channel set in the AkComponent's properties (`CollisionChannel`). If the line of sight is blocked, the occlusion level calculation starts. This calculation maps the hit point on the obstacle to its bounding box and creates twelve points around the obstacle. Do additional line of sight checks to see if these secondary paths are also blocked. The occlusion sent to the SoundEngine is modulated by the number of secondary paths that are blocked.

A temporal fade method is also available for smooth transitions between occlusion levels. To change the fade speed, change the `OCCLUSION_FADE_RATE` constant.

# Occlusion and Spatial Audio

When using Spatial Audio Rooms, obstruction is set instead of occlusion. In parallel, sources perform simple line of sight checks with [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) in the same Room. These portals need to have a non-zero **Obstruction Refresh Interval** property. The portals also perform simple line-of-sight checks with other portals with a non-zero **Obstruction Refresh Interval** property.

参见
:   - [Get Collision Channel](features_blueprintcomponent.html#features_blueprintcomponent_setocclusion)
    - [AkComponent](pg_features_objects_components.html#features_akcomponent)
    - [Obstruction and Occlusion with Game-defined Auxiliary Sends](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_obsocc.html)