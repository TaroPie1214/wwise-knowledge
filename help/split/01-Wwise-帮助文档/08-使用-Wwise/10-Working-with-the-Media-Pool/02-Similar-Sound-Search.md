# Similar Sound Search

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [Working with the Media Pool](00-Working-with-the-Media-Pool.md) > Similar Sound Search

## Similar Sound Search

Similar Sound Search allows you to search for sounds in your Media Pool databases
using either a text query or a reference audio clip. This removes the need for keyword
tagging and time-consuming manual navigation through vast sound libraries. It was
designed specifically for sound effects and discovers unexpected matches that would be
difficult to find using conventional search methods. For example, a sound labeled
“smashing fruit” might be found as a match for the query “footsteps in mud.”

In particular, Similar Sound Search allows for:

- **Text-to-audio retrieval:** In the list to
  the right of the Search field, select **Audio
  Description** and then type a description of the desired sound.
  Results are ranked based only on their audio content.
- **Audio-to-audio retrieval:** Right-click any
  file in the Results pane and click **Find
  Similar**. The sonic qualities of the file are used as a
  reference to find similar results.

In both cases, Similar Sound Search provides a new way to find audio,
even if it was recorded for a different purpose. These two techniques enrich traditional
filtering, which depends on metadata, extending the possibilities of existing sound
libraries.

Similar Sound Search uses a non-generative machine learning model to place audio and
text into a shared search space where sounds are grouped by acoustic and semantic
similarity. It is an optional package you can add to Wwise using the Audiokinetic
Launcher.

For more information about how Audiokinetic uses this non-generative machine learning
model, see [Use of Artificial
Intelligence](https://www.audiokinetic.com/en/solutions/use-of-ai).

### Installing Similar Sound Search

Similar Sound Search is an option in the Packages menu when installing Wwise or
modifying a Wwise installation. It is disabled by default. When enabled, more CPU is
used during scanning of the Original and Media Pool files after opening a project.
Additionally, more disk space is used in the `.cache` directory for the
project and for Media Pool databases.

To install Similar Sound Search:

1. From the Audiokinetic Launcher Wwise page, do one of the
   following:

   - Select a version of Wwise to install and click **Install**.
   - From an installed version of Wwise, click **Install options** (wrench icon) and
     then select **Modify**.
2. In the Packages list, select **Similar Sound
   Search**.
3. Click **Next**.
4. Click **Install** or **Modify**.

To use Similar Sound Search, you must enable it after installing it.

### Enabling Similar Sound Search

Similar Sound Search is disabled by default. To enable it:

1. From the menu bar, click **Project > User
   Preferences** (Shift+U).
2. In the Similarity Search group, select **Enable
   Similar Sound Search in Media Pool**.
3. Click **OK** to save your settings and
   close the dialog.

### Searching or filtering files using Similar Sound Search

You can search and filter for similar files in the following two ways:

- **Audio Description**: Ranks audio files
  in the Results pane using text-to-audio similarity. When you type a
  description of a sound, that description is compared directly to the
  audio content of all the files in the Results pane. This allows you to
  search for candidate sounds regardless of how they were labeled. For
  example, the description “footsteps in mud” might be highly similar to
  recordings labeled as “smashing fruit".
- **Audio Similarity**: Ranks audio files
  in the Results pane using audio-to-audio similarity. The audio content
  of the reference sound is compared to all of the audio files in the
  Results pane.

In both cases, the results are reordered based on their similarity score. Search
by Audio Description directly in the Search bar. Search for Audio Similarity in the
waveform. Search by both Audio Description and Audio Similarity using
filters.

### To search by Audio Description in the Search bar

1. From the **Selected Fields** drop-down list,
   select **Audio Description**.
2. Type in a phrase to describe the sound you are looking for. For example,
   "loud car crash".

   The search dynamically returns files that sound similar to the description
   as type, the most similar being at the top of the Results pane.

### To search by Audio Similarity in the waveform

- Right-click the waveform of a file in the Results pane or in the Audio
  Preview/Region Selector and select **Find
  Similar**.
- Right-click a region in waveform of the Audio Preview/Region Selector and
  select **Find Similar (Region)**.

The results are reordered with the most similar to the waveform or region you
selected at the top of the Results pane.

### To search by creating filters for both Audio Similarity and Audio Description

You can create filters for both Audio Similarity and Audio Description. 有关详细信息，请参阅[“Filtering databases”一节](01-Working-with-databases.md#filtering_media_pool_databases "Filtering databases")。

---