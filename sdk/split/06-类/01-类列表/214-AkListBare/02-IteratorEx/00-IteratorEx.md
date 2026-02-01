# IteratorEx

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkListBare](class_ak_list_bare.html)
- [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html)

[所有成员列表](struct_ak_list_bare_1_1_iterator_ex-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY >::IteratorEx结构体 参考

`#include <AkListBare.h>`

类 AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY >::IteratorEx 继承关系图:

![](../../../../images/struct_ak_list_bare_1_1_iterator_ex.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) & | [operator++](struct_ak_list_bare_1_1_iterator_ex_a3f9b66fcd8f9ddac6292ed6fc6fcd684.html#a3f9b66fcd8f9ddac6292ed6fc6fcd684) () |
|  | Operator ++. [更多...](struct_ak_list_bare_1_1_iterator_ex_a3f9b66fcd8f9ddac6292ed6fc6fcd684.html#a3f9b66fcd8f9ddac6292ed6fc6fcd684) |
|  | |
| - Public 成员函数 继承自 [AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY >::Iterator](struct_ak_list_bare_1_1_iterator.html) | |
| [Iterator](struct_ak_list_bare_1_1_iterator.html) & | [operator++](struct_ak_list_bare_1_1_iterator_aeec75eeaecb02c402d306a16ff8fd8ce.html#aeec75eeaecb02c402d306a16ff8fd8ce) () |
|  | Operator ++. [更多...](struct_ak_list_bare_1_1_iterator_aeec75eeaecb02c402d306a16ff8fd8ce.html#aeec75eeaecb02c402d306a16ff8fd8ce) |
|  | |
| T \* | [operator\*](struct_ak_list_bare_1_1_iterator_a62360128b28ea3aaeb01b3898e2114d2.html#a62360128b28ea3aaeb01b3898e2114d2) () const |
|  | Operator \*. [更多...](struct_ak_list_bare_1_1_iterator_a62360128b28ea3aaeb01b3898e2114d2.html#a62360128b28ea3aaeb01b3898e2114d2) |
|  | |
| T \* | [operator->](struct_ak_list_bare_1_1_iterator_a13ae9978ff28dc8b9670dc7e7f7d9ca5.html#a13ae9978ff28dc8b9670dc7e7f7d9ca5) () const |
|  | Operator -> [更多...](struct_ak_list_bare_1_1_iterator_a13ae9978ff28dc8b9670dc7e7f7d9ca5.html#a13ae9978ff28dc8b9670dc7e7f7d9ca5) |
|  | |
| bool | [operator!=](struct_ak_list_bare_1_1_iterator_a48c9a5ad8492a178b6970451bfb98b1e.html#a48c9a5ad8492a178b6970451bfb98b1e) (const [Iterator](struct_ak_list_bare_1_1_iterator.html) &in\_rOp) const |
|  | Operator !=. [更多...](struct_ak_list_bare_1_1_iterator_a48c9a5ad8492a178b6970451bfb98b1e.html#a48c9a5ad8492a178b6970451bfb98b1e) |
|  | |
| bool | [operator==](struct_ak_list_bare_1_1_iterator_a20dea9735a7c76923899c939535e46e3.html#a20dea9735a7c76923899c939535e46e3) (const [Iterator](struct_ak_list_bare_1_1_iterator.html) &in\_rOp) const |
|  | Operator ==. [更多...](struct_ak_list_bare_1_1_iterator_a20dea9735a7c76923899c939535e46e3.html#a20dea9735a7c76923899c939535e46e3) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| T \* | [pPrevItem](struct_ak_list_bare_1_1_iterator_ex_ad3285de620ea86cf15f4f83bcebdfc56.html#ad3285de620ea86cf15f4f83bcebdfc56) |
|  | Previous item. [更多...](struct_ak_list_bare_1_1_iterator_ex_ad3285de620ea86cf15f4f83bcebdfc56.html#ad3285de620ea86cf15f4f83bcebdfc56) |
|  | |
| - Public 属性 继承自 [AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY >::Iterator](struct_ak_list_bare_1_1_iterator.html) | |
| T \* | [pItem](struct_ak_list_bare_1_1_iterator_a76af47366da02dbb106af67356d1e167.html#a76af47366da02dbb106af67356d1e167) |
|  | Next item. [更多...](struct_ak_list_bare_1_1_iterator_a76af47366da02dbb106af67356d1e167.html#a76af47366da02dbb106af67356d1e167) |
|  | |

## 详细描述

### template<class T, template< class > class U\_NEXTITEM = AkListBareNextItem, template< class > class COUNT\_POLICY = AkCountPolicyNoCount, template< class > class LAST\_POLICY = AkLastPolicyWithLast> struct AkListBare< T, U\_NEXTITEM, COUNT\_POLICY, LAST\_POLICY >::IteratorEx

The [IteratorEx](struct_ak_list_bare_1_1_iterator_ex.html) iterator is intended for usage when a possible erase may occurs when simply iterating trough a list, use the simple [Iterator](struct_ak_list_bare_1_1_iterator.html "Iterator."), it is faster and lighter.

在文件 [AkListBare.h](_ak_list_bare_8h_source.html) 第 [209](_ak_list_bare_8h_source.html#l00209) 行定义.