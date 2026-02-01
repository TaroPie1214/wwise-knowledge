# Release Notes 2025.1.0 Beta 1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Release Notes 2025.1.0 Beta 1

The following sections list and describe the changes to Wwise between version 2024.1 and version 2025.1.0.  
此处提供了有关平台的特定信息：

[Windows 2025.1.0 Beta 1](windows_releasenotes_2025_1_0.html)

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [New Features](whatsnew_2025_1_0.html#generic_feature_changes_2025_1_0)
- [API Changes](whatsnew_2025_1_0.html#generic_api_changes_2025_1_0)
- [Behavior Changes](whatsnew_2025_1_0.html#generic_behavior_changes_2025_1_0)
- [Performance Changes](whatsnew_2025_1_0.html#generic_perf_changes_2025_1_0)
- [Miscellaneous Changes](whatsnew_2025_1_0.html#generic_misc_2025_1_0)
- [Bug Fixes](whatsnew_2025_1_0.html#generic_bugs_2025_1_0)
- [Fixes for Community-Reported Bugs](whatsnew_2025_1_0.html#generic_community_bugs_2025_1_0)
- [Documentation Improvements](whatsnew_2025_1_0.html#generic_documentation_improvements_2025_1_0)

# New Features

- **WG-42269** Added support for dynamic dialog in Unreal.
- **WG-46563** (WAAPI) Added the [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) topic to receive project structure changes in batch after the undo stack is modified.
- **WG-55874** (Spatial Audio) Added Dynamic Load Balancing.
- **WG-56147** Added the `HostReferenceSet` plug-in interface for Wwise Authoring. Plug-ins can use it to retrieve information about References to other objects in a Wwise project, which can simplify the development of plug-ins that refer to Game Parameters or Sidechain Mix ShareSets. See [Reference Set](plugin_backend_model.html#wwiseplugin_referenceset) and [Reference Set Notification](plugin_backend_model.html#wwiseplugin_referenceset_notification) for more information. If your plug-ins already used References and used `AK::Wwise::Plugin::Notifications::PropertySet::NotifyPropertyChanged` to receive notifications when References changed, update them to use `AK::Wwise::Plugin::Notifications::Referenceset::NotifyReferenceChanged` instead.
- **WG-56964** Files in standard WAV format can now be specified as external sources (`AkExternalSourceInfo`) when posting Events.
- **WG-60211** Added an option to hide the Diffraction and Transmission percentages in the 3D Viewer.
- **WG-62551** (Spatial Audio) A new flag, `in_bTransition`, was added to `SetPortalObstructionAndOcclusion`. When true, obstruction and occlusion are interpolated over the depth of the Portal.
- **WG-62681** A customizable toolbar was added to the top of the 3D View of the Game Object 3D Viewer. It replaces the Game Object 3D Viewer Options view. The toolbar has four buttons by default, each representing a category of options. Each category button opens a context menu with more options. You can pin options to the toolbar for quick access.
- **WG-62683** You can now select Game Objects, diffraction paths, and reflection paths in the 3D viewer to view information about them.
- **WG-62855** Added a selection property panel to the Game Object 3D Viewer, which displays the relevant properties of selected Game Objects, diffraction paths, and reflection paths.
- **WG-66841** Added an option to hide Virtual Positions in the 3D Viewer.
- **WG-68856** Auto-defined SoundBanks now package prefetch data. A new field, ContainsPrefetch, was added to the SoundBank metadata files.
- **WG-69303** Added a "Sidechain Mix" ShareSet to Wwise, which carries audio signals across Effect plug-ins so that Effects can use other audio signals as a part of their processing.
- **WG-72676** Added a Save Profiler Session command to the Profiler menu.
- **WG-73774** In the Property Editor, Notes are now shown on multiple lines when required.
- **WG-74448** New context menus were added to the Switch Container editor.
- **WG-74497** Added an "Open in New Window" button for references in the Property Editor.
- **WG-75163** (Spatial Audio) Added the ability to automatically cluster nearby sound emitters so that their paths are only computed once per cluster. See `AkSpatialAudioInitSettings::uClusteringMinPoints`, `AkSpatialAudioInitSettings::fClusteringMaxDistance`, and `AkSpatialAudioInitSettings::fClusteringDeadZoneDistance`.
- **WG-75197** (Spatial Audio) Added a new scaling factor to manipulate reverb send values for Rooms and Portals. `AK::SpatialAudio::SetAdjacentRoomBleed` and `AkPorrtalParams::AdjacentRoomBleed` affect the proportion of audio sent to adjacent Rooms versus the proportion sent to the emitter's current Room.
- **WG-75355** New WAQL accessors were added for various features.
- **WG-75356** Added a criterion for WAQL expressions to the Query Editor.
- **WG-75380** (Spatial Audio) "Propagation Path Gain" has been divided into separate drivers in the Voice Inspector.
- **WG-75559** External sources can now use WAV files.
- **WG-75584** Added a new effect plug-in to Wwise, the Multiband Meter. This plug-in expands on the existing Meter plug-in by mixing down an input signal and metering it at a series of user-specified frequency ranges to drive a set of user-defined game parameters.
- **WG-75589** Added Sidechain Mix support to the Compressor Effect.
- **WG-75676** A High Shelf Filter Emphasis setting was added to the Project Settings.
- **WG-75680** In the Game Object 3D Viewer, filtering the Game Object List and showing/hiding game objects in the 3D Viewer are now decoupled.
- **WG-75693** Added a cooldown feature to Events, configurable by time, maximum number of instances, and scope.
- **WG-76148** The Audio File Importer is now available as a view and can be docked to the layout.
- **WG-76399** Added a button to configure gain reduction meter range in the Compressor Effect editor.
- **WG-76401** Context menus were updated in the Music Playlist Editor and the Sequence Editor.
- **WG-76494** A new plug-in service, `PluginServiceType_Meter` was added. Plug-ins can use it for audio signal metering.
- **WG-76636** Wwise projects now have global Attenuation ShareSets instead of project curves. A migration transfers all project curves to a new Attenuation ShareSet called Envrionmental Curves Migration. Migration does not affect project behavior.

An Attenuation ShareSet can now set its Distance Volume curve to None, which has the same effect as a Constant curve at 0dB for all distance values.

- **WG-76670** Some Media Pool settings are available in the `settings/MediaPool.wpref` file .
- **WG-76739** Added "Tick Interval" performance counter to the Performance Monitor.
- **WG-76841** (Spatial Audio) Added `AkRoomParams::SubtractFromParent` to determine whether or not a Room causes distance attenuation to apply to a parent Room, or to a Room in which it is nested.
- **WG-77379** In an Attenuation ShareSet, you can now set the Distance Volume curve to None, which ensures that the volume of a sound does not change when the distance between the emitter and listener changes. If you also set game or user-defined curves to Use Distance Volume, they are also considered to be set to None.
- **WG-77381** The Audio File Importer has new context menu entries to add files and folders to the import list, and a new buttons to remove files and folders from the import list.
- **WG-77482** Spatial Audio emitters can now be clustered to optimize path computation.
- **WG-77788** Added the ability to control a Dynamic Sequence from a user callback instead of a Playlist array.
- **WG-78342** The Expander plug-in is no longer built as a separate library or DLL, and is now included as a part of the Compressor plug-in, which reduces overall memory usage. Any references to the AkExpanderFX library or DLL can be removed because only the AkCompressorFX needs to be included. See [移除了 AK Expander 插件库](whatsnew_2025_1_migration.html#remove_akexpander_lib) for more information.

# API Changes

- **WG-73367** Removed the `AK_EnableGetSourcePlayPosition` flag used in `AK::SoundEngine::PostEvent`. `AK::SoundEngine::GetSourcePlayPosition()` now works on all sources by default. If your code used `AK_EnableGetSourcePlayPosition`, delete the flag and pass 0 instead, or the other flags needed for `AK::SoundEngine::PostEvent`.
- **WG-75057** Removed the obsolete `IAkVoicePluginInfo::ComputePriorityWithDistance` function.
- **WG-76108** Added the [ak.wwise.core.workUnit.load](ak_wwise_core_workunit_load.html) and [ak.wwise.core.workUnit.unload](ak_wwise_core_workunit_unload.html) WAAPI functions, as well as the WAAPI/WAQL `workunitIsLoaded` accessor.
- **WG-76684** The `AK::MusicEngine` namespace was removed and `AK::MusicEngine::GetPlayingSegmentInfo` was moved to `AK::SoundEngine::GetPlayingSegmentInfo`.

# Behavior Changes

- **WG-75051** (Spatial Audio) Room Tone transmission path distances are now measured using geometry.
- **WG-76009** CPU limit behavior has been changed, resulting in improved Spatial Audio performance. The CPU limit now controls the load balancing spread: it distributes Spatial Audio tasks across the required number of frames to maintain the CPU constraint.

# Performance Changes

- **WG-74816** Improved performance of Capture Log rendering.
- **WG-75773** Improved Doppler mitigation in Reflect.
- **WG-77638** Improved performance of most SIMD code in Debug configurations on Arm platforms.

# Miscellaneous Changes

- **WG-76415** Improved Sink plug-in sample code provided by wp.py.
- **WG-76612** Significantly improved the precision of the AKSIMD\_SQRT\_V4F32 function for Arm-based platforms.
- **WG-76818** The Meter plug-in is now available as a separate plug-in DLL, and is no longer statically linked to the AkSoundEngineDLL binary.
- **WG-76834** The Actor-Mixer object was renamed to Property Container.
- **WG-76835** The Master Audio Bus was renamed to Main Audio Bus.
- **WG-77745** (WAAPI) Subscriptions to the `ak.wwise.core.log.itemAdded` topic are no longer revoked when a project is closed.
- **WG-78540** The Master-Mixer Console was renamed to Busses Console.
- **WG-78542** "High-shelf filter" curves in Wwise Reflect were renamed "Dual-shelf filter" to be consistent with the new Dual-shelf filters in Attenuations.
- **WG-78627** (wp.py) The bundle.json format for Authoring plug-in packages was changed to accommodate more configurations. Authoring targets are now packaged and identified in "Authoring.OS\_ARCH.CONFIG" format (for example, "Authoring.Windows\_x64.Release").

# Bug Fixes

- **WG-70576** Fixed: Spatial Audio API calls in the Capture Log do not show Room names.
- **WG-73571** Fixed: (Spatial Audio) Direct path distances are inconsistently calculated between the Listener and the Distance Probe.
- **WG-73928** Fixed: (Spatial Audio) Room tone distance in Reverb Zones with no transparent surfaces is always 0.
- **WG-74341** Fixed: (Authoring) Expanding a row moves the viewport to the wrong location.
- **WG-74342** Fixed: Clicks on the margins of buttons in tables and trees are accepted.
- **WG-74621** Fixed: Integral plug-in property types are clamped to a signed int32.
- **WG-74661** Fixed: (Spatial Audio) Opaque surfaces of Reverb Zones cause areas to incorrectly calculate direct path distance.
- **WG-74974** Fixed: Priority value calculation has floating point errors when there are RTPC or State values involved.
- **WG-75037** Fixed: Errors in priority calculation when updating priority through RTPCs or State Groups.
- **WG-75507** Fixed: Input validation relies on double type conversion.
- **WG-75665** Fixed: Slider text box is limited to its visible area.
- **WG-75956** Fixed: Metadata view is out of sync after a Work Unit is reloaded.
- **WG-76433** Fixed: Spatial Audio API calls in the Capture Log do not show Portal names.
- **WG-76489** Fixed: Line returns (ENTER) added to Notes fields are lost when the project is reloaded.
- **WG-76563** Fixed: Only one virtual emitter from a multi-position emitter has the correct color.
- **WG-76702** Fixed: Wrong focus order when navigating with the Tab key in lists with user-defined columns orders.
- **WG-77276** Fixed: Various crashes when processing asynchronous notifications.
- **WG-77336** Fixed: Transport "Reset Menu" button stays lit after platform change.
- **WG-77460** Fixed: Next To Play indicator in sequence container playlist editor not reset after platform change
- **WG-77578** Fixed: Buffer overrun when using Mackie Control control surface.
- **WG-77842** Fixed: Changing RTPC, Switch, or State dirties Soundcaster session Work Unit.
- **WG-77931** Fixed: Benign assert when registering some plug-ins while the sound engine is running.
- **WG-77948** Fixed: In the Audio File Importer, the object type is not correct after dragging a music object to the Destination Object.
- **WG-78005** Fixed: Nondeterministic file conversion in Impacter when reusing the same files across instances.
- **WG-78135** Fixed: Cannot always click Remove for State Group transitions.
- **WG-78219** Fixed: Crash when sorting the Game Object List by Room.
- **WG-78350** Fixed: Crash in low-memory conditions when executing a PrepareBank operation.
- **WG-78454** Fixed: Game Units to Meters renamed to Game Units Per Meter.
- **WG-78946** Fixed: Crash when importing or playing certain ADM files not following the production profiles.

# Fixes for Community-Reported Bugs

- **WG-71305** Fixed: (Spatial Audio) Concave Room shapes cause room tone distance jumps.
- **WG-77284** Fixed: Possible crash when exiting Wwise or opening the Game Object 3D Viewer after loading a `.prof` file.
- **WG-77862** Fixed: Parametric EQ pre-rendered effects add unnecessary silence at the end of the sound.
- **WG-77956** Fixed: Cannot sync a "Sync any" floating Object Tab Group with the selected object.

# Documentation Improvements

- **WG-77678** Added documentation to automatically generated `AKSoundEngine` C# functions and types.