# IAkList

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [SourceControlContainers](namespace_a_k_1_1_wwise_1_1_source_control_containers.html)
- [IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::SourceControlContainers::IAkList< Type, Arg\_Type > 模板类 参考abstract

`#include <SourceControlContainers.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [Reserve](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a77905d0783f49ef512e809e8a9996f36.html#a77905d0783f49ef512e809e8a9996f36) (size\_t in\_capacity) |
|  | |
| unsigned int | [GetCount](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a9690d2085f9f3453480dd50c6e3298e0.html#a9690d2085f9f3453480dd50c6e3298e0) () const |
|  | |
| virtual unsigned int | [GetSize](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_ab7e3263a3b5f3935948d9b4a80040b13.html#ab7e3263a3b5f3935948d9b4a80040b13) () const =0 |
|  | |
| virtual bool | [IsEmpty](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a3f301814068eae2f02acf1fd4aa58ea0.html#a3f301814068eae2f02acf1fd4aa58ea0) () const =0 |
|  | |
| virtual void | [AddHead](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a89f64a5d0f8c9d41e65125f8807c05f2.html#a89f64a5d0f8c9d41e65125f8807c05f2) (Arg\_Type in\_newElement)=0 |
|  | |
| virtual void | [AddTail](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_ad148966a617cb4164a43b3772bb4f321.html#ad148966a617cb4164a43b3772bb4f321) (Arg\_Type in\_newElement)=0 |
|  | |
| virtual void | [RemoveHead](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a11683c2b965a8c97ae6937db6ebbd5a6.html#a11683c2b965a8c97ae6937db6ebbd5a6) ()=0 |
|  | |
| virtual void | [RemoveTail](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_ad31b68677f5a08c15be8326423418c0b.html#ad31b68677f5a08c15be8326423418c0b) ()=0 |
|  | |
| virtual void | [RemoveAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_abc71b7d739aaafd26ccea2660bd36cb2.html#abc71b7d739aaafd26ccea2660bd36cb2) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) in\_position)=0 |
|  | |
| virtual void | [RemoveAll](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_ac354cf9bd7de37537de1757ccf3e02ec.html#ac354cf9bd7de37537de1757ccf3e02ec) ()=0 |
|  | |
| virtual Type & | [GetHead](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a91944d1d72888ef6efd376586ba26084.html#a91944d1d72888ef6efd376586ba26084) ()=0 |
|  | |
| virtual const Type & | [GetHead](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_ae5ffbbef7cdcbf52d956ba2019dce45c.html#ae5ffbbef7cdcbf52d956ba2019dce45c) () const =0 |
|  | |
| virtual Type & | [GetTail](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_aae93a31e8506426532302b31d2932aee.html#aae93a31e8506426532302b31d2932aee) ()=0 |
|  | |
| virtual const Type & | [GetTail](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a92a13c232a7584a3fae41f89baf65166.html#a92a13c232a7584a3fae41f89baf65166) () const =0 |
|  | |
| virtual [AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) | [GetHeadPosition](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_af5b416e617aa443b8a592c7574660fb7.html#af5b416e617aa443b8a592c7574660fb7) () const =0 |
|  | |
| virtual [AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) | [GetTailPosition](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a8bce83b62f30f76c6368c94c4a97cd47.html#a8bce83b62f30f76c6368c94c4a97cd47) () const =0 |
|  | |
| virtual Type & | [GetNext](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a530f1a1c4dd78188985892133d42a2a5.html#a530f1a1c4dd78188985892133d42a2a5) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) &in\_rPosition)=0 |
|  | |
| virtual const Type & | [GetNext](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a719ab86ba6c43d48a8dd136c698458ee.html#a719ab86ba6c43d48a8dd136c698458ee) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) &in\_rPosition) const =0 |
|  | |
| virtual Type & | [GetPrev](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a3ea1c4dc3e6fe9f2113bc6af51653d26.html#a3ea1c4dc3e6fe9f2113bc6af51653d26) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) &in\_rPosition)=0 |
|  | |
| virtual const Type & | [GetPrev](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a6078158c95fda25e75a415b94d5a5919.html#a6078158c95fda25e75a415b94d5a5919) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) &in\_rPosition) const =0 |
|  | |
| virtual Type & | [GetAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_af065059b737b7c7803518d4d4a64bf54.html#af065059b737b7c7803518d4d4a64bf54) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) in\_position)=0 |
|  | |
| virtual const Type & | [GetAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a8d55858f037ee2c9c7ce9393a763fc6a.html#a8d55858f037ee2c9c7ce9393a763fc6a) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) in\_position) const =0 |
|  | |
| virtual Type & | [GetAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_aa33394e056f8bac60a30b935dc72e87d.html#aa33394e056f8bac60a30b935dc72e87d) (unsigned int in\_index)=0 |
|  | |
| virtual const Type & | [GetAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a273099de5861360cf64624b456ef6796.html#a273099de5861360cf64624b456ef6796) (unsigned int in\_index) const =0 |
|  | |
| virtual void | [SetAt](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a28b49326c39a303368f6265e16bf5de5.html#a28b49326c39a303368f6265e16bf5de5) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) in\_pos, Arg\_Type in\_newElement)=0 |
|  | |
| virtual [AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) | [InsertBefore](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_aaf8059a6df71e318740574fc916ce99b.html#aaf8059a6df71e318740574fc916ce99b) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) in\_position, Arg\_Type in\_newElement)=0 |
|  | |
| virtual [AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) | [InsertAfter](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list_a8821d7c60e318d676cbf94bc413a8cbf.html#a8821d7c60e318d676cbf94bc413a8cbf) ([AkPos](namespace_a_k_1_1_wwise_1_1_source_control_containers_a92a2b54b670dbd29047b46e687b916e0.html#a92a2b54b670dbd29047b46e687b916e0) in\_position, Arg\_Type in\_newElement)=0 |
|  | |

## 详细描述

### template<class Type, class Arg\_Type = const Type&> class AK.Wwise::SourceControlContainers::IAkList< Type, Arg\_Type >

Template parameters:

- Type: Class of object stored in the list.
- Arg\_Type: Type used to reference objects stored in the list. Can be a reference. By default, this is a reference to the type.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

|  |  |
| --- | --- |
|  | **备注:** The class implementing this interface is a wrapper around the MFC **CList** class. Documentation can be found on MSDN. |

在文件 [SourceControlContainers.h](_source_control_containers_8h_source.html) 第 [59](_source_control_containers_8h_source.html#l00059) 行定义.