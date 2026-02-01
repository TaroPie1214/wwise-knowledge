# Combining Unreal and Wwise Audio with AudioLink

|  |
| --- |
| Wwise Unreal Integration Documentation |

Combining Unreal and Wwise Audio with AudioLink

Starting with version 5.1, Unreal includes a tool called [AudioLink](https://dev.epicgames.com/documentation/en-us/unreal-engine/audiolink). When you are developing audio for Unreal games, you can use Wwise or Unreal exclusively or, through AudioLink, use both systems together. This flexibility gives users the ability to create some sounds in Unreal during game development, but also use Wwise for advanced audio effects such as Spatial Audio.

In the context of the Wwise Unreal 集成, AudioLink can help two types of user:

- Wwise users who want to route Unreal Audio through Wwise.
- Unreal users who want to add Wwise features to their projects but also want to keep any Unreal audio work they have already completed.

In addition, after you enable AudioLink and configure your Unreal and Wwise projects appropriately, you can then listen to audio in Unreal and monitor the audio with the Wwise Profiler simultaneously.

# Selecting Audio Routing Options

There are several options for audio routing available in the Unreal Project Settings.

**To select an audio routing option:**

1. In Unreal, click **Edit** > **Project Settings**. The Project Settings dialog opens.
2. In the Wwise section, click **Integration Settings**. The Initialization section contains several audio routing options:  

   ![](../../../images/audiolink_settings.png)

   The Unreal Audio Routing menu contains the following options:
   - **Default**: Supports custom configurations and projects that were migrated from integration versions lower than 2022.1. If you select this option, you can manually select or clear the three checkboxes that follow. However, there are no limits on your selections or any automatic verification, so it is your responsibility to test your audio and ensure that your custom routing configuration works properly.
   - **Both Wwise and Unreal audio**: Use the Unreal audio system and the Wwise SoundEngine concurrently.  

     |  |  |
     | --- | --- |
     |  | **注記：** This option might not be compatible with all platforms. |
   - **Route through AudioLink**: Use AudioLink to route all Unreal audio sources to Wwise SoundEngine inputs. This option requires Unreal 5.1 or higher.
   - **Enable Wwise SoundEngine only**: Use Wwise for audio and disable the Unreal audio system.
   - **Enable Unreal Audio only**: Use Unreal Audio and disable the Wwise SoundEngine.

     |  |  |
     | --- | --- |
     |  | **注記：** After you select an option, do not change it. If you do, any existing AudioLink components will stop working. |
3. Select the desired audio routing option. For AudioLink, select **Route through AudioLink**.

# Setting Samples Per Frame and Callback Buffer Frame Sizes

After you enable AudioLink, some additional manual configuration might be required to ensure smooth audio playback during gameplay. You must ensure that platform-specific samples per frame values in Unreal correspond to callback buffer frame sizes in the Wwise project `.ini` files. Depending on your project settings and version of Wwise, you might not have to change anything but we recommend that you confirm that you follow the procedure anyway to confirm that the values are the same.

**To match the Unreal values with the Wwise configuration files:**

1. In Unreal, click **Edit** > **Project Settings**. The Project Settings dialog opens.
2. In the Wwise section, select a platform. The Wwise - {Platform} page opens.
3. Under Initialization > Common Settings, note the value of the Samples Per Frame setting:

   ![](../../../images/audiolink_samples_callback.png)
4. In Windows, navigate to the Unreal project directory and open the following files:
   - `..\{ProjectDirectory}\Config\DefaultEngine.ini`
   - `..\{ProjectDirectory}\Config\{Platform}\{Platform}Engine.ini` (if you have set platform-specific values)
5. Note the value of the `AudioCallbackBufferFrameSize` setting.
6. If the values in the `.ini` files are different than the values of the Samples Per Frame setting in Unreal, adjust one or the other as required to ensure that they match.
7. Repeat the preceding steps for all platforms in your project.

# Setting Default AudioLink Properties

AudioLink configuration settings determine its default behavior when enabled. The integration uses these default values unless there is an override asset associated with a particular Event (as described in [Overriding Default AudioLink Properties](using_audio_link.html#using_audio_link_override)).

Before you begin the following procedure, set up an [Audio Input Source Plug-in](https://www.audiokinetic.com/library/edge/?source=SDK&id=referencematerial_audioinput.html) in Wwise and create a Wwise "Play" Event that uses a Sound SFX with Audio Input as the source. This Event is required to ensure that the audio routing works correctly.

**To set default AudioLink properties:**

1. In Wwise, set up an [Audio Input Source Plug-in](https://www.audiokinetic.com/library/edge/?source=SDK&id=referencematerial_audioinput.html).
2. Create a Wwise "Play" Event that uses a Sound SFX with Audio Input as the source, then generate SoundBanks.
3. In Unreal, click **Edit** > **Project Settings**. The Project Settings dialog opens.
4. In the Wwise section, click **Wwise AudioLink**.
5. Set the following properties:
   - **Start Event**: Select the Wwise "Play" Event you created earlier.
   - **Should Clear Buffer on Receipt**: When selected, the receiving code clears the buffer after it is read so that Unreal doesn't render it. This setting only applies when both renderers are running simultaneously. 该项默认设为启用状态。
   - **Producer to Consumer Buffer Ratio**: The ratio of the producer to consumer buffer size. The default value is 2.0, which means that the producer buffer is twice as large as the consumer buffer.
   - **Initial Silence Fill Ratio**: The ratio of the initial buffer to fill with silence before consumption, which can prevent starvation at the cost of extra latency. The default value is 1.0.

# Overriding Default AudioLink Properties

You can create separate AudioLink assets for individual Wwise Events, which override the default settings.

**To override default AudioLink properties:**

1. In Wwise, create a "Play" Events with Audio Input as the source.
2. In the Unreal Content Browser, click **Add** > **Sounds** > **AudioLink** > **Wwise AudioLink Settings**. A Wwise AudioLink Settings asset is added to the Content Browser.
3. In the asset Details, set the Start Event to the newly created Wwise Event, and change any other property values as required.  

   ![](../../../images/audiolink_asset_unreal.png)

   You can now associate the custom settings with different audio assets.

# Connecting Unreal Audio to Wwise Audio Inputs

As with many aspects of the integration and Wwise in general, there are different ways to achieve the desired results. For example, you can create separate AudioLink assets for individual Wwise Events, which you can then use in Blueprints to play sounds and music as required.

**To use AudioLink on an audio asset:**

1. In the Unreal Content Browser, create an audio asset such as an Attenuation or Submix.
2. Edit the asset. The location of the AudioLink properties varies depending on the type of asset. The following image shows the AudioLink properties for an Attenuation asset:

   ![](../../../images/audiolink_asset_properties.png)
3. To enable AudioLink, select **Send to AudioLink**. The asset now routes audio through AudioLink with the default AudioLink settings.
4. (Optional) To use custom AudioLink settings, use the options next to **AudioLink Settings Override** to select the desired Wwise AudioLink Settings asset.

   ![](../../../images/audiolink_asset_override.png)

   The audio asset now uses custom AudioLink settings.
5. Add the audio asset to a Blueprint.

At this point, you can connect multiple Events to the same Blueprint or to others, and test the audio in Wwise through the Wwise Profiler (see [Profiling](https://www.audiokinetic.com/library/edge/?source=Help&id=profiling)).

There are other ways to work with AudioLink. Refer to the [Adventures With AudioLink](https://blog.audiokinetic.com/adventures-with-audiolink/) blog post for some more examples.