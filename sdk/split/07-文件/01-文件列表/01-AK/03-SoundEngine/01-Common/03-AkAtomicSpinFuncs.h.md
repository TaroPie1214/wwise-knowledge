# AkAtomicSpinFuncs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[命名空间](#namespaces) |
[函数](#func-members)

AkAtomicSpinFuncs.h 文件参考

`#include <AK/SoundEngine/Common/AkAtomic.h>`  
`#include <AK/Tools/Common/AkPlatformFuncs.h>`

[浏览源代码.](_ak_atomic_spin_funcs_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
|  | [AKPLATFORM](namespace_a_k_p_l_a_t_f_o_r_m.html) |
|  | Platform-dependent helpers |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| void | [AKPLATFORM::AkLimitedSpinForZero](namespace_a_k_p_l_a_t_f_o_r_m_a2d22136c5c291ebb6c15583a4c2fb50d.html#a2d22136c5c291ebb6c15583a4c2fb50d) ([AkAtomic32](_ak_atomic_types_8h_ad12c0f5c4a2718f4075c0b94212fb5e3.html#ad12c0f5c4a2718f4075c0b94212fb5e3) \*in\_pVal) |
|  | |
| bool | [AKPLATFORM::AkLimitedSpinToAcquire](namespace_a_k_p_l_a_t_f_o_r_m_a94b0b78ae270e1f9ae720bcdd92c7a1b.html#a94b0b78ae270e1f9ae720bcdd92c7a1b) ([AkAtomic32](_ak_atomic_types_8h_ad12c0f5c4a2718f4075c0b94212fb5e3.html#ad12c0f5c4a2718f4075c0b94212fb5e3) \*in\_pVal, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_proposed, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_expected) |
|  | |
| void | [AKPLATFORM::AkSpinWaitForZero](namespace_a_k_p_l_a_t_f_o_r_m_a8a00803478b9ef89e8bf807d29ab0957.html#a8a00803478b9ef89e8bf807d29ab0957) ([AkAtomic32](_ak_atomic_types_8h_ad12c0f5c4a2718f4075c0b94212fb5e3.html#ad12c0f5c4a2718f4075c0b94212fb5e3) \*in\_pVal) |
|  | |
| void | [AKPLATFORM::AkSpinToAcquire](namespace_a_k_p_l_a_t_f_o_r_m_a4a65c86dee2e4cb3c1d08f5fe204ce48.html#a4a65c86dee2e4cb3c1d08f5fe204ce48) ([AkAtomic32](_ak_atomic_types_8h_ad12c0f5c4a2718f4075c0b94212fb5e3.html#ad12c0f5c4a2718f4075c0b94212fb5e3) \*in\_pVal, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_proposed, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_expected) |
|  | |