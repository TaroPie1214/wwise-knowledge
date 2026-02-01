# Wwise Authoring Performance Monitor Counter Identifiers

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Authoring Performance Monitor Counter Identifiers

| 名称 | 说明 | 参数 |
| --- | --- | --- |
| ActiveEvents | The number of Events that have been posted by the game and have not yet reached their end number of active listeners. |
| ActiveListeners | The number of active listeners. |
| ActiveSends | The number of Game-defined or User-defined auxiliary sends that are active. |
| ActiveStreams | The number of streams that are active. A stream is active when it required or was waiting for at least one I/O transfer in the last profiling frame. |
| ActiveTransitions | The number of fades/transitions/interpolations that are active at any one time. |
| ApiCalls | The number of calls from the API to the sound engine. |
| CommandQueueSize | The current amount of memory allocated for storing commands that are sent from the game application to the sound engine. |
| CommandQueueUsed | The percentage of the command queue that is being used at any one time. |
| CpuPluginTotal | The amount of the CPU used for plug-ins. |
| CpuTotal | The amount of the CPU used by the audio thread. |
| HardwareAudioDecodeUsage | The percentage of the Hardware Audio Decode resources that is being used at any one time. This counter will only be displayed when certain platforms(PS4and PS5) are selected. |
| JobMgrMemoryCurrent | . |
| JobMgrMemoryPeak | . |
| JobMgrMemorySlabsCurrent | . |
| JobMgrMemorySlabsPeak | . |
| LoadedBanksMemory | The current size of the SoundBanks that have been loaded into memory. |
| LoadedUserBanksMemory | The current size of the SoundBanks that have been loaded into memory via LoadBankMemoryView. |
| LoudnessMomentaryInstanceA | The Loudness Meter momentary (0.4-second rectangular time window) loudness level for meter instance A. |
| LoudnessMomentaryInstanceB | The Loudness Meter momentary (0.4-second rectangular time window) loudness level for meter instance B. |
| LoudnessMomentaryInstanceC | The Loudness Meter momentary (0.4-second rectangular time window) loudness level for meter instance C. |
| LoudnessMomentaryInstanceD | The Loudness Meter momentary (0.4-second rectangular time window) loudness level for meter instance D. |
| LoudnessShortTermInstanceA | The Loudness Meter short-term (3-second rectangular time window) loudness level for meter instance A. |
| LoudnessShortTermInstanceB | The Loudness Meter short-term (3-second rectangular time window) loudness level for meter instance B. |
| LoudnessShortTermInstanceC | The Loudness Meter short-term (3-second rectangular time window) loudness level for meter instance C. |
| LoudnessShortTermInstanceD | The Loudness Meter short-term (3-second rectangular time window) loudness level for meter instance D. |
| OutputPeak | The peak output from the sound engine at any given time, in dB. |
| PreparedEvents | The number of Events that have been prepared using the [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)function. |
| PreparedEventsMemory | The amount of memory used for the prepared events. When an Event is prepared, only the media specifically associated with that Event gets loaded into memory. |
| ProfilerBandwidth | The volume of profiling data sent by the game to the Wwise authoring application. Units: KB/s (kilobytes per second). |
| RegisteredObjects | The number of game objects registered at any one time. |
| SpatialAudioCPU | The total amount of CPU used by spatial audio, expressed as a percentage of an audio frame. |
| SpatialAudioComputedEdges | The number of diffraction edges that have been processed during this frame. |
| SpatialAudioDiffractionEdges | The total number of diffraction edges in the current 3D environment. |
| SpatialAudioEmitters | The number of emitters processed by spatial audio: for each emitter spatial audio validates the reflection and diffraction paths. |
| SpatialAudioLBSpread | The current load balancing spread. |
| SpatialAudioPathDifferences | . |
| SpatialAudioPathValidationCPU | The amount of CPU used by the path validation phase of spatial audio expressed as a percentage of an audio frame. |
| SpatialAudioPortalPathValidationCPU | The amount of CPU used by spatial audio to validate paths from the portals to the listener and the emitters expressed as a percentage of an audio frame. |
| SpatialAudioPortalRaytracingCPU | The amount of CPU used by spatial audio to sample the environment to find potential paths from the portal to the listener and the emitters. Expressed as a percentage of an audio frame. |
| SpatialAudioPrimaryRays | The number of primary rays targeted by spatial audio. |
| SpatialAudioRaytracingCPU | The amount of CPU used by the raytracing phase of spatial audio expressed as a percentage of an audio frame. |
| SpatialAudioTasksExecuted | . |
| SpatialAudioTasksRemaining | . |
| SpatialAudioTriangles | The total number of triangles in the current 3D environment. |
| StateTransitions | The number of transitions between States that are played at any one time. |
| SystemAudioObjects | The number of System Audio Objects playing at any one time. |
| TickInterval | The interval between the previous audio render tick and this tick. |
| TotalMediaMemory | The total size of the media files that have been loaded into memory. |
| TotalReservedMemory | The total amount of memory that has been reserved, or mapped to physical memory, but not necessarily in use by runtime memory allocations. |
| TotalStreamingBandwidth | The total amount of streaming bandwidth that is used at any one time. This value includes both low-level I/O transfers and transfers from the Stream Manager's cache which don't require access to disk, and is therefore larger or equal to the Total I/O Bandwidth (Low-Level). |
| TotalStreamingBandwidthLowLevel | The total amount of streaming bandwidth that is used at any one time. This value takes low-level I/O transfers into account only, and excludes virtual transfers from cached data in the Stream Manager. |
| TotalStreams | The total number of streams open at any one time. |
| TotalUsedMediaMemory | The total size of the media files that have been provided to the soundengine from the user (e.g. via setMedia) |
| TotalUsedMediaMemory | The total size of the media files that have been transferred to the soundengine because of live edits in the project. This memory is not used in the Release configuration. |
| TotalUsedMemory | The total amount of memory in use by runtime memory allocations. |
| VoicesPhysical | The number of physical voices that are played at any one time. |
| VoicesTotal | The number of audio voices or separate playback instances that are played at any one time (Physical + Virtual). |
| VoicesVirtual | The number of virtual voices in the virtual voice list at any one time. |