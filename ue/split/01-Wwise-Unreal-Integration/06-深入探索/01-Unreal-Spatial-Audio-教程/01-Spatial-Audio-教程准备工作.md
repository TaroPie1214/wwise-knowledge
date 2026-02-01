# Spatial Audio 教程准备工作

|  |
| --- |
| Wwise Unreal Integration Documentation |

Spatial Audio 教程准备工作

|  |  |
| --- | --- |
|  | **注記：** 作为 Unreal Demo Game 的一部分，Audiokinetic Launcher 中专门提供了一个包含各项教程所需参数的地图。该地图名为 SpatialAudioTutorialMap。若要使用该地图，则可跳过以下章节。 |

# 创建新的工程

按照以下步骤来构建相应的工作环境。

1. 通过 Epic Launcher 启动 Unreal。
   1. 新建一个空白的 C++ Unreal 工程（没有初学者内容）。
   2. 关闭 Unreal。
2. 启动 Audiokinetic Launcher。
   1. 安装 Wwise。
   2. 选中 Unreal Engine 选项卡。
   3. 点击 **Integrate Wwise into Project** 按钮。
   4. 点击 **Open in Wwise** 按钮来启动 Wwise。
   5. 点击 **Open in Unreal** 按钮来启动 Unreal。

# Wwise 工程准备工作

对于本教程，您需要创建 Sound SFX 和用于播放声音的 Event。

1. In the Wwise project, create a new Sound SFX in the Default Work Unit of the Containers hierarchy and import a sound.
   1. 确保在 General Settings 选项卡中启用 **Use game-defined auxiliary sends**。

      ![](../../../../images/SATutorialSoundPropertyEditorGeneralSettings.png)
   2. 在 Positioning 选项卡中：

      1. 启用 **Listener Relative Routing**。
      2. 将 3D Spatialization 设为 **Position + Orientation**。
      3. 添加 Attenuation 并将 Max distance 设为 5000。
      4. 启用 **Diffraction and Transmission**。

      ![](../../../../images/SATutorialSoundPropertyEditorPositioning.png)
2. Right-click on the Sound SFX within the Containers hierarchy, then select **New Event** > **Play**.

   ![](../../../../images/SATutorialEventEditor.png)
3. 打开 Project Settings。
   1. 在 SoundBanks 选项卡中，确保启用 **Enable Auto-Defined SoudBanks**。

      ![](../../../../images/SATutorialProjectSettingsSoundBanks.png)
4. 保存工程。
5. 生成 SoundBank。

# Unreal 工程准备工作

1. 根据需要灵活地创建地面、由两个房间组成的建筑以及外部障碍物。在 SpatialAudioTutorialMap 中，我们为建筑使用了自定义 Mesh，并为外部障碍物使用了 Basic Cube Static Mesh 组件。
2. 在场景中放置发声体：
   1. Drag the Event created in the previous section from the Wwise Browser to the Content Browser.

      ![](../../../../images/SATutorialWwiseBrowser.png)
   2. 将 Event 拖到场景中来创建新的 `AkAmbientSound` Actor。
      1. 将其中一个放在外部，然后在每个 Room 中各放一个。
      2. For all `AkAmbientSound` actors, make sure to set **Refresh Interval** to 0.

         ![](../../../../images/SATutorialOcclusionRefreshInterval.png)

以下为 Spatial Audio Tutorial Map 的截图。

![](../../../../images/SATutorialSpatialAudioTutorialMap.png)

1. 从 Blueprints 菜单打开 Level Blueprint。
   1. 通过用户输入来触发 Event。
      1. 将新建的 AkAmbientSound 从 World Outliner 拖到 Blueprint 中。
      2. 从 AkAmbientSound 节点查找 Post Associated Ak Event 函数。
      3. 右键单击 Blueprint 背景，然后搜索 Left Mouse Button。
      4. 将 Pressed 输出引脚连接到 "Post Associated Ak Event" Exec。
   2. 针对所有 AkAmbientSound 条目重复同样的步骤。

      ![](../../../../images/SATutorialLevelBlueprint.png)
   3. 保存并关闭 Level Blueprint。

# 验证所作设置

1. 启动场景。现在按下相应的 Button，应会听到 3D 空间化声音。
2. 连接 Wwise 设计工具，然后打开 Profiler 布局（快捷键 F6）。

   1. 在外面播放声音时，应会看到与以下相似的 Voices Graph。

   ![](../../../../images/SATutorialAdvancedProfilerVoicesGraph.png)