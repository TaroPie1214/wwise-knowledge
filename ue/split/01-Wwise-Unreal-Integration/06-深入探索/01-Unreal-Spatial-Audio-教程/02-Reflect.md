# Reflect

|  |
| --- |
| Wwise Unreal Integration Documentation |

Reflect

This tutorial demonstrates how to use Spatial Audio geometry to send reflective surfaces to the Reflect plug-in, which simulates the early reflection implied by the propagation of sound in an acoustic environment.

**To prepare for this tutorial:**

1. Obtain a license for the Reflect plug-in. See [Reflect Plug-in](https://www.audiokinetic.com/wwise/plugins/reflect/) for licensing options.
2. Complete the steps in [Spatial Audio 教程准备工作](sa_setup.html).

# Wwise 工程

1. 为了访问出厂 Acoustic Texture 以及早期反射 Auxiliary Bus 预设，您需要导入 Factory Acoustic Texture 和 Reflect Factory Asset。
   1. 依次转到 Project > Import Factory Assets...。
   2. 选中 Reflect 和 Acoustic Texture 并按下 Import。
2. 使用出厂预设创建早期反射 Auxiliary Bus：
   1. In the Busses hierarchy, right-click on the Main Audio Bus
   2. 依次转到 New Child > Presets，并选择 **Simplified Early Reflection Auxiliary Bus**

      1. 在 Effects 选项卡中双击效果器，然后将 Speed of Sound 设为 34,500

      ![](../../../../images/SATutorialEffectEditorReflect.png)
3. 选中 [Wwise 工程准备工作](sa_setup.html#sa_setup_2) 中创建的声音，并转到 Sound SFX Sound Property Editor。

   1. 在 General Settings 选项卡中，在 Early Reflections 下添加刚才创建并应用了 Reflect 效果器的 Auxiliary Bus。

   ![](../../../../images/SATutorialSoundPropertyEditorGeneralSettingsEarlyReflections.png)
4. 保存工程并生成 SoundBank。

# Unreal 工程

在工程中，我们想让建筑物、地面和障碍物反射声音。实现方式有两种：[AkSpatialAudioVolume](pg_features_spatialaudio.html#features_objects_akspatialaudiovolume) 和 [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) 。

`AkGeometryComponent` 可添加到 Static Mesh Actor。它会将 Static Mesh Geometry 自动发送到 Spatial Audio。另外，还可配置为发送 Simple Collision Mesh。对于足够复杂且绑定有 `AkGeometryComponent` 的 Static Mesh，有时会生成过于复杂的几何构造。这样的话计算时间可能会很长，而且基于射线的声学模拟技术（比如 Wwise Spatial Audio 中所用的技术）通常会假设几何元素（表面和边缘）远远大于声源的波长。比方说，空气中 1000 Hz 的声音具有 34 cm 的波长。在这种情况下，与其直接使用 Static Mesh，不如使用 `AkSpatialAudioVolume` 来在 Mesh 周围（在其作为障碍物反射和阻挡声音时）或在 Mesh 之内（在其作为内墙时）创建简单形状。

1. 在教程地图中，障碍物是一个 Basic Static Mesh。我们可以轻松向其添加 `AkGeometryComponent`。

   1. Click on the actor and click on **Add+**. 选择 Ak Geometry。
   2. In the Geometry section, set the Mesh Type to Simple Collision.

   ![](../../../../images/SATutorialAkGeometryComponentSimpleCollision.png)
2. 针对地面重复同样的步骤。
3. 在 SpatialAudioTutorialMap 中，建筑物由自定义 Mesh 构成。虽然形状比较简单可以使用 AkGeometryComponent，不过在本教程中我们还是选择使用 `AkSpatialAudioVolume`。
   1. 将三个 `AkSpatialAudioVolumes` 拖放到场景中。
      1. 在建筑物附近设置其中一个来用于外墙。因为此 Volume 被放在了 Mesh 的外围，所以必须手动实施变换。
      2. 在每个 Room 之内各设一个来用于内墙。我们使用 **Fit To Geometry** 来放置两个 Room。
         1. 在各个 AkSpatialAudioVolume 所对应的 Details 面板中启用 **Fit To Geometry**。
         2. 若对最初获得的形状不满意，可使用 Transform 小组件将 AkSpatialAudioVolume 变换到新的位置。注意，在变换 `AkSpatialAudioVolume` 时，会显示黄色预览框线。在获得满意的形状后，松开鼠标按钮。这时 AkSpatialAudioVolume 会对齐到所需位置。
         3. 有关如何使用 **Fit To Geometry** 放置 AkSpatialAudioVolumes 的详细信息，请参阅 [Fit to Geometry](sa_fittogeometry.html) 章节。
      3. 确保三个 `AkSpatialAudioVolumes` 全部启用 **Enable Surface Reflectors**。

         - Leave **Enable Room** and **Enable Late Reverb** cleared. They are discussed in [Room 和 Portal](sa_roomsandportals.html).

         ![](../../../../images/SATutorialAkSpatialAudioVolumeExterior.png)

# 验证所作设置

1. 启动场景并连接到 Wwise 设计工具。
   1. 在 Advanced Profiler 的 Voices Graph 视图中，应会看到应用了 Reflect 效果器的新辅助发送。
      1. 在玩家的初始位置，播放置于外部的声音。

         ![](../../../../images/SATutorialAdvancedProfilerVoicesGraphReflect.png)

         |  |  |
         | --- | --- |
         |  | **注記：** 若在播放 Room 内的声音时玩家处在房外，则不会看到任何 Reflect 发送。另外，声音会基于透射应用衰减。这是因为我们在建筑物和每个 Room 附近创建的 AkSpatialAudioVolume 是封闭的。您可以通过修改 Brush 对象或使用 Spatial Audio Portal（参见 [Room 和 Portal](sa_roomsandportals.html) 章节）来为其创建开口。 |
      2. 在继续执行下一步之前，打开 Profiler Settings 视图并确保启用 **Spatial Audio**。
   2. 转到 Game Object Profiler 布局（快捷键 F12）。

      1. 在 Game Object 3D Viewer 中，应会看到不同的反射表面。
      2. 在播放声音时，将绘制早期反射射线以显示声音的传入路径。

         ![](../../../../images/SATutorialGameObject3DViewerReflect.png)
      3. 若无法看到射线，请确保在 Game Object 3D Viewer Settings 中启用 **Show Reflection Paths**。

      ![](../../../../images/SATutorialGameObject3DViewerSettings.png)

|  |  |
| --- | --- |
|  | **注記：** 若无法在 Game Object 3D Viewer 中看到任何几何构造，则可能需要调大 Monitor Queue Pool Size。该设置位于 [Platform Initialization Settings](using_initialsetup.html#initialsetup_inifiles) 中。 |

参见
:   - [Reflect 文档](https://www.audiokinetic.com/library/edge/?source=Help&id=wwise_reflect_plug_in_effect)
    - [使用 Geometry API 模拟早期反射](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry_er.html)