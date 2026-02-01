# Requirements and best practices for DLC SoundBanks

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [SoundBank 相关技巧和窍门](00-SoundBank-相关技巧和窍门.md) > Requirements and best practices for DLC SoundBanks

### Requirements and best practices for DLC SoundBanks

In order to deliver the desired sound structure in a DLC, it is necessary to understand how different changes and additions affect the release structure. 有一些常见情况需要特别注意，下面将详细介绍。

#### 添加子项

You can add DLC-specific children to various Wwise objects. Depending on which objects you
modify, you must either repackage SoundBanks and include them in the DLC package
or add new SoundBanks to the DLC package. The following table lists the objects
to which you can add DLC-specific children and whether the changes require
repackaging of existing SoundBanks or addition of new SoundBanks.

| 需重新打包 SoundBank 才能将子项添加到 DLC 的对象 | 可使用新增 SoundBank 将子项添加到 DLC 的对象 |
| --- | --- |
| - Random/Sequence Container（随机/序列容器） - Switch Container（切换容器） - Blend Container（混合容器） - Music Switch Container（音乐切换容器） - Music Playlist Container （音乐播放列表容器） - Music Segment （音乐段落） | - Property Container - Folder - Work Unit（工作单元） |

The following example shows a hierarchy before any DLC content is added:

- Work Unit（工作单元）

  - Property Container

    - ContainerA

      - Sound1
      - Sound2

ContainerA is included in SoundBank1 for the base game. For the DLC, you could add a
new container under the Containers hierarchy:

- Work Unit（工作单元）

  - Property Container

    - ContainerA

      - Sound1
      - Sound2

    - ContainerB

      - Sound1
      - Sound2

随后您可以创建一个新的 SoundBank2 并添加 ContainerB ，加载 SoundBank1 和 SoundBank2 时，其中的结构将自动合并。但 DLC 中，不能在 ContainerA 下添加声音，并将其加入新的 SoundBank 中进行打包。To do that, you would have to regenerate SoundBank1 and include it in the DLC. It would replace the base game version.

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| If you plan to release DLC, a good strategy is to separate media from other content (Events, structures, and so on). If the DLC does not change the media SoundBanks, you only need to repackage the other SoundBanks, which minimizes the DLC package sizes. |

#### 修改 Init Bank

For DLC, you must repackage the new version of the `Init.bnk` file in the DLC
if you modify busses, game syncs (Game Parameters, Switches, and States), or
environmental effects.

#### 发布多个 DLC

If you plan to release multiple DLCs in parallel or over time in a series, ensure that you continually update the project
`Init.bnk` to include all busses added for DLCs so that the base game and
any combination of DLCs are supported.

For example, you could release the base game (include `Init.bnk` and
`BaseGame.bnk`), the DLC-A (include the updated `Init.bnk` and
`DLC-A.bnk`), and the DLC-B (include the updated `Init.bnk` and
`DLC-B.bnk`). If the Bus structure is different in the base game,
DLC-A, and DLC-B, then any additional busses in DLC-A must also be included in
DLC-B.

Each of the three builds need to include an `Init.bnk` file that includes all busses in the project at the time of that release.
Users could have any of the following combinations of products:

- 没有 DLC
- 仅有 DLC-A
- 仅有 DLC-B
- 有 DLC-A 和 DLC-B

When users have DLC-A and DLC-B, Wwise loads the `Init.bnk` provided in DLC-B.
Because the `Init.bnk` in DLC-B was built after the project was updated for DLC-A, the busses
required for DLC-A are available.

---