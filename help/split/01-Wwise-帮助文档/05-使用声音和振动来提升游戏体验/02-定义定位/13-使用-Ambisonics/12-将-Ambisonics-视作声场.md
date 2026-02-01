# 将 Ambisonics 视作声场

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Ambisonics](00-使用-Ambisonics.md) > 将 Ambisonics 视作声场

### 将 Ambisonics 视作声场

Ambionics 声音（无论录制还是合成）特别适合实现环境声。虽然在游戏中通常以高阶 Ambionics 作为空间音频的中间表示形式，但对环境声来说一般低阶 Ambionics 就已足够。

在被视作声场并结合使用 3D Spatialization（3D 空间化）时，倘若 Spread（散布）保留设为默认值 0%，Ambisonics 会像其他多声道格式一样收缩成单声道点声源。为了确保被声场完全环绕，必须向声音对象添加相应的 Attenuation ShareSet（衰减共享集），以此将 Spread 值设为 100%。

如[《为动态环境声使用 Ambisonics》](https://blog.audiokinetic.com/using-ambisonics-for-dynamic-ambiences/)中所述，在将 Spread 设为 100% 并将 3D Spatialization 设为 **Position + Orientation**（位置 + 朝向）时，Ambisonics 声音将依据“发声体”和“听者”游戏对象的相对朝向进行旋转，给人一种声场与周边环境互动的感觉。

Ambisonics 代表传向听者的波前，所以构成声场的声源总是在远处。倘若使用其来表示声场的平移，听起来会比较奇怪。不过，我们可以借助 Spread 来模拟进出声场时的声音效果。事实上，只需将 Spread 降至 100% 以下便可实现沿“发声体”游戏对象所在方位收缩声场的效果。对此，“[“Spread 的影响”一节](../06-3D-定位图解/01-Spread-的影响.md "Spread 的影响")”中进行了阐释。Wwise Spatial Audio Room 正是通过这种方式处理房间底噪和混响的（参见[房间底噪](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_roomsportals_apioverview.html#spatial_audio_roomsportals_roomtones)）：

- 在听者位于 Room（房间）之内时，Spread 接近于 100%；房间底噪和混响总线在声场旋转时与 Room 朝向绑定。
- 在听者位于 Room 之外时，Room 游戏对象设在最近的 Portal（门户）上；此时，Spread 会降至 50% 以下（具体取决于 Portal 的开口大小）。声场会沿 Portal 方位收缩，并依据 Room 的朝向旋转。随着听者逐渐远离，声场会慢慢地在 Portal 所在位置收缩为点声源。

---