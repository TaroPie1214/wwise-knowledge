# 使用 Speaker Panning

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > 使用 Speaker Panning

## 使用 Speaker Panning

在经过扬声器声像摆位后，可将声音用于游戏中的各种对象，如菜单声音和角色语音。The Speaker Panning mode is defined for a sound or music object in the Positioning category of the Property Editor. 可用模式有三种，其各自功能如下：

- **Direct Assignment**（直接指派）：此项为默认模式。对象的源音频会根据需要进行[下混](../../../07-完善工程/01-管理输出/12-下混行为/00-下混行为.md "下混行为")，以确保与对象的 Output Bus（输出总线）的声道配置保持一致，继而直接指派给对应的声道。若源音频包含的声道少于 Output Bus，则不对内容进行上混；源音频中缺少的声道在 Output Bus 中保持静音。Speaker Panner 不可用。
- **Balance-Fade**（平衡-淡变）：对象的源音频会根据需要进行上混或[下混](../../../07-完善工程/01-管理输出/12-下混行为/00-下混行为.md "下混行为")，以确保与对象的 Output Bus 的声道配置保持一致。在这种情况下，Speaker Panner 允许通过移动 2D 平面内的控制点来调节各个声道的音量。有关更多详细信息及相关示例，请参阅[“Balance-Fade Speaker Panning 图解”一节](01-Balance-Fade-Speaker-Panning-图解.md "Balance-Fade Speaker Panning 图解")章节。
- **Steering**（转向）：对象的源音频会根据需要进行下混，以确保与对象的 Output Bus 的声道配置保持一致。在这种情况下，Speaker Panner 允许在 Output Bus 的各个声道（包括可能存在的高度声道）之间重新分配源音频的内容。若源音频包含的声道少于 Output Bus，则不对内容进行上混；除非使用 Speaker Panner 在这些声道之间重新分配音频内容，否则源音频中缺少的声道在 Output Bus 中保持静音。有关更多详细信息及相关示例，请参阅[“Steering Speaker Panning 图解”一节](02-Steering-Speaker-Panning-图解.md "Steering Speaker Panning 图解")章节。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Speaker Panner 不会对 Ambisonics 声音产生影响。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 无论在上述哪一模式下，扬声器声像摆位本身都不会考虑听者或发声体的位置或朝向。有关如何启用此类考量因素的详细信息，请参阅[“使用 3D 空间化对象”一节](../03-使用-3D-空间化对象.md "使用 3D 空间化对象")章节。 |

### 使用 Speaker Panner

**调节经过声像摆位的对象的声道：**

1. 将顶层对象加载到 Property Editor 中。
2. Switch to the Positioning category.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果该对象不是顶层对象，您则必须选择 **Override parent**选项后才能设置 Positioning 选项。 |
3. 从 Speaker Panning（扬声器声像摆位）列表选择 **Balance-Fade**（平衡-淡变）或 **Steering**（转向）选项。

   此时，**Edit...** 按钮将变为启用状态。
4. 单击 **Edit...**（编辑...），打开 Speaker Panner（扬声器声像摆位器）。
5. 将控制点拖到 2D 平面内的任意位置。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | You can specify exact values using the X, Y, and Z coordinate text boxes. |

   在 Balance-Fade 模式下，会根据所指定位置来调节各个声道的音量。在 Steering 模式下，会根据所指定位置重新分配声音内容。

   |  |  |
   | --- | --- |
   | [注意] | 注意 |
   | In Balance-Fade mode, the Z coordinate only applies to 7.1.4 sounds or busses routed to a 7.1.4 bus. Otherwise, no upmixing occurs towards the height speakers. |

### Using the center speaker

有些声音（如角色语音）对玩法来说至关重要。为了确保其能够被清晰听到，最好将其信号输出到中置扬声器。The **Center %** control in the Property Editor allows you to define the proportion of the signal that will pass through the center speaker. 有关如何使用 Center % 控件的详细信息，请参阅[“将音频信号传送到中置扬声器”一节](../09-将音频信号传送到中置扬声器.md "将音频信号传送到中置扬声器")章节。

### Attenuation（衰减）

除声像摆位外，还可定义对象的衰减设置。衰减设置用于模拟信号源远离听者时的自然减弱。Wwise 使用一系列曲线来把游戏中的距离值映射到 Wwise 的属性利用这些曲线，可为对象创建基于距离的复杂衰减。为了增加逼真效果，还可使用声锥。声锥根据对象相对于听者的朝向来衰减声音。对于经过摆位的对象，有关如何定义其衰减设置的详细信息，请参阅“[“应用衰减”一节](../07-应用衰减/00-应用衰减.md "应用衰减")”。

### 振动对象的声像摆位

对于较为简单的振动设备（如游戏控制器），其内部电机无法模拟 3D 环境，因此应将 Speaker Panning 设置为 Direct Assignment。不过，在有些情况下可能需要根据声源的距离来降低振动信号的强度。对此，为了在非 3D 环境下使用衰减设置，可启用 **Listener Relative Routing**（听者相对通路）并将 **3D Spatialization**（3D 空间化）设为 **None**（无）。

**相关主题**

- [Wwise Fundamentals Module 10: Using Speaker Panning](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=using_2d_panning)

---