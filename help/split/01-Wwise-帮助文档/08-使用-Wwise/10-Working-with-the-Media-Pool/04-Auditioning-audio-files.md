# Auditioning audio files

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [Working with the Media Pool](00-Working-with-the-Media-Pool.md) > Auditioning audio files

## Auditioning audio files

You can use the Transport and Audio Preview/Region Selector panes to audition your
audio files.

When you modify any of the property values in the Transport pane, these changes
persist after you select another file in the Results pane. When you close the Media Pool
view, the properties are reset to their default values.

![](../../../../images/media_pool_transport.png)

|  |  |
| --- | --- |
|  | Stop or play the audio file. Alternatively, press the spacebar. |
|  | Click the down arrow to expand or collapse the Audio Preview/Region Selector waveform. |
|  | Click the **Auto-Play on Selection** icon to auto play a file as soon as you select it. |
|  | Audition the Volume, Pitch, LPF, HPF, and Loop the playback.  You can transfer all the changes that you make to the Volume, Pitch, LPF, HPF, and Loop properties when you import the files by clicking the **Apply on Import** icon beside each option. The WAV file is never modified when you make changes to the options. The changes are transferred as properties in the imported object. You can modify these properties in the Property Editor after importing the file. |
|  | Click the **Auto Select Detected Regions** icon to let the Media Pool define regions for your audio file. Wwise can automatically detect regions in WAV files based on their content. It detects the energy and silence and uses heuristics to determine regions of interest in the audio. This is particularly useful when an audio file contains several takes or variations of the same type of sound.  For example, the detected regions can be imported into a Random Container, reducing the amount of work necessary to prepare the files. |
|  | The waveform of the audio file where you can:  - Select regions. - View markers that can be used to select   regions. - Right-click to import the entire audio file or the   selected regions. - Right-click a region to add an **Audio Similarity** filter to your   results. - Click where you want to start playback and then press   spacebar. Press spacebar again to return to the point   where you started. - Adjust the size of the region using the   handles. |
|  | Information about the waveform that includes:    - Duration - 采样率 - Bit Rate（比特率） - Channel Configuration |
|  | Click **Files (#)** to add selected files to the Audio File Importer.  Click **Regions (#)** to add selected regions to the Audio File Importer. |

---