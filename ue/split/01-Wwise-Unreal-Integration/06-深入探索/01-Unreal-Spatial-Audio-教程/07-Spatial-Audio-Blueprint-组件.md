# Spatial Audio Blueprint 组件

|  |
| --- |
| Wwise Unreal Integration Documentation |

Spatial Audio Blueprint 组件

目前为止，所有东西都是通过使用预构建 Actor 或向各个 Actor 实例添加组件在关卡中直接构建的。其实，我们也可以使用各种 Spatial Audio 组件来构建 Blueprint Actor，然后在整个关卡中根据需要进行复制。在本节中，我们将使用 Blueprint 类来构建 [Unreal 工程准备工作](sa_setup.html#sa_setup_3) 章节所述结构的副本，以便在游戏世界中轻松添加或生成 Actor。

|  |  |
| --- | --- |
|  | **注記：** 在开始学习本教程前，请务必先完成 [Spatial Audio 教程准备工作](sa_setup.html) 。 |

# 设置 Blueprint 类

`AkLateReverbComponent` 和 `AkRoomComponent` 需要借助几何包含关系检测来确认给定游戏对象位置是否在父级 `PrimitiveComponent` 之内。该测试使用 Simple Collision。因此，您需要使用包含 Simple Collision 的父级 `PrimitiveComponent` 。比如，您可以使用 Box Collision、Sphere Collision 或 Capsule Collision 组件。若 `PrimitiveComponent` 不含任何 Simple Collision，则几何包含关系检测将直接使用组件边界。这样可能会不太精确。

It is also possible to add simple collision to a mesh asset in Unreal (see [Setting Up Collisions With Static Meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine)). However, for complex meshes, such as those with doorways and openings, it is sometimes necessary to 'use complex collision as simple' in the collision settings for the mesh (see [Simple versus Complex Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine)). 比如，若想允许角色通过门廊进入 Room，同时还要与墙壁发生碰撞，便可能需要使用此设置。在使用此设置时，`AkLateReverbComponent` 和 `AkRoomComponent` 的几何包含关系检测会失败。因为这时会忽略 Simple Collision，转而使用 Mesh 的整个 Trimesh。`AkLateReverbComponent` 和 `AkRoomComponent` 所用的 Simple Collision 检测并不支持 Trimesh。为此，在使用 `AkLateReverbComponent` 和 `AkRoomComponent` 时，建议在 Blueprint 类中配置为将 Simple Collision 组件用作父对象。比如，Simple Collision 组件可以是 Box、Sphere 或 Capsule。若为 Room 或建筑特意设有 Mesh，则可将 Simple Collision 组件作为子组件添加到 Mesh。

|  |  |
| --- | --- |
|  | **注記：**  - It is possible to combine complex collision with simple collision by using two versions of the mesh. 如需了解如何实现这一点，请参阅 [将 Simple Collision 和 Complex Collision 结合起来](sa_components.html#sa_components_6) 章节。 - We will use assets from the Unreal Demo Game available from the Wwise Launcher. 若要在工程中使用这些素材，请下载 Unreal Demo Game 并转到资源管理器，然后在 `$<YourWwiseProjectsFolder>/WwiseDemoGame/Content` 下找到想要的素材。然后，将所需素材复制粘贴到在处理工程的 Content 文件夹。 |

1. 在 Content Browser 中，右键单击并选择 **Blueprint Class**。
2. 选择将 **Actor** 作为基类，并将新类命名为 SpatialAudioBP。
3. 双击 **SpatialAudioBP** 来打开类，然后单击 Viewport 选项卡。
4. 确保选中根组件，然后依次单击 **Add Component** > **Static Mesh**。
5. 单击刚添加的 Static Mesh 组件，然后在 Details 面板中选择 Mesh。

   - 在本例中，选择 [Unreal 工程准备工作](sa_setup.html#sa_setup_3) 章节中所用的 SpatialAudioDemoMesh。
   - 若使用 SpatialAudioDemoMesh，则需在 Materials 分区中选择 **SpatialAudioDemoMeshMaterial**。

   ![](../../../../images/SABPTutorialMeshAndMaterial.png)

   设置 Static Mesh 组件的 Mesh 和 Material

   |  |  |
   | --- | --- |
   |  | **注記：** 只有 Convex Mesh 支持将 Room 自动指派给 Portal。Concave meshes (for example, L-shaped rooms) do not produce accurate portal room intersection. |
6. Add a Box Collision component for each of the individual rooms and doorways in the mesh. Name them BoxRoomLarge, BoxRoomSmall, BoxPortalInner, and BoxPortalOuter.

# 重新定位 Box Collision 组件

此时，所有 Box Collision 组件均被放在了同一位置（相互层叠）。下面我们来重新定位、缩放并旋转这些组件以使其与 Room 和门廊对齐。最简单的方法就是使用 Orthographic 视图（以下步骤是针对 SpatialAudioDemoMesh 的，不过其他 Mesh 所执行的步骤与之类似）。

|  |  |
| --- | --- |
|  | **注記：** 在本教程中将 Room 和 Portal 与 Mesh 对齐时，不必担心其是否完全对齐或居于正中。只需确保大致覆盖相应区域即可。在设计实际环境时，可使用 Details 面板的 Transform 分区来输入确切数值。 |

1. 在 Viewport 选项卡中，单击 **Perspective** 并将视图改为 **Top**。

   - 现在看到的是使用线框渲染的俯视图。

   ![](../../../../images/SABPTutorialOrthographicView.png)

   Orthographic Top View
2. 选中 **BoxRoomLarge** 并沿 Y 轴下移，直到 Mesh 内 Large Room 的中间。
3. 沿 X 和 Y 轴缩放 **BoxRoomLarge**，直到其大小与 Large Room 的尺寸一致（您可以通过按下 R 或在 Viewport 选项卡中选择 Scale 小组件来切换到缩放界面）。

   ![](../../../../images/SABPTutorialRoomLargeFromTop.png)

   Position and Scale Large Room on X and Y Axes
4. 选中 **BoxRoomSmall** 并沿 X 和 Y 轴缩放，直到其大小与 Small Room 的尺寸一致。

   ![](../../../../images/SABPTutorialBothRoomsFromTop.png)

   Position and Scale Rooms on X and Y Axes
5. 选中 **BoxPortalInner** 并沿线框放大，直至在 Mesh 上看到内侧门廊的边界。

   ![](../../../../images/SABPTutorialInnerDoorwayMesh.png)

   在 Wireframe Mesh 上定位门廊的边界
6. 将 **BoxPortalInner** 移到门廊的中间，然后沿 X 轴缩放，直到其覆盖门廊的边界。

   ![](../../../../images/SABPTutorialInnerPortalFromTop.png)

   Position and Scale Inner Portal Box to Cover the Doorway
7. 选中并旋转 **BoxPortalOuter**，以使其局部 Y 维度指向门廊外面。

   |  |  |
   | --- | --- |
   |  | **注記：** 这样做很有必要。因为 Portal 有 Front Room 和 Back Room，而其通过检测 Portal 的 Y 维度上的最近相交 Room 来自动指派。对于 BoxPortalOuter，局部坐标空间的后部将与 Mesh 中的 Small Room 连通，而前部不与任何 Room 连通。 |
8. 围绕 Z 轴将 **BoxPortalOuter** 旋转 90 度。为此，可转到 Details 面板的 Transform 分区，并在 Z 轴 **Rotation** 文本框中键入 90。

   ![](../../../../images/SABPTutorialOuterPortalRotate.png)

   旋转 Outer Portal Box 以使其局部 Y 轴指向房门外面
9. 往外侧门廊方向移动 **BoxPortalOuter**，并通过缩放来使其覆盖房门的边界。
10. 在 Top 视图下，确保所有 Room 和 Portal 与 Mesh 对齐（如下所示）。

    ![](../../../../images/SABPTutorialRoomsAndPortalsFromAbove.png)

    Rooms and Portals Correctly Aligned in Top View
11. 现在需要沿 Z 轴重新定位并缩放 Box Collision 组件。在 Viewport 选项卡中，单击 **Top** 并将视图改为 **Back**。
12. 选中 **BoxRoomLarge** 和 **BoxRoomSmall**，然后沿 Z 轴缩放以使其与 Room 的尺寸一致。

    ![](../../../../images/SABPTutorialRoomsZ.png)

    Scale Room Boxes on Z-Axis
13. 选中 **BoxPortalOuter** 和 **BoxPortalInner** 并将其向下移到门廊中央，然后沿 Z 轴进行缩放以使其与房门的尺寸一致。

    ![](../../../../images/SABPTutorialPortalsZ.png)

    Position and Scale Portal Boxes on Z-Axis

# 设置 Room 和 Portal

下面我们来将 AkRoom 组件添加到 Room，并将 AkPortal 组件添加到 Portal。

1. 逐一选择各个 Box Collision 组件，然后选择 **Add Component**。
2. 针对每个 Box Collision 组件创建 Room 或 Portal 组件（视情况而定），并为其设置与父对象相似的名称。结果应如下图所示：

   ![](../../../../images/SABPTutorialRoomsAndPortalsHierarchy.png)

   Add AkRoom Components to the Room Boxes and AkPortal Components to the Portal Boxes

   |  |  |
   | --- | --- |
   |  | **注記：** 确保将组件添加到正确的父对象。比如，在将 AkRoomLarge 添加到 Large Room 时，确保在单击 **Add Component** 前选中 **BoxRoomLarge**。  AkRoomComponent 和 AkPortalComponent 为通用组件，可添加到任何 Primitive 组件。有关详细信息，请参阅 [AkRoomComponent](pg_features_spatialaudio.html#features_objects_akroomcomponent) 和 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 章节。 |
3. To confirm that the portals have valid placement, select the **Visualize Rooms and Portals** option in the Wwise User Settings.

   ![](../../../../images/SABPTutorialVisualizeRoomsAndPortals.png)

   Visualize Rooms and Portals option in the Wwise User Settings
4. 现在在连通的 Room 和 Portal 之间绘制了框线。若 Portal 的放置无效，则将其显示为红色。

   ![](../../../../images/SABPTutorialPortalPlacement.png)

   Portal Room Connections Visualized in the Viewport

   |  |  |
   | --- | --- |
   |  | **注記：** 若 Portal 不与任何 Room 连通或同一 Room 与两端连通，则将 Portal 的放置视为无效。有关详细信息，请参阅 [AkPortalComponent](pg_features_spatialaudio.html#features_objects_akportalcomponent) 章节。 |
5. Clear **Visualize Rooms and Portals** in the Wwise User Settings.

# 添加 Geometry 和 Late Reverb

最后还要将 AkGeometry 和 AkLateReverb 组件添加到 Blueprint 类。

1. 将 AkGeometry 组件添加到 Static Mesh 组件。
2. Select the AkGeometry component and in the Details panel, under Geometry, set the Mesh Type to **Static Mesh**.
3. 将 AkLateReverb 组件添加到 "BoxRoomLarge" Box Collision 组件。

   ![](../../../../images/SABPTutorialCompleteHierarchy.png)

   AkGeometry and AkLateReverb Added to the Blueprint Class
4. Select the **AkLateReverb** component.
5. In the Details panel, set the Aux Bus to **LargeRoom**.

# 验证所作设置

Blueprint 类现在可供使用了。我们可以将类的实例拖到游戏世界中。

1. 将 **SpatialAudioBP** 的实例从 Content Browser 拖到 Spatial Audio Demo 地图中。
2. 将其放在现有建筑旁边。

   ![](../../../../images/SABPTutorialInstanceInWorld.png)

   An instance of the Blueprint Class Added to the World
3. 远程连接到 Wwise，并进入 Play In Editor 模式。
4. 单击鼠标来播放 Outside 声音。
5. 在 Wwise 的 Game Object Profiler 布局中，确认已正确注册新 Blueprint 类的几何构造，并可从该几何构造正常反射射线。
6. 确认在新的 Blueprint 结构中射线正确穿过 Portal。

   ![](../../../../images/SABPTutorialRays.png)

   Spatial Audio Paths Correctly Interacting with the New Blueprint Class Instance
7. 若要测试 Late Reverb 组件，则须添加声音并将其定位在 SpatialAudioBP 实例中的 Large Room 内。右键单击并复制游戏世界中的现有 **Play\_Outside** AkAmbientSound Actor。
8. 将复制项重命名为 Play\_LargeRoom\_BP（您也可以在 World Outliner 中将 **Play\_LargeRoom\_BP** 拖到 **Button\_Outside** 之上，来将 Play\_LargeRoom\_BP 与 Button\_Outside 解绑）。
9. Move **Play\_LargeRoom\_BP** inside the large room of the SpatialAudioBP instance.
10. Open the Level Blueprint and add logic to play the Play\_LargeRoom\_BP sound when the B key is pressed (see [Unreal 工程准备工作](sa_setup.html#sa_setup_3)).

    ![](../../../../images/SABPTutorialPlaySoundLogic.png)

    Logic in the Level Blueprint to Play the New Sound Using the B Key
11. 编译并保存 Level Blueprint。
12. Play the level in the editor.
13. Press **B** to play the new sound.
14. 走进 SpatialAudioBP 建筑中的 Large Room。You can hear the reverb applied to the sound.

# 将 Simple Collision 和 Complex Collision 结合起来

本节将展示如何将 Simple Collision 和 Complex Collision 结合用于相同的 Mesh，以便使用 Simple Collision 执行 Spatial Audio 几何包含关系检测，并使用 Complex Collision 执行 Unreal 查询。

|  |  |
| --- | --- |
|  | **注記：** 本节基于 WwiseDemoGame 工程中的 SpatialAudioTutorialMap 和 ComplexRoomDemo 目录下的素材。您可以通过 Audiokinetic Launcher 下载安装该工程。然后，使用预制 Mesh 素材和自定义 Blueprint 类将 Simple Collision 和 Complex Collision 结合起来。 |

For complex meshes, such as those with doorways and openings, it is sometimes necessary to 'use complex collision as simple' in the collision settings for the mesh (refer to [Simple versus Complex Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine)). 比如，若想允许角色通过门廊进入 Room，同时还要与墙壁发生碰撞，便可能需要使用此设置。When this setting is used, the containment tests for `AkLateReverbComponent` and `AkRoomComponent` fail because the simple collision is ignored and the mesh's full trimesh is used. `AkLateReverbComponent` 和 `AkRoomComponent` 所用的 Simple Collision 检测并不支持 Trimesh。

One solution to this problem is to create two duplicates of the same mesh asset, using simple collision for one, and complex collision for the other. In the SpatialAudioTutorialMap, there is a complex room structure that demonstrates this technique.

To begin, test the complex room structure by playing in editor and walking around the building:

1. Open the SpatialAudioTutorialMap in Unreal.
2. Click **Play in Editor**.
3. Press **C** to trigger the sound in the non-box-shaped building.

   ![](../../../../images/SACR_BP_InLevel.png)

   SpatialAudioTutorialMap 中的 Non-Box-Shaped Room

   Walk around the exterior of the building. The sound is occluded.

The rest of this tutorial demonstrates how the building structure is configured to handle simple collision for Wwise Spatial Audio containment tests, as well as complex collision for Unreal physics containment tests.

1. In the context browser, browse to WwiseAssets/SpatialAudioDemo/ComplexRoomDemo.

   ![](../../../../images/SACR_ComplexRoomDemoAssets.png)

   SpatialAudioTutorialMap 中的 ComplexRoomDemo 素材

   This folder contains two Static Mesh assets: Building\_Complex and Building\_Simple.
2. Open each of these assets and scroll to the collision settings in the Details Panel.

   Notice that they have different values for their respective Collision Complexity properties.

![](../../../../images/SACR_BuildingComplex_Collision.png)

Building\_Complex

Mesh 素材

![](../../../../images/SACR_BuildingSimple_Collision.png)

Building\_Simple

Mesh 素材

Building\_Complex 将 Collision Complexity 设为了 Use Complex Collision As Simple，表示 Unreal 不会为此 Mesh 生成简化几何构造，而是使用整个 Trimesh。这样角色才能穿过门廊开口。 Building\_Simple 将 Collision Complexity 设为了 Use Simple Collision As Complex，表示 Unreal 会生成简化几何构造并忽略 Trimesh。这样 Spatial Audio 才能执行几何包含关系检测来确认 Room 的几何包含关系。

|  |  |
| --- | --- |
|  | **注記：** 当然，也可将 Collision Complexity 设为 Simple And Complex。不过，这样的话 Unreal 会使用简化几何构造来执行碰撞查询。在这种情况下，角色无法穿过门廊开口。相反，可以使用两个完全相同的 Mesh。一个具有复杂几何构造，一个具有简单几何构造。 |

接下来，在自定义 Blueprint 类内将两个 Mesh 结合起来。

- 打开 "BuildingBP" Blueprint。

此 Blueprint 使用了两个相互层叠的 Static Mesh 组件。

![](../../../../images/SACR_BP_Components.png)

BuildingBP

Blueprint 中的两个 Static Mesh 组件

![](../../../../images/SACR_BP_ComplexMesh-Mesh.png)

对于 StaticMesh\_Complex 组件，使用了 "Building\_Complex" Mesh

![](../../../../images/SACR_BP_SimpleMesh-Mesh.png)

对于 StaticMesh\_Simple 组件，使用了 "Building\_Simple" Mesh

![](../../../../images/SACR_BP_SimpleMesh-Rendering.png)

StaticMesh\_Simple 的 Rendering 设置

对于 StaticMesh\_Simple 组件，在 Rendering 分区中禁用了 Visible 并启用了 Hidden in Game。这是因为此 Mesh 仅用于简化几何构造，以便可以针对 Spatial Audio 执行几何包含关系检测。

![](../../../../images/SACR_BP_SimpleMesh-Trigger.png)

StaticMesh\_Simple 的 Collision Presets 设置

另外，对于 StaticMesh\_Simple 组件，将 Collision Presets 属性设为了 Trigger。该简化几何构造会在门廊开口位置形成一道障碍。通过使用 "Trigger" Collision Presets，可确保角色和其他游戏对象可自由穿过简化几何构造。

StaticMesh\_Simple 组件绑定有 AkRoom 组件和 AkLateReverb 组件。这样的话，会将 "Building\_Simple" Mesh 的 Simple Collision 用于对 Room 实施几何包含关系检测。

为了允许声音在 BuildingBP 的 Mesh 上反射和衍射，需要将 AkGeometry 组件添加到其中一个 Static Mesh 组件。In this solution, because we are also using [Reverb Parameter Estimation](sa_reverbestimation.html), it is best to add it to the StaticMesh\_Simple component. AkLateReverb 组件使用同级 AkGeometry 组件的 Acoustic Texture 计算 HF Damping。通过将 AkGeometry 组件设为 Static Mesh，可将整个复杂几何构造而非其 Simple Collision Mesh 发送到 Spatial Audio。

最后，使用绑定有 AkPortal 组件的 Box Collision 组件来将声学 Portal 添加到门廊。

![](../../../../images/SACR_BP_Portal.png)

BuildingBP

Blueprint 中的 Portal

另外，为了能够看到建筑的内部，还添加了 Point Light。

|  |  |
| --- | --- |
|  | **注記：**  - When sending geometry to Wwise, there is a limitation that each edge can have no more than two triangles connected. Remember this when designing meshes to use with Spatial Audio. - When using the Game Object Profiler in Wwise, Room Extents will always be visualized as green cuboids, regardless of the geometry assigned to the room. - Adding simple collision to meshes in Unreal will only work correctly when the mesh is convex. 对于更为复杂的 Mesh 结构，最好使用 Simple Collision 几何构造来模拟 Mesh。您可以在 Static Mesh 编辑器的 Collision 菜单中将 Simple Collision Primitive 添加到 Mesh。 将 Collision Primitive 添加到 Mesh 素材 Refer to [Setting Up Collisions With Static Meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine) for further information. |