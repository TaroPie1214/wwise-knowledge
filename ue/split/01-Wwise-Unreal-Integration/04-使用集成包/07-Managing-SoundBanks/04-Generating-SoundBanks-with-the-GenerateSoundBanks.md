# Generating SoundBanks with the GenerateSoundBanks Commandlet

|  |
| --- |
| Wwise Unreal Integration Documentation |

Generating SoundBanks with the GenerateSoundBanks Commandlet

The Wwise Unreal plug-in includes a Commandlet you can use to generate SoundBanks and submit them to source control from the command line.

|  |  |
| --- | --- |
|  | **注記：** The GenerateSoundBanks Commandlet is now deprecated. You can use the Wwise Console to generate SoundBanks instead. See [Generating all the SoundBanks](https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_cli_generatesoundbank_example_generating_all_the_soundbanks.html) for more information. |

Commandlet 用法：

<UnrealEditor-cmd.exe> <path\_to\_uproject> -run=GenerateSoundBanks [-platforms=listOfPlatforms] [-languages=listOfLanguages] [-wwiseConsolePath=pathToWwiseConsole]

The Commandlet has the following parameters:

- **platforms**: (Optional) Comma-separated list of platforms for which to generate SoundBanks, as specified in the Wwise project. If not specified, SoundBanks are generated for all platforms.
- **languages**: (Optional) Comma-separated list of Languages for which to generate SoundBanks, as specified in the Wwise project. 若未指定，则将针对所有语言生成 SoundBank。
- **wwiseConsolePath**: (Optional) Full path to the Wwise command-line tool, used to generate the SoundBanks. If not specified, the path from the Wwise settings is used.
- **help**：（可选）输出此帮助消息。此项会马上终止 Commandlet。

使用示例：

C:\UE\_5.0\Engine\Binaries\Win64\UnrealEditor-Cmd.exe C:\MyProjects\Demo\WwiseDemoGame.uproject -run=GenerateSoundBanks -platforms=Windows,Mac

|  |  |
| --- | --- |
|  | **注記：** If you have problems because the Development Editor is not built or available yet, you can skip the plug-in activation by setting the environment variable `SKIP_PLUGIN_ACTIVATION` to `true`. |