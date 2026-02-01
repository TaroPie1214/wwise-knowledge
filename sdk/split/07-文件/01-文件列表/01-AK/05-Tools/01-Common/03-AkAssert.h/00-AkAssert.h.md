# AkAssert.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[宏定义](#define-members)

AkAssert.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_assert_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)(Condition)   do { switch ( 0 ) { case 0: break; default: if ( !( Condition ) ) {} } } while ( 0 ) |
|  | |
| #define | [AKVERIFY](_ak_assert_8h_a7cad688743dfea863122787fe71bce27.html#a7cad688743dfea863122787fe71bce27)(x)   ((void)(x)) |
|  | |
| #define | [AK\_IS\_ASSERT\_HOOKED](_ak_assert_8h_a5884d82f3fbd18205c7baf1340ce8dc7.html#a5884d82f3fbd18205c7baf1340ce8dc7)   (false) |
|  | |
| #define | [AKASSERTD](_ak_assert_8h_a00dc614bb13cadd39785870ac7fa2d09.html#a00dc614bb13cadd39785870ac7fa2d09)(Condition)   ((void)0) |
|  | |
| #define | [AKASSERT\_RANGE](_ak_assert_8h_a0c76cf87cb77b1e74a3cdcb9de7f6777.html#a0c76cf87cb77b1e74a3cdcb9de7f6777)(Value, Min, Max)   ([AKASSERT](_ak_assert_8h_ac0e6cc4061c0a7c154a8c921a0af74cb.html#ac0e6cc4061c0a7c154a8c921a0af74cb)(((Value) >= (Min)) && ((Value) <= (Max)))) |
|  | |
| #define | [AKASSERTANDRETURN](_ak_assert_8h_a89461dec0452e3376a360cd54c903050.html#a89461dec0452e3376a360cd54c903050)(\_\_Expression, \_\_ErrorCode) |
|  | |
| #define | [AKASSERTPOINTERORFAIL](_ak_assert_8h_a72825f9f4080d246ee46ae10b449f1af.html#a72825f9f4080d246ee46ae10b449f1af)(\_\_Pointer)   [AKASSERTANDRETURN](_ak_assert_8h_a89461dec0452e3376a360cd54c903050.html#a89461dec0452e3376a360cd54c903050)( \_\_Pointer != NULL, [AK\_Fail](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63a904c9822fd2d40bb0ea6bfad9ead659b) ) |
|  | |
| #define | [AKASSERTSUCCESSORRETURN](_ak_assert_8h_a0239ab339d7b565ded591ba997077e50.html#a0239ab339d7b565ded591ba997077e50)(\_\_akr)   [AKASSERTANDRETURN](_ak_assert_8h_a89461dec0452e3376a360cd54c903050.html#a89461dec0452e3376a360cd54c903050)( \_\_akr == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e), \_\_akr ) |
|  | |
| #define | [AKASSERTPOINTERORRETURN](_ak_assert_8h_a32029a1b927d3609e2db585d29d27e3b.html#a32029a1b927d3609e2db585d29d27e3b)(\_\_Pointer) |
|  | |
| #define | [AKSTATICASSERT](_ak_assert_8h_a1c6d871d2dfc01214622dd25cf8ccd25.html#a1c6d871d2dfc01214622dd25cf8ccd25)(\_\_expr\_\_, \_\_msg\_\_)   typedef char \_\_AKSTATICASSERT\_\_[(\_\_expr\_\_)?1:-1] |
|  | |