# Fit to Geometry

|  |
| --- |
| Wwise Unreal Integration Documentation |

Fit to Geometry

To facilitate quick and accurate placement of AkAcousticPortal and AkSpatialAudioVolume actors, the Wwise Unreal integration is able to detect surrounding static mesh geometry in a scene and determine the appropriate size and location of the portals and volumes within the scene. 用户可将 Fit to Geometry 用于各种常见的房间、窗户和地板形状。This section gives an overview of how to use Fit To Geometry for AkAcousticPortal and AkSpatialAudioVolume actors.

|  |  |
| --- | --- |
|  | **注記：**  - The [Spatial Audio 教程准备工作](sa_setup.html) must be completed prior to starting this tutorial. - For Fit To Geometry to function correctly, **Realtime** must be enabled in the viewport options. |

# Fit To Geometry 前提要求

The Fit To Geometry feature uses the Unreal Engine to perform ray traces, and the rays must be able to be blocked by the surrounding static mesh geometry. By default, the Fit to Geometry collision channels of AkAcousticPortals and AkSpatialAudioVolumes are set to the Integration Default value. Before using the Fit to Geometry feature:

- Select the desired default Fit to Geometry collision channel inside the [Integration Settings](using_initialsetup.html#initialsetup_gamesettings).
- Set the collision preset of the static mesh surrounding future AkAcousticPortals and AkSpatialAudioVolumes to Block the Fit to Geometry collision channel.
- If desired, individual AkAcousticPortal and AkSpatialAudioVolume actors can override the default collision channel and choose a different one. This setting is found in the Details panel for both AkAcousticPortal and AkSpatialAudioVolume actors.
- If automatic Surface Property assignment is desired on AkSpatialAudioVolumes, set up the Geometry Surface Properties Table in the [Integration Settings](using_initialsetup.html#initialsetup_gamesettings). 有关详细信息，请参阅 [Automatically Assigning Surface Properties to AkSpatialAudioVolumes](sa_fittogeometry.html#sa_fittogeometry_3) 章节。

|  |  |
| --- | --- |
|  | **注記：** Fit To Geometry 功能仅可用于 Level Editor 视口内的 "AkAcousticPortal" 和 "AkSpatialAudioVolume" Actor。其既不可用在 Blueprint Editor 视口内，也不可用在构成上述 Actor 的各个组件（AkPortalComponent、AkSurfaceReflectorSet、AkRoomComponent 和 AkLateReverb）上。 |

# 使用 Fit To Geometry 放置 AkSpatialAudioVolume

- 最初会在 AkSpatialAudioVolume 所对应的 Details 面板中启用相应选项后执行 Fit To Geometry 操作。随后，每次使用 Transform 小组件将 Volume 变换到新的位置都会执行 Fit To Geometry 操作。
- 在拖动 Transform 小组件时，会显示黄色预览框线以指示 AkSpatialAudioVolume 与游戏世界中特定位置的贴合状况。您可以拖动 Volume 直至达到想要的贴合效果，然后松开鼠标来更新 AkSpatialAudioVolume 的 Brush Volume。注意，在执行 Fit To Geometry 操作后，"AkSpatialAudioVolume" Actor 的变换保持不变，而只修改子级 Brush 组件。
- Fit To Geometry 操作通过追踪从 Actor 的原点以球状形式向外散发的若干条射线来探测墙壁。这些射线的碰撞点会显示为绿色（忽略碰撞时显示为红色）。It can be useful to take note of where the rays hit to make sense of the resulting shape, to make sure that the correct collision channel is being used, and lastly, to make sure the correct properties are assigned to the resulting surfaces.
- 支持的形状共有三种；可在 AkSpatialAudioVolume 的 Details 面板中选择形状类型。
  1. **Oriented Box** – 朝向任意的箱形 Room。系统会在 Fit To Geometry 操作过程中自动确定箱体的朝向。同时，通过查找能将所有绿色碰撞点涵盖在内的最小箱体（按容量计）来计算形状。
  2. **Aligned Box** – 朝向固定的箱形 Room。箱体的朝向由用户指定。您可以使用 Transform 小组件旋转 "AkSpatialAudioVolume" Actor 来更改其朝向。Aligned Box 适合用于调节 Volume 以使其与可能包含多个障碍物的箱形区域相称（若使用 Oriented Box 形状，则无法精确对齐），或者调节箱体以使其与墙壁之间或窄道之内的室外区域相称。
     - 在有些情况下（比如所有碰撞点位于同一平面），一组给定的追踪射线会生成体积为零的 AkSpatialAudioVolume。这时将把箱体的框线显示为红色，并且不会更新形状。同时，在屏幕左下方显示错误消息。若要解决此问题，请将 AkSpatialAudioVolume 移到新的位置并重试。
  3. **Convex Polyhedron** – 完全封闭的凸多面体形 Room。这种形状最为复杂，放置时容易产生偏差。不过，在调节 Volume 以使其与不含平行墙壁的 Room 或非箱形 Room 相称时会比较省力。注意，Room 必须为凸形且完全封闭。也就是说，其不能包含带有开口的墙壁、天花板等等。
     - 在有些情况下，无法从来自特定位置的追踪射线找到封闭的凸形形状。这时会将形状的框线显示为红色，并且不会更新形状。同时，在屏幕左下方显示错误消息。若要解决此问题，请将 AkSpatialAudioVolume 移到新的位置并重试。
- 可使用 AkSpatialAudioVolume 所对应 Details 面板中的滑杆来过滤射线投射碰撞点。
  - 这些射线在内部按长度排序。由滑杆决定当中最短碰撞射线所占的百分比。
    - 比如，若将滑杆设为 0.75，则使用 75% 的最短射线来应用放置操作，而忽略 25% 的最长射线。
  - 留下的碰撞射线显示为绿色，滤掉的碰撞射线显示为红色。
  - 在有部分射线通过窗户或房门逸出而使得其碰撞点产生错误结果时，可通过过滤碰撞点很好地加以解决。
  - 在使用 Aligned Box 形状时，碰撞点过滤功能最为有用。因为在减少碰撞射线时不会导致朝向定位错误（Aligned Box 的朝向是固定的），而且任何形状都可应用射线过滤。

# Automatically Assigning Surface Properties to AkSpatialAudioVolumes

- Surface Properties (that is Acoustic textures and Transmission Loss values) are automatically assigned to the surfaces of the AkSpatialAudioVolume based on the collision results of the ray traces performed by Fit To Geometry, and the acoustic material mapping defined in the Geometry Surface Properties Table chosen in the [Integration Settings](using_initialsetup.html#initialsetup_gamesettings).
  - Since the result of a ray trace in the Unreal Engine yields a physical material, the table maps each physical material to surface properties.
  - 一般会将一条以上的碰撞射线投射到所生成的 AkSpatialAudioVolume 表面上，而且每条碰撞射线都可能会返回一种不同的 Physical Material。The physical material with the most hits is chosen.
  - It is possible that some rays will hit undesirable surfaces that are not representative of the properties of the resulting AkSpatialAudioVolume surface. For example, a drywall surface may have a wooden trim in some areas, but using 'drywall' for the acoustic texture representation makes more sense than 'wood' for the wall as a whole. 在大部分情况下，都有足够的碰撞点可供指派给表面积较大的 Acoustic Texture。If not, try translating the AkSpatialAudioVolume slightly so that the hit points move slightly, or if desired results are still not achieved, the acoustic texture can be manually assigned in the Details panel for the AkSurfaceReflectorSet component.
- It is necessary to create the desired mapping between physical materials and surface properties in the Geometry Surface Properties Table before using Fit To Geometry on an AkSpatialAudioVolume. If you change the material mapping after fitting an AkSpatialAudioVolume, its properties are not updated.

# 使用 Fit To Geometry 放置 AkAcousticPortal

- 跟 AkSpatialAudioVolume 一样，最初会在 AkAcousticPortal 所对应的 Details 面板中启用相应选项后执行 Fit To Geometry 操作。随后，每次使用 Transform 小组件将该 Actor 变换到新的位置都会执行 Fit To Geometry 操作。
- 在拖动 Transform 小组件时，会显示黄色预览框线以指示 AkAcousticPortal 与游戏世界中特定位置的贴合状况。您可以拖动 Actor 直至达到想要的贴合效果，然后松开鼠标来更新 AkAcousticPortal。
- Fit To Geometry 操作通过追踪从 Actor 的原点以球状形式向外散发的若干条射线来探测窗户和门廊。在找到潜在的窗户或门廊时，会沿着表面法线方向发射二次射线，来检测窗户或门框的另一端。
- 只有在开口具有明显边框且垂面朝内时才能检测到 Portal。

![](../../../../images/SATutorialPortalFit.png)

在左侧示例中，AkAcousticPortal 可检测到开口；在右侧示例中，无法检测到开口，因为 Mesh 太薄了。

- 使用 Details 面板内的 **Detection Radius** 属性来限制所检测开口的大小。通常来说，该值要大于所要检测的开口大小，同时又小于整个 Room 的尺寸。
  - 对于大部分采用厘米作为单位且窗户和房门开口大小适中的 Unreal 工程，500 的默认值即可满足需要。当然，您也可以根据具体情况来调节该值以贴合 Static Mesh 的尺寸。
  - 若 **Detection Radius** 小于开口大小，则将无法找到 Portal。
  - 若 **Detection Radius** 太大，则可能会检测到宽度跨越整个 Room 的错误 Portal。
- Portal 不能带有与 Fit To Geometry 追踪射线碰撞的实体房门或窗户（由 **Collision Channel** 属性决定）。否则，将无法检测到开口。若开口带有窗户或房门，请使用不同的碰撞设定，或按下 H 来隐藏窗户/房门，以便忽略 Mesh。

# Fit To Geometry 使用技巧

- 要想在关卡中快速填充 "AkAcousticPortal" 和 "AkSpatialAudioVolume" Actor，一般只需在相应 Actor 上启用 Fit To Geometry，然后在按住 Alt 的同时拖动 Actor 的 Translation 小组件，以此复制 Actor 并将其放置到关卡中的新位置。
- 若某些 Static Mesh Actor（如家具、道具、灯具等）妨碍了 Fit To Geometry 所执行的射线追踪并导致产生错误的结果，可通过按下 H 来隐藏这些 Actor，以便 Fit To Geometry 射线追踪将之忽略。