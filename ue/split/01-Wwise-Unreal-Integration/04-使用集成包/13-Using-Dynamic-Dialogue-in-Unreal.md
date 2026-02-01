# Using Dynamic Dialogue in Unreal

|  |
| --- |
| Wwise Unreal Integration Documentation |

Using Dynamic Dialogue in Unreal

The Wwise Unreal Integration includes a dynamic dialogue system, which sound designers can use to manage dynamic audio. Although the system and its associated components refer to "dialogue," it supports any type of dynamic audio: voices, sound effects, music, and so on.

The dynamic dialogue system consists of a set of rules in a tree-like structure that determine which audio clip to play at any given time in a game. For example, you can use dynamic dialogue to manage the speech of play-by-play announcers in a sports game. Similarly, you can use dynamic dialogue to determine the sound of a player's footsteps based on the terrain, the player's footwear, and so on.

The dynamic dialogue system is composed of two systems:

- **Dialogue Events**, which contain decision-tree structures that resolve to audio nodes.
- **Dynamic Sequences**, which open into regular game objects (AkComponents) that contain sequential playlists of resolved audio nodes.

The *audio nodes* that these systems use are any objects in the Containers Hierarchy that can be played in a regular Event, such as sound effects, voices, and containers. Each audio node has an ID value calculated from its name.

For more information about dynamic dialogue in Wwise, see [Managing dynamic dialogue](https://www.audiokinetic.com/library/edge/?source=Help&id=managing_dynamic_dialogue).

# Dialogue Events

Dialogue Events consist of paths of Switch and State Groups that resolve into an assigned object in one of two ways: through the provision of Switch and State values, or through a default path.

The sound engine uses this decision tree to determine which assigned object to use in any situation in the game. In practical terms, dynamic dialogues are similar to Switch Containers with manual purposeful resolving, or game-controlled Music Switch Containers.

## Packaging and importing Dialogue Events

Dialogue Events must be packaged in user-defined SoundBanks ([Understanding Auto-Defined and User-Defined SoundBanks](unreal_using_soundbanks_concepts.html)). After you generate SoundBanks, you can then import the Dialogue Event through the Wwise Browser, like any other type of Event ([Managing Assets with the Wwise Browser](features_editor_wwise_browser.html)).

After you import Dialogue Events, you can preview them. However, the preview only plays the default path because resolving the Events requires arguments.

## Resolving Dialogue Events

The path arguments for Dialogue Events are composed of Switch and State Groups. For example, in a *Footstep* Dialogue Event, the first argument could be terrain. Depending on the Switch value, the object assigned to play is different: a grass surface plays a different sound than concrete. You could then add a second argument for footwear material, and provide different results for leather or metal footwear.

As a best practice, use different Switch Groups for different arguments. For example, the *Footstep* Event could include a *FootwearCondition* Group with values for *New* and *Broken*. You can also create Boolean Groups with true and false values for multiple arguments. If no Switch Groups are reused, you can provide unordered Resolve arguments, which provide all the arguments in any order. If the arguments are ordered, they must all be populated.

The Resolve operation is performed on assets and not on game objects, so no global parameters or object parameters are used. You must explicitly add every required argument to the Resolve operation. Avoid retrieving the current values from the sound engine because the retrieval delay might take a long time, which could cause discrepancies with the stored values if the queue is not processed by the time the values are retrieved. In such a scenario, use a Switch Container instead.

After an audio node is obtained, you can add it to a Dynamic Sequence Playlist for eventual playback. Any Switch, State, or game parameter used in the audio node is resolved according to the game object context, in a manner similar to AkAudioEvents posted into game objects.

### Audio node limitations

When working with audio nodes, be aware of the following limitations:

- You can hard-code audio node values in Unreal. However, you must use your own processes because no audio node information exists in the SoundBank metadata. Because this is an advanced option with limited testing, you must extend the basic implementation yourself.
- In Unreal, Wwise audio nodes are considered unbreakable structures. Audio nodes do not support the AkAudioEvent code that allows Switch Containers to be split according to individual Switch and State Groups. Therefore, if a Dialogue Event is forked in multiple audio nodes with optional Switch Containers, it cannot be split again.
- Exported Dialogue Event metadata does not contain any media usage information. All media from the SoundBank used in the Dialogue Event is primed for reading, which also means that you cannot use auto-defined SoundBanks.
- Exported Dialogue Event metadata does not contain any External Source information. Unreal does not support External Sources.

# Dynamic Sequences

A Dynamic Sequence is a playlist of audio nodes bound to a game object. It is similar to a game-controlled music playlist container, or to a sequence container.

Although you can Dynamic Sequences for any audio system, two common uses are for a character's mouth, and off-screen voice overs. In each case, typically the usage is to open a game object's Dynamic Sequence, add resolved audio nodes to its internal playlist, then use transport commands to start playing the Dynamic Sequence.

By default, the Dynamic Sequence is stored inside the game object. However, if a new instance is requested, it is owned by the game code.

## Playlist classes

The Dynamic Sequence is a container object that binds the game object to a dynamic playlist that is modified by the sound engine whenever an item is played. The integration code synchronizes Unreal objects with sound engine objects. To read or write to a playlist, you must first modify it, which enables access. When you are finished, you must then commit the playlist as soon as possible.

In the integration, the playlist is composed of playlist items that contain resolved audio nodes, as well as supplemental parameters (playback delays, fade curves and delays, and custom object arrays).

## Transport operations

You can play and stop the Dynamic Sequence's processing of the playlist, and can seek, pause, or resume audio playback.

As long as the Dynamic Sequence is playing, the Unreal object and the playlist items and their audio nodes remain alive in memory.

# Playback flows

In order to play a Dialogue Event that includes all steps, perform the following operations:

1. Create a `UAkGroupValue` arguments array.
2. Resolve the Dialogue Event onto an audio node with `UAkDialogueEvent::Resolve*Arguments`.
3. Create a playlist item using the Dialogue Event's audio node with `UAkDynamicSequenceBlueprintFunctionLibrary::CreateDynamicSequencePlaylistItemFromAudioNode`.
4. Open a Dynamic Sequence on a game object with `UAkGameObject::OpenDynamicSequence`.
5. Modify the playlist of the Dynamic Sequence with `UAkDynamicSequence::ModifyPlaylist`.
6. Create an array of playlist items containing the playlist item.
7. (Optional) Retrieve the current playlist and merge both with `UAkDynamicSequencePlaylist::GetItems`.
8. Set the playlist array in the Dynamic Sequence's playlist with `UAkDynamicSequencePlaylist::SetItems`.
9. Commit the playlist into the Dynamic Sequence with `UAkDynamicSequencePlaylist::Commit`.
10. Play the Dynamic Sequence with `UAkDynamicSequence::Play`.

You can post a Dialogue Event directly into a game object with `UAkGameObject::PostAkDialogueEvent`. The following operations are performed automatically:

1. A `groupvalue` arguments array is created in most cases. If no parameters are provided, the fallback path is used.
2. The Dialogue Event is resolved onto an audio node.
3. A playlist item is created from the Dialogue Event's audio node with default values, no fade, no delay, and no custom data.
4. The default Dynamic Sequence of the game object is opened with default parameters.
5. The Dynamic Sequence playlist is modified.
6. The playlist item is added to the end of the playlist.
7. The playlist array is set into the Dynamic Sequence's playlist.
8. The playlist is committed into the Dynamic Sequence.
9. Depending on the **Play immediately** parameter, the Dynamic Sequence might be played.

Each sequence of steps above has multiple helper functions that simplify advanced workflows. Because the convenience functions use these helper functions, we recommend that you follow the C++ code to see the details of the process. These steps are all available through Blueprint calls as well.

For example, `UAkDynamicSequenceBlueprintFunctionLibrary::CreateDynamicSequencePlaylistItemFromDialogueEvent` resolves the Dialogue Event and creates a playlist item. `UAkDynamicSequencePlaylist::AddAndCommit` simplifies the process of appending a single item into the Dynamic Sequence's playlist, and committing the playlist.