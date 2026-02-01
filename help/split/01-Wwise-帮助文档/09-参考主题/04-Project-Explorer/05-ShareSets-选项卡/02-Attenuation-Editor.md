# Attenuation Editor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [ShareSets 选项卡](00-ShareSets-选项卡.md) > Attenuation Editor

### Attenuation Editor

Attenuation Editor（衰减编辑器）允许定义特定对象的衰减属性。通过创建一系列曲线来定义特定 Wwise 属性（如 Volume 和 Low-Pass Filter）和特定驱动因素（如声源和听者之间的距离或声障）之间的关系，可模拟游戏中声音、音乐和振动的复杂衰减行为。您可以利用声锥对衰减实施进一步的微调，来基于发声体相对于听者的朝向模拟衰减。

您可通过定义每条曲线段的形状来创建详细、复杂的衰减曲线。曲线段是两个控制点之间的部分。您可选择各种曲线形状，包括线性曲线、恒定曲线、对数曲线、幂数曲线和 S 曲线。

这些衰减设置也可另存为共享集，这意味着您可在工程中的多个对象之间共享这些设置。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 衰减值总是加到相关对象的现有属性值上。因此，如果声音或者音乐的层级结构具有 -20 dB 的累积音量电平，然后将音量衰减 -64 dB，则对象的音量为 -84 dB。 |

一些衰减属性可使用 RTPC 进行控制。要了解 RTPC 属性的说明，请切换至 [“RTPC tab”一节](../01-Audio-tab/05-Common-tabs-and-categories-audio-structures/02-RTPC-tab/00-RTPC-tab.md "RTPC tab") 并点击 Help 图标。要了解有关如何应用 RTPC 的更多信息，请参阅[*使用 RTPC*](../../../04-与游戏互动/05-使用-RTPC/00-使用-RTPC.md "使用 RTPC")/>。

| 界面元素 | 描述 |
| --- | --- |
| Name | 衰减共享集的名称。 |
| Shared by | 共享对象。当前采用所选共享集的对象列表。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Notes | 有关已应用的共享集或衰减设置的额外信息。 |
| **Attenuation Settings（衰减设置）** | |
| 坐标图视图 | 以图形形式显示特定 Wwise 属性（如 Volume 和 Low-Pass Filter）和不同驱动因素（如距离和声障）之间的关系。所有这些曲线合起来基于距离、声障、声笼、衍射和透射模拟游戏内声音、音乐和振动对象的衰减。  对于由距离驱动的曲线，X 轴表示距离。其最小值为 0，最大值由当前 Max distance 值决定。对于由声障、声笼、衍射和透射驱动的曲线，X 轴表示百分比。Y 轴值取决于在 Curves 列表中选择的属性曲线。  坐标图视图中的两个默认控制点表示半径中心和最大距离的值。  半径中心无法删除或沿 X 轴移动，因为它由游戏对象（3D 游戏定义）或听者位置（3D 自动化）定义。您可以添加额外的点来修改衰减曲线的形状。  在播放过程中，可通过拖动 Distance、Obstruction、Occlusion、Diffraction 和 Transmission 光标来预览衰减曲线所产生的效果。  坐标图视图可同时显示多条曲线。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
|  | Show Game Object values in the curve graph when capturing. |
| **坐标** | |
| X | 所选控制点的 X 轴坐标。X 轴的值可能因 Curves 列表中所选的曲线而异。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 X 文本框中输入 -5，则两个控制点都将向左移动 5 个单位。 |
| Y | 所选控制点的 Y 轴坐标。根据在 Curves 列表中所选的曲线，Y 轴值可能不同。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 Y 文本框中输入 -5，则两个控制点都将向下移动 5 个单位。 |
| **曲线** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| (固定/取消固定) | 确定是否在坐标图视图中显示衰减曲线。  当选择了 Pin 图标时，无论是否选择曲线，坐标图视图中都将显示衰减曲线。 |
| |  | | --- | |  |  （颜色块） | 在坐标图视图中显示衰减曲线的颜色。每条属性曲线分配有不同的颜色。 |
| |  | | --- | |  |  (Link/Unlink) | 显示曲线是否作用于所有平台。 |
| 属性 | 应用了衰减的 Wwise 属性。Properties are categorized by their driver.  Drivers are displayed along the X axis in the graph view. 您可以为以下驱动因素创建衰减曲线：  - **Distance**（距离）：发声体和听者之间的距离。其最大值由 Max distance 滑杆决定。 - **Obstruction**（声障）：“发声体”游戏对象和听者之间的声障百分比。它的值介于 0 ~ 100 之间。 - **Occlusion**（声笼）：“发声体”游戏对象和听者之间的声笼百分比。它的值介于 0 ~ 100 之间。 - **Diffraction**（衍射）：发声体和听者之间的衍射路径的衍射百分比。该值由 Spatial Audio 设定，其大小介于 0 ~ 100 之间。 - **Transmission**（透射）：发声体和听者之间的透射路径的透射损失百分比。该值由 Spatial Audio 设定，其大小介于 0 ~ 100 之间。  Properties are displayed along the Y axis in the graph view. 您可为以下 Wwise 属性创建衰减曲线：  - **Volume**（音量）：对声音的音量施加偏置。对应于湿声/干声中的干声部分。 - **Auxiliary Send Volume** —— 辅助发送音量。偏置游戏定义和用户定义的辅助发送音量。对应于湿声/干声场景中的湿声部分。 - **Low-pass filter** —— 根据指定值来衰减高频的递归滤波器。 - **High-pass filter** —— 高通滤波器。根据指定值来衰减低频的递归滤波器。 - **Dual-shelf filter** - The recursive filter that attenuates high frequencies based on a specified gain. - **Spread** —— 散布。扩散到附近扬声器的音频量或百分比，以使声音能够随着距离的增加从低扩散的点声源变为完全扩散的传播源。对于多声道声音，各个声道单独扩散。 - **Focus** —— 聚焦。百分比值，用于收缩由扩散值生成的虚拟发声体。对于 0% 焦点，虚发声体保持不变，但值越高，各个虚拟点距离源声道原始位置越近。  |  |  | | --- | --- | | [备注] | 备注 | | Obstruction、Occlusion、Diffraction 和 Transmission 驱动因素仅可与 Volume、Low-pass filter 和 High-pass filter 属性关联。  Auxiliary send volumes、Spread 和 Focus 属性仅可与 Distance 驱动因素关联。 | |
| Curve | 指定将用于各个属性的衰减曲线。您可选择以下任一选项：  - **None**（无）：不创建衰减曲线，**不**基于关联驱动因素对相应属性应用衰减。不过，若属性包含在其他曲线中，则仍有可能对其应用衰减。 - **Use Distance Volume**（使用距离音量）：使用 Distance Volume 衰减曲线。此选项仅适用于 Distance Auxiliary send volumes 曲线。 - **Use Project Obstruction**（使用工程声障）：使用相同属性的工程 Obstruction 曲线。This option is only available for curves driven by Obstruction. - **Use Project Occlusion**（使用工程声笼）：使用相同属性的工程 Occlusion 曲线。This option is only available for curves driven by Occlusion. - **Use Project Diffraction** - The Project's Diffraction curve of the same property is used. This option is only available for curves driven by Diffraction. - **Use Project Transmission** - The Project's Transmission curve of the same property is used. This option is only available for curves driven by Transmission. - **Custom**（自定义）：为对应驱动因素属性对创建自定义衰减曲线。  请记住，您创建的每条新曲线都需要额外的运算资源。 |
| Max distance | 最大距离。对象的信号达到其最低电平时与声源的距离。此距离仅用于由距离驱动的曲线，由坐标图中最后一个控制点表示。在此控制点之后，对象信号的衰减保持不变。  声音和振动的传播各向均匀的，因此最大距离值围绕发射源呈现球面形状。  默认值：100 默认滑杆范围：1 至 200 输入范围：1 至 10,000,000,000 单位：Wwise 距离单位  Wwise 距离单位将与您在游戏中使用的距离单位（例如厘米、米等）相匹配。 |
| **Objects using this Attenuation** | |
|  | Refresh the list of objects using this Attenuation. |
|  | Select this icon to scale the curve graph to the scaled max distance of the object. If **Show Game Object Values** is enabled, all game objects with the same effective max distance will be shown in the curve graph. Icon is grayed out if the object is not using this Attenuation. |
| Name | The name of the object using the current attenuation. Clicking on this opens the object in a new tab. |
| Distance Scaling % | 默认值：100 取值范围：1 ~ 10000  距离缩放 %。按比例对此对象上应用的最大衰减距离进行调节。您可以在此属性上添加 RTPC 来在运行时按比例调节声音的最大衰减距离。  Default value: 1  Range: 0.01 to 100 |
| Effective Max Distance | The effective max distance value using the object's distance scaling percentage. |
| **Properties** | |
| Height Spread | 高度散布。若在 2D 配置下实施声像摆位，则 Height Spread 根据高度角自动计算最小散布值；若在 7.1.4 之类的 3D 配置（半球空间）下实施声像摆位，则直接根据负高度角计算最小散布值。藉此，可帮助实现 3D 声音从听者上方或下方掠过时声像摆位的平滑过渡。  在默认情况下，始终启用 Height Spread，即便声音没有衰减。只能通过取消选中 Height Spread 来禁用该属性。若想在声音没有衰减的情况下禁用 Height Spread，须专门为此创建 Attenuation ShareSet，并设置恒定不变的 Output Bus Volume。  有关详细信息，请参阅 [Height Spread 的效果](../../../05-使用声音和振动来提升游戏体验/02-定义定位/06-3D-定位图解/05-Height-Spread-的效果.md "Height Spread 的效果") 页面。  Default value: true |
| Cone Use | 声锥衰减。创建使用一系列具有不同角度的锥形来控制衰减的声锥。锥形边界的方向最终由游戏对象的朝向控制。  声锥衰减值会加到基于距离的衰减值上。  Default value: false |
| Cone max attenuation | 最大衰减。当发射源位于过渡区以外时的音量衰减量。  Cone max attenuation 设有链接标志和 RTPC 标志。有关详细信息，请参阅 [使用 Property Editor](../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md "使用 Property Editor") 页面。  单位：dB  Default value: -6.0  Range: -200 to 0  Units: dB |
| Cone inner angle | 内角。该角度用于定义不发生衰减的区域。  Cone inner angle 定义 Cone Preview 的顶部边界。在修改值时实时重新绘制。  内角和外角之间的区域称为过渡区。该区域内的音量衰减在零衰减和 Cone max attenuation 值之间以线性方式做插值处理。  单位：°  Default value: 90  Range: 0 to 360 |
| Cone outer angle | 外角。该角用于定义音量、低通滤波器、扩散和焦点衰减保持其最大电平的区域。  Cone outer angle 定义 Cone Preview 的底部边界。在修改值时实时重新绘制。  内角和外角之间的区域称为过渡区。该区域内的音量衰减在零衰减和 Cone max attenuation 值之间以线性方式做插值处理。  单位：°  Default value: 245  Range: 0 to 360 |
| Cone Low-pass filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位代表将要应用的低通滤波百分比。其中，0 表示无低通滤波（信号不受影响），100 表示最大衰减。  Cone Low-pass filter 设有链接标志和 RTPC 标志。有关详细信息，请参阅 [使用 Property Editor](../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md "使用 Property Editor") 页面。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Cone High-pass filter | 声部高通滤波器。基于指定频率针对低频进行衰减的递归滤波器。  此滤波器的单位代表将要应用的高通滤波百分比。其中，0 表示无高通滤波（信号不受影响），100 表示最大衰减。  Cone High-pass filter 设有链接标志和 RTPC 标志。有关详细信息，请参阅 [使用 Property Editor](../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md "使用 Property Editor") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| **Cone Preview** | |
| |  | | --- | |  | | 衰减预览。声音最大半径衰减的图形表示，其中声音源直接位于圆圈的中心。  **该工具不是声像摆位器，因此移动红色圆圈不会将声音放置在环绕声场中。该工具仅可用于预览衰减设置。**  Cone Preview 具有以下两项功能：  - 显示声锥衰减的不同区域。当修改内角值和外角值时，声锥的不同区域会实时更新。 - 您可通过在播放过程中修改听者的位置来预览声音的衰减。听者的位置由它与声音源之间的角度（黑线）和距离（红圈）确定。您可以通过在 Cone Preview 窗口中直接单击/拖动来调节距离和角度。  Cone Preview 仅适用于使用听者位置的对象。 |

**相关主题**

- [“定义各种对象属性的衰减曲线”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/03-定义各种对象属性的衰减曲线.md "定义各种对象属性的衰减曲线")
- [“使用锥形边界模拟方向性”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/04-使用锥形边界模拟方向性.md "使用锥形边界模拟方向性")
- [“预览声音的衰减设置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/05-预览声音的衰减设置.md "预览声音的衰减设置")
- [“管理多份衰减”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/01-管理多份衰减.md "管理多份衰减")
- [“将音频信号传送到中置扬声器”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/09-将音频信号传送到中置扬声器.md "将音频信号传送到中置扬声器")
- [“更改坐标图的显示内容”一节](../../../08-使用-Wwise/07-了解坐标图视图/01-更改坐标图的显示内容.md "更改坐标图的显示内容")
- [“添加控制点”一节](../../../08-使用-Wwise/07-了解坐标图视图/02-在坐标图中使用控制点.md#adding_control_points "添加控制点")
- [“指定控制点之间曲线的形状”一节](../../../08-使用-Wwise/07-了解坐标图视图/03-在坐标图中使用曲线.md#specifying_shape_of_curve_between_control_points "指定控制点之间曲线的形状")
- [“定义坐标图的坐标显示方式”一节](../../../08-使用-Wwise/07-了解坐标图视图/01-更改坐标图的显示内容.md#defining_scaling_method_of_graph_view "定义坐标图的坐标显示方式")
- [“Creating Game Parameters”一节](../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")
- [“将 Wwise 属性指派给游戏参数”一节](../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/01-将-Wwise-属性指派给游戏参数.md "将 Wwise 属性指派给游戏参数")
- [“映射 RTPC 坐标图中的值”一节](../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/02-映射-RTPC-坐标图中的值.md "映射 RTPC 坐标图中的值")

---