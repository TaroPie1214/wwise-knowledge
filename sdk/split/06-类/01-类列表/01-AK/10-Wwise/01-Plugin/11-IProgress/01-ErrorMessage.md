# ErrorMessage

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [IProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ErrorMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a8e380c8480d74520139fbeffca5b9089.html#a8e380c8480d74520139fbeffca5b9089) | | [IsCancelled](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a17958067a0608c0bbd4fc1556b7f8767.html#a17958067a0608c0bbd4fc1556b7f8767) | | [NotifyProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a60e742bd2d53086e978e45c62a1415d1.html#a60e742bd2d53086e978e45c62a1415d1) | | [SetCurrentOperationName](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a614204cbb0b851b0c87cafde36ee4330.html#a614204cbb0b851b0c87cafde36ee4330) | | [SetRange](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_af8e34a3d90e226e19de4cfa63b09fb38.html#af8e34a3d90e226e19de4cfa63b09fb38) | | [◆](#a8e380c8480d74520139fbeffca5b9089)ErrorMessage() |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual void AK.Wwise::Plugin::IProgress::ErrorMessage | ( | const char \* | *in\_rErrorText*, | |  |  | [Severity](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) | *in\_eSeverity* = `Severity_Warning` | |  | ) |  |  | | pure virtual |  Display an error message to the user. The message should be on a single line. |