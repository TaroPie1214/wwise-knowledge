# SidechainMix

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

SidechainMix

- **Plugin ID**: 86
- **Class ID**: 5636112

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# Properties, References, Lists

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **Inclusion** | Inclusion | bool | true | None | true | None | true |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **SidechainMixChannelConfig** | Sidechain Mix Configuration | int32 | 16641 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 3584 | Same as primary main mix | | 3840 | Same as primary passthrough mix | | 16641 | 1.0 | | 12546 | 2.0 | | 45315 | 2.1 | | 28931 | 3.0 | | 6304004 | 4.0 | | 6353158 | 5.1 | | 6549768 | 7.1 | | 90239240 | 5.1.2 | | 761327882 | 5.1.4 | | 90435850 | 7.1.2 | | 761524492 | 7.1.4 | | 516 | Ambisonics 1st order | | 521 | Ambisonics 2nd order | | 528 | Ambisonics 3rd order | | 537 | Ambisonics 4th order | | 548 | Ambisonics 5th order | | 769716491 | Auro 10.1 | | 803270924 | Auro 11.1 | | 803467534 | Auro 13.1 | | 33025 | LFE | | true | None | true |