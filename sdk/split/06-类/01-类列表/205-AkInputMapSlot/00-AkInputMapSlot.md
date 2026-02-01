# AkInputMapSlot

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_input_map_slot-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkInputMapSlot< KEY, USER\_DATA > 模板结构体 参考

Structure of an entry in the [AkMixerInputMap](class_ak_mixer_input_map.html "AkMixerInputMap: Map of inputs (identified with AK::IAkMixerInputContext *) to user-defined blocks of...") map.
[更多...](struct_ak_input_map_slot.html#details)

`#include <AkMixerInputMap.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkInputMapSlot](struct_ak_input_map_slot_af2fc485c09673e03843ce2f5d256be78.html#af2fc485c09673e03843ce2f5d256be78) () |
|  | User data. Here we have a buffer. Other relevant info would be the game object position and input parameters of the previous frame. [更多...](struct_ak_input_map_slot_af2fc485c09673e03843ce2f5d256be78.html#af2fc485c09673e03843ce2f5d256be78) |
|  | |
| bool | [operator==](struct_ak_input_map_slot_ae1567cced16c342ba35f62574eec5f77.html#ae1567cced16c342ba35f62574eec5f77) (const [AkInputMapSlot](struct_ak_input_map_slot.html) &in\_Op) const |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| KEY | [key](struct_ak_input_map_slot_a8e9d8db07c925bd63892596cb9f99d93.html#a8e9d8db07c925bd63892596cb9f99d93) |
|  | |
| USER\_DATA \* | [pUserData](struct_ak_input_map_slot_a998b6324aee6c22530da8a0e180bb69a.html#a998b6324aee6c22530da8a0e180bb69a) |
|  | Key. [更多...](struct_ak_input_map_slot_a998b6324aee6c22530da8a0e180bb69a.html#a998b6324aee6c22530da8a0e180bb69a) |
|  | |

## 详细描述

### template<class KEY, class USER\_DATA> struct AkInputMapSlot< KEY, USER\_DATA >

Structure of an entry in the [AkMixerInputMap](class_ak_mixer_input_map.html "AkMixerInputMap: Map of inputs (identified with AK::IAkMixerInputContext *) to user-defined blocks of...") map.

Collection class to manage inputs in mixer plugins. The inputs are identified by their context. The type of data attached to it is the template argument USER\_DATA. The collection performs allocation/deallocation of user data via AK\_PLUGIN\_NEW/DELETE(). Usage

// Init AkMixerInputMap<void\*, MyStruct> m\_mapInputs; m\_mapInputs.Init( in\_pAllocator ); // in\_pAllocator passed at plugin init.

// Add an input. m\_mapInputs.AddInput( in\_pInput ); // void \* in\_pInput

// Find an input MyStruct \* pInput = m\_mapInputs.Exists( in\_pInputContext ); // void \* in\_pInputContext passed to ConsumeInput()

// Iterate through inputs. AkMixerInputMap<MyStruct>::Iterator it = m\_mapInputs.End(); while ( it != m\_mapInputs.End() ) { MyStruct \* pInput = (\*it).pUserData; ... ++it; }

在文件 [AkMixerInputMap.h](_ak_mixer_input_map_8h_source.html) 第 [62](_ak_mixer_input_map_8h_source.html#l00062) 行定义.