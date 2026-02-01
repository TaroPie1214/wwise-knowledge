# Working with databases

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [Working with the Media Pool](00-Working-with-the-Media-Pool.md) > Working with databases

## Working with databases

In the Media Pool you can create databases, which you can then organize, search, and
filter to quickly find audio files in your local or network libraries.

### Creating databases

There are two folders in the **Databases** tab:

- **Project Originals**: Lists the audio files
  in your project. After you import files into your project, they are included
  in this list.
- **User Databases**: Used to create databases
  and Virtual Folders to organize the audio files in your libraries.

**To create databases:**

1. From the Media Pool **Databases** tab, do one
   of the following:

   - Right-click **User Databases**
     and then select **New Child** >
     **Media Pool Database**.
   - Click the **Create Media Pool
     Database** icon.
   - Drag and drop one or many folders from your local file browser
     to a User Databases Virtual Folder.
2. Enter a name for your database.
3. To open the Media Pool Database Settings dialog, do one of the following:

   - Double-click the database.
   - Right-click the database and then select **Database Settings**.
4. Click **+**  to create a path to the folder
   containing the files you want to add to the database.
5. Browse to select the folder and then click **Select
   Folder**.
6. 单击 **OK**（确定）。

   The Media Pool recursively scans the folders linked to the database and
   adds all audio file metadata to that database. The files are then displayed
   in the Results pane.

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | The Media Pool detects the following audio formats: .wav, .amb, and .adm. |

![](../../../../images/mediapool_data_settings.png)

|  |  |
| --- | --- |
|  | Open the folder containing the database cache files. |
|  | Click + to link your library folder to the database. |
|  | The list of library folders that are tracked by your database. |
|  | Click **Rescan Database** to manually scan your database because of file changes. Media Pool databases are scanned every time you open a project.  |  |  | | --- | --- | | [备注] | 备注 | | If you suspect a scan has failed or a database cache is corrupted. Click **Open Containing Folder** to delete the cached files, and then click **Rescan Database**. The tracked folders are stored in a separate settings file and are not affected. Database settings are found in: `%AppData%\Audiokinetic\MediaPool\` | |

### Organizing databases

To organize your databases and access files quickly, you can create Virtual
Folders and add databases to them. To create a folder or database:

- Right-click a folder and then select **New Child >
  Virtual Folder** or **Media Pool
  Database**: Creates a new child folder or child
  database.
- Click the **Create new Media Pool
  Database** icon: Creates a new database under the folder or
  database you have selected.
- Right-click a folder or database and then select **New Parent > Virtual Folder**: Creates a new parent
  Virtual Folder where you can add databases.
- With a virtual folder selected, click the **Create
  new Virtual Folder** icon. Creates a new folder under the
  selected virtual folder.

You can further organize your Databases pane by right-clicking a
folder or database and then selecting:

- **Delete**: Delete your database or
  folder. Alternatively, you can press the **Delete** key.
- **Rename**: Rename you database or
  folder. Alternatively, you can press **F2**.
- **Set color**: Select a color for a
  folder or database. A color bar is displayed beside the folder or
  database name.

### Configuring the Results columns

By default, the Results pane displays only the **Name** and **Waveform** columns. To
configure the columns, do one of the following:

- To add or remove columns, right-click the column header and select
  **Configure Columns** and then select
  the field to display as a column.
- To reorder the columns, right-click the column header and select
  **Configure Columns**. Reorder a
  selected field by dragging and dropping it.
- To add a column from a field in the Metadata pane, right-click a field
  and select **Add Field as Column**. For
  example, to add a **Sample Rate** column,
  right-click **Sample Rate** and then select
  **Add Field as Column**.

![](../../../../images/media_pool_columns.png)

|  |  |
| --- | --- |
|  | Select a field to include in the Results pane. Deselect a field to remove from Results pane.  Search for a field in the Search bar. |
|  | Select and drag the field to place it in the order it will be displayed in the Results pane. In this image, the WAV/Channels field is being dragged to appear after the General/Name field. |

### Searching for files by metadata

Use the Search field at the top of the Results pane to find specific audio files.
As you type in the Search field, the Media Pool searches the metadata in the
database files and displays matches in the Results pane.

The Results pane displays both the Project Originals and the Database files.
Select or deselect the check box next to the folders or databases you want to
include or exclude from the search.

To search for files by metadata:

1. Select the **Selected Fields** option
   Search drop-down list.
2. Click the gear icon to the right of the **Search** field and then select the check box for each
   field to include in the search.
3. Type in the text string to search by.

   You can use the following operators to get more precise results:

   - **Exact phrase**: Use double
     quotes (") to find a specific phrase, for example, "footstep
     medium".
   - **Exclude words**: Use a
     hyphen (-) or exclamation mark (!) to remove unwanted
     results. For example: footstep !concrete.

   As you type, the Results pane is dynamically populated with matches.
   The best matches appear at the top of the list.

For a file to appear in the Results pane, each word in the search string
must be found at least once in the selected metadata fields. Using quotation marks
to specify an exact phrase enforces that the words should appear in the same field
in the written order.

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| Right-click the file in the Results pane or the waveform in the Audio Preview/Region Selector and select either **Copy Path to Clipboard** or **Copy Filename to Clipboard** to paste exact matches. |

The word matching process is approximate, allowing for prefix matches. For
example, “foot” matches with “footstep”. The approximate search also allows for
typos. For example, “foottep” matches with “footstep”.

Matched files are given a score that ranks the exact matches higher than
approximate matches. To view the **Score** column,
right-click the column header and select **Configure
Columns** to select the Score field.

|  |  |
| --- | --- |
| [备注] | 备注 |
| You can also search by Similar Sound Search. 请参阅 [“Similar Sound Search”一节](02-Similar-Sound-Search.md "Similar Sound Search")。 |

### Filtering databases

You can create filters to refine the list of audio files in the Results
pane.

![](../../../../images/mediapool_filters.png)

|  |  |
| --- | --- |
|  | The number of filters in the Filters pane. |
|  | Click the delete icon to delete all filters. Alternatively you can click the delete icon beside a filter to delete only that one. |
|  | Click **+** to add a filter. |
|  | A field filter created by selecting or right-clicking a metadata field. |
|  | An **Audio Similarity** filter to find audio files with a similar sound to the waveform of the selected file. |
|  | An **Audio Description** filter to find audio files that sound similar to the description you type. |

**To create a filter from the Metadata pane:**

1. Select a file from the Results pane. The metadata for that file is
   displayed in the Metadata pane.
2. In the Metadata pane, right-click a field and select **Add Field Filter**. For example, to filter the results by
   Sample Rate, right-click **Sample Rate** and
   then click **Add Field Filter**.

   The field is displayed in the **Filters**
   pane with its current value.
3. Select an operator and enter or edit the value.

   The Results pane is updated based on the operator and value that you have
   configured.

**To create a filter in the Filters pane:**

1. Click the Filters tab.
2. Click **+**.
3. 选择以下任一选项：

   - **Field**: Filters by metadata
     fields.
   - **Audio Similarity**: Ranks
     search results based on their similarity to the waveform of the
     audio of the selected file.
   - **Audio Description**: Ranks
     search results based on their similarity to the description of a
     sound.
4. If you selected **Field**, click the pencil
   icon to select a field you want to filter by and then click **OK**.
5. Select an operator and enter the value.

   The Results pane is updated based on the operator and value that you have
   selected.

**To create an Audio Similarity filter**

1. 执行以下操作之一：

   - In the Media Pool Results pane, right-click a file and select
     **Find Similar**.
   - In the Media Pool Audio Preview/Region Selector, right-click
     anywhere in the waveform and select **Find
     Similar**.
   - In the Media Pool Audio Preview/Region Selector, right-click a
     selected region and then select **Find
     Similar (Region)**.
   - In the Project Explorer, right-click a Sound SFX object and
     select **Find Similar in Media
     Pool**.

   The filter is added to the Filters pane.
2. Set a weight for the filter, if desired.

|  |  |
| --- | --- |
| [备注] | 备注 |
| For more information on **Audio Similarity** and **Audio Description**, see [“Similar Sound Search”一节](02-Similar-Sound-Search.md "Similar Sound Search"). |

The following tables describe the filter properties.

| Properties shared by all filters | 描述 |
| --- | --- |
| Filter name | Displays the name and information about the filter configuration. To change the order of how the filters appear in the Filters pane, right-click the name of the filter and select either **Move Up Media Pool Filter at index #** or **Move Down Media Pool Filter at index #**. |
| 包含 | Select to filter based on the field. If you deselect this check box, this filter is removed from your search criteria. |

| Field Filter Properties | 描述 |
| --- | --- |
| Field | The metadata field by which to filter the results. |
| Operator | The operation that defines how to filter the field. This operator changes depending if the field is a text or numeric field.  The operators for text fields:  - != (not equal to) - = (equal to) - contains - starts with - ends with - matches regex (regular expression).  For more information about regular expressions   that Wwise uses, see [Regular expression reference](https://www.audiokinetic.com/library/edge/?source=Help&id=regexref).  The operators for numeric fields:  - < (less than) - <= (less than or equal to) - != (not equal to) - = (equal to) - &gt;= (greater than or equal to) - &gt; (greater than) |
| Value | The value by which the operator filters the results. For example, for the numeric field **Sample Rate**, you can filter a your results to include only audio files that have a Sample Rate of < 48000 Hz.  The operator is less than (**<**) and the value is **48000**. |

| Similar Sound Search Properties | 描述 |
| --- | --- |
| 描述 | Used for the **Audio Description** for Similar Sound Search filter. Type a description of the sound to filter by, for example, "buzzing". |
| Similar To | Displays the waveform that other audio files are compared to. |
| Weight | The relative importance of the similarity filter to other filters. Used for both **Audio Similarity** and **Audio Description** filters. Use this to boost or reduce the impact of a given similarity filter for ranking the search results. |

---