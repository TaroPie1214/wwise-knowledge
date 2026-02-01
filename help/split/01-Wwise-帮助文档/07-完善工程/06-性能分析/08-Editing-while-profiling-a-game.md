# Editing while profiling a game

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [性能分析](00-性能分析.md) > Editing while profiling a game

## Editing while profiling a game

A remote connect session can be used to make modifications to a game that is currently
running, without regenerating SoundBanks. These changes to the Wwise project can be
extensive and even include new media. This is supported on all platforms and all game
engines.

Any changes made during a remote connect session do not change the files deployed on a game
console. This means that restarting the game reverts to the content available in the
SoundBanks deployed with the game. To reapply the changes made to the Wwise Project, you
must reconnect Wwise to the game. To make these changes permanent, you must regenerate
the SoundBanks and deploy them with the game.

To enable editing while profiling, in the Remote Connections dialog, set the
synchronization method to **Profile and Edit (Sync Inspected Objects
Only)** or **Profile and Edit (Sync All Modified
Objects)**.

With **Profile and Edit (Sync Inspected Objects Only)**,
only objects that are currently inspected in the Transport Control are updated, in
addition to all necessary related objects, such as the Output Bus, Effects, and
Attenuation. Each time the object in the Transport Control changes, a new update is done
if necessary. With this method, only a small subset of objects is updated at a time.

With **Profile and Edit (Sync All Modified Objects)**, all
objects that are modified in the Wwise project and are currently loaded in the game
through SoundBanks are updated at the moment of connection. They are also updated each
time additional changes are made to the Wwise project during the remote connect session.
Because a large number of sound structures can be loaded in game, the connection process
can take several seconds while Wwise verifies what needs to be updated.

With the synchronization method set to **Profile Only**,
nothing is updated, so you won't hear any changes if you edit your project while
connected to a game. However, this is the preferred method for troubleshooting issues in
game.

### Side effects of editing while profiling

When either of the **Profile and Edit** methods is
selected, if you change a structure or a playlist that is currently playing, you
might hear audible glitches, sounds that start abruptly, or sounds that stop
abruptly. All these changes are reflected in the Capture Log. Wwise uses the new
structure as if the game loaded it from the start. If you are unsure about the
behavior of these new sounds, redo the scenario from the start in game; at this
point, the new structures will already be in memory, so no transitional glitches
will occur.

If you change media that is currently in use, you will probably hear a click.
Wwise automatically seeks to the same point in the new file that it was at in the
old file. If the content is different, the sound won't match. Also, the transfer of
media takes some time. For this reason, you might see errors related to source
starvation.

Editing while profiling increases memory usage in the game. New media is
transferred to a region of memory reserved specifically for this feature. This
memory is only used in the Debug and Profile configurations and does not count
toward the audio memory budget. You can control the maximum amount of memory used
for Live Media Transfer in the [“设置用户偏好”一节](../../02-入门/04-个性化您的工作空间/04-设置用户偏好.md "设置用户偏好"). When this memory
limit is reached, unused media is evicted from this region of memory. If you
experience memory issues, you can disable Live Media Transfer by setting the maximum
to 0.

---