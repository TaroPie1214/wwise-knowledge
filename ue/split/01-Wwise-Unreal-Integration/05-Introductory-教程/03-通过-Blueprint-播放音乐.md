# 通过 Blueprint 播放音乐

|  |
| --- |
| Wwise Unreal Integration Documentation |

通过 Blueprint 播放音乐

This tutorial explains how to use Unreal Blueprints to play music from an integrated Wwise project. A Blueprint is suitable for music, which might play for the entire duration of the game across different levels.

**To prepare for this tutorial:**

1. In Wwise Authoring, create a Music Playlist Container.
2. Add a Music Segment that loops indefinitely. The following image shows the Container configuration:

   ![](../../../images/GSTutorialMusicRepeat.png)
3. Create an Event that plays the Music Segment. This tutorial uses an example called Play\_Music.
4. Generate SoundBanks in either Wwise or Unreal.
5. In the Unreal Editor, drag the music Event from the Wwise Picker into the Level Editor. Just as in [Adding Ambient Sound to a Level](gs_silence_to_sound.html), the Event is added and a `uasset` is created.
6. Select the Event and in the Details panel, select the Auto Post option.

# Posting an Event

In this part of the tutorial, you will add sounds to the ThirdPersonExampleMap level. The level already contains various Actors such as Lights, Meshes, and a character.

|  |  |
| --- | --- |
|  | **注記：** If you have multiple scenes, you can create a Persistent Level so that the music survives when a different map is loaded. See [Managing Multiple Levels](https://dev.epicgames.com/documentation/en-us/unreal-engine/managing-multiple-levels-in-unreal-engine) for more information. |

This tutorial uses the Blueprint of the playable character, which is available by default in the ThirdPersonCharacter content. To play, or "post", a Wwise Event, you have to do three things:

1. Call the Unreal Event when you begin to play.
2. Connect it to the function that plays the Wwise Event.
3. Specify which Actor plays the Event.

The following procedure explains this process in detail.

**To post an event:**

1. In the Content Browser, go to **ThirdPerson** > **Blueprints** and double-click **BP\_ThirdPersonCharacter**. The BP\_ThirdPersonCharacter Blueprint opens. The Event Graph tab contains three disabled nodes.
2. Drag a pin from the BeginPlay node, search for the **Post Event** Audiokinetic function and click it.

   ![](../../../images/GSTutorialExecutableActions.png)

   The Post Event function requires a reference to an Actor to place the Wwise Event.
3. Drag a pin from the Actor Object Reference, search for the **Get a reference to self** Variable and click it.

   ![](../../../images/GSTutorialActorReference.png)
4. In the **Post Event** function, select the Play\_Music Ak Event.

   ![](../../../images/GSTutorialSelectWwiseEvent.png)
5. Click **Compile** and then in the Level Editor, click **Play**. The music plays.

# Using AkComponents

The Blueprint environment is ideal for controlling Actor behavior. However, to efficiently manage and position Actors in levels, you can expose some Blueprint controls in the Details panel and work primarily in the Level Editor instead. To do this, you can add an AkComponent to the Actor, which you can then use to offset the position of the sound from the Level Editor.

**To use an AkComponent:**

1. In the Blueprint Editor, on the Components tab, click **Add**, then search for the **Ak** Audiokinetic component and click it.
2. In the Event Graph, delete the **Post Event** function and the reference to **Self**.
3. Drag the Ak component into the Blueprint, then drag a pin from the component, search for **Post Ak Event** and click it.

   ![](../../../images/GSTutorialPostAKEvent.png)
4. Connect **BeginPlay** to the **Post Ak Event**.

   ![](../../../images/GSTutorialConnectBeginPlay.png)

   You can now retrieve the Wwise Event selected in the AkComponent.
5. Drag a pin from the AkEvent Object Reference, find and select a **Get Ak Audio Event** and connect it to the Ak component.

   ![](../../../images/GSTutorialAKAudioEvent.png)
6. Click **Compile**.
7. In the Components panel, select **Ak**, then in the Details panel, expand the Ak Event section. It is currently empty.
8. Drag the music Event from the Wwise Picker into the empty Ak Audio Event area.

   ![](../../../images/GSTutorialAudioEventPlayMusic.png)

   You can now change the Event without opening the Blueprint, and you can offset the position of the sound relative to the Actor to which it is attached.

# Controlling Music with States

In most cases, you want interactive music in your game to adapt to gameplay conditions and provide variety. This tutorial demonstrates a common implementation strategy, which is to use States to control music.

Before you start, you must create a new music system in Wwise that consists of two distinct types of music: in this case, selection of calm music and a selection of intense music.

Create a Music Switch Container that can switch between "Repeat Calm" and "Repeat Intense" Music Playlists based on a “Music” State, as shown in the following image.

![](../../../images/GSTutorialMusicSwitch.png)

In the example, there are three States: Calm, Intense, and None. With this setup, you can set States from the game to change the music during runtime. You can also choose which State to set when the game starts.

A common approach, which this tutorial uses, is to set States when the player enters a certain area, defined by a Trigger. You create a Trigger Box and use a Blueprint system to set the State when the player crosses the boundaries of the box.

Ensure that you complete the steps in [Using AkComponents](gs_music_from_blueprint.html#gs_akcomponent) before you proceed.

**To control music with States:**

1. In the Blueprint Editor, drag a **SetState** Audiokinetic function from **BeginPlay**.

   ![](../../../images/GSTutorialSetStateFunction.png)
2. 将 Initial State 设为 **Music-Calm**。

   ![](../../../images/GSTutorialMusicCalm.png)

   The initial state is now set up.
3. 将 Box Trigger 拖到 Level 中。

   ![](../../../images/GSTutorialBoxTrigger.png)
4. 增大 Box Trigger 的尺寸。

   ![](../../../images/GSTutorialIncreaseBoxTriggerSize.png)
5. In the Details view, click the button with the three boxes (1), then **New Subclass** (2), type a Blueprint name (3), and then click **Select** (4), as shown in the following image.

   ![](../../../images/GSTutorialCreateBlueprint.png)

   The Blueprint is created, and contains an ActorBeginOverlap Event, which you can use to detect when something enters the Trigger Box.
6. 从 **ActorBeginOverlap** 向外拖动连线，接着赋值给 **ThirdPersonCharacter**，然后将 Exec 连到 Set State 函数。

   ![](../../../images/GSTutorialCastToThirdPersonCharacter.png)

   To ensure that you can use the Trigger Box for multiple states, you must create a Variable that is accessible outside the Blueprint.
7. Drag from the State Value and click **Promote to variable**.

   ![](../../../images/GSTutorialPromoteToVariable.png)

   There is now a variable under **My Blueprint** > **Variables** on the left.
8. Rename the variable to “MusicState” and click the eye icon.

   ![](../../../images/GSTutorialMusicState.png)

   The variable is now public (accessible outside the Blueprint).
9. Click **Compile**, and close the Blueprint.
10. Select the Trigger, then in the Details view select a State under **Default** > **Music State**.

    ![](../../../images/GSTutorialMusicIntense.png)
11. In the level, walk into the new Trigger with the ThirdPersonCharacter and wait for the music to change.

    ![](../../../images/GSTutorialWalkIntoTrigger.png)

    You can now duplicate the trigger, reuse it somewhere else and set a different state without affecting the original trigger.

|  |  |
| --- | --- |
|  | **注記：** If your Music Switch Container's Transition is set to **Exit Cue**, you might have to wait to hear the music change. |