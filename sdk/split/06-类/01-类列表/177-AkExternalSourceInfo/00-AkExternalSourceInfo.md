# AkExternalSourceInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_external_source_info-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkExternalSourceInfo结构体 参考

`#include <AkSoundEngineTypes.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkExternalSourceInfo](struct_ak_external_source_info_aadca68de3836d3a3f09d38692d654975.html#aadca68de3836d3a3f09d38692d654975) () |
|  | Default constructor. [更多...](struct_ak_external_source_info_aadca68de3836d3a3f09d38692d654975.html#aadca68de3836d3a3f09d38692d654975) |
|  | |
|  | [AkExternalSourceInfo](struct_ak_external_source_info_a27cb9c0e9d174362467bebf3b7271fc4.html#a27cb9c0e9d174362467bebf3b7271fc4) (void \*in\_pInMemory, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiMemorySize, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_iExternalSrcCookie, [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) in\_idCodec) |
|  | Constructor: specify source by memory. [更多...](struct_ak_external_source_info_a27cb9c0e9d174362467bebf3b7271fc4.html#a27cb9c0e9d174362467bebf3b7271fc4) |
|  | |
|  | [AkExternalSourceInfo](struct_ak_external_source_info_a1ff2f5e1cf304ee76c754c69cd78a0ca.html#a1ff2f5e1cf304ee76c754c69cd78a0ca) (const char \*in\_pszFileName, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_iExternalSrcCookie, [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) in\_idCodec) |
|  | Constructor: specify source by streaming file name. [更多...](struct_ak_external_source_info_a1ff2f5e1cf304ee76c754c69cd78a0ca.html#a1ff2f5e1cf304ee76c754c69cd78a0ca) |
|  | |
|  | [AkExternalSourceInfo](struct_ak_external_source_info_ac30289ccfb1a5bffa38567c0775f08a7.html#ac30289ccfb1a5bffa38567c0775f08a7) ([AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_idFile, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_iExternalSrcCookie, [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) in\_idCodec) |
|  | Constructor: specify source by streaming file ID. [更多...](struct_ak_external_source_info_ac30289ccfb1a5bffa38567c0775f08a7.html#ac30289ccfb1a5bffa38567c0775f08a7) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [iExternalSrcCookie](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77) |
|  | Cookie identifying the source, given by hashing the name of the source given in the project. See [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d). [更多...](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77) |
|  | |
| [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) | [idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) |
|  | Codec ID for the file. One of the audio formats defined in AkTypes.h (AKCODECID\_XXX) [更多...](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) |
|  | |
| const char \* | [szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) |
|  | UTF-8 File path for the source. If not NULL, the source will be streaming from disk. Set pInMemory to NULL. If idFile is set, this field is used as stream name (for profiling purposes). The only file formats accepted are a fully formed WEM file, as converted by Wwise, or a standard WAV file. [更多...](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) |
|  | |
| void \* | [pInMemory](struct_ak_external_source_info_a5eda2911fdb2f31d42474eb8e62218ac.html#a5eda2911fdb2f31d42474eb8e62218ac) |
|  | Pointer to the in-memory file. If not NULL, the source will be read from memory. Set szFile and idFile to NULL. The only file format accepted is a fully formed WEM file, as converted by Wwise. [更多...](struct_ak_external_source_info_a5eda2911fdb2f31d42474eb8e62218ac.html#a5eda2911fdb2f31d42474eb8e62218ac) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uiMemorySize](struct_ak_external_source_info_a32be3912e313caa6c1882103292c58b8.html#a32be3912e313caa6c1882103292c58b8) |
|  | Size of the data pointed by pInMemory [更多...](struct_ak_external_source_info_a32be3912e313caa6c1882103292c58b8.html#a32be3912e313caa6c1882103292c58b8) |
|  | |
| [AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) | [idFile](struct_ak_external_source_info_aa97a8c8dfdd8e18a508bac3045ae71c8.html#aa97a8c8dfdd8e18a508bac3045ae71c8) |
|  | File ID. If not zero, the source will be streaming from disk. This ID can be anything. Note that you must override the low-level IO to resolve this ID to a real file. See [Low-Level I/O](streamingmanager_lowlevel.html) for more information on overriding the Low Level IO. [更多...](struct_ak_external_source_info_aa97a8c8dfdd8e18a508bac3045ae71c8.html#aa97a8c8dfdd8e18a508bac3045ae71c8) |
|  | |

## 详细描述

This structure allows the game to provide audio files to fill the external sources. See [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) You can specify a streaming file or a file in-memory, regardless of the "Stream" option in the Wwise project. The recommended format is a fully formed WEM file, as converted by Wwise. WAV files are also supported, but only in file streaming mode and with some limitations (e.g. PCM samples only, exotic channel configurations may not work as expected)

|  |  |
| --- | --- |
|  | **警告:** Make sure that only one of szFile, pInMemory or idFile is non-null. if both idFile and szFile are set, idFile is passed to low-level IO and szFile is used as stream name (for profiling purposes). |

|  |  |
| --- | --- |
|  | **警告:** When using the in-memory file (pInMemory & uiMemorySize), it is the responsibility of the game to ensure the memory stays valid for the entire duration of the playback. You can achieve this by using the AK\_EndOfEvent callback to track when the Event ends. |

参见
:   - [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

在文件 [AkSoundEngineTypes.h](_ak_sound_engine_types_8h_source.html) 第 [127](_ak_sound_engine_types_8h_source.html#l00127) 行定义.