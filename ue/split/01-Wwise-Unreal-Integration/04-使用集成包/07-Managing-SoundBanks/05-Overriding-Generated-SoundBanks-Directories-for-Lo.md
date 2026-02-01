# Overriding Generated SoundBanks Directories for Local Users

|  |
| --- |
| Wwise Unreal Integration Documentation |

Overriding Generated SoundBanks Directories for Local Users

Some organizations generate and store their SoundBanks on dedicated servers under source control. This approach can be efficient with large projects or teams, in which different contributors work on different aspects of audio. If the SoundBanks are generated automatically on a schedule, for example with the SoundBank generation commandlet ([Generating SoundBanks with the GenerateSoundBanks Commandlet](using_features_generatecommandlet.html)), the changes are reconciled and the SoundBanks are available for other developers to use. However, some team members might need to generate SoundBanks locally to experiment or test changes in Unreal. In this case, you can override the project settings to generate and store SoundBanks in custom locations outside of source control.

Before you change anything, it is important to understand how Wwise stores the SoundBank path information, and also how Unreal accesses that information.

Wwise records SoundBank path locations in a ProjectInfo.json metadata file, which is created when you first generate SoundBanks for a project and is located at the Wwise project's Root Output Path. The default Root Output Path is in following directory:

`[WwiseProjectName]\GeneratedSoundBanks`

SoundBanks, by default, are generated in subdirectories of the same folder, divided by platform:

`[WwiseProjectName]\GeneratedSoundBanks\[Platform]`

The ProjectInfo.json file itself contains a list of paths to the generated SoundBanks for each platform. In the Unreal Project Settings, the Generated Sound Banks Path actually points to the Root Output Path, which contains the ProjectInfo.json file, and *not* the paths that contain the actual generated SoundBanks. This is an important thing to remember when you want to override paths, for the following reasons:

- For the Wwise Unreal 集成 to function correctly, the Unreal Generated Sound Banks Path *must* be the same as the Wwise Root Output Path.
- If your Wwise SoundBank paths and the Root Output Path are both under source control, you have to override both.
- If you use a user override for the Root Output Path, you must also set a user override in Unreal to match the Wwise override.

Essentially, Unreal requires access to the ProjectInfo.json file to determine where the SoundBanks are. It does not have any direct knowledge of the SoundBank folder paths.

**To override the SoundBanks directory:**

1. In Wwise, click **Layouts** > **SoundBank**. The SoundBank Layout opens.
2. In the upper right of the SoundBank Manager, click the **gear icon** > **User SoundBank Settings**. The User SoundBank Settings dialog opens.
3. Select **Override Project SoundBank Settings** and **Override Project SoundBank Paths**. The various SoundBank settings are activated.

   |  |  |
   | --- | --- |
   |  | **警告：** If **Enable Auto-Defined SoundBanks** is selected in the regular project settings, it is cleared when you select **Override Project SoundBank Settings**. You must select it in the override settings as well to ensure that SoundBanks can be generated successfully. |
4. Click the ellipses next to **Root Output Path** and in the file explorer, browse to the desired local directory and click **Select Folder**. Ensure that the location is not under source control.
5. Click the ellipses next to a SoundBank Folder and in the file explorer, browse to the desired local directory and click **Select Folder**. Ensure that the location is not under source control. Repeat for each platform for which you want to generate SoundBanks locally.
6. Click **OK**, then generate SoundBanks. The SoundBanks are created in the folders you specified, and the ProjectInfo.json file is created in the Root Output Path you specified.
7. In Unreal, click **Edit** > **Project Settings**. The Project Settings dialog opens.
8. Scroll to the Wwise section and click **User Settings**. The Wwise - User Setting page opens.
9. Click the ellipses next to **Root Output Path Override**. In the file explorer, browse to the same Root Output Path directory you specified as a user override in Wwise.  
     
   You can now modify the Wwise project and generate SoundBanks as required, without any effect on the shared project SoundBanks.