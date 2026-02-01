# GetCreationMessage

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1_adb5c5fc3786aa19b5e4cac479483ccd1.html#adb5c5fc3786aa19b5e4cac479483ccd1) | | [GetCreationMessage](structak__wwise__plugin__first__time__creation__message__v1_ad0ebe12f6bfd42d23870916e3dc5c7b1.html#ad0ebe12f6bfd42d23870916e3dc5c7b1) | | [GetKey](structak__wwise__plugin__first__time__creation__message__v1_a16dee487f9b91bf1b3f912d6e14a1d43.html#a16dee487f9b91bf1b3f912d6e14a1d43) | | [Instance](structak__wwise__plugin__first__time__creation__message__v1_a1c9a5836249ac8dae52e0819ce04e372.html#a1c9a5836249ac8dae52e0819ce04e372) | | [◆](#ad0ebe12f6bfd42d23870916e3dc5c7b1)GetCreationMessage |  | | --- | | const char\*(\* ak\_wwise\_plugin\_first\_time\_creation\_message\_v1::GetCreationMessage) (const struct [ak\_wwise\_plugin\_first\_time\_creation\_message\_instance\_v1](structak__wwise__plugin__first__time__creation__message__instance__v1.html) \*in\_this) |  Returns a unique creation message shown to the user.  Shown when the plug-in is first created and the key is not present in the .wproj yet.  参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. |  返回  Null-terminated string containing the text to show to the end user.  在文件 [FirstTimeCreationMessage.h](_first_time_creation_message_8h_source.html) 第 [77](_first_time_creation_message_8h_source.html#l00077) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V1::FirstTimeCreationMessage::Interface::Interface()](_first_time_creation_message_8h_source.html#l00130). |