# 为音乐对象设置 State 切换点

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 State](../00-使用-State.md) > [将 State 指派给对象和总线](00-将-State-指派给对象和总线.md) > 为音乐对象设置 State 切换点

### 为音乐对象设置 State 切换点

在互动音乐中，为 State（状态）指定精确的切换时间点非常有用，这样就可以按照正在播放的音乐节奏，确保过渡平滑。在音乐对象属性级别和总线级别都可以设置切换时间点。在音乐对象或总线的 Property Editor（属性编辑器）中，您可以为每个 State Group（状态组）设置最优的切换时间点。时间点可以是 Immediate（立即）、Next Cue（下个提示点） 或 Next Beat（下一拍）等。不过，当 State 切换涉及多个音乐对象且切换设置各不相同时，State 切换将发生在段落中遇到的下一个时间点。

|  |  |
| --- | --- |
| [备注] | 备注 |
| If an Audio Bus only contains Containers hierarchy sound objects, these settings will be ignored and the changes will occur immediately. If however, both music and sound objects are routed through an Audio Bus, the State change will be based on the State change settings of the music objects. |

**为音乐对象和总线定义 State 切换点的方法如下：**

1. 将音乐对象或总线加载到 Property Editor。
2. Switch to the States tab of the Primary Editor.
3. 对于采用的 State Group，在 **Change occurs at** 列中选择下列之一：

   - **Immediate** —— 立即切换状态。如果音轨设置了 Look-ahead time（预读时间），那么经过预读时间之后 State 才会切换。
   - **Next Grid** —— 在下一网格线处 **切换状态**。网格线允许您按照任意间隔长度来分割音乐对象。
   - **Next Bar** —— 在下一小节**切换状态**。
   - **Next Beat** —— 在下一拍**切换状态**。
   - **Next Cue** —— 在下一提示点处**切换状态**。下一提示点可以是 Entry cue（入口提示点）、Exit cue（出口提示点），也可以是 Custom Cue（自定义提示点）。
   - **Next Custom Cue** —— 在下一自定义提示点处**切换状态**。
   - **Entry Cue** —— 在 Entry cue 处**切换状态**。
   - **Exit Cue** —— 在 Exit cue 处**切换状态**。

   当前 State Group 中的所有 State 切换都将发生在指定时间点。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果多个音乐对象采用了同一个 State Group，State 切换将对所有对象生效。在遇到的下一个时间点，会为所有对象切换 State。 |

---