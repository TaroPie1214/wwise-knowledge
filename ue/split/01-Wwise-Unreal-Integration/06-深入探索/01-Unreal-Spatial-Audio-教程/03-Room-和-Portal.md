# Room 和 Portal

|  |
| --- |
| Wwise Unreal Integration Documentation |

Room 和 Portal

在现实声学环境中，封闭空间内的声音会穿透墙壁，还会通过房门和窗户等开口传到外面。Spatial Audio 可利用上层几何抽象概念（即 Room 和 Portal）来模拟这种效果。

|  |  |
| --- | --- |
|  | **注記：** 在开始学习本教程前，请务必先完成 [Spatial Audio 教程准备工作](sa_setup.html) 。 |

# Wwise 工程

1. 在 Wwise 工程中，为每个 Room 创建新的 Auxiliary Bus。
   1. 右键单击相应对象来添加子 Auxiliary Bus
   2. 依次转到 New Child > Presets，然后选择 **Room Auxiliary Bus**

      1. 在 Effects 选项卡中，可调节 RoomVerb 效果器。

      ![](../../../../images/SATutorialAuxiliaryBusPropertyEditorEffectsSmallRoom.png)
2. 保存工程并生成 SoundBank。

# Unreal 工程

1. In Unreal, drag and drop the new Auxiliary Busses from the Wwise Browser to the Content Browser.
2. 针对建筑的每个 Room 拖放两个 [AkSpatialAudioVolume](pg_features_spatialaudio.html#features_objects_akspatialaudiovolume) 对象（如尚未在另一教程中执行该操作）。我们使用 **Fit To Geometry** 来放置两个 Room。
   1. 在各个 `AkSpatialAudioVolume` 所对应的 Details 面板中启用 **Fit To Geometry**。
   2. 若对最初获得的形状不满意，可使用 Transform 小组件将 `AkSpatialAudioVolume` 变换到新的位置。注意，在变换 AkSpatialAudioVolume 时，会显示黄色预览框线。在获得满意的形状后，松开鼠标按钮。这时 AkSpatialAudioVolume 会对齐到所需位置。
   3. 有关如何使用 **Fit To Geometry** 放置 `AkSpatialAudioVolumes` 的详细信息，请参阅 [Fit to Geometry](sa_fittogeometry.html) 章节。
      1. 确保针对两个 `AkSpatialAudioVolume` 对象启用 **Enable Room** 和 **Enable Late Reverb**。
         1. 若未学习 [Reflect](sa_reflect.html) 教程，请将 **Enable Surface Reflectors** 保持设为禁用状态。
         2. 在 Late Reverb 分区中取消选中 **Auto Assign Aux Bus**，并将新导入的 Auxiliary Bus 从 Content Browser 拖放到 Aux Bus 参数。

            |  |  |
            | --- | --- |
            |  | **注記：** 有关 **Auto Assign Aux Bus** 的信息，请参阅 [Reverb Parameter Estimation](sa_reverbestimation.html) 章节。 |
3. 添加两个 [AkAcousticPortal](pg_features_spatialaudio.html#features_objects_akacousticportal) 对象。

   1. 将其放在建筑物的开口附近。
      1. 为便于放置 AkAcousticPortal，请在 Details 面板中启用 **Fit To Geometry** 复选框。
      2. 在启用 **Fit To Geometry** 时，Integration 会利用周围的几何构造来查找合理的 Portal 放置位置。在使用 Transform 小组件将 `AkAcousticPortal` 拖到相应开口附近时，会显示黄色预览框线。在找到满意的放置位置后，松开鼠标按钮。这时 AkAcousticPortal 会对齐到所需位置。
      3. 有关如何使用 **Fit To Geometry** 放置 `AkAcousticPortals` 的详细信息，请参阅 [Fit to Geometry](sa_fittogeometry.html) 章节。
      4. 在将 `AkAcousticPortal` 放在各个门廊内之后，使用 Scale 小组件来调节各个 Portal 的深度，以获得想要的交叉淡变距离。在 `AkComponent` 穿过 Portal 时，Portal 越深（沿局部 X 轴），交叉淡变距离越长。这对混响发送和散布过渡来说都是适用的。
   2. Select the portals and set their **Initial State** to Enabled in the **Ak Portal Component** section. In the **Obstruction Occlusion** section, set the **Initial Occlusion** and **Obstruction Refresh Interval** to 0.0.

   ![](../../../../images/SATutorialAkPortalComponent.png)

|  |  |
| --- | --- |
|  | **注記：** An `AkAcousticPortal` must be oriented in a way that the rooms to which it connects are positioned on its local Y axis. 为了便于识别，在选中 Portal 时其周围会显示黄色条带。黄线用来分隔前后区域。If the rooms overlap, the room with the highest priority is chosen. When working with rooms and portals in the level editor, be sure to set the viewport to **Realtime** so that the portal visualisations are updated correctly as you move portals. |

# 验证所作设置

1. 启动场景并待在起点位置。在针对 Room 内的发声体播放 Event 时，应当能够听到相应的声音。
2. 连接 Wwise 设计工具并转到 Game Object Profiler 布局（快捷键 F12）。在 Game Object 3D Viewer 中，应会看到：

   1. 以灰色框线表示的 Portal 模型（如 AkSpatialAudioVolume 未启用 Surface Reflector）。
   2. 以绿色框线表示的 Portal 模型。
   3. 声音在 Portal 边缘衍射时的传播路径及关联衍射值（依据弯曲角度在各个边缘予以显示）。
   4. 声音穿透 Room 墙壁时的传播路径及关联透射损失值。

      |  |  |
      | --- | --- |
      |  | **注記：** 您可以通过更改 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 中 Room 的透射损失参数来设置此透射损失值。 |
   5. 声音衍射和透射路径的散布声锥（如设有散布曲线）。

   ![](../../../../images/SATutorialGameObject3DViewerRoomsAndPortal.png)

|  |  |
| --- | --- |
|  | **注記：** 这时 Diffraction 和 Transmission Loss 会使用声音的 Attenuation ShareSet 中的 Diffraction 和 Transmission 曲线对声音实施衰减。When these curves are set to **Use Project Diffraction/Transmission**, they use the curves in the Environmental Curves tab of the Project Settings in the Authoring application. |

# Portal 和 Reverb

通过 Portal 传播的声音可进行混响处理并输出到听者当前所在 Room。以下步骤阐述了如何予以配置。

1. 在 Wwise 工程中：
   1. 找到 Room Reverb 所用 Auxiliary Bus。我们希望将发出声音的 Room 的混响效果馈送到其他 Room 的混响效果中。

      1. 在 Auxiliary Bus Property Editor 的 General Settings 选项卡中，确保启用 Use game-defined auxiliary sends。

      ![](../../../../images/SATutorialAuxiliaryBusPropertyEditorGeneralSettingsRoom.png)
2. 生成 SoundBank，然后启动场景并连接到 Wwise 设计工具。
3. 在启用了辅助发送的 Room 中播放声音，然后转到相连的 Room。

   1. 您应会看到声音信号的湿声部分还会馈送听者所在 Room 的混响效果。

   ![](../../../../images/SATutorialAdvancedProfilerVoicesGraphPortalReverb.png)

# Room Tone

有时，Room 内会有像空调嗡嗡声这样的特定环境声。为了重现这种效果，您可以针对 Spatial Audio Room 游戏对象发送 Event。在听者和发声体处在同一 Room 时，声音会被定位在听者所在位置。在听者和发声体处在不同 Room 时，听者会通过连通的 Portal 和墙壁听到房间底噪 (Room Tone)。

1. 在 Wwise 工程中：
   1. 创建新的 Sound SFX 并用于房间底噪。
      1. 若要将声音发送到混响效果器，则在 General Settings 选项卡中启用 **Use game-defined aux sends**。
      2. 在 Positioning 选项卡中：
         1. 为距离衰减、衍射和透射曲线添加衰减。
         2. 启用 **Diffraction and Transmission**。
   2. 右键单击 Sound SFX，然后依次选择 **New Event** > **Play**，来创建带有房间底噪的 Play Event。
   3. 保存工程并生成 SoundBank。
2. 在 Unreal 中：
   1. Drag the Event created in the previous section from the Wwise Browser to the Content Browser.
   2. 在其中一个 Room 对应的 Ak Event 分区下，将此 Event 添加到 Ak Audio Event 参数。

      1. 调节 Aux Send Level 来将部分声音馈送到该 Room 的混响效果中。
      2. 您可以通过选中 Auto Post 方框来在 BeginPlay 时发送房间底噪 Event，也可调用常用的 Blueprint 函数来针对游戏对象发送 Event。

      ![](../../../../images/SATutorialLargeRoomAkAudioEvent.png)
   3. 在 Spatial Audio Tutorial Map 中，我们在 Level Blueprint 中使用了 Blueprint 函数来激活和停用房间底噪。

      1. 在 World Outliner 中选中带有房间底噪的 AkSpatialAudioVolume 时，右键单击 Level Blueprint 来创建引用对象。
      2. 从引用对象拖动连线，并搜索 Post Associated Ak Event。
      3. 按照相同方式搜索 Stop 函数。
      4. 添加按键作为输入节点。

      ![](../../../../images/SATutorialLevelBlueprintRoomTone.png)
3. 启动场景并连接到 Wwise 设计工具。
4. 转到带有房间底噪的 Room，并按下按键来触发房间底噪。确认可以听到声音。

   1. 在 Advanced Profiler 视图中，应会看到当前触发的 Event。

   ![](../../../../images/SATutorialRoomToneAdvancedProfiler.png)

   在播放房间底噪时查看 Advanced Profiler 视图

   1. 在 3D Game Object Viewer 中，可一边来回移动听者，一边察看 Room 游戏对象。

      1. 若听者和发声体处在同一 Room，则 Room 会在听者所在位置播放声音。您会看到 Room 游戏对象跟随“听者”游戏对象。
      2. 若听者和发声体处在不同 Room，则：
         1. 将 Room 游戏对象定位在 Portal 位置（来指示衍射声音的位置），并在其与“听者”游戏对象之间绘制路径。
         2. 将 Room 游戏对象定位在直达路径上的 Room 边界来指示透射声音的位置。
         3. 针对所有这些位置绘制散布声锥。

      ![](../../../../images/SATutorialRoomToneGameObject3DViewer.png)

参见
:   - [Spatial Audio Room 和 Portal 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=using_rooms_and_portals.html)