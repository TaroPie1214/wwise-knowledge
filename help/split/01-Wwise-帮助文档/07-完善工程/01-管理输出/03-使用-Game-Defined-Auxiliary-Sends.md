# 使用 Game-Defined Auxiliary Sends

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理输出](00-管理输出.md) > 使用 Game-Defined Auxiliary Sends

## 使用 Game-Defined Auxiliary Sends

除了 4 个用户定义的辅助发送外，最多还可以设置 4 个游戏定义的辅助发送。在游戏中使用以下 Wwise SDK 函数，即可控制游戏定义的辅助发送：

- [`AK::SoundEngine::SetGameObjectAuxSendValues()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af960fca0239e219b9d08c2659fe9e5d4.html)

  使用该函数可以针对特定游戏对象来定义输出至辅助总线的发送音量。通常也被称为湿声音量。
- [`AK::SoundEngine::SetGameObjectOutputBusVolume()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_adf1401ce64872af26cdff05b36e98161.html)

  使用该函数可以定义输出总线音量。通常也被称为干声音量。

但要启用某个对象的游戏定义辅助发送功能，必须激活 **Use game-defined auxiliary sends** 选项。

**启用游戏定义的辅助发送**

1. 在 Project Explorer 中双击某个对象可察看该对象
2. In the Property Editor, in the group **Game-defined Auxiliary
   Sends**:
3. - 如果允许，则点击 **Override parent**。
   - 点击 **Use game-defined auxiliary sends。**

通过为特定对象启用游戏定义的辅助发送，您可以控制哪个对象将会受其影响。在使用游戏定义的辅助发送来控制环境效果的场景中，您将能够控制哪个对象受环境效果的影响，哪个对象不受影响。

当游戏定义的辅助发送被激活时，您可以直接在 Wwise 中更改游戏定义的辅助发送音量，从而对游戏发送音量值（该值将与游戏定义的值叠加）进行调整。

### 结合使用 Game-Defined Auxiliary Sends 和 Attenuation

游戏定义的辅助发送可以与对象定位属性中所定义的衰减设置结合使用。衰减设置用来根据听者与游戏对象之间的距离来控制以下游戏定义的属性：

- **Game-defined send volume**：用来基于距离来控制衰减多少湿声信号。
- **Output bus volume**：用来基于距离来控制衰减多少干声信号。

---