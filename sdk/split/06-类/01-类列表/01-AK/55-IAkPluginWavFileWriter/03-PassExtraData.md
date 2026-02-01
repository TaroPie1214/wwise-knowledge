# PassExtraData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginWavFileWriter](class_a_k_1_1_i_ak_plugin_wav_file_writer.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [Destroy](class_a_k_1_1_i_ak_plugin_wav_file_writer_af2bbf829a294612781e6016ad225517a.html#af2bbf829a294612781e6016ad225517a) | | [PassAudioData](class_a_k_1_1_i_ak_plugin_wav_file_writer_a47e314a49b194f5a7068f3c2bb6f763c.html#a47e314a49b194f5a7068f3c2bb6f763c) | | [PassExtraData](class_a_k_1_1_i_ak_plugin_wav_file_writer_ac9b3924f3079c9253685a3c6c5b4d28d.html#ac9b3924f3079c9253685a3c6c5b4d28d) | | [◆](#ac9b3924f3079c9253685a3c6c5b4d28d)PassExtraData() |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) AK::IAkPluginWavFileWriter::PassExtraData | ( | void \* | *in\_pData*, | |  |  | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | *in\_size* | |  | ) |  |  | | pure virtual |  Pass extra data to be written as-is after the data chunk of the wav file, including any associated wav chunk header.  参数  |  |  | | --- | --- | | in\_pData | Pointer to extra data | | in\_size | Size of extra data | |