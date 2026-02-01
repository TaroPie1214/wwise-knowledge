# Memory Usage Considerations

|  |
| --- |
| Wwise Unreal Integration Documentation |

Memory Usage Considerations

Memory management is an important part of working with the Wwise Unreal 集成. For background on memory management in Wwise, refer to [Optimizing Memory Allocation](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_optimizingmempools.html) and [Tips to Reduce Memory Usage](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_optimizingmempools_reducing_memory.html).

Memory usage in the Wwise Unreal 集成 is strongly affected by the type of SoundBank your project uses:

- With auto-defined SoundBanks, much of the memory management is automatic: each Event has its own SoundBank, which is loaded when the Event occurs, but media assets are stored outside of the bank. Individual SoundBank memory usage is therefore kept to a minimum; however, if many Events occur at the same time, memory usage can spike.
- With user-defined SoundBanks, you have granular control over memory. However, because the SoundBank contains Events as well as associated media assets, and the entire SoundBank must be loaded even if only a single Event is required, memory usage can be inefficient without manual optimization. It is your responsibility to optimize your SoundBank memory, which can add a significant amount of time and effort to your project. The [Performance Optimization](https://www.audiokinetic.com/learning/learn-wwise/wwise-performance-optimization) learning materials contain several strategies and tips about memory management in projects with user-defined SoundBanks.

For more information about the differences between auto-defined and user-defined SoundBanks, refer to [Managing SoundBanks](using_soundbanks.html).

# Media Loading and Unloading

As described in the previous section, Wwise media Assets are loaded in memory when the SoundBanks that reference or contain them are loaded. The media is unloaded when both of the following conditions are met:

- All Unreal assets that reference the media are destroyed.
- The Wwise sound engine no longer needs the media.

In certain situations, the Wwise sound engine might still need a media asset after its associated Unreal assets are destroyed. For example, there might be a reverb tail that continues for several frames after the sound stops.

# Wwise and Unreal Memory Allocations

In integrated projects, some items are loaded in Wwise memory and others are loaded in Unreal. Because memory usage is divided between Wwise and Unreal, you have to monitor memory in each program to obtain a complete picture of memory usage. In Wwise, you can use the Advanced Profiler to view memory allocated by Wwise (see [Advanced Profiler](https://www.audiokinetic.com/library/edge/?source=Help&id=game_profiler_advanced_profiler)). In Unreal, use the [Wwise Memory Stats](using_soundbanks_memory.html#using_soundbanks_memory_stats) to monitor memory allocated by Unreal.

Each item's memory location is passed to Wwise through either the [LoadBankMemoryView](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a4de50fa493c71964d8d27ba660a87cbb.html) or [LoadBankMemoryCopy](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a30fbe890a910aa75e4ae9457b46e822a.html) function. `LoadBankMemoryView` is not shown in Wwise, but `LoadBankMemoryCopy` is.

The function that is used and the memory location both vary depending on how your Events and media are structured:

- SoundBanks that contains Events as well as media use `LoadBankMemoryView`.
- SoundBanks that contains Events, structures, but no media use `LoadBankMemoryCopy`.

# Wwise Memory Stats

The Wwise Unreal 集成 enables several options in Unreal Stats that monitor Wwise memory usage, including several items in the **WwiseMemory** category. You can view the stats as an overlay in the editor or through the Session Frontend. For more information about Unreal Stats, see [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine).

The following Wwise memory statistics are available, which you can view in different places in Unreal:

- **SoundEngine Reserved**: The total amount of memory reserved by Wwise's memory manager. It is used exclusively by Wwise.
- **ExtSrc**: Memory allocated for External sources that are loaded, not streamed.
- **ExtSrc Prefetch**: Memory allocated for external sources' prefetch when they are configured for zero latency.
- **ExtSrc Device**: Memory allocated for external sources on certain platforms for hardware-accelerated operations.
- **Media**: Memory allocated to load media.
- **Media Prefetch**: Memory allocated for prefetch media of zero-latency streaming sounds.
- **Media Device**: Memory allocated for media on certain platforms for hardware-accelerated operations.
- **SoundBank Mapped**: Memory allocated for mapped files, only relevant in the editor or on iOS.
- **SoundBank**: Memory allocated for SoundBanks. For auto-defined SoundBanks, which do not contain media, memory consumption is only loaded briefly and then transferred to Wwise. However, some memory usage might appear here for user-defined SoundBanks that contain media.
- **SoundBank Device**: Memory allocated for SoundBanks that contain media that require device-allocated memory on certain platforms for hardware-accelerated operations.

## Viewing Stats in the Viewport

Through the Unreal Stats, you can view Wwise memory usage information in the Unreal Editor's level viewport.

**To view Wwise memory usage:**

1. Open the Unreal project in the Unreal Editor.
2. In the viewport, open the menu in the upper left and select **Stat** > **Wwise** > **WwiseMemory**. The Unreal memory monitor opens in the viewport and displays Wwise memory usage statistics.

   ![](../../../../images/unreal_stats.png)

## Viewing Stats in the Session Frontend

The Unreal Session Frontend includes a Profiler, in which you can view the Wwise memory Stats. For more information about the Session Frontend, see [Unreal Frontend](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-unreal-frontend-tool).

**To view Stats in the Session Frontend:**

1. Open the Unreal project in the Unreal Editor.
2. Open **Tools** > **Session Frontend**, and open the **Profiler**.
3. Enable **Data Capture** and **Data Preview**. You can select any of the WwiseMemory Stats:

   ![](../../../../images/unreal_session_frontend.png)