# Speaker Panning 和 3D Spatialization 交叉淡变

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [定义定位](00-定义定位.md) > Speaker Panning 和 3D Spatialization 交叉淡变

## Speaker Panning 和 3D Spatialization 交叉淡变

有时，需要同时使用 Speaker Panning（扬声器声像摆位）和 3D Spatialization（3D 空间化）。其中一种典型情况就是，从需要声像摆位的环境过渡到需要空间化的环境。

例如，在玩家在车内收听音乐时，将使用 Direct Assignment（直接指派）来输出声音。在玩家位于车外的城市街道上时，设计师则可能需要使用 3D Spatialization 选项，使其变成开放世界声音。在玩家打开车门走上街道时，还要避免定位方式之间的转换太过突然。这时可通过平滑过渡来消除这种差异。

在 Wwise 内，若未将 3D Spatialization 设为 None（无），则 Speaker Panning / 3D Spatialization Mix 滑杆将变为可用状态。在设为 0 时，不启用 3D Spatialization；在设为 100 时，不启用 Speaker Panning。在设为这两个极限值之间的值时，则会相应地结合两种定位输出。

若要在示例情况下获得所需结果，则可以使用基于距离的 Game Parameter（游戏参数），并针对音乐对象的 Speaker Panning / 3D Spatialization Mix 设置 RTPC。玩家距离汽车越远，滑杆值越小。距离增大时仍可听到汽车音乐，但它会逐渐融入空间化游戏世界音景，而不会像标准立体声音乐一样输出。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 虽然整体影响极小，但仍应注意：在对 Speaker Panning 和 3D Spatialization 进行交叉淡变时，必须同时计算两种定位类型，因此消耗的运行时 CPU 资源也比只选择一种类型时更多一些。 |

---