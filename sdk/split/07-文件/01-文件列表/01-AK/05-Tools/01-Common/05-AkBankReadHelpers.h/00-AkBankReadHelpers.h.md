# AkBankReadHelpers.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[命名空间](#namespaces) |
[宏定义](#define-members) |
[函数](#func-members)

AkBankReadHelpers.h 文件参考

`#include <AK/Tools/Common/AkPlatformFuncs.h>`  
`#include <type_traits>`

[浏览源代码.](_ak_bank_read_helpers_8h_source.html)

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [READBANKDATA](_ak_bank_read_helpers_8h_a18513ab855bc8316634d74b9a17138c5.html#a18513ab855bc8316634d74b9a17138c5)(\_Type, \_Ptr, \_Size)    [AK::ReadBankData](namespace_a_k_af3f9275781a5ff20cf5b7adf136cb510.html#af3f9275781a5ff20cf5b7adf136cb510)<\_Type>( \_Ptr ) |
|  | Read and return bank data of a given type, incrementing running pointer and decrementing block size for debug tracking purposes [更多...](_ak_bank_read_helpers_8h_a18513ab855bc8316634d74b9a17138c5.html#a18513ab855bc8316634d74b9a17138c5) |
|  | |
| #define | [READVARIABLESIZEBANKDATA](_ak_bank_read_helpers_8h_a4b95136204a1804681c5cc2a2213497c.html#a4b95136204a1804681c5cc2a2213497c)(\_Type, \_Ptr, \_Size)    [AK::ReadVariableSizeBankData](namespace_a_k_a5b317b41042b34c0cca22dfb3f56e0eb.html#a5b317b41042b34c0cca22dfb3f56e0eb)<\_Type>( \_Ptr ) |
|  | |
| #define | [READBANKSTRING](_ak_bank_read_helpers_8h_af813417cb61114d2cc32debba6cc0fd6.html#af813417cb61114d2cc32debba6cc0fd6)(\_Ptr, \_Size, \_out\_StringSize)    [AK::ReadBankStringUtf8](namespace_a_k_a5924b0008326f24e29cb9bdeb9f611c0.html#a5924b0008326f24e29cb9bdeb9f611c0)( \_Ptr, \_out\_StringSize ) |
|  | |
| #define | [SKIPBANKDATA](_ak_bank_read_helpers_8h_a13114359dc06c2788d5141dcd31933b6.html#a13114359dc06c2788d5141dcd31933b6)(\_Type, \_Ptr, \_Size)    ( \_Ptr ) += sizeof( \_Type ) |
|  | Skip over some bank data of a given type, incrementing running pointer and decrementing block size for debug tracking purposes [更多...](_ak_bank_read_helpers_8h_a13114359dc06c2788d5141dcd31933b6.html#a13114359dc06c2788d5141dcd31933b6) |
|  | |
| #define | [SKIPBANKBYTES](_ak_bank_read_helpers_8h_a6e59e6f0fcd4de1f81a2bdc3d734fb48.html#a6e59e6f0fcd4de1f81a2bdc3d734fb48)(\_NumBytes, \_Ptr, \_Size)    ( \_Ptr ) += \_NumBytes; |
|  | Skip over some bank data by a given size in bytes, incrementing running pointer and decrementing block size for debug tracking purposes [更多...](_ak_bank_read_helpers_8h_a6e59e6f0fcd4de1f81a2bdc3d734fb48.html#a6e59e6f0fcd4de1f81a2bdc3d734fb48) |
|  | |
| #define | [COPYBANKSTRING\_CHAR](_ak_bank_read_helpers_8h_ac19dc056fd4415f5be43cc166f1f2339.html#ac19dc056fd4415f5be43cc166f1f2339)(\_Ptr, \_Size, \_OutPtr, \_MaxPtrSize) |
|  | Read and copy to a null-terminated UTF-8 string conversion from string stored in bank. [更多...](_ak_bank_read_helpers_8h_ac19dc056fd4415f5be43cc166f1f2339.html#ac19dc056fd4415f5be43cc166f1f2339) |
|  | |
| #define | [COPYBANKSTRING\_OSCHAR](_ak_bank_read_helpers_8h_a63718c2ee59b9c1f671debd9e606c7f1.html#a63718c2ee59b9c1f671debd9e606c7f1)(\_Ptr, \_Size, \_OutPtr, \_MaxPtrSize) |
|  | Read and copy to a null-terminated OSChar string conversion from string stored in bank. [更多...](_ak_bank_read_helpers_8h_a63718c2ee59b9c1f671debd9e606c7f1.html#a63718c2ee59b9c1f671debd9e606c7f1) |
|  | |
| #define | [COPYBANKSTRING\_WCHAR](_ak_bank_read_helpers_8h_ab694de4575d1a1d4504a84e8905b42df.html#ab694de4575d1a1d4504a84e8905b42df)(\_Ptr, \_Size, OutPtr, \_MaxPtrSize) |
|  | Read and copy to a null-terminated wchar\_t string conversion from string stored in bank. [更多...](_ak_bank_read_helpers_8h_ab694de4575d1a1d4504a84e8905b42df.html#ab694de4575d1a1d4504a84e8905b42df) |
|  | |
| #define | [GETBANKDATABIT](_ak_bank_read_helpers_8h_a3c4df010f47861c232a6df1b52d8e105.html#a3c4df010f47861c232a6df1b52d8e105)(\_Data, \_Shift)    (((\_Data) >> (\_Shift)) & 0x1) |
|  | |
| #define | [CHECKBANKDATASIZE](_ak_bank_read_helpers_8h_a50c3e7712a0452bd3ee8d5ac2185d2cf.html#a50c3e7712a0452bd3ee8d5ac2185d2cf)(\_DATASIZE\_, \_ERESULT\_) |
|  | Helper macro to determine whether the full content of a block of memory was properly parsed [更多...](_ak_bank_read_helpers_8h_a50c3e7712a0452bd3ee8d5ac2185d2cf.html#a50c3e7712a0452bd3ee8d5ac2185d2cf) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| template<typename T , typename std::enable\_if< std::is\_fundamental< T >::value||std::is\_enum< T >::value, bool >::type = true> | |
| T | [AK::ReadUnaligned](namespace_a_k_a2eec40204264e1de9dc544696a0a723f.html#a2eec40204264e1de9dc544696a0a723f) (const [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*in\_pVal) |
|  | |
| template<typename T , typename std::enable\_if< std::is\_fundamental< T >::value||std::is\_enum< T >::value, bool >::type = true> | |
| void | [AK::WriteUnaligned](namespace_a_k_a01491bfff846cdedfde144b44f8ba45d.html#a01491bfff846cdedfde144b44f8ba45d) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*out\_pVal, const T in\_val) |
|  | |
| template<typename T , typename std::enable\_if< std::is\_class< T >::value, bool >::type = true> | |
| void | [AK::WriteUnaligned](namespace_a_k_a5e1e105a0e624d4b5998668786b9eddb.html#a5e1e105a0e624d4b5998668786b9eddb) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*out\_pVal, const T &in\_val) |
|  | |
| template<typename T > | |
| T | [AK::ReadBankData](namespace_a_k_af3f9275781a5ff20cf5b7adf136cb510.html#af3f9275781a5ff20cf5b7adf136cb510) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*&in\_rptr) |
|  | Read data from bank and advance pointer. [更多...](namespace_a_k_af3f9275781a5ff20cf5b7adf136cb510.html#af3f9275781a5ff20cf5b7adf136cb510) |
|  | |
| template<typename T > | |
| T | [AK::ReadVariableSizeBankData](namespace_a_k_a5b317b41042b34c0cca22dfb3f56e0eb.html#a5b317b41042b34c0cca22dfb3f56e0eb) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*&in\_rptr) |
|  | |
| char \* | [AK::ReadBankStringUtf8](namespace_a_k_a5924b0008326f24e29cb9bdeb9f611c0.html#a5924b0008326f24e29cb9bdeb9f611c0) ([AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) \*&in\_rptr, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &out\_uStringSize) |
|  | |