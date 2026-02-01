# 使用 State

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > 使用 State

## 使用 State

游戏设计师一直面临着一些挑战，那就是利用最少的内存、CPU、素材和磁盘空间创建最动听音频。一种创新而高效的应对方案就是 State（状态）。 使用 State 可以优化声音和音乐素材，允许您为同样的声音灵活创建不同的“Mixing Snapshot”（混音器快照），响应游戏中的变化并改变全局属性。通过改变声音或音乐对象的属性，无需添加新素材就可以创造性地匹配各种游戏情景。在规划工程时，您可以确定 State 在什么时候和什么地方效率最高、最具创意。

## Using States - example

假设您要模拟当角色处于水下时的声音处理。对此时正在播放的声音，可以用 State 来更改 Volume 和 Low-Pass Filter 值。这样的声音变化就可以模仿角色在水下听到的的枪声或手榴弹爆炸声。

下图演示当游戏调用“underwater”State 时将如何影响枪声和手榴弹声对象的音量和低通滤波器属性。

![](../../../images/000027_01e_online.png)

**相关主题**

- [Wwise Fundamentals Module 6: Using States](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=using_states)

---