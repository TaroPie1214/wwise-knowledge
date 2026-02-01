# 对 Ambisonics 进行子混音

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Ambisonics](00-使用-Ambisonics.md) > 对 Ambisonics 进行子混音

### 对 Ambisonics 进行子混音

和其他声道配置一样，Ambisonics 中的声源定位基于混音时游戏对象和听者的位置。因此，Ambisonics 声音对象可采用其他配置进行子混音；但是如果这样做，可能会丢失声音对象的空间信息。例如，如果子混音配置是 7.1，那么当 Ambisonics 音频总线与之混音时，将会失去所有的高度信息。同样，对于 7.1.4 子混音，原先位于听者耳朵下方的对象听起来将位于齐耳高度。因此，建议使用 Ambisonics 配置进行子混音。若空间精度不那么重要，您可以使用较低的阶数。

#### Routing behavior

Wwise 会根据不同配置的输出方式自动将音频转码为 Ambisonics 或从 Ambisonics 转码为其他配置。最终输出取决于所用的不同声道配置和 Spatialization Mode（空间化模式）。根据这些因素，下表提供了路由行为相关的一般信息。

| Routing（信号通路） | 不带 3D Spatialization 的行为 (Direct Speaker Assignment) | 带有 3D Spatialization 的行为 |
| --- | --- | --- |
| 标准配置转换为 Ambisonics | 该信号被编码为 Ambisonics。  单声道信号源将直接编码到 W（全向）声道。  对于多声道声源，每个声道都被视为一个单声道源，入射角度由声道位置决定。例如，对于立体声源，会将其左声道编码为一个单声道源，位于左侧 45 度，右声道同样编码为单声道源，位于右侧 45 度。输入声道角度的详细列表，以度为单位（顺时针）表示：  - L: -45° - R: 45° - C: 0° - SL: -90° - SR: 90° - BL: -135° - BR: 135° - 高度声道的高度角为 +45 度。  使用给定的入射角对声源进行编码非常简单。 | 根据游戏对象相对于听者的位置和朝向，信号将被编码为 Ambisonics。  对于多声道文件，[Spread](../../../14-词汇表.md#glossary_spread "Spread") 和 [Focus](../../../14-词汇表.md#glossary_focus "Focus") 的处理方式跟标准配置完全相同：以虚拟的声源代表各个输入声道，并基于游戏对象、听者、Focus 和 Spread 值将虚声源部署在听者周围，然后进行相应的编码。有关 Spread 和 Focus 的更多详细信息，请参阅 [“定义各种对象属性的衰减曲线”一节](../07-应用衰减/03-定义各种对象属性的衰减曲线.md "定义各种对象属性的衰减曲线") 和 [“3D 定位图解”一节](../06-3D-定位图解/00-3D-定位图解.md "3D 定位图解") 。 |
| Ambisonics 转换为 Ambisonics | 各阶 Ambisonics 之间转换时将直接进行扬声器分配。如果输入的阶数较高，则会丢弃额外的声道。如果输入的阶数较低，则输出的额外通道将保持静音。  |  |  | | --- | --- | | [备注] | 备注 | | Ambisonics 始终忽略 Speaker Panning 模式 Balance-Fade。 | | Ambisonics 音频源的 3D 空间化类似于普通的多声道 3D 空间化。在 [Spread](../../../14-词汇表.md#glossary_spread "Spread") 为 0% 时，Ambisonics 输入会收缩为单声道声音，并定位在“发声体”游戏对象所在位置。在 [Spread](../../../14-词汇表.md#glossary_spread "Spread") 为 100% 且 **Spatialization Mode** 设为 **Position + Orientation** 时，Ambisonics 输入会随着游戏对象和听者的相对朝向旋转。不过，若 **Spatialization Mode** 设为 **Position Only**，则不会旋转。有关 3D 空间化的更多详细信息，请参阅 [“3D 定位图解”一节](../06-3D-定位图解/00-3D-定位图解.md "3D 定位图解") 。  当输入和输出阶数不同时，旋转是按较低阶数计算的，较高阶数将被静音。 |
| Ambisonics 转换为标准配置 | 根据游戏指定的扬声器位置，Ambisonics 信号将被解码为输出配置。有关如何设置扬声器位置的信息，请参阅 [`SetSpeakerAngles()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a7dccf0e26a520d09169fca735daeca80.html) （位于 `AK::SoundEngine`中）。 | 若输出配置为 Ambisonics（如上所述），则 Ambisonics Bed 将会旋转和收缩，不过之后会解码为标准输出配置。 |

  

|  |  |
| --- | --- |
| [注意] | 注意 |
| 若将采用 Direct Speaker Assignment 的单声道音频源编码为 W（全向）声道，而不是将其视为正对前方的音频源，则将导致播放异常。若单声道音频源被输出到 Ambisonics 总线，而该总线又被输出到采用标准配置的总线，则将导致在所有输出声道中播放单声道音频源。这跟 Wwise 中的典型行为不同，通常单声道音频源只会发送到 C 或 L 和 R 声道。 |

---