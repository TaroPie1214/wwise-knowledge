# CAkSmartPtr

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_c_ak_smart_ptr-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods) |
[Protected 属性](#pro-attribs)

CAkSmartPtr< T > 模板类 参考

`#include <AkSmartPtr.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [CAkSmartPtr](class_c_ak_smart_ptr_ab9e0add9ad64b00b920b21f43b73d6e7.html#ab9e0add9ad64b00b920b21f43b73d6e7) () |
|  | Smart pointer constructor [更多...](class_c_ak_smart_ptr_ab9e0add9ad64b00b920b21f43b73d6e7.html#ab9e0add9ad64b00b920b21f43b73d6e7) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [CAkSmartPtr](class_c_ak_smart_ptr_a40394a79c68f8434d82d76f264522e8f.html#a40394a79c68f8434d82d76f264522e8f) (T \*in\_pT) |
|  | Smart pointer constructor [更多...](class_c_ak_smart_ptr_a40394a79c68f8434d82d76f264522e8f.html#a40394a79c68f8434d82d76f264522e8f) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [CAkSmartPtr](class_c_ak_smart_ptr_adf92e499ad36ffffc68be9299ac1ee69.html#adf92e499ad36ffffc68be9299ac1ee69) (const [CAkSmartPtr](class_c_ak_smart_ptr.html)< T > &in\_rPtr) |
|  | Smart pointer copy constructor [更多...](class_c_ak_smart_ptr_adf92e499ad36ffffc68be9299ac1ee69.html#adf92e499ad36ffffc68be9299ac1ee69) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [CAkSmartPtr](class_c_ak_smart_ptr_a6f48403006fe530b0fc388c569dd4e52.html#a6f48403006fe530b0fc388c569dd4e52) ([CAkSmartPtr](class_c_ak_smart_ptr.html)< T > &&in\_rPtr) |
|  | Smart pointer move constructor [更多...](class_c_ak_smart_ptr_a6f48403006fe530b0fc388c569dd4e52.html#a6f48403006fe530b0fc388c569dd4e52) |
|  | |
|  | [~CAkSmartPtr](class_c_ak_smart_ptr_a198962db03e5112172c58e7dece654c4.html#a198962db03e5112172c58e7dece654c4) () |
|  | Smart pointer destructor [更多...](class_c_ak_smart_ptr_a198962db03e5112172c58e7dece654c4.html#a198962db03e5112172c58e7dece654c4) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Release](class_c_ak_smart_ptr_a9df08e40337edf513e543a4c8df53078.html#a9df08e40337edf513e543a4c8df53078) () |
|  | Release [更多...](class_c_ak_smart_ptr_a9df08e40337edf513e543a4c8df53078.html#a9df08e40337edf513e543a4c8df53078) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [Attach](class_c_ak_smart_ptr_a9a8f7d7f2989800b875f38e0c1404458.html#a9a8f7d7f2989800b875f38e0c1404458) (T \*in\_pObj) |
|  | Assign with no Addref. [更多...](class_c_ak_smart_ptr_a9a8f7d7f2989800b875f38e0c1404458.html#a9a8f7d7f2989800b875f38e0c1404458) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [Detach](class_c_ak_smart_ptr_af8c7e024940023dabf158453325a3d20.html#af8c7e024940023dabf158453325a3d20) () |
|  | Give the pointer without releasing it. [更多...](class_c_ak_smart_ptr_af8c7e024940023dabf158453325a3d20.html#af8c7e024940023dabf158453325a3d20) |
|  | |
| const [CAkSmartPtr](class_c_ak_smart_ptr.html)< T > & | [operator=](class_c_ak_smart_ptr_ad18a981c71e3b4fc36adaa24090b6de5.html#ad18a981c71e3b4fc36adaa24090b6de5) (const [CAkSmartPtr](class_c_ak_smart_ptr.html)< T > &in\_pObj) |
|  | Copy Assignation operator [更多...](class_c_ak_smart_ptr_ad18a981c71e3b4fc36adaa24090b6de5.html#ad18a981c71e3b4fc36adaa24090b6de5) |
|  | |
| [CAkSmartPtr](class_c_ak_smart_ptr.html)< T > & | [operator=](class_c_ak_smart_ptr_af6a014fe4d723f358261afff0ca87849.html#af6a014fe4d723f358261afff0ca87849) ([CAkSmartPtr](class_c_ak_smart_ptr.html)< T > &&in\_pObj) |
|  | Move Assignation operator [更多...](class_c_ak_smart_ptr_af6a014fe4d723f358261afff0ca87849.html#af6a014fe4d723f358261afff0ca87849) |
|  | |
| const [CAkSmartPtr](class_c_ak_smart_ptr.html)< T > & | [operator=](class_c_ak_smart_ptr_af0758ef2de94b573176c1086989fb1c2.html#af0758ef2de94b573176c1086989fb1c2) (T \*in\_pObj) |
|  | Assignation operator [更多...](class_c_ak_smart_ptr_af0758ef2de94b573176c1086989fb1c2.html#af0758ef2de94b573176c1086989fb1c2) |
|  | |
| T & | [operator\*](class_c_ak_smart_ptr_a04f123c4aeb8d41e7ba0a5feb91f3a0d.html#a04f123c4aeb8d41e7ba0a5feb91f3a0d) () |
|  | Operator \* [更多...](class_c_ak_smart_ptr_a04f123c4aeb8d41e7ba0a5feb91f3a0d.html#a04f123c4aeb8d41e7ba0a5feb91f3a0d) |
|  | |
| T \* | [operator->](class_c_ak_smart_ptr_a5fbf1f1d7d8c61475c60fa2396954f49.html#a5fbf1f1d7d8c61475c60fa2396954f49) () const |
|  | Operator -> [更多...](class_c_ak_smart_ptr_a5fbf1f1d7d8c61475c60fa2396954f49.html#a5fbf1f1d7d8c61475c60fa2396954f49) |
|  | |
|  | [operator T\*](class_c_ak_smart_ptr_aeabb41fc81f5493afc4d29b64a370870.html#aeabb41fc81f5493afc4d29b64a370870) () const |
|  | Operator [更多...](class_c_ak_smart_ptr_aeabb41fc81f5493afc4d29b64a370870.html#aeabb41fc81f5493afc4d29b64a370870) |
|  | |
| T \*\* | [operator&](class_c_ak_smart_ptr_a8cafa45cc48c417002a47de3d427f730.html#a8cafa45cc48c417002a47de3d427f730) () |
|  | Operators to pass to functions like QueryInterface and other functions returning an addref'd pointer. [更多...](class_c_ak_smart_ptr_a8cafa45cc48c417002a47de3d427f730.html#a8cafa45cc48c417002a47de3d427f730) |
|  | |
| const T & | [operator\*](class_c_ak_smart_ptr_a59d750698b0d0d087553111bc35ea035.html#a59d750698b0d0d087553111bc35ea035) () const |
|  | Operator \* [更多...](class_c_ak_smart_ptr_a59d750698b0d0d087553111bc35ea035.html#a59d750698b0d0d087553111bc35ea035) |
|  | |
| T \* | [Cast](class_c_ak_smart_ptr_a225d5e17f3db0e2e4bf996c81a55a191.html#a225d5e17f3db0e2e4bf996c81a55a191) () |
|  | Cast [更多...](class_c_ak_smart_ptr_a225d5e17f3db0e2e4bf996c81a55a191.html#a225d5e17f3db0e2e4bf996c81a55a191) |
|  | |
| const T \* | [Cast](class_c_ak_smart_ptr_aeeaca48b3f7e6957ea7c108b144e382f.html#aeeaca48b3f7e6957ea7c108b144e382f) () const |
|  | Cast [更多...](class_c_ak_smart_ptr_aeeaca48b3f7e6957ea7c108b144e382f.html#aeeaca48b3f7e6957ea7c108b144e382f) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| void | [\_Assign](class_c_ak_smart_ptr_af59eca9e47feb94dc9c221ce1d191bbe.html#af59eca9e47feb94dc9c221ce1d191bbe) (T \*in\_pObj, bool in\_bAddRef=true) |
|  | internal use only [更多...](class_c_ak_smart_ptr_af59eca9e47feb94dc9c221ce1d191bbe.html#af59eca9e47feb94dc9c221ce1d191bbe) |
|  | |
| bool | [\_Compare](class_c_ak_smart_ptr_adb1e9a0339ee2c872a767dfcac57a444.html#adb1e9a0339ee2c872a767dfcac57a444) (const T \*in\_pObj) const |
|  | internal use only [更多...](class_c_ak_smart_ptr_adb1e9a0339ee2c872a767dfcac57a444.html#adb1e9a0339ee2c872a767dfcac57a444) |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| T \* | [m\_pT](class_c_ak_smart_ptr_a68bdb678bbd5ee41cc201bc84773ccc0.html#a68bdb678bbd5ee41cc201bc84773ccc0) |
|  | internal use only [更多...](class_c_ak_smart_ptr_a68bdb678bbd5ee41cc201bc84773ccc0.html#a68bdb678bbd5ee41cc201bc84773ccc0) |
|  | |

## 详细描述

### template<class T> class CAkSmartPtr< T >

在文件 [AkSmartPtr.h](_ak_smart_ptr_8h_source.html) 第 [37](_ak_smart_ptr_8h_source.html#l00037) 行定义.