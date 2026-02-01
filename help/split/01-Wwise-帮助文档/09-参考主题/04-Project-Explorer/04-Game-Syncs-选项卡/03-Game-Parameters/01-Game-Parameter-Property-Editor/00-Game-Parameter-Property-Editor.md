# Game Parameter Property Editor

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Game Syncs 选项卡](../../00-Game-Syncs-选项卡.md) > [Game Parameters](../00-Game-Parameters.md) > Game Parameter Property Editor

#### Game Parameter Property Editor

在 Game Parameter Property Editor（游戏参数属性编辑器）中，可定义各个 Game Parameter 的最大值和最小值，以便将属性值映射至值范围之内。例如，您可以将赛车游戏中的值设置为映射至车辆的加速度。当车加速时，映射的属性会作用于声音。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。RTPC 所用 Game Parameter 的名称。 |
| Notes | 备注。与 Game Parameter 有关的附加信息。 |
| Bind to Built-In Param: | 绑定至内置参数。将此 Game Parameter 绑定至声音引擎中计算得出的内置参数。选择以下其中一项：  **有关内置参数的详细信息，请参阅 [可用内置参数](../../../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#avaialble_builtin_parameters "可用的内置参数：") 。**  - **Distance**:与游戏对象的距离。 - **Azimuth**:水平方位角。 - **Elevation**:竖直仰角。 - **Emitter Cone**:游戏对象的朝向与听者之间的夹角。 - **Obstruction**:由游戏对该游戏对象进行设定。 - **Occlusion**:由游戏对该游戏对象进行设定。 - **Listener Cone**:游戏对象与听者朝向（前部）之间的夹角。 - **Diffraction**:由 Wwise Spatial Audio 对游戏对象进行设定。 - **Transmission Loss**:由 Wwise Spatial Audio 对游戏对象进行设定。  |  |  | | --- | --- | | [备注] | 备注 | | 如果RTPC绑定到初始延迟或优先级，使用内置参数来控制RTPC会导致出问题。使用给定游戏对象播放声音时，会计算这些内置参数。因此，它们对大部分声音属性来说都很适用。内置参数控制的 RTPC 不适用于对象的播放逻辑属性（如 Initial Delay 和 Priority），因为触发 Play Action 时它们的值是未知的。 |  Default value: None |
| **Range** | |
| Min/Max | The minimum and maximum values of the Game Parameter that is mapped to properties in Wwise. 请参阅 [“Game Parameter Settings”一节](01-Game-Parameter-Settings.md "Game Parameter Settings")。 |
| Default | 默认值。游戏对象使用的全局值，这些游戏对象不会具体指定一个值。  如果游戏程序员使用 SDK 为游戏对象定义了全局 RTPC 值，则默认值也将被忽略。 |
| Interpolation Mode | 插值模式。选择 Game parameter 插值模式  - **None**:*None*\*：直接跳至目标值。 - **Slew Rate**:*Slew Rate*\*：将 Game Parameter 变化速率限制为指定的 Attack 和 Release 速率。 - **Filtering Over time**:*Filtering Over time*\*：在特定 Attack/Release 时间内将 Game Parameter 当前值设为目标值的 99.5%。  Default value: None |
| Attack | 起振。在变量增大时插值模式使用的比率（或时间）。  Default value: 50  Range: 0 to 1000000 |
| Release | 释放。变量减小时插值模式使用的比率（或时间）。  Default value: 0  Range: 0 to 100000 |

**相关主题**

- [“Creating Game Parameters”一节](../../../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")
- [“Defining the range of values for a Game Parameter”一节](../../../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#defining_range_of_values_for_game_parameter "Defining the range of values for a Game Parameter")
- [“将 Wwise 属性指派给游戏参数”一节](../../../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/01-将-Wwise-属性指派给游戏参数.md "将 Wwise 属性指派给游戏参数")
- [“Deleting Game Parameters”一节](../../../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#deleting_game_parameter "Deleting Game Parameters")
- [“Binding Game Parameters to built-in parameters”一节](../../../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#binding_game_parameter_to_built_in_parameter "Binding Game Parameters to built-in parameters")

---