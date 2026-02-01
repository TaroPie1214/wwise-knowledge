# DeviceCollection

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Win32](namespace_a_k_1_1_win32.html)
- [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html)

[所有成员列表](class_a_k_1_1_win32_1_1_device_collection-members.html) |
[类](#nested-classes) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK::Win32::DeviceCollection类 参考

`#include <AkMMDevice.h>`

|  |  |
| --- | --- |
| 类 | |
| class | [Iterator](class_a_k_1_1_win32_1_1_device_collection_1_1_iterator.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection_ac4d27a3986d242ec5bbf9190202012c9.html#ac4d27a3986d242ec5bbf9190202012c9) (IMMDeviceEnumerator \*pEnumerator) |
|  | |
|  | [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection_ae551c2881198f73829bd72544f428447.html#ae551c2881198f73829bd72544f428447) (IMMDeviceEnumerator \*pEnumerator, EDataFlow eFlow, DWORD dwStateMask) |
|  | |
|  | [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection_aa66af1508b09b62c5dd35a5f3a97ab58.html#aa66af1508b09b62c5dd35a5f3a97ab58) ([DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html) &&other) |
|  | |
|  | [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection_a9d40739ac963381a13ab3cb063a7c3cb.html#a9d40739ac963381a13ab3cb063a7c3cb) (const [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html) &other)=delete |
|  | |
|  | [~DeviceCollection](class_a_k_1_1_win32_1_1_device_collection_a9c39eb8e343d630c55729e6c5481d07e.html#a9c39eb8e343d630c55729e6c5481d07e) () |
|  | |
| [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html) & | [operator=](class_a_k_1_1_win32_1_1_device_collection_a452892e20e52939a2d400bdfb2c3dee3.html#a452892e20e52939a2d400bdfb2c3dee3) ([DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html) &&other) |
|  | |
| [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html) & | [operator=](class_a_k_1_1_win32_1_1_device_collection_a4dd02d2470e3a3ba6a7a8043f5a5c61b.html#a4dd02d2470e3a3ba6a7a8043f5a5c61b) (const [DeviceCollection](class_a_k_1_1_win32_1_1_device_collection.html) &other)=delete |
|  | |
| bool | [IsValid](class_a_k_1_1_win32_1_1_device_collection_aec4da12bb86218db5da1f3dce4316835.html#aec4da12bb86218db5da1f3dce4316835) () const |
|  | |
| UINT | [Count](class_a_k_1_1_win32_1_1_device_collection_a88df3b0e59b4fa23f38f88fca4b49ad7.html#a88df3b0e59b4fa23f38f88fca4b49ad7) () const |
|  | |
| [Iterator](class_a_k_1_1_win32_1_1_device_collection_1_1_iterator.html) | [Begin](class_a_k_1_1_win32_1_1_device_collection_aef550a912bbcbd3a7e41f0b443fb8744.html#aef550a912bbcbd3a7e41f0b443fb8744) () |
|  | |
| [Iterator](class_a_k_1_1_win32_1_1_device_collection_1_1_iterator.html) | [End](class_a_k_1_1_win32_1_1_device_collection_aced4eaf47e93a62cc2b9beffa1ac98c6.html#aced4eaf47e93a62cc2b9beffa1ac98c6) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| interface IMMDeviceCollection \* | [pDevices](class_a_k_1_1_win32_1_1_device_collection_aa0b6c011e61023b7d5eb67bb6b8912d9.html#aa0b6c011e61023b7d5eb67bb6b8912d9) |
|  | |
| UINT | [uCount](class_a_k_1_1_win32_1_1_device_collection_a4d4618564dc53a5bf2ae7d8c107941bb.html#a4d4618564dc53a5bf2ae7d8c107941bb) |
|  | |

## 详细描述

在文件 [AkMMDevice.h](_ak_m_m_device_8h_source.html) 第 [271](_ak_m_m_device_8h_source.html#l00271) 行定义.