# Game Object 3D Viewer

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > Game Object 3D Viewer

## Game Object 3D Viewer

Game Object 3D Viewer（游戏对象 3D 查看器）会以三维动态视觉形式呈现游戏中的游戏对象（发声体和听者）。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Wwise 中，默认情况下可以按 **F12** 键切换至 Game Object Profiler 布局。 |

The Game Object 3D Viewer can be separated in three distinct sections: [“Scene Graph”一节](00-Game-Object-3D-Viewer.md#game_object_3d_viewer_scene_graph "Scene Graph"), [“Game Object 3D Viewer”一节](00-Game-Object-3D-Viewer.md#game_object_3d_viewer_3d_viewer "Game Object 3D Viewer"), and [“Selection Properties”一节](00-Game-Object-3D-Viewer.md#game_object_3d_viewer_selection_properties "Selection Properties").

| Game Object 3D Viewer | |
| --- | --- |
|  | |
|  | **Scene Graph**: Shows a list of Game Objects present in the profiled game. |
|  | **3D Viewer**: Shows a 3D representation of the profiled game. |
|  | **Selection Properties**: Shows the properties of selected objects in the 3D Viewer. |

### Scene Graph

The Scene Graph displays a list of Game Objects in the 3D Viewer.

| 筛选器工具栏 | |
| --- | --- |
| This view includes a filtering toolbar, which allows you to reduce the amount of information displayed in the view so you can focus on specific elements. 有关更多详细信息，请参阅 [“在性能分析视图中筛选数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/03-在性能分析视图中筛选数据.md "在性能分析视图中筛选数据") 章节。 | |
|  | |
|  | **Unlink Filter**：禁止在多个筛选器视图之间同步。 |
|  | **Text Filter**：通过指定文本来筛选内容。系统会将您所指定的字词与内容中所含名称或字符串的开头进行匹配。键入的字词越多，显示的结果越细化。匹配项不区分大小写。有关高级用法的信息，请参阅“[“使用性能分析器筛选器表达式”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/04-使用性能分析器筛选器表达式.md "使用性能分析器筛选器表达式")”。 |
|  | **Object Filter**：通过指定 Wwise 对象来筛选内容。系统会将您所指定的 Wwise 工程对象与视图中的内容进行匹配。同时，还会依据对象关系（如父子对象关系和输出总线关系）对内容进行匹配。 |
|  | **Browse Object Filter**：显示 Project Explorer 浏览器，以便选择所要筛选的对象。 |
|  | **Mute/Solo Filtering**：若启用，则从结果中排除激活了 Mute 的对象，而只显示激活了 Solo 的对象。 |
|  | **Options**：显示其他操作。 |

| 界面元素 | 描述 |
| --- | --- |
| (启用/禁用) | Select to enable all Game Object Filters in the Game Object Filter list. When selected, the Game Object Filters and the Filtering Toolbar criteria are applied to the Game Object List. When deselected, only the Filtering Toolbar criteria are applied.  This button is selected by default.  |  |  | | --- | --- | | [备注] | 备注 | | If a Game Object Filter is not selected in the Game Object Filter list, it will not be enabled by selecting this button. | |
| **Game Object Filter** | |
| (启用/禁用) | Select to filter the Game Object List by name or ID. When a new filter is created, it is selected by default. |
| （选择器） | 允许通过选择 **Name or ID** 并输入游戏对象的名称或 ID 来创建新的 Game Object Filter。The filter is applied to the Game Object List.  若要从列表中移除筛选器，请选择 **Remove** 选项。 |
| **Game Object List** | |
| (Shown/Hidden) | Shows/hides an object in the Game Object List from the 3D Viewer. |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (固定/取消固定) | 固定/取消固定 Game Object List 中的对象。A pinned object is displayed in the list regardless of the Game Object Filter or its presence in the 3D Viewer. |
| Emitting Voices | 发出的声部数量。游戏对象发出的声部数量。 |
| Listening Voices | 听到的声部数量。游戏对象听到的声部数量。有关详细信息，请参阅[集成 Listener](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_listeners.html)。 |
| Virtual Voices | 虚声部的数量。 |
| ID | 在注册时为 Game Object 指定的 ID。 |
|  | 注册。游戏对象的注册时间戳。有关详细信息，请参阅[注册游戏对象](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_gameobj.html#soundengine_gameobj_reg)。 |
| Unregistered | 注销。游戏对象的注销时间戳。有关详细信息，请参阅[注册游戏对象](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_gameobj.html#soundengine_gameobj_reg)。 |
| Room ID | 房间 ID。当前包含 Game Object 的 Room 的 ID。Room ID 仅适用于 Spatial Audio Emitter 和 Spatial Audio Listener。它不适用于 Room Game Object 和未使用 Spatial Audio 的 Game Object。 |
| **Game Object List Context Menu** | |
| Add to Game Object Filters | Add the names of the selected game object(s) in the Game Object Filter section above. |
| Hide Selected in 3D Viewer | Hide the selected game object(s) in the 3D Viewer. |
| Show Only Selected in 3D Viewer | Show the selected game object(s) in the 3D Viewer and hide all other game objects. |
| Show All in 3D Viewer | Show all the game objects of the list in the 3D Viewer. |

### Game Object 3D Viewer

The 3D viewer is the middle section of the Game Object 3D Viewer. It shows a 3D representation of the profiled game.

| 3D Viewer Toolbar | |
| --- | --- |
|  | |
|  | **Select Camera**: Indicates the camera option currently being used. 您可以选择以下选项之一：  - **Perspective 1** to switch to Camera 1, which you can move freely in the scene. - **Perspective 2** to switch to Camera 2, which you can move freely in the scene. - **Top** to position the camera above the scene. - **Bottom** to position the camera below the scene. - **Left** to position the camera to the left of the scene. - **Right** to position the camera to the right of the scene. - **Front** to position the camera to the front of the scene. - **Back** to position the camera to the back of the scene. |
|  | **Reset Camera**: Returns the camera to its default position. |
|  | **Locate Game Object**: Displays a list of game objects from which you can choose one on which the camera will be centered. |
|  | **Follow Game Object**: Sets the camera to follow the selected game object during capture. |
|  | **Frame All**: Adjusts the Game Object 3D Viewer to show all followed game objects. |
|  | **Display Options**: Opens a context menu that you can use to select which categories are displayed or hidden in the Options Toolbar below. |

| 3D Viewer Toolbar: Options | |
| --- | --- |
| This toolbar displays the Game Object 3D Viewer options, allowing you to show and hide information in the 3D Viewer. 有关更多详细信息，请参阅“[“Game Object 3D Viewer Options”一节](01-Game-Object-3D-Viewer-Options.md "Game Object 3D Viewer Options")”。 | |
|  | |
|  | **View**: Displays options about the 3D Viewer in general. |
|  | **Game Object**: Displays options about game objects in the 3D Viewer. |
|  | **Acoustics**: Displays options about Acoustics elements in the 3D Viewer. |
|  | |
|  | **View Menu**: Displays the options related to the View category. Each category has their own menu. |
|  | **Pin button**: Adds or removes the option from the toolbar itself. This helps accessing frequently used options more easily. An option that doesn't have a pin button will be included in the option above when the latter is added to the toolbar. |

| 界面元素 | 描述 |
| --- | --- |
| Game Object 3D Viewer | 以图形形式在三维空间中呈现游戏对象的相对位置。  The following camera movements are possible:  - Hold the middle mouse button and drag to pan. - Use the mouse wheel or Alt+Right-click and drag to zoom. - Alt+click and drag to orbit the camera. - Right-click and drag to rotate (orient) the camera. - Hold the right mouse button and press WASD or the arrow keys to move the   camera. - Hold the Shift key to move faster (only for walk movement). |
| |  | | --- | |  |  （轴标志） | 根据三个轴来指示摄像机方向。 |
|  | 指示 Game Object 是发声体。 |
|  | 指示 Game Object 既是发声体又是听者。 |
| Attenuation Radius and Cone | 直观地显示所发出声音的衰减半径和声锥。若声音带有衰减，则为由距离驱动的曲线设置最大距离。此距离表示为围绕“发声体”游戏对象的球体的半径。若衰减还有声锥，则还会在 3D 视图中显示内锥。内锥的角度对应于衰减的内锥值。 |
| Direct Path | 在通过“发声体”游戏对象播放声音且听者处于视野之内时，会在两者之间绘制直达路径。“处于视野之内”意味着听者和发声体之间的距离小于衰减半径。 |
| Spread Cones | 散布声锥。直观地显示发声体的声音散布。散布角度会随声音上应用的 Spread Attenuation（散布衰减）曲线变化。您可以在 [“Game Object 3D Viewer Options”一节](01-Game-Object-3D-Viewer-Options.md "Game Object 3D Viewer Options") 中调节整个散布声锥的大小。  另外，还可由 Spatial Audio 应用散布声锥。在这种情况下，会将其显示为其他颜色。有关更多详细信息，请参阅 [Spatial Audio Spread Cones](00-Game-Object-3D-Viewer.md#sa_spread_cones)。 |
| **Spatial Audio** | |
|  | 指示 Game Object 是 Spatial Audio Room，而该 Spatial Audio Room 既是发声体又是听者。 |
|  | 指示通过 Reflect 插件创建的 Spatial Audio 镜像声源。They represent the position from where the reflected sound is emitted. 根据反射阶数（一阶、二阶或高阶），它们将显示为三种不同的颜色。 |
|  | 对于穿过 Spatial Audio Portal 的衍射或声音传播，指示其所创建的 Spatial Audio 发声体的虚声源位置。The virtual emitter icon takes the color of the path it is created from. |
| Geometry | 几何构造。指示通过 Spatial Audio 注册的几何构造。其会依据 **Display as Wire Frame** [“Game Object 3D Viewer Options”一节](01-Game-Object-3D-Viewer-Options.md "Game Object 3D Viewer Options") 显示为空心线框 (1) 或实心色块 (2)。  When grey, geometry is associated with a room and is not used for reflection or diffraction (a).  When geometry is of other colors (b and c), they represent Spatial Audio Geometry. 声音在遇到此类几何构造时会发生反射、衍射或透射（取决于具体配置）。其颜色因几何构造各个表面上应用的 Acoustic Texture（声学材质）而异。有关如何设置 Wwise 对象颜色的详细信息，请参阅[“设置颜色”一节](../../../02-入门/04-个性化您的工作空间/03-设置颜色.md "设置颜色")章节。在示例 (b) 中，没有指派任何 Acoustic Texture。在示例 (c) 中，指派了 “Wood Deep Factory” Acoustic Texture。  另请参阅：[Geometry](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry.html) |
| Portal | 门户。指示 Spatial Audio Room 中的入口。它们在 3D Viewer 中显示为彩色条带。声音可在非彩色区域内传播。The color of the Portal changes depending if it is opened or closed (Disabled). 其会依据 **Display as Wire Frame** [“Game Object 3D Viewer Options”一节](01-Game-Object-3D-Viewer-Options.md "Game Object 3D Viewer Options") 显示为空心线框 (1) 或实心色块 (2)。  另请参阅：[Room 和 Portal](https://www.audiokinetic.com/library/edge/?source=SDK&id=using_rooms_and_portals.html) |
| Reflection Paths | 反射路径。这些路径代表启用了 Reflect 的声音如何从发声体发出，然后通过 Spatial Audio Geometry 反射，最后到达 Spatial Audio Listener 所在位置。我们将声音到达听者所在位置前经过的反射表面数量称为反射阶数。每一阶的反射都会显示为不同的颜色。  | 颜色 | Light 主题 | Dark/Classic 主题 | | --- | --- | --- | | 红色 | 一阶 | 四阶 | | 深橙色 | 二阶 | 三阶 | | 浅橙色 | 三阶 | 二阶 | | 黄色 | 四阶 | 一阶 |  下图中使用了 Light 主题。其中，一阶反射路径显示为了红色，二阶反射路径显示为了深橙色。    若 Geometry（几何构造）启用了衍射，则将显示衍射后的反射路径。衍射类型有两种：视区衍射和影区衍射。At the edge of the Geometry, a percentage appears representing the amount of filtering applied to the reflected sound from the diffraction. The more filtering is applied, the more the path becomes transparent.  在反射点和 Spatial Audio Listener 之间被启用了衍射的 Geometry 阻挡时，将出现影区衍射。    在路径未被启用了衍射的 Geometry 遮挡时，将出现视区衍射。The reflection point snaps on the edge of the Geometry and a diffraction percentage and level appears on the path.    另请参阅：  - [使用 Geometry API 模拟早期反射](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry_er.html) - [早期反射的几何衍射](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry_diffract.html#spatial_audio_apigeometry_diffract_er) |
| Diffraction and Transmission Paths | 衍射和透射路径。这些路径代表启用了衍射和透射的声音如何从 Emitter 发出，然后传播到启用了衍射的 Geometry 背后，最后到达 Spatial Audio Listener 所在位置。The more a sound is filtered, the more the path becomes transparent.  衍射路径上的每个边缘都会显示一个百分比值，其代表衍射边缘对声音产生的滤波强度。下图展示了几何衍射路径。  在听者处于启用了衍射的 Geometry 背后时，将使用透射路径来替代直达路径。几何构造表面上的点表示由于声音穿过启用了衍射的 Geometry 表面而产生的透射损失。路径可能会穿过多个表面，但只会将最大的透射损失值应用于声音并显示在路径上。    在声音穿过房间的墙壁时也会生成透射路径。在这种情况下，会在透射损失值下显示 "(Room)"。若路径穿过 Room 和启用了衍射的 Geometry，则在透射路径上显示两个值当中的较大值。    可在 Portal 的边缘生成衍射路径。这些路径会采用不同的绘制方式，以区别于由启用了衍射的 Geometry 产生的衍射路径。    衍射路径既可由 Portal 也可由启用了衍射的 Geometry 产生。在这种情况下，会同时显示两种颜色的衍射路径。    另请参阅：  - [使用 Geometry API 模拟衍射和透射](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_apigeometry_diffract.html) - [为其他房间的声音传播建模](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_roomsportals_apioverview.html#spatial_audio_roomsportals_modelingsoundpropagationfromotherrooms) |
| Radial Emitter | 圆形发声体。Radial Emitter 会显示两个代表其内外半径的球体。这两条半径决定在模拟圆形声源时为声音应用多少散布效果。 |
| Spatial Audio Spread Cones | 在 Spatial Audio 产生散布时，其可能会显示为不同的颜色。下图分别显示了 (1) Radial Emitter 散布、(2) 被阻挡的 Radial Emitter（依据路径是衍射还是透射路径显示不同颜色的散布声锥）、(3) 因受 Portal 开口限制而收缩的散布声锥。 |
| Room Extent | Room 边界代表 Room 的 Volume。该值用于估算穿透房间墙壁的声音产生的散布。只有在 Spatial Audio 知晓几何构造的情况下，才会为 Room 赋予边界。有关更多详细信息，请参阅[设置 Room Geometry](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_roomsportals_apiconfig.html#spatial_audio_roomsportals_apiconfigroomgeometry)。由几何构造的顶点生成凸形形状。在下图中，可看到不同 Room 形状的边界。 |
| 边缘受体 | 边缘受体由射线投射引擎用于查找与衍射边缘的潜在交点。每个衍射边缘与一个或多个边缘受体关联。 |
| 反射射线 | 通过投射反射射线可对环境进行采样并查找潜在的反射路径。 |
| 衍射射线 | 通过投射衍射射线可对环境进行采样并查找潜在的衍射路径。 |
| Emitter clusters | Emitter clusters group emitters based on distance to the listener and other criteria. |

### Selection Properties

The selection property panel is on the right of the Game Object 3D Viewer. It shows the properties of objects selected in the 3D Viewer. Selectable objects include Game Objects, Acoustic Paths, and Image Sources. For more information on how to select objects in the 3D Viewer, refer to [“Selecting objects in the 3D Viewer”一节](../../../07-完善工程/06-性能分析/11-使用-Game-Object-3D-Viewer-检查对象.md#object_selection "Selecting objects in the 3D Viewer").

| 属性 | 描述 |
| --- | --- |
| **Game Objects** | |
| Type | The type of Game Object:  - Listener: Listens to a sound source. - Distance Probe: An object that is used for distance calculations for a   specified listener. - Emitter: Emits a sound source. - Virtual Position: The position of the game object that is created by   diffraction or game object radius. - Room: A symbolic representation of a distinct acoustic environment within   the simulation. Assigned to a game object, the room emits Reverb and Room   Tone. |
| Ray ID | The ID of the selected game object's position followed by the ID of its corresponding path, if there is one. |
| Position | The position of the Game Object |
| 输入声道 | Indicates which channels are emitted by the Game Object if it only uses a subset of the possible source channels. |
| Emitting Voices | The number of voices emitted by the Game Object. |
| Listening Voices | The number of voices listened to by the Game Object. |
| Virtual Voices | 虚声部的数量。 |
| Voice Names | The emitted voice names. |
|  | The registration timestamp of the Game Object. |
| Unregistered | The unregistration timestamp of the Game Object. |
| Outer Radius | The outer radius applied to the Game Object in game units. |
| Inner Radius | The inner radius applied to the Game Object in game units. |
| Room | The Room containing the selected Game Object. |
| Room Data | The monitoring data of the Room.  This data is only present if the selected Game Object is of type Room.  | 属性 | 描述 | | --- | --- | | Front | Front Room Orientation. Room orientation has an effect when the associated auxiliary bus is set with 3D Spatialization in Wwise, as 3D Spatialization implements relative rotation of the emitter (room) and listener. | | Up | Up Room Orientation. Room orientation has an effect when the associated auxiliary bus is set with 3D Spatialization in Wwise, as 3D Spatialization implements relative rotation of the emitter (room) and listener. | | Reverb Aux Bus | The reverb auxiliary bus that is associated with this room. | | Reverb Level | The reverb control value for the send to Reverb Aux Bus. Valid range: (0.f-1.f). | | Transmission Loss % | The transmission loss value for the Room, describing the average amount of sound energy dissipated by the walls of the room. | | Aux Send Level | Send level for sounds that are posted on the room game object; adds reverb to ambience and room tones. Valid range: (0.f-1.f). | | Prority | The prority of this room. Room priority is used by the room containment system to disambiguate cases where an object is inside several rooms at the same time. In this case, the room with the higher priority is selected. | | Geometry Instance ID | The Geometry Instance which describes the size and shape of the Room. | | Is a Reverb Zone | A Reverb Zone establishes a parent-child relationship between two Rooms and allows for sound propagation between them as if they were the same Room, without the need for a connecting Portal. | | Parent Room | The Parent Room of the Reverb Zone. | |
| **Diffraction Paths and Direct Paths** | |
| Emitter（发声体） | The Game Object emitting the source of this path. |
| Path Length | The length of the path in game units. |
| Transmission Loss % | The total transmission loss percentage applied on this path. |
| Diffraction % | The total diffraction percentage applied on this path. |
| Obstruction % | The total obstruction percentage applied on this path. |
| Occlusion % | The total occlusion percentage applied on this path. |
| Spread % | The percentage of spread applied on this path. |
| Aperture % | The smallest portal opening along the path. It restricts the maximum spread. |
| Gain | The propagation path gain. Includes volume tapering gain to ensure that diffraction paths do not cut in or out when the maximum diffraction angle is exceeded. |
| Hit Point  (Direct Paths with Transmission Loss Only) | The point where the path hits a geometry surface with the highest amount of transmission loss.  | 属性 | 描述 | | --- | --- | | Position | The position of the transmission hit point. | | Transmission Loss % | The percentage of transmission loss at hit point. | |
| Node  (Diffraction Paths Only) | A diffraction node in the path. Diffraction nodes are listed in order from listener to emitter.  | 属性 | 描述 | | --- | --- | | Position | The position of the diffraction edge. | | Diffraction % | The diffraction percentage applied on this edge. | | Portal | The node's Portal. | |
| **Reflection Paths** | |
| Emitter（发声体） | Game Object emitting the sound of this Reflection path. |
| Distance | Length of the reflection path. |
| Level（电平） | Linear gain applied to the image source. |
| Diffraction % | Total diffraction percentage value of the reflection path. |
| Occlusion % | Total occlusion percentage value of the reflection path. |
| Reflection Order | The order of reflection. |
| Node | A reflection or diffraction node in the path. Nodes are listed in order from listener to emitter.  | 属性 | 描述 | | --- | --- | | Position | The position of the reflection point or the diffraction edge. | | Diffraction % | The diffraction percentage applied on the diffraction edge. | | Acoustic Texture | The Acoustic Texture of the surface at the reflection point. | |
| **Image Sources** | |
| Position | Position of the image source. |
| Level（电平） | Linear gain applied to the image source. |
| Game Object | The Game Object of the image source. |

**相关主题**

- [“Game Object 3D Viewer Options”一节](01-Game-Object-3D-Viewer-Options.md "Game Object 3D Viewer Options")
- [“Game Object 3D Viewer 键盘快捷方式”一节](02-Game-Object-3D-Viewer-键盘快捷方式.md "Game Object 3D Viewer 键盘快捷方式")
- [“使用 Game Object 3D Viewer 检查对象”一节](../../../07-完善工程/06-性能分析/11-使用-Game-Object-3D-Viewer-检查对象.md "使用 Game Object 3D Viewer 检查对象")

---