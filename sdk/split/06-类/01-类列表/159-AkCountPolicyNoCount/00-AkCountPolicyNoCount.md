# AkCountPolicyNoCount

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_count_policy_no_count-members.html) |
[Protected 成员函数](#pro-methods)

AkCountPolicyNoCount< T > 模板类 参考

`#include <AkListBare.h>`

类 AkCountPolicyNoCount< T > 继承关系图:

![](../../../images/class_ak_count_policy_no_count.png)

|  |  |
| --- | --- |
| Protected 成员函数 | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [ResetCount](class_ak_count_policy_no_count_a83bc9422f710d915135ebdd51152aa49.html#a83bc9422f710d915135ebdd51152aa49) (T \*) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [IncrementCount](class_ak_count_policy_no_count_a41957418694743bc3bb1147dbe8e9299.html#a41957418694743bc3bb1147dbe8e9299) (T \*) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [DecrementCount](class_ak_count_policy_no_count_a3ee57f38e9f0e9eed8f9d2b043b54226.html#a3ee57f38e9f0e9eed8f9d2b043b54226) (T \*) |
|  | |

## 详细描述

### template<class T> class AkCountPolicyNoCount< T >

Item count policy. These policy classes must define protected methods [ResetCount()](class_ak_count_policy_no_count_a83bc9422f710d915135ebdd51152aa49.html#a83bc9422f710d915135ebdd51152aa49), [IncrementCount()](class_ak_count_policy_no_count_a41957418694743bc3bb1147dbe8e9299.html#a41957418694743bc3bb1147dbe8e9299), [DecrementCount()](class_ak_count_policy_no_count_a3ee57f38e9f0e9eed8f9d2b043b54226.html#a3ee57f38e9f0e9eed8f9d2b043b54226) and optionally, public unsigned int Length() const.

在文件 [AkListBare.h](_ak_list_bare_8h_source.html) 第 [78](_ak_list_bare_8h_source.html#l00078) 行定义.