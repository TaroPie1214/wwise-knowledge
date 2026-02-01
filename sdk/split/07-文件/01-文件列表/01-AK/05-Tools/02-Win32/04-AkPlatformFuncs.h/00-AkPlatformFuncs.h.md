# AkPlatformFuncs.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Win32](dir_651ef90891711df69986912befd4fda9.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[函数](#func-members) |
[变量](#var-members)

AkPlatformFuncs.h 文件参考

`#include <windows.h>`  
`#include <malloc.h>`  
`#include <AK/Tools/Common/AkAssert.h>`  
`#include <stdio.h>`  
`#include <intrin.h>`

[浏览源代码.](_win32_2_ak_platform_funcs_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkThreadProperties](struct_ak_thread_properties.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AKPLATFORM](namespace_a_k_p_l_a_t_f_o_r_m.html) |
|  | Platform-dependent helpers |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [WIN32\_LEAN\_AND\_MEAN](_win32_2_ak_platform_funcs_8h_ac7bef5d85e3dcd73eef56ad39ffc84a9.html#ac7bef5d85e3dcd73eef56ad39ffc84a9) |
|  | |
| #define | [AK\_DECLARE\_THREAD\_ROUTINE](_win32_2_ak_platform_funcs_8h_aec12ec04aab5878a38cd74f5d48e155d.html#aec12ec04aab5878a38cd74f5d48e155d)(FuncName)   DWORD WINAPI FuncName(LPVOID lpParameter) |
|  | |
| #define | [AK\_THREAD\_RETURN](_win32_2_ak_platform_funcs_8h_aeb25a8ac376e337bf89374521091f63c.html#aeb25a8ac376e337bf89374521091f63c)(\_param\_)   return (\_param\_); |
|  | |
| #define | [AK\_THREAD\_ROUTINE\_PARAMETER](_win32_2_ak_platform_funcs_8h_a79a5fd183a38d1e1f2953c8e17883a27.html#a79a5fd183a38d1e1f2953c8e17883a27)   lpParameter |
|  | |
| #define | [AK\_GET\_THREAD\_ROUTINE\_PARAMETER\_PTR](_win32_2_ak_platform_funcs_8h_afed1697b8f2fe998dff72e36e4270f91.html#afed1697b8f2fe998dff72e36e4270f91)(type)   reinterpret\_cast<type\*>( [AK\_THREAD\_ROUTINE\_PARAMETER](_win32_2_ak_platform_funcs_8h_a79a5fd183a38d1e1f2953c8e17883a27.html#a79a5fd183a38d1e1f2953c8e17883a27) ) |
|  | |
| #define | [AK\_RETURN\_THREAD\_OK](_win32_2_ak_platform_funcs_8h_a0c5045e5dac01d66abd0350f71c09675.html#a0c5045e5dac01d66abd0350f71c09675)   0x00000000 |
|  | |
| #define | [AK\_RETURN\_THREAD\_ERROR](_win32_2_ak_platform_funcs_8h_a05ff49725555272c3471934bcf5baeac.html#a05ff49725555272c3471934bcf5baeac)   0x00000001 |
|  | |
| #define | [AK\_DEFAULT\_STACK\_SIZE](_win32_2_ak_platform_funcs_8h_a54ddd9a5016d4da1b8e9a4cf4d51b2f1.html#a54ddd9a5016d4da1b8e9a4cf4d51b2f1)   (128\*1024) |
|  | |
| #define | [AK\_THREAD\_PRIORITY\_NORMAL](_win32_2_ak_platform_funcs_8h_a3d61a8f2e5dc67921d162db7e3f16455.html#a3d61a8f2e5dc67921d162db7e3f16455)   THREAD\_PRIORITY\_NORMAL |
|  | |
| #define | [AK\_THREAD\_PRIORITY\_ABOVE\_NORMAL](_win32_2_ak_platform_funcs_8h_a3455a4dd58b2446e7f93121099836a51.html#a3455a4dd58b2446e7f93121099836a51)   THREAD\_PRIORITY\_ABOVE\_NORMAL |
|  | |
| #define | [AK\_THREAD\_PRIORITY\_BELOW\_NORMAL](_win32_2_ak_platform_funcs_8h_a77eb2153a8f57dd6b5839e56aedd2237.html#a77eb2153a8f57dd6b5839e56aedd2237)   THREAD\_PRIORITY\_BELOW\_NORMAL |
|  | |
| #define | [AK\_THREAD\_PRIORITY\_TIME\_CRITICAL](_win32_2_ak_platform_funcs_8h_ad1b17234ba8be6d59028da369a3184e8.html#ad1b17234ba8be6d59028da369a3184e8)   THREAD\_PRIORITY\_TIME\_CRITICAL |
|  | |
| #define | [AK\_THREAD\_MODE\_BACKGROUND\_BEGIN](_win32_2_ak_platform_funcs_8h_a33ef9d870660e622c0f605804e844590.html#a33ef9d870660e622c0f605804e844590)   THREAD\_MODE\_BACKGROUND\_BEGIN |
|  | |
| #define | [AK\_NULL\_THREAD](_win32_2_ak_platform_funcs_8h_a4d3db10e52de79bbcbbf5dfa26bff1e8.html#a4d3db10e52de79bbcbbf5dfa26bff1e8)   NULL |
|  | |
| #define | [AK\_INFINITE](_win32_2_ak_platform_funcs_8h_a818830499d4a2e8cfb7f6576a7d44126.html#a818830499d4a2e8cfb7f6576a7d44126)   INFINITE |
|  | |
| #define | [AkExitThread](_win32_2_ak_platform_funcs_8h_a062f641fb543fe31305093881ef0f19e.html#a062f641fb543fe31305093881ef0f19e)(\_result)   return \_result; |
|  | |
| #define | [CONVERT\_WIDE\_TO\_OSCHAR](_win32_2_ak_platform_funcs_8h_acfb9f21bb4cc74f2712c8c7366d1c53e.html#acfb9f21bb4cc74f2712c8c7366d1c53e)(\_wstring\_, \_oscharstring\_)   ( \_oscharstring\_ ) = ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664)\*)( \_wstring\_ ) |
|  | |
| #define | [CONVERT\_CHAR\_TO\_OSCHAR](_win32_2_ak_platform_funcs_8h_a376af2b5208ec2c3be41b6d369dca92a.html#a376af2b5208ec2c3be41b6d369dca92a)(\_astring\_, \_oscharstring\_) |
|  | |
| #define | [CONVERT\_OSCHAR\_TO\_WIDE](_win32_2_ak_platform_funcs_8h_ace7a8c731abffdef37ac97f76f7636b9.html#ace7a8c731abffdef37ac97f76f7636b9)(\_osstring\_, \_wstring\_)   \_wstring\_ = \_osstring\_ |
|  | |
| #define | [CONVERT\_OSCHAR\_TO\_CHAR](_win32_2_ak_platform_funcs_8h_a6443890bce7e26c820eef2d234eb1fd0.html#a6443890bce7e26c820eef2d234eb1fd0)(\_osstring\_, \_astring\_) |
|  | |
| #define | [AK\_OSPRINTF](_win32_2_ak_platform_funcs_8h_a9b245a80c6e27bb5a4e2e690cf5e1359.html#a9b245a80c6e27bb5a4e2e690cf5e1359)   swprintf\_s |
|  | AkOSChar version of sprintf(). [更多...](_win32_2_ak_platform_funcs_8h_a9b245a80c6e27bb5a4e2e690cf5e1359.html#a9b245a80c6e27bb5a4e2e690cf5e1359) |
|  | |
| #define | [AK\_UTF16\_TO\_WCHAR](_win32_2_ak_platform_funcs_8h_ab3aa56d49c975edb39b37d1d675355cc.html#ab3aa56d49c975edb39b37d1d675355cc)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991)( in\_pdDest, in\_pSrc, in\_MaxSize ) |
|  | |
| #define | [AK\_WCHAR\_TO\_UTF16](_win32_2_ak_platform_funcs_8h_a800ed71bd6e980fa1de08a9ddc8b1e8b.html#a800ed71bd6e980fa1de08a9ddc8b1e8b)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991)( in\_pdDest, in\_pSrc, in\_MaxSize ) |
|  | |
| #define | [AK\_UTF8\_TO\_OSCHAR](_win32_2_ak_platform_funcs_8h_abdfa77374a60830d2e23f8e3399441e9.html#abdfa77374a60830d2e23f8e3399441e9)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::AkCharToWideChar](namespace_a_k_p_l_a_t_f_o_r_m_a2e556ab1a4cccdcf1ecc139008cd6f09.html#a2e556ab1a4cccdcf1ecc139008cd6f09)( in\_pSrc, in\_MaxSize, in\_pdDest ) |
|  | |
| #define | [AK\_UTF16\_TO\_OSCHAR](_win32_2_ak_platform_funcs_8h_aa241fce3e0b84fe3c9be9aac360c930c.html#aa241fce3e0b84fe3c9be9aac360c930c)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991)( in\_pdDest, in\_pSrc, in\_MaxSize ) |
|  | |
| #define | [AK\_UTF16\_TO\_CHAR](_win32_2_ak_platform_funcs_8h_a30a9f22b50a9bb295685f5645b09a1c6.html#a30a9f22b50a9bb295685f5645b09a1c6)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::AkWideCharToChar](namespace_a_k_p_l_a_t_f_o_r_m_a79c12f8f0710c4772f99b341006af233.html#a79c12f8f0710c4772f99b341006af233)( in\_pSrc, in\_MaxSize, in\_pdDest ) |
|  | |
| #define | [AK\_CHAR\_TO\_UTF16](_win32_2_ak_platform_funcs_8h_a2e9b757a7c0501d1802e12ceaa08b9ae.html#a2e9b757a7c0501d1802e12ceaa08b9ae)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::AkCharToWideChar](namespace_a_k_p_l_a_t_f_o_r_m_a2e556ab1a4cccdcf1ecc139008cd6f09.html#a2e556ab1a4cccdcf1ecc139008cd6f09)( in\_pSrc, in\_MaxSize, in\_pdDest ) |
|  | |
| #define | [AK\_OSCHAR\_TO\_UTF16](_win32_2_ak_platform_funcs_8h_a337acb91c8ecfcf878a8a70d12029574.html#a337acb91c8ecfcf878a8a70d12029574)(in\_pdDest, in\_pSrc, in\_MaxSize)   [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991)( in\_pdDest, in\_pSrc, in\_MaxSize ) |
|  | |
| #define | [AK\_PATH\_SEPARATOR](_win32_2_ak_platform_funcs_8h_ad6e0377ee663eaeaf6250073a78a0dff.html#ad6e0377ee663eaeaf6250073a78a0dff)   L"\\" |
|  | |
| #define | [AK\_LIBRARY\_PREFIX](_win32_2_ak_platform_funcs_8h_ae3a230758bed9422c5fb39d5485886ab.html#ae3a230758bed9422c5fb39d5485886ab)   L"" |
|  | |
| #define | [AK\_DYNAMIC\_LIBRARY\_EXTENSION](_win32_2_ak_platform_funcs_8h_a993bf0781a473d35be75046f3753a6e9.html#a993bf0781a473d35be75046f3753a6e9)   L".dll" |
|  | |
| #define | [AK\_FILEHANDLE\_TO\_UINTPTR](_win32_2_ak_platform_funcs_8h_aa52c4d4fe11a02810b13851abe61657b.html#aa52c4d4fe11a02810b13851abe61657b)(\_h)   (([AkUIntPtr](_ak_numeral_types_8h_aba972f179e9ca267106fac77b6d3c78b.html#aba972f179e9ca267106fac77b6d3c78b))\_h) |
|  | |
| #define | [AK\_SET\_FILEHANDLE\_TO\_UINTPTR](_win32_2_ak_platform_funcs_8h_a1804755c5c299b59c98b888034b7ecc2.html#a1804755c5c299b59c98b888034b7ecc2)(\_h, \_u)   \_h = ([AkFileHandle](_platforms_2_windows_2_ak_types_8h_a2b0b834e6d7c934fb7e04a739f38025d.html#a2b0b834e6d7c934fb7e04a739f38025d))\_u |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| void | [AKPLATFORM::AkClearEvent](namespace_a_k_p_l_a_t_f_o_r_m_a061125f2a77dfbb8ce69ebb5db73595e.html#a061125f2a77dfbb8ce69ebb5db73595e) ([AkEvent](_platforms_2_windows_2_ak_types_8h_a5cc1e7bd24ca284c81adff59c6118ab3.html#a5cc1e7bd24ca284c81adff59c6118ab3) &out\_event) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a061125f2a77dfbb8ce69ebb5db73595e.html#a061125f2a77dfbb8ce69ebb5db73595e) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AKPLATFORM::AkCreateEvent](namespace_a_k_p_l_a_t_f_o_r_m_afc79aa046695b8b19a1fe7032b74c8ab.html#afc79aa046695b8b19a1fe7032b74c8ab) ([AkEvent](_platforms_2_windows_2_ak_types_8h_a5cc1e7bd24ca284c81adff59c6118ab3.html#a5cc1e7bd24ca284c81adff59c6118ab3) &out\_event) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_afc79aa046695b8b19a1fe7032b74c8ab.html#afc79aa046695b8b19a1fe7032b74c8ab) |
|  | |
| void | [AKPLATFORM::AkDestroyEvent](namespace_a_k_p_l_a_t_f_o_r_m_a378049c6bd409da6dae8c59022bb00f1.html#a378049c6bd409da6dae8c59022bb00f1) ([AkEvent](_platforms_2_windows_2_ak_types_8h_a5cc1e7bd24ca284c81adff59c6118ab3.html#a5cc1e7bd24ca284c81adff59c6118ab3) &io\_event) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a378049c6bd409da6dae8c59022bb00f1.html#a378049c6bd409da6dae8c59022bb00f1) |
|  | |
| void | [AKPLATFORM::AkWaitForEvent](namespace_a_k_p_l_a_t_f_o_r_m_af108174bf5afbe899ae3d6937884ec93.html#af108174bf5afbe899ae3d6937884ec93) ([AkEvent](_platforms_2_windows_2_ak_types_8h_a5cc1e7bd24ca284c81adff59c6118ab3.html#a5cc1e7bd24ca284c81adff59c6118ab3) &in\_event) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_af108174bf5afbe899ae3d6937884ec93.html#af108174bf5afbe899ae3d6937884ec93) |
|  | |
| bool | [AKPLATFORM::AkWaitForEvent](namespace_a_k_p_l_a_t_f_o_r_m_adc9240d9a7f06a9891998f485b75d7da.html#adc9240d9a7f06a9891998f485b75d7da) ([AkEvent](_platforms_2_windows_2_ak_types_8h_a5cc1e7bd24ca284c81adff59c6118ab3.html#a5cc1e7bd24ca284c81adff59c6118ab3) &in\_event, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_dwMilliseconds) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_adc9240d9a7f06a9891998f485b75d7da.html#adc9240d9a7f06a9891998f485b75d7da) |
|  | |
| void | [AKPLATFORM::AkSignalEvent](namespace_a_k_p_l_a_t_f_o_r_m_a510e38a878472fe6f62ba64f349a22ce.html#a510e38a878472fe6f62ba64f349a22ce) (const [AkEvent](_platforms_2_windows_2_ak_types_8h_a5cc1e7bd24ca284c81adff59c6118ab3.html#a5cc1e7bd24ca284c81adff59c6118ab3) &in\_event) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a510e38a878472fe6f62ba64f349a22ce.html#a510e38a878472fe6f62ba64f349a22ce) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AKPLATFORM::AkClearSemaphore](namespace_a_k_p_l_a_t_f_o_r_m_a8e439eb37fbc66df59bd8c2112ca748f.html#a8e439eb37fbc66df59bd8c2112ca748f) ([AkSemaphore](_platforms_2_windows_2_ak_types_8h_a36eafa134256295c2e5951282f02ee5a.html#a36eafa134256295c2e5951282f02ee5a) &io\_semaphore) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a8e439eb37fbc66df59bd8c2112ca748f.html#a8e439eb37fbc66df59bd8c2112ca748f) |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AKPLATFORM::AkCreateSemaphore](namespace_a_k_p_l_a_t_f_o_r_m_ac7506e3bf11a0e39d45263004647facb.html#ac7506e3bf11a0e39d45263004647facb) ([AkSemaphore](_platforms_2_windows_2_ak_types_8h_a36eafa134256295c2e5951282f02ee5a.html#a36eafa134256295c2e5951282f02ee5a) &out\_semaphore, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_initialCount) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_ac7506e3bf11a0e39d45263004647facb.html#ac7506e3bf11a0e39d45263004647facb) |
|  | |
| void | [AKPLATFORM::AkDestroySemaphore](namespace_a_k_p_l_a_t_f_o_r_m_aa6e376dc490a6fb6c897ffce6a0edb6c.html#aa6e376dc490a6fb6c897ffce6a0edb6c) ([AkSemaphore](_platforms_2_windows_2_ak_types_8h_a36eafa134256295c2e5951282f02ee5a.html#a36eafa134256295c2e5951282f02ee5a) &io\_semaphore) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_aa6e376dc490a6fb6c897ffce6a0edb6c.html#aa6e376dc490a6fb6c897ffce6a0edb6c) |
|  | |
| void | [AKPLATFORM::AkWaitForSemaphore](namespace_a_k_p_l_a_t_f_o_r_m_a32d0125e85d2949adb9e9597ac69100c.html#a32d0125e85d2949adb9e9597ac69100c) ([AkSemaphore](_platforms_2_windows_2_ak_types_8h_a36eafa134256295c2e5951282f02ee5a.html#a36eafa134256295c2e5951282f02ee5a) &in\_semaphore) |
|  | Platform Independent Helper - Semaphore wait, aka Operation P. Decrements value of semaphore, and, if the semaphore would be less than 0, waits for the semaphore to be released. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a32d0125e85d2949adb9e9597ac69100c.html#a32d0125e85d2949adb9e9597ac69100c) |
|  | |
| void | [AKPLATFORM::AkReleaseSemaphore](namespace_a_k_p_l_a_t_f_o_r_m_a0a50b05f9fadab7c9a7bf2be46a9385b.html#a0a50b05f9fadab7c9a7bf2be46a9385b) ([AkSemaphore](_platforms_2_windows_2_ak_types_8h_a36eafa134256295c2e5951282f02ee5a.html#a36eafa134256295c2e5951282f02ee5a) &in\_semaphore, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_count) |
|  | Platform Independent Helper - Semaphore signal, aka Operation V. Increments value of semaphore by an arbitrary count. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a0a50b05f9fadab7c9a7bf2be46a9385b.html#a0a50b05f9fadab7c9a7bf2be46a9385b) |
|  | |
| void | [AKPLATFORM::PerformanceCounter](namespace_a_k_p_l_a_t_f_o_r_m_a6c599e9422422ecc3f78dd4e7a5644ef.html#a6c599e9422422ecc3f78dd4e7a5644ef) ([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) \*out\_piLastTime) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a6c599e9422422ecc3f78dd4e7a5644ef.html#a6c599e9422422ecc3f78dd4e7a5644ef) |
|  | |
| void | [AKPLATFORM::PerformanceFrequency](namespace_a_k_p_l_a_t_f_o_r_m_a6bd636229ca943158040885acf23c80e.html#a6bd636229ca943158040885acf23c80e) ([AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) \*out\_piFreq) |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a6bd636229ca943158040885acf23c80e.html#a6bd636229ca943158040885acf23c80e) |
|  | |
| void | [AKPLATFORM::UpdatePerformanceFrequency](namespace_a_k_p_l_a_t_f_o_r_m_a7d40760b5695e8137c359ff80a8b9d12.html#a7d40760b5695e8137c359ff80a8b9d12) () |
|  | Platform Independent Helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a7d40760b5695e8137c359ff80a8b9d12.html#a7d40760b5695e8137c359ff80a8b9d12) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AKPLATFORM::Elapsed](namespace_a_k_p_l_a_t_f_o_r_m_abf25104492c057143fc2b19f3ea86909.html#abf25104492c057143fc2b19f3ea86909) (const [AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) &in\_iNow, const [AkInt64](_ak_numeral_types_8h_a3f2533eb6fb2011f230af7474daabc6c.html#a3f2533eb6fb2011f230af7474daabc6c) &in\_iStart) |
|  | Returns a time range in milliseconds, using the sound engine's updated count->milliseconds ratio. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_abf25104492c057143fc2b19f3ea86909.html#abf25104492c057143fc2b19f3ea86909) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AKPLATFORM::AkWideCharToChar](namespace_a_k_p_l_a_t_f_o_r_m_a79c12f8f0710c4772f99b341006af233.html#a79c12f8f0710c4772f99b341006af233) (const wchar\_t \*in\_pszUnicodeString, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiOutBufferSize, char \*io\_pszAnsiString) |
|  | String conversion helper. If io\_pszAnsiString is null, the function returns the required size. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a79c12f8f0710c4772f99b341006af233.html#a79c12f8f0710c4772f99b341006af233) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AKPLATFORM::AkCharToWideChar](namespace_a_k_p_l_a_t_f_o_r_m_a2e556ab1a4cccdcf1ecc139008cd6f09.html#a2e556ab1a4cccdcf1ecc139008cd6f09) (const char \*in\_pszAnsiString, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiOutBufferSize, void \*io\_pvUnicodeStringBuffer) |
|  | String conversion helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a2e556ab1a4cccdcf1ecc139008cd6f09.html#a2e556ab1a4cccdcf1ecc139008cd6f09) |
|  | |
| [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AKPLATFORM::AkUtf8ToWideChar](namespace_a_k_p_l_a_t_f_o_r_m_a57dca045a850746825f81ab78d5a94b8.html#a57dca045a850746825f81ab78d5a94b8) (const char \*in\_pszUtf8String, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiOutBufferSize, void \*io\_pvUnicodeStringBuffer) |
|  | String conversion helper [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a57dca045a850746825f81ab78d5a94b8.html#a57dca045a850746825f81ab78d5a94b8) |
|  | |
| void | [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991) (wchar\_t \*in\_pDest, const wchar\_t \*in\_pSrc, size\_t in\_uDestMaxNumChars) |
|  | Safe unicode string copy. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991) |
|  | |
| void | [AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_ab9230128457df978ab4b0914abe16fdf.html#ab9230128457df978ab4b0914abe16fdf) (char \*in\_pDest, const char \*in\_pSrc, size\_t in\_uDestMaxNumChars) |
|  | Safe string copy. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_ab9230128457df978ab4b0914abe16fdf.html#ab9230128457df978ab4b0914abe16fdf) |
|  | |
| void | [AKPLATFORM::SafeStrCat](namespace_a_k_p_l_a_t_f_o_r_m_a12fd4acd1971bead09935c8c9f12ed33.html#a12fd4acd1971bead09935c8c9f12ed33) (wchar\_t \*in\_pDest, const wchar\_t \*in\_pSrc, size\_t in\_uDestMaxNumChars) |
|  | Safe unicode string concatenation. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a12fd4acd1971bead09935c8c9f12ed33.html#a12fd4acd1971bead09935c8c9f12ed33) |
|  | |
| void | [AKPLATFORM::SafeStrCat](namespace_a_k_p_l_a_t_f_o_r_m_a0503e2b62671e9f92564d27425b0f085.html#a0503e2b62671e9f92564d27425b0f085) (char \*in\_pDest, const char \*in\_pSrc, size\_t in\_uDestMaxNumChars) |
|  | Safe string concatenation. [更多...](namespace_a_k_p_l_a_t_f_o_r_m_a0503e2b62671e9f92564d27425b0f085.html#a0503e2b62671e9f92564d27425b0f085) |
|  | |
| int | [AKPLATFORM::SafeStrFormat](namespace_a_k_p_l_a_t_f_o_r_m_a2977916c5e7a44e7362ee73f68af0412.html#a2977916c5e7a44e7362ee73f68af0412) (wchar\_t \*in\_pDest, size\_t in\_uDestMaxNumChars, const wchar\_t \*in\_pszFmt,...) |
|  | |
| int | [AKPLATFORM::SafeStrFormat](namespace_a_k_p_l_a_t_f_o_r_m_af0d57b8643c134721797c519b87c3977.html#af0d57b8643c134721797c519b87c3977) (char \*in\_pDest, size\_t in\_uDestMaxNumChars, const char \*in\_pszFmt,...) |
|  | |
| void | [AKPLATFORM::OutputDebugMsg](namespace_a_k_p_l_a_t_f_o_r_m_af1c96c7db4b10a7b52fd69072d5f4472.html#af1c96c7db4b10a7b52fd69072d5f4472) (const wchar\_t \*in\_pszMsg) |
|  | Output a debug message on the console [更多...](namespace_a_k_p_l_a_t_f_o_r_m_af1c96c7db4b10a7b52fd69072d5f4472.html#af1c96c7db4b10a7b52fd69072d5f4472) |
|  | |
| void | [AKPLATFORM::OutputDebugMsg](namespace_a_k_p_l_a_t_f_o_r_m_ab89509783de099f2b2fb82a2cdf0bb96.html#ab89509783de099f2b2fb82a2cdf0bb96) (const char \*in\_pszMsg) |
|  | Output a debug message on the console [更多...](namespace_a_k_p_l_a_t_f_o_r_m_ab89509783de099f2b2fb82a2cdf0bb96.html#ab89509783de099f2b2fb82a2cdf0bb96) |
|  | |
| template<int MaxSize = 256> | |
| void | [AKPLATFORM::OutputDebugMsgV](namespace_a_k_p_l_a_t_f_o_r_m_ac11ab17883b9df951f2523abd90b7128.html#ac11ab17883b9df951f2523abd90b7128) (const wchar\_t \*in\_pszFmt,...) |
|  | |
| template<int MaxSize = 256> | |
| void | [AKPLATFORM::OutputDebugMsgV](namespace_a_k_p_l_a_t_f_o_r_m_a354421a9be233e3d0b0b98ddaad070cc.html#a354421a9be233e3d0b0b98ddaad070cc) (const char \*in\_pszFmt,...) |
|  | |
| size\_t | [AKPLATFORM::AkUtf16StrLen](namespace_a_k_p_l_a_t_f_o_r_m_a22c16a9b7b6b4a94491d31730560aaef.html#a22c16a9b7b6b4a94491d31730560aaef) (const [AkUtf16](_platforms_2_windows_2_ak_types_8h_aa322c734de4000b9c01ce3c033b59089.html#aa322c734de4000b9c01ce3c033b59089) \*in\_pStr) |
|  | |
| size\_t | [AKPLATFORM::OsStrLen](namespace_a_k_p_l_a_t_f_o_r_m_ad4940495c382a07f11c564e1298d5d9f.html#ad4940495c382a07f11c564e1298d5d9f) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszString) |
|  | |
| int | [AKPLATFORM::OsStrCmp](namespace_a_k_p_l_a_t_f_o_r_m_aa4d3bbb3488b0a5d9ab994ab9b680ca2.html#aa4d3bbb3488b0a5d9ab994ab9b680ca2) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszString1, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszString2) |
|  | |
| int | [AKPLATFORM::OsStrNCmp](namespace_a_k_p_l_a_t_f_o_r_m_a530cbc829ff1268191fca28373974590.html#a530cbc829ff1268191fca28373974590) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszString1, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszString2, size\_t in\_MaxCountSize) |
|  | |
| bool | [AKPLATFORM::IsAbsolutePath](namespace_a_k_p_l_a_t_f_o_r_m_ab7ff888132d7fd9652abec59b37b12ae.html#ab7ff888132d7fd9652abec59b37b12ae) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszPath, size\_t in\_pathLen) |
|  | Detects whether the string represents an absolute path to a file [更多...](namespace_a_k_p_l_a_t_f_o_r_m_ab7ff888132d7fd9652abec59b37b12ae.html#ab7ff888132d7fd9652abec59b37b12ae) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AK::g\_fFreqRatio](namespace_a_k_a67247c5e540637806c96c648d281bbda.html#a67247c5e540637806c96c648d281bbda) |
|  | |