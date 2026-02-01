# Actor Blueprint 函数

|  |
| --- |
| Wwise Unreal Integration Documentation |

Actor Blueprint 函数

这些 Blueprint 函数指向 Actor 的根组件。若 Actor 的根组件没有绑定 [AkComponent](pg_features_objects_components.html#features_akcomponent) ，则将创建一个。

# Post and Wait for End of Event

该 Blueprint 隐藏节点会发送该 Actor 的根组件绑定和控制的 Wwise Event，并在 Event 结束后继续执行流程图的后续节点。

# Post and Wait for End Of Event Async

该 Blueprint 隐藏节点会发送该 Actor 的根组件绑定和控制的 Wwise Event，并在 Event 结束后继续执行流程图的后续节点。异步版本会等到加载媒体之后再发送 Event。

# Post Event

发送给定 Actor 的根组件绑定和控制的 Wwise Event。

# Post Event Async

发送给定 Actor 的根组件绑定和控制的 Wwise Event。异步版本会等到加载媒体之后再发送 Event。

# Execute Action on Event

针对给定 Actor 的根组件绑定和控制的 Event 执行 Action。您可以指定淡变时间和插值曲线类型。另外，还可使用播放 ID（Post Event 蓝图返回的值）来针对特定实例执行 Action。

# Post Trigger

将 Trigger 发送给 Wwise，并指向给定 Actor 的根组件。

# Set Attenuation Scaling Factor

设置衰减比例系数，以便针对游戏对象修改衰减计算结果，从而模拟具有更大或更小传播区域的声音。

# Set Obstruction Occlusion Refresh Interval

Sets the time interval at which the [AkComponent](pg_features_objects_components.html#features_akcomponent) attached to the root component performs obstruction/occlusion calculations. Set to 0 to turn off obstruction/occlusion on the component.

# Set Switch

针对给定 Switch Group 设置活跃 Switch，并指向给定 Actor 的根组件。

# Set Output Bus Volume

设置给定游戏对象的直达声输出总线音量。Bus Volume 的取值范围为 0.0f ~ 1.0f。

# Stop Actor

针对给定 Actor 停止播放所有声音。

# Use Reverb Volumes

设置根组件绑定的 [AkComponent](pg_features_objects_components.html#features_akcomponent) 是否受 [AkReverbVolume](pg_features_objects_actors.html#features_akreverbvolume) 影响。