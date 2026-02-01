# IAkMap

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [SourceControlContainers](namespace_a_k_1_1_wwise_1_1_source_control_containers.html)
- [IAkMap](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::SourceControlContainers::IAkMap< Key, Arg\_Key, Value, Arg\_Value > 模板类 参考abstract

`#include <SourceControlContainers.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| unsigned int | [GetCount](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a5822aa9a8e1d53a59e3fe2c3ff85e2c2.html#a5822aa9a8e1d53a59e3fe2c3ff85e2c2) () const |
|  | |
| virtual unsigned int | [GetSize](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_aed450ac0d4803f4205a5a492c627079c.html#aed450ac0d4803f4205a5a492c627079c) () const =0 |
|  | |
| virtual bool | [IsEmpty](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_aaf24b869353ee1cfd7d036dc8c08ce81.html#aaf24b869353ee1cfd7d036dc8c08ce81) () const =0 |
|  | |
| virtual bool | [Lookup](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a35f22486af1ad40c6770d8c299f7a866.html#a35f22486af1ad40c6770d8c299f7a866) (Arg\_Key in\_key, Value &in\_rValue) const =0 |
|  | |
| virtual Value & | [operator[]](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a567ef3a78bcf1c87511abf48b9bbdbad.html#a567ef3a78bcf1c87511abf48b9bbdbad) (Arg\_Key in\_key)=0 |
|  | |
| virtual void | [SetAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a6400d73e233a92a7e20a4dfb1bbbf7ab.html#a6400d73e233a92a7e20a4dfb1bbbf7ab) (Arg\_Key in\_key, Arg\_Value in\_newValue)=0 |
|  | |
| virtual bool | [RemoveKey](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a2496402477b50e0b204e9016b1efe88a.html#a2496402477b50e0b204e9016b1efe88a) (Arg\_Key in\_key)=0 |
|  | |
| virtual void | [RemoveAll](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a2183f8657afd77ab5d1d0fae5f70b8fd.html#a2183f8657afd77ab5d1d0fae5f70b8fd) ()=0 |
|  | |
| virtual [AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) | [GetStartPosition](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a9c84f47060455e8e8aee137356f1fc86.html#a9c84f47060455e8e8aee137356f1fc86) () const =0 |
|  | |
| virtual void | [GetNextAssoc](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_map_a6a0bdc0b905ae3c49901c0390f8e4753.html#a6a0bdc0b905ae3c49901c0390f8e4753) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) &in\_rNextPosition, Key &in\_rKey, Value &in\_rValue) const =0 |
|  | |

## 详细描述

### template<class Key, class Arg\_Key, class Value, class Arg\_Value> class AK.Wwise::SourceControlContainers::IAkMap< Key, Arg\_Key, Value, Arg\_Value >

Template parameters:

- Key: Class of the object used as the map key.
- Arg\_Key: Data type used for Key arguments.
- Value: Class of the object stored in the map.
- Arg\_Value: Data type used for Value arguments; usually a reference to Value.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

|  |  |
| --- | --- |
|  | **备注:** The class implementing this interface is a wrapper around the MFC **CMap** class. Documentation can be found on MSDN. |

在文件 [SourceControlContainers.h](_source_control_containers_8h_source.html) 第 [126](_source_control_containers_8h_source.html#l00126) 行定义.