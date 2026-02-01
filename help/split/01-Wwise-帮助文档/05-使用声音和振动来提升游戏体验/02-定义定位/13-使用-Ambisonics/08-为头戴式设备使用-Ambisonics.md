# 为头戴式设备使用 Ambisonics

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Ambisonics](00-使用-Ambisonics.md) > 为头戴式设备使用 Ambisonics

### 为头戴式设备使用 Ambisonics

要想确保针对头戴式设备 (HMD) 旋转以 Ambisonics 形式表示的声音，游戏引擎必须将 HMD 头部追踪数据作为听者朝向通过 SetListenerPosition() API 不断传给 Wwise。定位被设为 3D 的声音会与游戏对象绑定。当这些声音在 Ambisonics 总线中混音时，角度的编码取决于游戏对象相对于听者朝向的位置。因此，Ambisonics 下混是由相对于 HMD 作了旋转的声源构成的。

另外，还可结合 B-format 声源使用 3D Spatialization（3D 空间化）。在这种情况下，其将被视作声场并依据游戏对象和听者之间的相对朝向旋转（参见[“将 Ambisonics 视作声场”一节](12-将-Ambisonics-视作声场.md "将 Ambisonics 视作声场")）。

---