# Game Object 3D Viewer Options

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Game Object 3D Viewer](00-Game-Object-3D-Viewer.md) > Game Object 3D Viewer Options

### Game Object 3D Viewer Options

您可以使用 Game Object 3D Viewer Options（游戏对象 3D 查看器选项）来指定要在 [“Game Object 3D Viewer”一节](00-Game-Object-3D-Viewer.md "Game Object 3D Viewer") 中显示哪些信息。

| 界面元素 | 描述 |
| --- | --- |
| **视图** | |
| Icon Size | 3D 对象图标大小。Game Object 图标大小的缩放倍数。  默认值：1.0 范围：0.0 ~ 4.0 单位：不适用 |
| Text Size | 文本大小。3D Viewer 中文本大小的缩放倍数。  默认值：1.0 范围：0.1 ~ 4.0 单位：不适用 |
| Game Units Per Meter | 游戏单位/米。一米之内包含多少个游戏单位。该项便于以米为单位调节设置的大小。  默认值：1  UI 范围：0.001 ~ 1000  范围：FLT\_MIN ~ FLT\_MAX  单位：游戏单位/米  若游戏通过 [`fGameUnitsToMeters`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_acbb4594e7634edbe91adec361e2cf111.html) 初始化设置予以设定，则无需调节此设置。 |
| Grid（网格） | 显示网格。决定是否在 3D Viewer 中显示基底平面上的网格。 |
| Grid Subdivision Size | 网格细分大小。基底网格线之间的间距。  默认值：1  范围：0.1 至 10,000  单位：游戏计量单位 |
| World Axis | 显示世界轴。决定是否在 3D Viewer 中显示世界轴标志。 |
| World Orientation | 世界朝向。3D Viewer 内坐标图中指向朝上的矢量。以下选项可用：  - **Y Up**（Y 朝上）– 将 X-Z 平面用作基底。 - **Z Up**（Z 朝上）– 将 X-Y 平面用作基底。 - **X Up**（X 朝上）– 将 Y-Z 平面用作基底。 |
| Camera Speed | 移动速度。决定摄像机移动的速度。  Default value: 1.0 (approximately 15 units per second) Range: 0.1 to 10 Units: Wwise units per frame |
| Camera Acceleration | 移位加速因子。用于决定在按住 Shift 并移动摄像机时加速的倍数。  Default value: 3  Range: 0.1 to 10  Units: N/A |
| **Game Object** | |
| Game Object Name（游戏对象名称） | 显示名称文本。决定是否在 3D Viewer 中显示游戏对象的名称。 |
| Game Object Input Channels | 显示输入声道文本。指示给定 Game Object 的各个位置由哪些声道发声。  如果指定 Game Object 在各位置上仅使用源声道中的一部分，开启 **Input Channel** 选项将显示每个位置使用了哪些声道。 ---------例如使用 [`AK::SoundEngine::SetMultiplePositions`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad63431938ab1e605a1f6e7fb013c0128.html) 函数的 AkChannelEmitter 版本来设定游戏对象位置的时候。  如果指定 Game Object 的所有位置都使用全部声道发声，那么启用 **Input Channels** 选项将没有变化。 |
| Game Object Position | 显示定位文本。决定是否在 3D Viewer 中显示游戏对象的坐标。 |
| Game Object Voices | 显示名称文本。决定是否在 3D Viewer 中显示所用 Attenuation ShareSet 的名称（如有）。 |
| Active Voices Only | 仅显示活跃声部。若启用此选项，则仅在查看器中显示具有活跃声部的游戏对象。若游戏对象发出活跃声部或其为活跃声部的听者，则认为该游戏对象包含活跃声部。 |
| Virtual Voices | 显示虚声部。若启用此选项，则在查看器中显示包含虚声部的游戏对象。 |
| Axis | 显示轴。决定是否在 3D Viewer 中显示与游戏对象前轴和顶轴对齐的箭头。这些箭头的颜色分别与 Z 轴和 Y 轴对应。  Also determines whether the arrow aligned with the front of a Portal is displayed in the 3D Viewer. This arrow is shown in the same color and opacity as the Portal. |
| Axis Size | The length of the top and front axes that indicate the orientation of a Game Object or Portal.  默认值：1 范围：0.1 至 10,000 单位：游戏单位 |
| Radius Opacity | Adjusts visibility of the Game Object radii within the Game Object 3D Viewer, where 0 is transparent and 1 is fully opaque.  默认值：0.5  范围：0 至 1  单位：不适用 |
| Inaudible Radius | Determines whether the radii of a Game Object are shown when the listener is beyond the Max distance defined in its attenuation. |
| Attenuation Cone | 显示衰减声锥。决定是否在 3D Viewer 中显示声部的衰减声锥（如有）。 |
| Attenuation Radius | 显示衰减半径。决定是否在 3D Viewer 中显示声部的衰减半径（如有）。 |
| Attenuation Spread | 显示散布声锥。决定是否在 3D Viewer 中的“听者”游戏对象上显示散布声锥。 |
| Spread Size | 散布声锥大小。调节散布声锥的大小。  默认值：2.0  滑杆范围：0.01 ~ 1000 单位：米 |
| **Acoustics** | |
| Diffraction | Determines whether diffraction paths or diffraction rays are displayed in the 3D Viewer. 以下选项可用：  - **None** - Neither diffraction paths nor   diffraction rays are displayed in the 3D Viewer. - **Paths** - Displays diffraction paths in the 3D Viewer. 它们代表声音如何发出，然后经过 Spatial Audio Portal 或 Spatial Audio Geometry 边缘衍射，最后到达听者所在位置。 - **Rays** - Displays the diffraction rays cast by the ray casting engine instead of the audio paths. 通过投射衍射射线可对环境进行采样并查找潜在的衍射路径。 |
| Diffraction Edges | 显示衍射边缘。决定是否在 3D Viewer 中的 Spatial Audio Geometry 上显示衍射边缘。 |
| 边缘受体 | 显示边缘受体。显示各个边缘受体。边缘受体由射线投射引擎用于查找潜在的衍射边缘。 |
| Virtual Emitters | Determines whether virtual emitters are displayed in the 3D Viewer. They represent the simulated position of the emitted sound after diffracting from Spatial Audio Portals or Geometry edges. |
| Inaudible Paths | 显示不可闻路径。决定是否在 3D Viewer 中显示不可闻路径。 |
| Reflection | Determines whether reflection paths or reflection rays are displayed in the 3D Viewer. 以下选项可用：  - **None** - Neither reflection paths nor   reflection rays are displayed in the 3D Viewer. - **Paths** - Displays reflection paths in the 3D Viewer. 这些路径由 Spatial Audio 创建以发送到 Reflect 效果器插件。它们代表声音如何发出，然后经过 Spatial Audio Geometry 反射，最后到达听者所在位置。 - **Rays** - Displays the reflection rays cast by the ray casting engine instead of the audio paths. 通过投射反射射线可对环境进行采样并查找潜在的反射路径。 |
| Image Sources | 显示反射镜像声源。决定是否在 3D Viewer 中显示镜像声源及图标。它们代表 Reflect 插件所创建镜像声源的位置。 |
| Portal Info | Determines if captured Portal information, such as the name and state, is displayed. |
| Diffraction % | Determines whether diffraction percentages are displayed in the 3D Viewer. They represent the amount of diffraction applied at a Spatial Audio Geometry edge. |
| Transmission % | Determines whether transmission percentages are displayed in the 3D Viewer. They represent the amount of transmission loss applied when a sound passes through a Spatial Audio Geometry. |
| Wire Frame | 显示为透明线框。决定是将 Portal 和 Geometry 显示为透明线框还是实心色块。 |
| Transparent Triangles | 显示透明三角形。决定是否显示透明三角形。透明三角形是透射损失为 0.0 的三角形。 |
| Reverb Zone Transition Regions | 显示过渡区。决定是否在 3D Viewer 中显示 Reverb Zone 的 Transition Region。 |
| Geometry Opacity | 几何构造不透明度。调节 Game Object 3D Viewer 中 Spatial Audio Geometry 的不透明度。其中，0 表示透明，1 表示完全不透明。  默认值：0.5  范围：0 至 1  单位：不适用 |
| Portal Opacity | 门户不透明度。调节 Game Object 3D Viewer 中 Spatial Audio Portal 的不透明度。其中，0 表示透明，1 表示完全不透明。  默认值：0.5  范围：0 至 1  单位：不适用 |
| Room Extent Opacity | 房间边界不透明度。调节 Game Object 3D Viewer 中 Spatial Audio Room Extent 的不透明度。其中，0 表示透明，1 表示完全不透明。  Room 边界是通过不同的 Room 顶点计算得出的边界框。Room 边界可用于计算 Room 的湿声透射散布。  有关更多详细信息，请参阅[设置 Room Geometry](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_roomsportals_apiconfig.html#spatial_audio_roomsportals_apiconfigroomgeometry)。  默认值：0.0  滑杆范围：0 ~ 1 单位：不适用 |
| Clusters | Select to display emitter clusters in the 3D Viewer. They represent grouped emitters based on their distance from the listener and other criteria. Clusters are represented by transparent spheres. Each cluster has a different color, and colors might change from frame to frame. The largest sphere represents the cluster leader. See [Emitter Clustering](https://www.audiokinetic.com/library/edge/?source=SDK&id=raytracing_geometry_guide.html#emitter_clustering_(experimental)) for more information. |
| Cluster Size | Adjusts the size of spheres representing emitter clusters in the 3D Viewer.    Default value: 1.0  Slider Range: 0 to 5.0 Units: N/A |

#### 相关主题

- [“Game Object 3D Viewer”一节](00-Game-Object-3D-Viewer.md "Game Object 3D Viewer")
- [“在 Game Object 3D Viewer 中启用 Spatial Audio”一节](../../../07-完善工程/06-性能分析/11-使用-Game-Object-3D-Viewer-检查对象.md#enable_spatial_audio_objects "在 Game Object 3D Viewer 中启用 Spatial Audio")
- [“指定要在 Game Object 3D Viewer 中显示哪些数据”一节](../../../07-完善工程/06-性能分析/11-使用-Game-Object-3D-Viewer-检查对象.md#specifying_data_to_be_displayed_in_game_object_3d_viewer "指定要在 Game Object 3D Viewer 中显示哪些数据")
- [“使用 Camera”一节](../../../07-完善工程/06-性能分析/11-使用-Game-Object-3D-Viewer-检查对象.md#working_with_camera "使用 Camera")

---