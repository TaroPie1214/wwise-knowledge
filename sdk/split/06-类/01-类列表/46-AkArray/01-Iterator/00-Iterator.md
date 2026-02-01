# Iterator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkArray](class_ak_array.html)
- [Iterator](struct_ak_array_1_1_iterator.html)

[所有成员列表](struct_ak_array_1_1_iterator-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkArray< T, ARG\_T, TAlloc, TGrowBy, TMovePolicy >::Iterator结构体 参考

[Iterator](struct_ak_array_1_1_iterator.html "Iterator")
[更多...](struct_ak_array_1_1_iterator.html#details)

`#include <AkArray.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| [Iterator](struct_ak_array_1_1_iterator.html) | [operator+](struct_ak_array_1_1_iterator_adcd5949f53c834c27fe2b10991487371.html#adcd5949f53c834c27fe2b10991487371) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) inc) const |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [operator-](struct_ak_array_1_1_iterator_a03397dc941c66cf07aa4f4ad88d2f020.html#a03397dc941c66cf07aa4f4ad88d2f020) ([Iterator](struct_ak_array_1_1_iterator.html) const &rhs) const |
|  | |
| [Iterator](struct_ak_array_1_1_iterator.html) & | [operator++](struct_ak_array_1_1_iterator_aa0848efb74a03bef58f7232ee9458ac1.html#aa0848efb74a03bef58f7232ee9458ac1) () |
|  | ++ operator [更多...](struct_ak_array_1_1_iterator_aa0848efb74a03bef58f7232ee9458ac1.html#aa0848efb74a03bef58f7232ee9458ac1) |
|  | |
| [Iterator](struct_ak_array_1_1_iterator.html) & | [operator--](struct_ak_array_1_1_iterator_aeca6c0f1cd199a62c665d28cc34b7e91.html#aeca6c0f1cd199a62c665d28cc34b7e91) () |
|  | – operator [更多...](struct_ak_array_1_1_iterator_aeca6c0f1cd199a62c665d28cc34b7e91.html#aeca6c0f1cd199a62c665d28cc34b7e91) |
|  | |
| T & | [operator\*](struct_ak_array_1_1_iterator_abd227445b9ff88fdb8bc629626665abd.html#abd227445b9ff88fdb8bc629626665abd) () |
|  | |
| T \* | [operator->](struct_ak_array_1_1_iterator_acf55a4ed46bacfdf552e3ec5804f3181.html#acf55a4ed46bacfdf552e3ec5804f3181) () const |
|  | |
| bool | [operator==](struct_ak_array_1_1_iterator_ad6ac9d1a187afb67a3908dde5bd8dc45.html#ad6ac9d1a187afb67a3908dde5bd8dc45) (const [Iterator](struct_ak_array_1_1_iterator.html) &in\_rOp) const |
|  | == operator [更多...](struct_ak_array_1_1_iterator_ad6ac9d1a187afb67a3908dde5bd8dc45.html#ad6ac9d1a187afb67a3908dde5bd8dc45) |
|  | |
| bool | [operator!=](struct_ak_array_1_1_iterator_a955dac8dd9b00161753af7c63a1ddf65.html#a955dac8dd9b00161753af7c63a1ddf65) (const [Iterator](struct_ak_array_1_1_iterator.html) &in\_rOp) const |
|  | != operator [更多...](struct_ak_array_1_1_iterator_a955dac8dd9b00161753af7c63a1ddf65.html#a955dac8dd9b00161753af7c63a1ddf65) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| T \* | [pItem](struct_ak_array_1_1_iterator_a77845a9947a186c81128b5021382cea3.html#a77845a9947a186c81128b5021382cea3) |
|  | Pointer to the item in the array. [更多...](struct_ak_array_1_1_iterator_a77845a9947a186c81128b5021382cea3.html#a77845a9947a186c81128b5021382cea3) |
|  | |

## 详细描述

### template<class T, class ARG\_T, class TAlloc = ArrayPoolDefault, class TGrowBy = AkGrowByPolicy\_DEFAULT, class TMovePolicy = AkAssignmentMovePolicy<T>> struct AkArray< T, ARG\_T, TAlloc, TGrowBy, TMovePolicy >::Iterator

[Iterator](struct_ak_array_1_1_iterator.html "Iterator")

在文件 [AkArray.h](_ak_array_8h_source.html) 第 [282](_ak_array_8h_source.html#l00282) 行定义.