# Positioning category: Containers hierarchy objects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > Positioning category: Containers hierarchy objects

#### Positioning category: Containers hierarchy objects

The properties in the Positioning category allow you to define how sounds will propagate in your game. 声音的传播取决于它的定位类型。在 Wwise 中，声音可使用扬声器声像摆位或 3D 空间化。两种定位之间的主要区别在于源声道映射到输出扬声器的方式上。在默认情况下，对于采用声像摆位的声音，其源声道与输出扬声器一致。而且，无论听者或游戏对象的位置或朝向如何，都会通过左前和右前扬声器来播放声音。不过，您可以使用 Speaker Panner（扬声器声像器）来平衡各个声道的音量，以使声音可以通过不同的扬声器听到。

对于 3D 空间化声音，可将各个输入声道输出至环绕声环境中的任意扬声器，从而轻松模拟声音相对于听者的移动。使用 3D 空间化声音时，可在 Wwise 中自行预定义空间化，或者使用游戏对象在游戏中的实际位置。

3D 空间化依赖于发声体相对于听者的位置。只有发声体和听者为不同的游戏对象，才能执行 3D 空间化。In the Wwise Project, objects of the Containers hierarchy are associated to their emitter when the game posts events. 在 Wwise 对象启用 Listener Relative Routing 选项时，其输出总线将关联至听者。Normally, the Listener Relative Routing option is enabled in the Containers hierarchy, so that busses that follow are associated with the listener. 注意，只有启用 Listener Relative Routing 选项的 Wwise 对象才能执行 3D 空间化，因为对象必须关联至发声体，并混音到与听者关联的总线中。

|  |  |
| --- | --- |
| [备注] | 备注 |
| You should enable Listener Relative Routing on sounds and other objects of the Containers hierarchy even if they don't utilize 3D spatialization. 否则，其输出总线会关联至发声体而非听者，进而导致总线实例出现差异。 |

此外，还可将距离衰减应用于随“发声体”和“听者”游戏对象之间距离变化的声音，然后在 Wwise 内利用 Attenuation ShareSet 来让各种不同的对象共享这些设置。

对于不太复杂的设备（例如游戏控制器），它们的马达无法模拟 3D 环境，因此定位无关紧要。然而，可以使用衰减来降低当振动信号远离游戏玩家时振动信号的强度。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Although the positioning of busses must be considered in relation to its impact on all objects that go through it, their [Positioning properties](../02-Busses-hierarchy/04-Common-tabs-and-categories-Busses-hierarchy-object/05-Positioning-category-Audio-and-Auxiliary-Busses.md "Positioning category: Audio and Auxiliary Busses") is almost identical to the Positioning properties of objects in the Containers hierarchy. 只是没有 Override parent（不沿用父对象）选项。 |

| Positioning | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Override parent | 不沿用父项。确定定位和衰减设置是从父项继承还是在层级结构的当前层级定义。当选择此选项时，Positioning 控件不可用。  对于顶层对象，此选项将不可用。  Default value: false |
| Center % | 中置百分比。通过中置扬声器的音量或音量百分比。  - 对于启用 Direct Assignment 的扬声器声像摆位，仅当单声道对象输出至带中置声道的总线时，Center % 值才适用。在底层源文件或插件为单声道时，Container 对象为单声道。在 Bus Configuration 设为 1.0 时，总线为单声道。 - 对于应用 Balance-Fade 的扬声器声像摆位，Center % 值仅适用于带中置声道的输出（如单声道、3.0、5.1 和 7.1）。 - 对于 3D 空间化，Center % 值同样仅适用于带中置声道的输出；不过还要注意，只有开启此值，信号才会发送至中置声道。  |  |  | | --- | --- | | [技巧] | 技巧 | | 有关如何使用 Center % 的详细信息，请参阅 [将音频信号传送至中置扬声器](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/09-将音频信号传送到中置扬声器.md "将音频信号传送到中置扬声器") 页面。 |  Default value: 0  Range: 0 to 100 |
| Speaker Panning | 默认设为 Direct Assignment。其中，FL 对应 FL 扬声器，FR 对应 FR 扬声器，以此类推。  若设为 Balance - Fade，则允许调节 2.0 ~ 7.1 Audio Bus 中各个声道的音量。参照 Speaker Panner，离圆点较近的声道的音量会增大，离圆点较远的声道的音量会减小。  若设为 Steering，则允许在输出总线声道当中重新分配不同声道的声音。配比将依据相对于 Speaker Panner 中圆点的位置进行计算。  Panner 不受音频源内所含声道数影响。  |  |  | | --- | --- | | [备注] | 备注 | | Panner 不会对 Ambisonics 声音产生影响。 |  Default value: Direct Assignment |
| **Listener Relative Routing** | |
| Listener Relative Routing | 听者相对通路。若启用，将针对该 Wwise 对象计算发声体与听者的关系。对于 Containers 层级结构中的对象，一般都要评估发声体与听者的关系。因为这些对象与发声体关联，而总线大多都是跟听者关联。  确保信号链中至少有一个对象启用了 Listener Relative Routing（是何定位类型并不重要）；否则，可能导致混音图完全重复（包括总线及效果器）。这样不仅会使用更多 CPU 处理资源，还会导致大部分插入到总线中的效果器（如压缩器）出现异常。  在发声体和听者为不同的游戏对象时，Wwise Profiler 的 Voice Graph 中应会显示此故障。注意，在通过设计工具播放声音时可能不会显示，因为 Transport/SoundCaster 游戏对象同时为发声体和听者。  在执行游戏对象驱动的 3D 定位（衰减和空间化）时，同样要评估发声体与听者的关系。  Default value: true |
| 3D Spatialization | 3D 空间化。指定是否计算音频源定位以便模拟 3D 空间内的运动。根据需要选择以下选项：  - **None**（默认）：声音将依据 Speaker Panning 设置进行摆位。 - **Position**:声音将依据发声体和听者的相对位置进行摆位。 - **Position + Orientation**:声音将依据发声体和听者的相对位置进行摆位。同时，声音的多声道内容还会随着发声体和听者的相对朝向旋转。仅当输入文件为多声道且散布大于零时，Orientation 才会起作用。  Default value: None |
| Speaker Panning / 3D Spatialization Mix | 扬声器声像摆位/3D 空间化混音。Speaker Panning 和 3D Spatialization 之间的交叉淡变。在将空间化设为 None 以外的值时可用。  Default value: 100  Range: 0 to 100 |
| **Listener Relative Routing > Attenuation** | |
| Enable Attenuation | 启用衰减。在选中时，将应用指定 Attenuation ShareSet 的衰减曲线。您可以为此属性添加 RTPC，以此控制是否在运行时应用衰减曲线。  Default value: true |
| Attenuation Instance | 衰减实例。Wwise 对象的 Attenuation 实例。该实例分为 ShareSet 和自定义两种。有关详细信息，请参阅 [将 Attenuation 实例应用于对象](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/02-将衰减应用到对象.md "将衰减应用到对象") 页面。 |
| Distance Scaling % | 默认值：100 取值范围：1 ~ 10000  距离缩放 %。按比例对此对象上应用的最大衰减距离进行调节。您可以在此属性上添加 RTPC 来在运行时按比例调节声音的最大衰减距离。  Default value: 1  Range: 0.01 to 100 |
| **Listener Relative Routing > 3D Position** | |
| 3D Position | 3D 定位。定义如何计算位置，以便进行 3D 定位（衰减和空间化）。  – Emitter：游戏定义的定位。 – Emitter + Automation：基于“发声体”游戏对象位置的 User-Defined 自动化定位。使用 **Automation** 按钮进行编辑。  |  |  | | --- | --- | | [备注] | 备注 | | 对于使用 Emitter + Automation 的声音，Wwise Spatial Audio 功能存在一定限制。对于这样的声音，会禁用衍射和透射处理。而且，自动化偏置不适用于早期反射处理。对此，会使用基准 Game Object 位置来计算反射。 |  – Listener + Automation：基于“听者”游戏对象的 User-Defined 自动化定位。使用 **Automation** 按钮进行编辑。  |  |  | | --- | --- | | [备注] | 备注 | | 对于使用 Listener + Automation 的声音，Wwise Spatial Audio 功能会被禁用。其中包括早期反射处理、Distance Probe、衍射和透射以及 Room 发送。 |  Default value: Emitter |
| Hold Listener Orientation | 跟踪听者方向。确定动画路径的位置是否锁定到听者的朝向。  若未选中此选项，则路径将随听者移动。这意味着无论听者的朝向是什么，总是能够通过相同的扬声器听到声音。若选中，则听者将独立于路径移动。这意味着当听者转身时将通过不同的扬声器听到声音。  比如可以在听者周围使用自动化路径，在游戏中创建非固定位置的鸟叫声。有一个单点路径位于右前象限中。当听者在游戏中转身时，将发生以下情况：  - Hold Listener Orientation (OFF)：始终通过右前扬声器播放鸟叫声。 - Hold Listener Orientation (ON)：通过不同的扬声器播放鸟叫声。  此选项可用于创建非固定位置的环境声。  此选项只能在游戏中测试，因为 Wwise 设计工具中还没有听者的概念。  Default value: false |
| Hold Emitter Position and Orientation | 若启用，则将存储声音开始播放时游戏对象的瞬时位置和朝向，以及声音播放期间相对该基准位置的偏移。  |  |  | | --- | --- | | [备注] | 备注 | | 对于启用 **Hold Emitter Position and Orientation** 的声音，Wwise Spatial Audio 功能会被禁用。其中包括早期反射处理、Distance Probe、衍射和透射以及 Room 发送。 |  Default value: false |
| Diffraction and Transmission | 衍射和透射。针对声音在 Spatial Audio 中启用衍射和透射处理。  衍射用于模拟声波在障碍物周围发生弯曲的声学现象，透射则用于模拟声波在虚拟环境中穿透障碍物的传播情形。障碍物由通过 API 从游戏传到 Spatial Audio 的 Room、Portal 或几何构造定义。声波在障碍物周围的弯曲取决于衍射设置，声波穿透障碍物的传播情形则取决于透射损失。两者都会影响声音的最终音量和滤波效果。  为了对衍射和透射进行模拟，游戏必须定义上层几何构造或 Room 和 Portal，并将其发送到 Wwise Spatial Audio。  在针对声音启用衍射和透射时，Wwise Spatial Audio 中会发生以下情况：  - 计算发声体和听者之间的声音路径。该路径由一条直达/透射路径和零条或多条衍射路径构成。 - 针对直达/透射路径计算透射损失系数 (0%-100%)。透射损失由声音所穿透的 Room 和几何构造决定。 - 按照声音衰减设置中定义的 **Transmission** 曲线将透射损失系数 (%) 换算为音量/低通/高通滤波器值。声音会相应地被衰减和滤波。 - 根据衍射路径中的角度之和计算衍射系数 (0%-100%)。直线路径视为 0% 衍射，弯曲角度达到或超过 180 度的路径视为 100% 衍射。 - 按照声音衰减设置中定义的 **Diffraction** 曲线将衍射系数 (%) 换算为音量/低通/高通滤波器值。声音会相应地被衰减和滤波。 - 对于衍射路径，通过计算声音相对于听者的视位置创建虚声源位置，让听者感觉声音就像围绕角落或通过 Portal 传播一样。  |  |  | | --- | --- | | [备注] | 备注 | | Game Object 3D Viewer 允许用户查看 Wwise Spatial Audio 内发生了什么，包括上层几何构造、Portal 以及声音的衍射路径和生成的虚声源位置。 |  |  |  | | --- | --- | | [备注] | 备注 | | 为了使 **Diffraction and Transmission** 生效，Wwise Spatial Audio 库必须初始化，而且游戏必须将上层几何构造或 Room 和 Portal 发送到 Wwise Spatial Audio。 |  Default value: false |

**相关主题**

- [“使用 Speaker Panning”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/02-使用-Speaker-Panning/00-使用-Speaker-Panning.md "使用 Speaker Panning")
- [“使用 3D 空间化对象”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/03-使用-3D-空间化对象.md "使用 3D 空间化对象")
- [“应用衰减”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/00-应用衰减.md "应用衰减")
- [“将衰减应用到对象”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/02-将衰减应用到对象.md "将衰减应用到对象")
- [“使用动画路径定义空间定位”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/08-使用动画路径定义空间定位/00-使用动画路径定义空间定位.md "使用动画路径定义空间定位")
- [“创建顺着听者朝向的动画路径”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/08-使用动画路径定义空间定位/00-使用动画路径定义空间定位.md#creating_animation_paths_that_follow_orientation_of_listener "创建顺着听者朝向的动画路径")
- [“将音频信号传送到中置扬声器”一节](../../../../05-使用声音和振动来提升游戏体验/02-定义定位/09-将音频信号传送到中置扬声器.md "将音频信号传送到中置扬声器")

---