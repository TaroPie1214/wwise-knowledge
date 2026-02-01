# Adding a Motion Bus to a Wwise Project

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [管理 Motion](00-管理-Motion.md) > Adding a Motion Bus to a Wwise Project

## Adding a Motion Bus to a Wwise Project

Before you add a motion to a Wwise project, you need a bus associated to the Motion source
plug-in.

### To add a Motion Bus to a Wwise Project

1. In Wwise Authoring, open the Busses Hierarchy and create a new Audio bus under the
   Default Work Unit.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | It's good practice to rename your motion objects to include "motion". For example, "Motion Bus". |
2. Double-click the new bus to open its Property Editor.
3. In the Audio Device group, click the **Set Audio
   Device** icon and browse the list of devices and select
   Motion.

   This is the Wwise Motion source plug-in.
4. In the Container Default Work Unit, right-click and select **New Child** > **Sound
   SFX**.
5. Rename the Sound SFX object to indicate that it is a motion object. For
   example, "MotionSFX".
6. Double-click the new MotionSFX object to open its Property Editor.
7. In the **Routing** group, click the **Set Output Bus** icon and browse to select the
   Motion Bus you created.
8. (Optional) Do one or both of the following in the Motion Source
   Editor:

   - Change the Actuator Configuration of the Motion plug-in to
     something that matches the targeted controller device.
   - Unlink the Actuator Configuration, depending on the platform.

   You can test the Motion SFX object to verify that the controller
   vibrates.

---