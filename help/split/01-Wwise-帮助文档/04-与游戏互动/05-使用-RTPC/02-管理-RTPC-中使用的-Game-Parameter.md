# 管理 RTPC 中使用的 Game Parameter

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 RTPC](00-使用-RTPC.md) > 管理 RTPC 中使用的 Game Parameter

## 管理 RTPC 中使用的 Game Parameter

在创建 Game Parameter（游戏参数）之后，才能将游戏中的参数映射到 Wwise 中的属性。您可以管理多个游戏参数，并在 Project Explorer 中 Game Syncs 选项卡中定义其最小值和最大值。

为了帮助您轻松识别界面中的 Game Parameter，它由以下图标表示。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | Game Parameter（游戏参数） |

### Creating Game Parameters

若要使用 Game Parameter 来驱动对象的属性值，必须先创建 Game Parameter。您可以在 Wwise 中的以下两个位置创建 Game Parameter：

- Project Explorer 的 Game Sync 选项卡
- Property、Attenuation 或 Effect Editor 的 RTPC 选项卡

|  |  |
| --- | --- |
| [注意] | 注意 |
| 在 Wwise 中命名 Game Parameter 时，只能使用字母，数字和下划线，并确保每个 Game Parameter 名称都是唯一的。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| Unless absolutely necessary, you should not rename a Game Parameter after it has been integrated into the game. If you rename a Game Parameter after it has been integrated into a game, you must also update any instances of the name in the game. The Game Parameter will not work until you do this, including while remote connected in either of the Profile and Edit modes |

**在 Project Explorer 中创建新的 游戏参数 的方法是：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Game Parameter 部分，执行以下操作之一：

   - 选择工作单元或虚拟文件夹，然后点击 Project Explorer 工具栏中的 **Game Parameter**（对白事件）图标。
   - 右键点击工作单元或虚拟文件夹，然后从快捷菜单中选择 **New Child** > **Game Parameter**（新建子项 > 对白事件）。

   一个新的 Game Parameter 被添加到 Game Parameter 列表中。
3. 将默认名称替换为最适合该游戏参的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 第一个字符只能使用字母或下划线。 |
4. 根据需要继续添加游戏参数。

**在 RTPC 选项卡中新建 Game Parameter 的方法如下：**

1. 在 Property Editor、Attenuation Editor 或 Effect Editor 的 RTPC 选项卡中，选择 RTPC 列表中的一个条目。

   如果还没有为该条目选择属性，则通过选择按钮选择一个。![](../../../../images/btn_selector.png)
2. 选择 **Game Parameter** 菜单项，然后选择 **New**。

   The New Game Parameter dialog opens.
3. 选择您要在其中创建游戏参数的工作单元。
4. 在 Name 字段中，将默认名称替换成最适合游戏参数的名称。
5. 点击 **OK** 来创建新的 Game Parameter。

### Defining the range of values for a Game Parameter

创建 Game Parameter 后，您必须设置其最小值和最大值。以赛车为例，最小和最大速度可为 0 和 300 km/h。

您也可以指定 Game Parameter 的默认值。通过游戏参数，您可以为没有明确指定特殊值的所有参数对象设置一个全局值。在以下情况下， Wwise 中指定的 Game Parameter 默认值将被忽略：

- 游戏对象明确地指定了一个特殊值。
- 游戏程序员在 SDK 中定义了一个全局 RTPC 值。

**定义游戏参数的取值区间：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Game Parameter 部分中，双击要定义其值的 Game Parameter 。

   此时游戏参数加载到 Property Editor 中。
3. 通过指定最小值和最大值来定义参数取值区别。请参阅 [“Game Parameter Settings”一节](../../09-参考主题/04-Project-Explorer/04-Game-Syncs-选项卡/03-Game-Parameters/01-Game-Parameter-Property-Editor/01-Game-Parameter-Settings.md "Game Parameter Settings")。
4. 如果没有明确地指定特殊值，则在 Default 文本框中，指定一个您希望游戏对象使用的全局值。

### Deleting Game Parameters

您可以删除工程中不再需要的 Game Parameter。删除 Game Parameter 后，对于之前使用它的对象、事件和预设，该参数将变为不可用。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 删除 Game Parameter 之前，请务必与您的音频程序员沟通，以确保不会影响游戏代码。 |

**删除游戏参数：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Game Parameters 部分中，右键点击您要删除的该游戏参数，然后选择 **Delete Selection**（删除选中项）。

   Game Parameter 将从 Wwise 中删除。

### Binding Game Parameters to built-in parameters

声音引擎会基于来自游戏的输入计算一组标准值，以便声音设计师以此为基础创建动态音频和振动。这些内置参数可通过 Game Parameter 对应 Property Editor（属性编辑器）中的 **Bind to Built-In Parameter**（绑定到内置参数）列表来访问。系统会根据从游戏接收的游戏对象定位数据来在每帧更新内置参数值。在 Wwise 设计工具中，只有在远程连接到游戏的情况下才会更新这些值。

与标准 Game Parameter 有所不同，无需进行额外的游戏编程就可使用与内置参数绑定的 Game Parameter。

|  |  |
| --- | --- |
| [备注] | 备注 |
| - 当 RTPC 绑定到内置参数时，声音引擎更新各个游戏对象的值。如果 RTPC 用于没有游戏对象关联的全局 Wwise 对象，例如总线或总线效果，则使用默认值。 - Obstruction and occlusion values set on Spatial Audio Portals do not affect the values   of RTPCs bound to built-in parameters. This behavior is intentional and   occurs because RTPCs only provide one value per game object, but a   single game object can have multiple paths through different Portals,   each with different obstruction and occlusion values. - 系统会通过*游戏对象*的位置评估基于发声体位置的内置参数（如 Distance、Azimuth、Emitter Cone 等）。因而，3D 定位设置（如 Automation 和 Hold Listener Orientation）会被忽略。 |

**可用的内置参数：**

- **Distance**

  距离。游戏对象和听者之间的距离。当多个听者或位置指定到同一个游戏对象时，将使用所有听者与声音位置组合之间的最短距离值。
- **Azimuth**

  方位角。投射在水平面上的听者与游戏对象之间的角，单位为度。0 度值表示声音来自听者正前方，-90 度表示声音来自左侧，90 度表示声音来自右侧，+/- 180 度表示声音位于听者正后方。

  当为游戏对象指定了多个听者或声音位置时，则使用听者和声音之间位置最靠近的角度值。
- **Elevation**

  仰角。听者与游戏对象之间相对于水平线的顶角，单位为度。0 度值表示声音位于听者的同一水平面上；90 度值表示声音位于正上方；-90 度表示声音位于正下方。

  当为游戏对象指定了多个听者或声音位置时，则使用听者和声音之间位置最靠近的角度值。
- **Emitter Cone**

  Emitter Cone（发声体锥）表示发声体朝向与发声体和听者间连线所形成的向量之间的 3D 角度。0 度表示发声体直接朝向听者，180 度表示发声体完全背朝听者。

  当为游戏对象指定了多个听者或声音位置时，则使用听者和声音之间位置最靠近的角度值。
- **Obstruction**

  声障。通过 Obstruction，可访问通过  [SetObjectObstructionAndOcclusion](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a1b3e18a25b405e55ba82de9b70cd11ba.html)  API 为游戏对象设置的声障值。

  如果为游戏对象指定了多个听者，则声障取值为给距离当前声音位置最近的听者指定的值。
- **Occlusion**

  声笼。通过 Occlusion，可访问通过 SetObjectObstructionAndOcclusion API 为游戏对象设置的声笼值。

  当为游戏对象指定了多个听者时，则声笼取值为给距离当前声音位置最近的听者指定的值。
- **Listener Cone**

  Listener Cone（听者锥）表示听者朝向与发声体和听者间连线形成的向量之间的 3D 夹角。0 度表示听者直接朝向发声体，180 度表示听者完全背朝发声体。

  当为游戏对象指定了多个听者或声音位置时，则使用听者和声音之间位置最靠近的角度值。
- **Diffraction**

  在使用带有 Room 和 Portal 或几何构造的声音传播路径时，Diffraction 可提供由 Wwise Spatial Audio 计算得出的衍射角度。

  In order to receive this built-in parameter, **Diffraction and
  Transmission** must be enabled in the Property Editor, and the
  emitter and listener must be either in separate Rooms connected by one or
  more Portals, or obstructed by geometry that was passed to Wwise Spatial
  Audio.

  通过 Room 和 Portal，“发声体”游戏对象可接收与其干声衍射相关的值；由发散角（度）表示传播路径与发声体和听者之间直线路径的偏差角度。由 Spatial Audio 内部注册的房间游戏对象也会接收到一个衍射值，但与其“湿声”衍射相关——即房间内声音扩散后，声场的衍射保留区。湿声衍射角度是传播路径与从门户开口法线之间的发散角，以度为单位。

  在声音可通过多个 Portal 或多条路径到达听者所在位置时，将选用各条路径当中的最小衍射角度。衍射值的范围为 0 - 100，其代表衍射百分比而非衍射角度。
- **Transmission Loss**

  在使用带有 Room 和 Portal 或几何构造的声音传播路径时，Transmission Loss 可提供由 Wwise Spatial Audio 计算得出的透射损失。

  In order to receive this built-in parameter, **Diffraction and
  Transmission** must be enabled in the Property Editor, and the
  emitter and listener must be either in separate Rooms connected by one or
  more Portals (enabled or not), or obstructed by geometry that was passed to
  Wwise Spatial Audio.

  计算得出的 Transmission Loss 可应用于直接连接发声体和听者的射线。几何构造的 Transmission Loss 可在几何构造上定义 (AkAcousticSurface::transmissionLoss)，Room 的 Transmission Loss 则在 Room 上定义 (AkRoomParams::TransmissionLoss)。该参数的值域为 0 ~ 100。

  将最大值用于发声体和听者所在 Room 以及与之交叉的所有几何构造表面。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | Although the Transmission Loss is taken from the ray corresponding to the direct path, Wwise does not allow signal processing of rays independently, except when using Attenuation curves or project-wide Environmental curves. 比如，倘若存在与透射路径平行的衍射路径，并且想要控制声音上的属性或带有内置 Transmission Loss RTPC 的效果器，则将此属性应用于透射和衍射路径共同产生的信号。这样获得的效果可能并不理想。这一点必须予以考虑。为此，最好基于 Attenuation 曲线来处理音量和由 Transmission Loss 导致的滤波。 |

---