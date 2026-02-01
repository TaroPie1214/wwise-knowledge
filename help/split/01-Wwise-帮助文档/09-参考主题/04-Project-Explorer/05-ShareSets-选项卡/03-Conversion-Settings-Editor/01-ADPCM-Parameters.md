# ADPCM Parameters

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [ShareSets 选项卡](../00-ShareSets-选项卡.md) > [Conversion Settings Editor](00-Conversion-Settings-Editor.md) > ADPCM Parameters

#### ADPCM Parameters

In the ADCPM Parameters dialog you can set the Loop fix parameter of the ADPCM codec. Platinum Games Inc. 贴心地向 Audiokinetic 提供了其在 Wwise 中使用的 ADPCM 编码器和解码器。

| 界面元素 | 描述 |
| --- | --- |
| ADPCM Encoding Parameters（ADPCM 编码参数） | |
| Loop fix | 循环播放修复。当循环标记不在数据块边界采样点上时，将其对齐的方法列表。  - **Pitch Shifting**：根据平台升高或降低音高来保证文件转换时能对齐样本边界。 - **Interpolation/Elimination** —: 根据平台添加或删除样本来保证文件转换时能对齐样本边界。 |
|  | Closes the ADPCM Parameters dialog and saves your settings. |
|  | Closes the ADPCM Parameters dialog without saving your settings. |

---