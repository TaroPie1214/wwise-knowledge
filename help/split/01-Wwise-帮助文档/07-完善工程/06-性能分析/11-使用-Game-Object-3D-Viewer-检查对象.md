# 使用 Game Object 3D Viewer 检查对象

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [性能分析](00-性能分析.md) > 使用 Game Object 3D Viewer 检查对象

## 使用 Game Object 3D Viewer 检查对象

The Game Object 3D Viewer allows you to see how objects interact and move relative to one another in real time.

![](../../../../images/game_object_3D_viewer.png)

Each game object is displayed in the Game Object 3D Viewer with an icon.
You can customize the view depending on the options you select in
the Options Toolbar. For example, you can add any cone
or radius that has been applied to a game object to the 3D Viewer. You can also
reduce the number of game objects in the view by using the show/hide button
in the Game Object List. The Game Object List can be filtered by using
the Game Object Filters.

|  |  |
| --- | --- |
| [备注] | 备注 |
| Game objects are kept up to date only when being used. When a game object is registered but is not being used by any playing Event, Effect, or plug-in, the game object position might display the last known used position. |

### 在 Game Object 3D Viewer 中启用 Spatial Audio

若要在 Game Object 3D Viewer 中显示 Spatial Audio 视觉表示，则需先对其启用性能分析。

Spatial Audio 性能分析数据包括 Geometry（几何构造）和 Portal（门户）的视觉表示，也包括 Emitter（发声体）、Listener（听者）和 Room（空间）的新图标以及由 Diffraction（衍射）、Sound Propagation（声音传播）和 Reflect 插件所创建的声音路径和虚拟对象。

**指定所要分析的数据的方法如下：**

1. 在 Advanced Profiler（高级性能分析器）中，单击 Settings（设置）图标。

   这时将打开 Profiler Settings（性能分析器设置）对话框。
2. 选择 Spatial Audio。
3. 点击 **Close**。

   这时 Game Object 3D Viewer 中将显示相应数据。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Spatial Audio 会使用大量的资源。Game Object 3D Viewer（游戏对象 3D 查看器）中可能会缺少某些信息，如 Spatial Audio Geometry（Spatial Audio 几何构造）。确保通过 [AkInitSettings](https://www.audiokinetic.com/library/?source=SDK&id=struct_ak_init_settings.html) 调大 [uMonitorQueuePoolSize](https://www.audiokinetic.com/library/?source=SDK&id=struct_ak_init_settings_acdb64f2cf024ac17b7db878eb135c523.html#acdb64f2cf024ac17b7db878eb135c523)。 |

### 指定要在 Game Object 3D Viewer 中显示哪些数据

By toggling options in the 3D Viewer toolbar, you can have as
much or as little information displayed as you choose. The
more options you select, the more complex the view is.

**To specify the information to be displayed in the Game Object 3D
Viewer:**

1. Select from the four categories of options in the toolbar above the 3D Viewer.

   - 视图
   - Text
   - Game Object
   - Acoustics
2. Select an option from the chosen category.

   The corresponding change will appear in the 3D Viewer.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | For a description of each of the options see [“Game Object 3D Viewer Options”一节](../../09-参考主题/06-Profiler-视图/11-Game-Object-3D-Viewer/01-Game-Object-3D-Viewer-Options.md "Game Object 3D Viewer Options"). |
3. You can pin options that you use often to the toolbar by selecting their corresponding pin icon.

### 使用 Camera

To view game objects interacting with each other, you can move the 3D viewer camera in all three dimensions.

| 操作 | Control | 描述 |
| --- | --- | --- |
| **Perspective Camera** | | |
| 平移 | 鼠标中键+拖动 | The camera pans left, right, up, and down. |
| Zoom | 鼠标滚轮  Alt+Right-Click+Drag | 摄影机镜头将被推近和拉远。 |
| Orbit | Alt+Left-Click+Drag | 围绕中心点旋转透视摄像机。 |
| Rotate | 单击+拖动 | 调节透视摄像机镜头的朝向。 |
| Walk Navigation | Click+WASD  Click+Arrow Keys | 以第一人称视角移动透视摄像机，跟玩家在游戏中导航的方式类似。  - W/向上键：前移 - S/向下键：后移 - A/向左键：左移 - D/向右键：右移 - E/Page Up：上移（相对于 World Orientation） - Q/Page Down：下移（相对于 World Orientation）  按住 Shift 来加快移动速度。 |
| **Orthographic Camera** | | |
| 平移 | 鼠标中键+拖动  Right-Click+Drag | The camera pans left, right, up, and down. |
| Zoom | 鼠标滚轮  Alt+Right-Click+Drag | 摄影机镜头将被推近和拉远。 |
| **Camera Toolbar Options** | | |
| Reset Camera |  | 摄影机将被重置，并回到默认位置。 |
| Locate Object |  | 将列表中的选定对象置于摄像机中央。 |
| Follow Object |  | Capture（捕捉）过程中，如果对象移动，摄影机将跟随对象。  选择在使用 Locate Object 操作时跟随的对象。 |
| Frame All |  | 调节摄像机来让 Game Object 3D Viewer 显示所有游戏对象。 |

### 使用 Game Object Filter

By creating Game Object Filters, you can reduce the number of game objects displayed in the Game Object List. 您可以启用或禁用这些筛选器，并固定 Game Object List 中的个别游戏对象，以便覆盖相应的筛选器设置。

**创建 Game Object Filter：**

1. 在 Game Object 3D Viewer（游戏对象 3D 查看器）的 Game Object Filter（游戏对象筛选器）窗格中，单击选择器按钮 [>>]。
2. 选择 **Name or ID**（名称或 ID）选项。
3. Enter the game object name or ID you would like to
   retain in the Game Object List.

   Game objects that do not have a name or ID matching
   the filter are hidden from the Game Object List.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在筛选器字符串中可使用星号作为通配符。 |

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 或者也可以先在 Game Object List 中选择一个或多个条目，然后从快捷菜单中选择 **Add to Game Object Filters**（添加到游戏对象筛选器）。这样会为每个选定游戏对象自动创建一个筛选器。 |

**删除 Game Object Filter：**

1. 在 Game Object 3D Viewer（游戏对象 3D 查看器）的 Game Object Filter（游戏对象筛选器）窗格中，单击所要删除的筛选器左侧的选择器按钮 [>>]。
2. 选择 **Remove**（移除）选项。

   这时便会移除该筛选器。

**禁用 Game Object Filter：**

- In the Game Object Filter pane of the Game Object 3D
  Viewer, click the check box located to the left of the
  filter you would like to disable.

  The check box is unselected and all objects that were
  removed by the filter reappear in the Game Object
  List.

**禁用所有 Game Object Filter：**

- 在 Game Object 3D Viewer 中，单击 ![](../../../../images/btn_game_object_filter_on.png) 按钮。

  The button turns gray and all objects that were removed by any of the Game
  Object Filters reappear in the Game Object List.

**固定游戏对象：**

- In the Game Object List pane of the Game Object 3D
  Viewer, click the ![](../../../../images/unpin_icon.png) button associated to the
  game object you would like to pin. Multiselection is supported.

  The pin button turns blue and the game object
  remains in the Game Object List, regardless of the Game Object Filters.

### Showing/hiding Game Objects from the 3D Viewer

You can reduce the number of game objects displayed in the 3D Viewer by using the Game Object List.

1. All game objects are shown by default.
2. Hide a game object by unselecting the ![](../../../../images/GameObject3DViewer_show_icon.png) button associated to the game object you would like to hide. Multiselection is supported.

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | Alternatively, you can select one or more game objects in the list, right-click and select **Hide Selected in 3D Viewer**.  The shortcut menu also has two other options:  - **Show Only Selected in 3D Viewer**: Show all selected Game Objects and hide all the others from the 3D Viewer. - **Show All in 3D Viewer**: Show all Game Objects in the 3D Viewer, whether selected in the Game Object List or not. |

### Selecting objects in the 3D Viewer

Select objects in the 3D viewer to view the list of properties in the Selection Property pane. Selectable objects include Game Objects, Acoustic paths, and Image Sources. For more information about the Selection Properties, refer to [“Selection Properties”一节](../../09-参考主题/06-Profiler-视图/11-Game-Object-3D-Viewer/00-Game-Object-3D-Viewer.md#game_object_3d_viewer_selection_properties "Selection Properties").

| 操作 | Control | 描述 |
| --- | --- | --- |
| Single Select | Left-mouse button | Selects an object at the position of the mouse cursor in the 3D Viewer and displays the object properties in the Selection Property pane.  Replaces previously selected objects with the newly selected object.  If selected area contains multiple selectable objects close to each other, selects one of these objects. Repeating this action cycles through all possible selectable objects.  If selected area doesn't contain any selectable object, selection is cleared. |
| Multi-Select | Ctrl+Left-mouse button | Selects an object at the position of the mouse cursor in the 3D Viewer and displays the object properties in the Selection Property pane.  Adds the newly selected object to the selection. |

**相关主题**

- [“Game Object 3D Viewer”一节](../../09-参考主题/06-Profiler-视图/11-Game-Object-3D-Viewer/00-Game-Object-3D-Viewer.md "Game Object 3D Viewer")
- [“Game Object 3D Viewer 键盘快捷方式”一节](../../09-参考主题/06-Profiler-视图/11-Game-Object-3D-Viewer/02-Game-Object-3D-Viewer-键盘快捷方式.md "Game Object 3D Viewer 键盘快捷方式")

---