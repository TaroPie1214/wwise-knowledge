# Spatial Audio

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Spatial Audio

![](../../../images/spatialAudio_flowChart.png)

# 简介

Spatial Audio 模块提供了一些与空间音频相关的服务，尤其便于执行以下操作：

- 基于给定几何构造计算 Reflect 的镜像声源
- 通过控制 3D 总线对 Room 和 Portal 的声音传播进行建模
- 对声音在几何构造上的传播进行建模
- 访问 [Reflect](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_reflect_plug_in_effect) 的原始 API

在内部，Spatial Audio 会执行以下操作：

- 通过管理游戏对象及其属性（位置、辅助发送、声障和声笼）来控制 3D 总线
- 控制 Spatial Audio 游戏对象的单点/多点定位和辅助发送
- 运行几何声音反射、衍射和透射算法
- 为 [Reflect](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_reflect_plug_in_effect) 打包数据

它是一个与 Wwise 声音引擎协同使用的 SDK 组件（如以下流程图所示）。

![SpatialAudioFlow](../../../images/spatialAudio_flowChart.png)

# Spatial Audio 服务

Spatial Audio 暴露了 3 类服务，具体可参见以下对应章节：

- [使用房间和门户](using_rooms_and_portals.html)
- [Geometry](spatial_audio_apigeometry.html)
- [使用原始镜像声源](spatial_audio_using_raw_image_sources.html)

[使用房间和门户](using_rooms_and_portals.html) 利用简单的上层几何抽象概念对其他房间内发声体的声音传播进行建模。[Geometry](spatial_audio_apigeometry.html) 使用三角形来计算镜像声源以结合 Reflect 模拟动态早期反射，或者计算几何衍射。另外，Spatial Audio 还提供有一些辅助函数，方便直接访问 Reflect 的原始 API（参见 [使用原始镜像声源](spatial_audio_using_raw_image_sources.html) 章节）。

# API 设置

Spatial Audio 功能和定义可以在 *SDK/include/AK/SpatialAudio/Common/* 中找到。 其主要函数暴露在 `AK::SpatialAudio` 命名空间中。

## 初始化

通过 `AK::SpatialAudio::Init()` 对 Spatial Audio 进行初始化。

在使用 Spatial Audio 时，必须明确指派一个游戏对象作为 Spatial Audio Listener。为此，需要调用 `AK::SpatialAudio::RegisterListener()` 并传入所需听者的 ID。另外，还要把该游戏对象注册到声音引擎中，并将其指派为听者。如需进一步了解声音引擎中的 Listener，请参阅 [集成 Listener](soundengine_listeners.html) 。

|  |  |
| --- | --- |
|  | **警告:** Spatial Audio 仅支持一个顶层听者。 |

## Spatial Audio Emitter

如果某个声音有若干设置与 Wwise 设计工具中启用的 Spatial Audio 相关，那么游戏对象在播放该声音时就会成为 Spatial Audio Emitter：

- 若要启用房间混响，请在该声音的 General Settings 选项卡中启用游戏定义的辅助发送。
- 若要启用反射处理，请根据需要通过以下方式将早期反射总线指派给该声音：
  - 在该声音的 General Settings 选项卡中，指派相应的 Auxiliary Bus。
  - 使用 `AK::SpatialAudio::SetEarlyReflectionsAuxSend` 将总线指派给 Game Object。
- 若要启用衍射和透射处理，请在该声音的 Positioning 选项卡中选中 **Enable Diffraction and Transmission**。

您可以使用 `AK::SoundEngine::SetPosition` 将游戏对象（无论是发声体还是听者）的位置传给声音引擎。Spatial Audio 会直接从声音引擎检索位置信息，来确定声源位置以进行反射和衍射处理。

## 终止

Spatial Audio 会在 Wwise 声音引擎终止时自动终止。

参见
:   - [Spatial Audio 概念](spatial_audio_concepts.html)
    - [使用房间和门户](using_rooms_and_portals.html)
    - [Geometry](spatial_audio_apigeometry.html)
    - [第三人称视角和 Spatial Audio](spatial_audio_third_person.html)
    - [Parameter Smoothing [Experimental]](spatial_audio_parameter_smoothing.html)
    - [使用原始镜像声源](spatial_audio_using_raw_image_sources.html)
    - [Radial Emitters](spatial_audio_radial_emitters.html)
    - [Spatial Audio Experimental Features](spatial_audio_experimental.html)
    - Wwise Help 中的[在总线上应用定位](https://www.audiokinetic.com/library/?source=Help&id=applying_positioning_to_busses)一节
    - Wwise Help 中的[发声体-听者关联](https://www.audiokinetic.com/library/?source=Help&id=game_defined_sends)一节。
    - Wwise Help 中的 [Reflect](https://www.audiokinetic.com/library/?source=Help&id=wwise_reflect_plug_in_effect) 章节。