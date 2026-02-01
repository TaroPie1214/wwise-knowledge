# Using the Editor Listener

|  |
| --- |
| Wwise Unreal Integration Documentation |

Using the Editor Listener

A single listener is activated in edit mode. You can use it to, for example, properly preview Level Sequences that contain positioned audio. 此听者的位置取决于聚焦视口的 Camera 位置。Click between multiple viewports to "jump" from one position to another.

The listener is also used in the Animation Editor viewport, where you can accurately preview 3D-spatialized sounds while you work on animations.

Note that when you start a Play in Editor (PIE) session, the Editor listener is deactivated, and the traditional listener on the Camera is enabled. When you leave a PIE session to start a Simulate in Editor (SIE) session, both the Editor listener and the Camera listener are active at the same time. When you switch back to PIE mode, the Editor listener is disabled again.