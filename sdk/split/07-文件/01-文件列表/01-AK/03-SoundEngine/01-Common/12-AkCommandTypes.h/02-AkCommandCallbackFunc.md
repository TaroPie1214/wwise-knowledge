# AkCommandCallbackFunc

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)
- [AkCommandTypes.h](_ak_command_types_8h.html)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkCommand](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfd) | | [AkCommand\_t](_ak_command_types_8h_a0ed0dc74e5d2f23c676b705b31df3a1b.html#a0ed0dc74e5d2f23c676b705b31df3a1b) | | [AkCommandCallbackFunc](_ak_command_types_8h_adf806f94d5311616d788b6b479caac85.html#adf806f94d5311616d788b6b479caac85) | | [◆](#adf806f94d5311616d788b6b479caac85)AkCommandCallbackFunc |  | | --- | | typedef void( \* AkCommandCallbackFunc) (void \*in\_pCookie) |  Function called when processing the command AkCommand\_Callback.  备注  This callback is executed from the audio processing thread. The processing time in the callback function should be minimal. Having too much processing time could result in slowing down the audio processing.  在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [134](_ak_command_types_8h_source.html#l00134) 行定义. |