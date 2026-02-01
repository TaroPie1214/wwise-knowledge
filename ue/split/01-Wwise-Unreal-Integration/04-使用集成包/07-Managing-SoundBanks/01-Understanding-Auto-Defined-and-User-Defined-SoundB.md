# Understanding Auto-Defined and User-Defined SoundBanks

|  |
| --- |
| Wwise Unreal Integration Documentation |

Understanding Auto-Defined and User-Defined SoundBanks

Your SoundBank management strategy has significant implications for your Wwise Unreal 集成 project. Your approach affects memory usage, file packaging, file size, and the way in which SoundBanks are loaded. There are three basic strategies: use auto-defined SoundBanks, use user-defined SoundBanks, or take a hybrid approach with auto-defined SoundBanks for some audio assets and user-defined SoundBanks for others.

The preferred strategy is to use auto-defined SoundBanks, which is the simplest and most efficient approach: auto-defined SoundBanks ensure that only the required assets are loaded in memory, and they require the least amount of manipulation in Wwise Authoring. In contrast, user-defined SoundBanks require manual asset management, which can be time-consuming and is more prone to error than using auto-defined SoundBanks.

User-defined SoundBanks were part of the Legacy workflow in Wwise Unreal 集成 versions 21.1, 19.2, 19.1 and earlier. Auto-defined SoundBanks were introduced in Wwise 22.1 although the Event-Based Packaging model, which was the default in Wwise 19.2 and 21.1, shared some characteristics with auto-defined SoundBanks.

# Using Auto-Defined SoundBanks

Auto-defined SoundBanks are created automatically when you enable the corresponding option in your Wwise Project Settings. They automate some of the manual tasks related to SoundBank management but function differently than user-defined SoundBanks. They possess several important characteristics:

- A separate SoundBank is created for each Event.
- Each SoundBank contains only the Event and structure information, while media is stored outside of the SoundBank. Therefore, if multiple Events require the same media asset, it is generated on disk once and loaded once.
- File sizes are generally smaller than those associated with user-defined SoundBanks. Auto-defined SoundBanks rely on Unreal to map dependencies and load the necessary audio. An Unreal component can link to a specific Event and load only the files required for playback. In contrast to user-defined SoundBanks, auto-defined SoundBanks provide much more granularity.

You can enable auto-defined SoundBanks in Wwise Authoring. For details, refer to [Automatically Defining SoundBanks](https://www.audiokinetic.com/library/edge/?source=Help&id=auto_defining_soundbank).

## Reference-Loaded Switch Containers

In addition to the memory optimization that auto-defined SoundBanks provide, you can use them in combination with reference-loaded Switch Containers to further optimize memory usage. The Wwise Unreal 集成 can determine which assets in a Switch Container are used in the current map, and only loads the media assets when required. For example, you might have a footstep Event that uses different surface types, but only certain types of surface are used in different maps (sand in desert maps but not city maps, leafy surfaces in forest maps but not desert maps, and so on). For more information about this type of Switch Container, refer to [Optimizing Memory Usage with Reference-Loaded Switch Containers](using_features_reference_load_switch_container.html).

# Using User-Defined SoundBanks

With user-defined SoundBanks, you create the SoundBanks yourself and decide what to include in them. User-defined SoundBanks give you direct control over SoundBank content, although this degree of control requires planning, time, and effort to manage. As with any manual process, it is open to user error.

User-defined SoundBanks possess several important characteristics:

- They include Events as well as all associated audio assets.
- They are loaded with the corresponding Unreal levels and are available for any of the Events they contain.
- The entire SoundBank is loaded, even if only a single Event out of hundreds in the bank is required. The SoundBank is only loaded once, though.
- Loading time might be shorter than auto-defined SoundBanks because only a single SoundBank is loaded, instead of separate SoundBanks for every Event. Conversely, the larger size of the single SoundBank might require a longer time to load. File sizes are also generally larger.

For instructions on how to create user-defined SoundBanks, refer to [Creating a SoundBank](https://www.audiokinetic.com/library/edge/?source=Help&id=creating_soundbank). The [Performance Optimization](https://www.audiokinetic.com/learning/learn-wwise/wwise-performance-optimization) learning materials also describe in detail how to optimize user-defined SoundBanks.

# Taking a Hybrid Approach

If desired, you can take a hybrid approach to SoundBank management: use both user-defined and auto-defined SoundBanks. With this method, you can optimize your project's use of SoundBanks. There is no ideal hybrid approach, but here are some possible use cases:

- Use a user-defined SoundBank for all small user interface sounds, additional user-defined SoundBanks for the core atmosphere of every level, and auto-defined SoundBanks for all other Events. In this way, the short and repetitive UI interactions are loaded only once, level music is loaded only as required, and Event assets are loaded dynamically.
- Put most sounds and Events in a user-defined SoundBank, and use several optimized Switch Container Event SoundBanks for complex asset hierarchies such as music or banter.
- Isolate debugging Events in auto-defined SoundBanks so that you can remove them from the packaged game.
- Store Events and their associated media in different user-defined SoundBanks (the [Integration Demo Sample](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_integration_samplecode.html) contains an example of this). You could implement a highly complex user-defined SoundBank inclusion pattern and use a custom strategy to load Switch Containers. For example, you could use a media-centric SoundBank for different surface types (such as grass, wood, and metal), and put the Event in a separate SoundBank.

|  |  |
| --- | --- |
|  | **警告：** There are many possible ways to manage and generate SoundBanks in Wwise Authoring, but be aware of the potential risks when you are working with the Wwise Unreal 集成. If your desired pattern is very complex, it might not be supported and could cause asset duplication, missing assets, or even cause the Integration to malfunction. |

# Posting Events

In order to post Events, you must use UAkAudioEvents to do so regardless of the type of SoundBank that you use. UAkAudioEvent is a lightweight structure that contains only the essential information required to load SoundBanks and Media, and process and package the Event.