# External Source（外部源）

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > External Source（外部源）

## External Source（外部源）

In Wwise, each sound object is linked to a specific source. The source is the sound that
plays, for example, when triggered by an Event. Typically, the source is an audio file found
in a static SoundBank that is generated before the game is played.

With the External Source plug-in, the source can be an audio file that is not part of a
SoundBank. Instead, the file is provided externally and loaded dynamically at runtime. This
is especially useful for scenarios where there are large numbers of sounds. Without the
plug-in, you would need to create a sound object and an Event in Wwise for each sound, and
manage the resulting SoundBanks. The plug-in also supports the playback of audio generated
at runtime, such as that based on user input or preferences.

However, compared to using precompiled SoundBanks, the External Source plug-in introduces
complexity to the workflow, and some manual setup in the Wwise SDK. For detailed
instructions, see the [Integrating External Sources](https://www.audiokinetic.com/library/?source=SDK&id=integrating__external__sources.html) and [Using External Sources](https://www.audiokinetic.com/en/library/edge/?source=UE4&id=using_features_ext_src.html) sections of the Wwise SDK documentation. It also requires
implementation in Wwise Authoring, as in this example:

1. On a sound object, add an External Source:

   1. Open the Contents Editor of the sound object. 请参阅 [“Sound objects”一节](../../../08-使用-Wwise/04-认识-Contents-Editor-视图/01-Sound-objects.md "Sound objects")。
   2. Click **Add Source**, and select **External Source**.
   3. In the Contents Editor, if multiple SFXs are present, select the one to use in the
      **Use** column. For this and other
      properties, see [“Contents Editor：External Source”一节](01-Contents-Editor：External-Source.md "Contents Editor：External Source").
2. Create a play Event with the sound object as its Target.
3. Add the Event to a SoundBank, unless **Enable Auto-Defined
   SoundBanks** is enabled in the [“SoundBanks 选项卡”一节](../../../09-参考主题/01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡").
4. Add the target sound files to the External Sources List file. This is an XML file
   containing paths to your input files and their conversion settings. WAV files must
   be converted to WEM to be used by the sound engine at runtime. The conversion can be
   done either when the banks are generated, or by the audio programmer from the [Wwise command line](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=bankscommandline.html).
5. In Project Settings, set the location of the External Sources List file, and the directory for the converted output files. 请参阅 [“为 External Source 指定工程设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/06-为-External-Source-指定工程设置.md "为 External Source 指定工程设置")。To override these project settings for your user, go to the [“SoundBanks Settings - External Sources 选项卡”一节](../../../09-参考主题/02-视图/09-SoundBank-Manager-视图/01-SoundBanks-Settings-对话框/02-SoundBanks-Settings-External-Sources-选项卡.md "SoundBanks Settings - External Sources 选项卡") and enable **Override Project SoundBank Settings**.

---