# HDR category: Containers hierarchy objects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > HDR category: Containers hierarchy objects

#### HDR category: Containers hierarchy objects

You can adjust the properties in the HDR category for an object to further define
the behavior of the sound in the HDR system.

HDR 系统对所有声音执行离线分析，并抽取包络。这些信息用于与总线和声音 HDR 设置一起驱动 HDR 动力学。

有关详细信息，请参阅[“理解 HDR”一节](../../../../07-完善工程/01-管理输出/08-理解-HDR.md "理解 HDR")。

| H DR | |
| --- | --- |
| 界面元素 | 描述 |
| **Envelope Tracking** | |
| Override parent | 不沿用父项。确定 HDR 包络跟踪是从父项继承还是在层级结构的当前层级定义。当不选择此选项时，包络跟踪控件将不可用。  对于顶层对象，此选项将不可用。  Default value: false |
| Enable Envelope | 启用包络。启用时，HDR 窗口遵循最响声音的分析包络（如果高于阈值）。它还用于确定声音是否位于其活跃范围内（请参阅下文的 Active Range 属性）。  禁用时，计算窗口顶部不考虑声音的包络。  有关详细信息，请参阅 [使用振幅包络](../../../../07-完善工程/01-管理输出/09-使用-HDR/02-使用振幅包络.md "使用振幅包络") 。  Default value: false |
| HDR Envelope Sensitivity | 敏感度。定义算法中采用的包络灵敏度，用于减少包络中的点数。  - 两个端点之间始终保留一个点。 - 在设为 0 时，将不保留其他点。 - 在设为 100 时，将保留所有点。  在手动编辑包络前一直使用灵敏度。  有关详细信息，请参阅 [包络灵敏度和手动编辑](../../../../07-完善工程/01-管理输出/09-使用-HDR/02-使用振幅包络.md#envelope_sensitivity_and_manual_editing "Envelope Sensitivity 和手动编辑") 。  单位：%  Default value: 20  Range: 0 to 100 |
| Active Range | 活跃范围。根据声音的峰值为各个声部定义 HDR 动态处理激活的值域，单位：分贝。活跃范围根据声音的分析包络定义声音中的兴趣区：只要当前包络电平大于“峰值电平”与“活跃电平”之差，则为“活跃”。当不活跃时，HDR 动态处理不考虑声音的内容。当活跃范围为 0 时，声音对 HDR 窗口的位置无影响。  有关详细信息，请参阅 [有效区域：活跃范围](../../../../07-完善工程/01-管理输出/09-使用-HDR/02-使用振幅包络.md#region_of_interest_active_range "相关区域：Active Range") 。  单位：dB  Default value: 12  Range: 0 to 96 |

---