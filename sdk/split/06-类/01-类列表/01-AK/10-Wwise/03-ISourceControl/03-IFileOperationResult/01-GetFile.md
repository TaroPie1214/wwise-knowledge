# GetFile

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html)
- [IFileOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetFile](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_ae68be19e4a417667d831affe84f73e51.html#ae68be19e4a417667d831affe84f73e51) | | [GetFileCount](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a1a0a60903c3186af3a59292d3e6e82df.html#a1a0a60903c3186af3a59292d3e6e82df) | | [GetMovedFile](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a33726538aaac562be5b32de46f18b34e.html#a33726538aaac562be5b32de46f18b34e) | | [◆](#ae68be19e4a417667d831affe84f73e51)GetFile() |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual void AK.Wwise::ISourceControl::IFileOperationResult::GetFile | ( | unsigned int | *in\_uiIndex*, | |  |  | LPWSTR | *out\_szPath*, | |  |  | unsigned int | *in\_uiArraySize* | |  | ) |  |  | | pure virtual |  Return the successful file at index in\_uiIndex  参数  |  |  | | --- | --- | | in\_uiIndex | in: The index of the file. Must be >= 0 and < [GetFileCount()](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a1a0a60903c3186af3a59292d3e6e82df.html#a1a0a60903c3186af3a59292d3e6e82df "Returns how many files were moved during the operation") | | out\_szPath | out: String buffer to receive the source path | | in\_uiArraySize | in: Size of the buffers (out\_szFrom and out\_szTo) | |