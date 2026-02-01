# AkLastPolicyWithLast

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_last_policy_with_last-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods) |
[Protected 属性](#pro-attribs)

AkLastPolicyWithLast< T > 模板类 参考

`#include <AkListBare.h>`

类 AkLastPolicyWithLast< T > 继承关系图:

![](../../../images/class_ak_last_policy_with_last.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) T \* | [Last](class_ak_last_policy_with_last_a46fcbabc609e3d24abd305fdcb296d41.html#a46fcbabc609e3d24abd305fdcb296d41) () |
|  | Get last element. [更多...](class_ak_last_policy_with_last_a46fcbabc609e3d24abd305fdcb296d41.html#a46fcbabc609e3d24abd305fdcb296d41) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) const T \* | [Last](class_ak_last_policy_with_last_a97897fc2ff7552f02c538eea9fe8d2d5.html#a97897fc2ff7552f02c538eea9fe8d2d5) () const |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) | [AkLastPolicyWithLast](class_ak_last_policy_with_last_a9e3d4aef05bc5dc0da5d96ee0795f350.html#a9e3d4aef05bc5dc0da5d96ee0795f350) () |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [UpdateLast](class_ak_last_policy_with_last_ad4012f3f3e325e3d654b2e6c68de60ed.html#ad4012f3f3e325e3d654b2e6c68de60ed) (T \*in\_pLast) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetLast](class_ak_last_policy_with_last_a4f651c8dff13c3cb6f41e5e462160520.html#a4f651c8dff13c3cb6f41e5e462160520) (T \*in\_pLast) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [RemoveItem](class_ak_last_policy_with_last_a7231e2e7a73477844302ffd508110782.html#a7231e2e7a73477844302ffd508110782) (T \*in\_pItem, T \*in\_pPrevItem) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AddItem](class_ak_last_policy_with_last_a08c26b7ee2366f354531652682c366e3.html#a08c26b7ee2366f354531652682c366e3) (T \*in\_pItem, T \*in\_pNextItem) |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| T \* | [m\_pLast](class_ak_last_policy_with_last_a955a4a5db2f04d2ab858ed883223b259.html#a955a4a5db2f04d2ab858ed883223b259) |
|  | bottom of list [更多...](class_ak_last_policy_with_last_a955a4a5db2f04d2ab858ed883223b259.html#a955a4a5db2f04d2ab858ed883223b259) |
|  | |

## 详细描述

### template<class T> class AkLastPolicyWithLast< T >

Last item policy. These policy classes must define protected methods [UpdateLast()](class_ak_last_policy_with_last_ad4012f3f3e325e3d654b2e6c68de60ed.html#ad4012f3f3e325e3d654b2e6c68de60ed), [SetLast()](class_ak_last_policy_with_last_a4f651c8dff13c3cb6f41e5e462160520.html#a4f651c8dff13c3cb6f41e5e462160520), [RemoveItem()](class_ak_last_policy_with_last_a7231e2e7a73477844302ffd508110782.html#a7231e2e7a73477844302ffd508110782) and [AddItem()](class_ak_last_policy_with_last_a08c26b7ee2366f354531652682c366e3.html#a08c26b7ee2366f354531652682c366e3).

在文件 [AkListBare.h](_ak_list_bare_8h_source.html) 第 [110](_ak_list_bare_8h_source.html#l00110) 行定义.