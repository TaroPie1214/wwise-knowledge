# IAkDeviceEnumerator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Win32](namespace_a_k_1_1_win32.html)
- [IAkDeviceEnumerator](class_a_k_1_1_win32_1_1_i_ak_device_enumerator.html)

[所有成员列表](class_a_k_1_1_win32_1_1_i_ak_device_enumerator-members.html) |
[Public 成员函数](#pub-methods)

AK::Win32::IAkDeviceEnumerator类 参考abstract

Interface to access the IMMDevice cache. This avoids driver accesses.
[更多...](class_a_k_1_1_win32_1_1_i_ak_device_enumerator.html#details)

`#include <AkMMDevice.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [Count](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a9b7278f8a2a09c316f6cd5b81ada4729.html#a9b7278f8a2a09c316f6cd5b81ada4729) ()=0 |
|  | |
| virtual [Device](class_a_k_1_1_win32_1_1_device.html) | [Item](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a6a443d52805294631082cd2665b9c5ce.html#a6a443d52805294631082cd2665b9c5ce) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_idx)=0 |
|  | Returns the number of devices. This function can block. [更多...](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a6a443d52805294631082cd2665b9c5ce.html#a6a443d52805294631082cd2665b9c5ce) |
|  | |
| virtual void | [Lock](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a146f625398ae22a3537b46d2a483ba49.html#a146f625398ae22a3537b46d2a483ba49) ()=0 |
|  | Gets item in\_idx from the cache. Must be smaller than [Count()](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a9b7278f8a2a09c316f6cd5b81ada4729.html#a9b7278f8a2a09c316f6cd5b81ada4729). This function can block. [更多...](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a146f625398ae22a3537b46d2a483ba49.html#a146f625398ae22a3537b46d2a483ba49) |
|  | |
| virtual void | [Unlock](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_ab3a1ff037874797d19317cbc721b4b54.html#ab3a1ff037874797d19317cbc721b4b54) ()=0 |
|  | For thread safety. If you iterate through all the devices, lock the enumerator to avoid changes. However, if only accessing one single item, [Item()](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a6a443d52805294631082cd2665b9c5ce.html#a6a443d52805294631082cd2665b9c5ce "Returns the number of devices. This function can block.") is thread safe in itself. [更多...](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_ab3a1ff037874797d19317cbc721b4b54.html#ab3a1ff037874797d19317cbc721b4b54) |
|  | |
| virtual [Device](class_a_k_1_1_win32_1_1_device.html) | [FindDevice](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_aa032b287d13fa630155d686c01c2f82e.html#aa032b287d13fa630155d686c01c2f82e) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_id)=0 |
|  | For thread safety. See [Lock()](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_a146f625398ae22a3537b46d2a483ba49.html#a146f625398ae22a3537b46d2a483ba49) [更多...](class_a_k_1_1_win32_1_1_i_ak_device_enumerator_aa032b287d13fa630155d686c01c2f82e.html#aa032b287d13fa630155d686c01c2f82e) |
|  | |

## 详细描述

Interface to access the IMMDevice cache. This avoids driver accesses.

在文件 [AkMMDevice.h](_ak_m_m_device_8h_source.html) 第 [477](_ak_m_m_device_8h_source.html#l00477) 行定义.