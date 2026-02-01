# Working with the Media Pool

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > Working with the Media Pool

## Working with the Media Pool

The Media Pool is where you can search, organize, audition, and select your audio files to
import into Wwise. This is invaluable if you have downloaded Strata libraries or are working
with third-party sound libraries. These libraries often contain large numbers of files,
which can make it time-consuming to find what you want. You can add these library folders to
Media Pool databases to search for and audition your files directly in Wwise.

When you create a database and point to a path on your local or network drive, the Media
Pool extracts the metadata of each file, such as duration, bit depth, and sample rate. The
Media Pool caches the metadata so you can quickly search your libraries and filter the
results to get the files you want.

The databases you create in the Media Pool are not project-specific. You can open a
different project in Wwise and the databases you created persist. The databases are created
locally. If someone else opens the same project on their computer, they do not have access
to your databases.

You can access the Media Pool through the following menus or by pressing **Ctrl+P**:

- **Views > Utilities > Media Pool**
- **Project > Media Pool**

![](../../../images/media_pool.png)

|  |  |
| --- | --- |
|  | Databases pane lists the Project Originals folder and the User Databases folder where you can create databases and Virtual Folders to organize your databases. From here you can:  - Create new Databases and Virtual folders. - Rename and organize your folders and databases. - Open the Database Settings dialog. - See the number of Databases you have in the Media Pool   beside name of the Databases tab. - Select which Databases to search.  For more information on Databases, see [“Working with databases”一节](01-Working-with-databases.md "Working with databases"). |
|  | Use the drop-down list to select a type of search:  - **Selected Fields**: When you type a text string, the Results pane displays the closest matches for that string on the top of the list. The string is searched in the metadata fields that you selected to search by. Click the **Select Searchable Fields** (gear) icon to choose which fields to search by. 参见[“Searching for files by metadata”一节](01-Working-with-databases.md#searching_media_pool_databases "Searching for files by metadata")。 - **Audio Description**:   Uses Similar Sound Search to find files that sound like   the description you type. For example if you type, "loud   car crash", the Media Pool searches your databases to   find files with similar sounds to a loud car crash. For   more information about Similar Sound Search, see [“Similar Sound Search”一节](02-Similar-Sound-Search.md "Similar Sound Search").  |  |  |   | --- | --- |   | [备注] | 备注 |   | You must have Similar Sound Search installed to use **Audio Description**. 详请参阅[“Installing Similar Sound Search”一节](02-Similar-Sound-Search.md#install_similar_sound_search "Installing Similar Sound Search")。 | |
|  | Type a text string to search by file fields or a description of a sound to search by Similar Sound Search.  |  |  | | --- | --- | | [备注] | 备注 | | Only text fields can be searched. | |
|  | The Results pane displays the list of audio files based on your search and filter criteria. From here you can:  - View the audio files resulting in your search and   filter criteria. - Right-click a file or files to import them into your   project. - Right-click a file to find similar sounds in your   databases. - Right-click a file to import auto-detected   regions. - Configure the columns.  For more information, see:  - [“Configuring the Results columns”一节](01-Working-with-databases.md#configuring_media_pool_results "Configuring the Results columns") - [“Importing from the Results pane”一节](05-Importing-audio-files-into-your-project.md#importing_from_results_list "Importing from the Results pane") - [“Similar Sound Search”一节](02-Similar-Sound-Search.md "Similar Sound Search") |
|  | Click **Stop Search** to stop any search in progress.  Click **Refresh Search** if the contents of your database changes. |
|  | Metadata pane where you can view the metadata information for a selected file by which you can search and filter. Right-click on the metadata field and select to either add it as a column in the Results pane or add it as filter in the Filters pane. For information about the metadata fields, see [“Media Pool metadata”一节](03-Media-Pool-metadata.md "Media Pool metadata"). |
|  | Filters pane where you can add, modify, and delete filters that can be included or excluded when searching for audio files. You can see the number of Filters you have created by the number in parentheses beside the name of the Filters tab.  For more information on Filters, see [“Filtering databases”一节](01-Working-with-databases.md#filtering_media_pool_databases "Filtering databases"). |
|  | Transport pane where can control the following playback parameters:  - Volume - Pitch - LPF - HPF - Loop - Auto-play on Selection - Stop or play the playback. Alternatively, you can   press the spacebar.  You can transfer all the changes that you make to the Volume, Pitch, LPF, HPF, and Loop properties when you import the files by clicking the **Apply on Import** icon beside each option.  有关详细信息，请参阅[“Auditioning audio files”一节](04-Auditioning-audio-files.md "Auditioning audio files")。 |
|  | Audio Preview/Region Selector where you can:  - Position the playback cursor using the mouse. - Play or stop playback with the spacebar. - Skip to next and previous regions using the arrow   keys. - Select regions by:  - Manually clicking and dragging in the     waveform.   - Clicking on audio file markers.   - Enabling **Auto Select     Detected Regions**.   - Right-clicking the waveform and selecting     **Select All Detected     Regions**. - View the file path. - Add files or regions to the Audio File   Importer. - Find similar sounds to the selected regions or file   with Similar Sound Search.  For more information, see:  - [“Importing from the Audio Preview/Region Selector pane”一节](05-Importing-audio-files-into-your-project.md#importing_from_preview "Importing from the Audio Preview/Region Selector pane") - [“Importing regions into your project”一节](06-Importing-regions-into-your-project.md "Importing regions into your project") - [“Similar Sound Search”一节](02-Similar-Sound-Search.md "Similar Sound Search") |

---