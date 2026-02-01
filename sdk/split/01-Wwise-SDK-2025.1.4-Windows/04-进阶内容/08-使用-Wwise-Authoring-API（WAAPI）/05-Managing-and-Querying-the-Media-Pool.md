# Managing and Querying the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Managing and Querying the Media Pool

The Media Pool is a central repository in Wwise that stores cached information about audio files and their metadata in databases. You can use the Media Pool to quickly and efficiently search audio files across your file system according to various search criteria including natural language descriptions and audio similarity to other media files. You can add databases to the Media Pool to search files even if they are not part of the Wwise project.

You can access the Media Pool in Wwise Authoring, where you can also audition the audio files. You can use the Wwise Authoring API (WAAPI) to create, organize, and query databases.

# Managing Media Pool Databases

Media Pool databases are organized in a tree structure, with a private root node. The databases contain metadata about audio files such as their names, fields, and extracted audio features. The databases do not contain the audio files themselves. Wwise never writes, renames, or moves the actual audio files added to the Media Pool.

There is one Project Originals database, which contains information about audio files that are already included in the Wwise project. You can also create User Databases, which link to libraries or directories that contain audio files that are not included in the Wwise project (for example, a recently downloaded [Strata](https://www.audiokinetic.com/strata-library/overview/) collection). If you import files into Wwise from a location linked to a User Database, their information is added to the Project Originals database as well.

Add User Databases as required to search audio files from multiple locations in your file system. When you use WAAPI to create databases, ensure that you create them under the User Databases folder.

The following example shows the tree structure of the Media Pool databases and folders along with their GUIDs:

- Databases (Folder)
  - Project Originals
  - User Databases (Folder)
    - Database 1
    - Database 2
    - ...

The databases are created in:

- **Windows**: `LOCALAPPDATA%\Audiokinetic\Wwise\MediaPool\Databases`
- **macOS**: `$HOME/Library/Application Support/Audiokinetic/Wwise/MediaPool/Databases`

Each database has an associated Lightning Memory-Mapped Database (LMDB) as its storage backend.

## Using WAAPI to Manage Media Pool Databases

The databases in the Media Pool are standard Wwise objects and can be managed with the following WAAPI functions:

- [ak.wwise.core.object.create](ak_wwise_core_object_create.html) : Creates a Media Pool database.
- [ak.wwise.core.object.set](ak_wwise_core_object_set.html) : Creates a Media Pool database and sets its properties, or sets the properties of an existing database. See [Creating a Media Pool Database](ak_wwise_core_object_set_example_creating_a_media_pool_database.html) for an example.
- [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) : Sets the database properties.
- [ak.wwise.core.object.setName](ak_wwise_core_object_setname.html) : Sets the database name.

The WAAPI object type for a database is `"MediaPoolDatabase"`. See [Wwise 对象参考](wobjects_index.html) for more object types.

# Querying the Media Pool

When querying the Media Pool, you can search for audio files based on various criteria such as names, metadata fields, or audio features. You can filter results by specific fields and values.

To query the Media Pool, use [ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html).

Queries executed through WAAPI can define the following arguments:

- **searchText**: The text to search for in the audio files.
- **databases**: A list of Media Pool databases to search within, identified by name or GUID. If not specified, all databases are included.
- **maxResults**: The maximum number of results to return, as an integer. If not specified, the maximum is 1000.
- **filters**: A list of filters to apply to the search. The following filter types are supported:
  - **Field**: Filters files by the value of the specified field. This filter requires an `operator` and a `value`.
    - Supported text operators: `"equals"`, `"notEquals"`, `"contains"`, `"startsWith"`, `"endsWith"`, `"matchesRegex"`.
    - Supported numeric operators: `"equals"`, `"notEquals"`, `"lessThan"`, `"greaterThan"`, `"lessThanOrEqual"`, `"greaterThanOrEqual"`.
  - **Audio Similarity**: Finds files that are audibly similar to an audio file at the specified path. You can set a `weight` (0-1) to influence its importance in the search.
  - **Audio Description**: Finds files based on a natural language description of the desired audio content. You can set a `weight` (0-1) to influence its importance.

See [Examples](ak_wwise_core_mediapool_get.html#ak_wwise_core_mediapool_get_examples) for examples of Media Pool queries.

## Media Pool Fields

The Media Pool provides access to various metadata fields. In Wwise Authoring, these fields appear in the Media Pool's metadata pane.

You can use Media Pool fields to do the following:

- Filter audio files by properties set in the "filters" argument in [ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html).
- Specify return values in the options of [ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html). If you do not specify any return values, the query returns the `Path`, `FileId`, and `Db` for each file.

The Media Pool supports additional return options such as "Markers" and "DetectedRegions". See the `return` option in [ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html) for the complete list.

The fields are collected from the audio files and arranged under the following categories:

- **WAV**: Standard fields available for all audio files. Common fields include the following:
  - "WAV/Sample Rate"
  - "WAV/Bit Depth"
  - "WAV/Duration"
  - "WAV/Channel Configuration"
  - ...
- **BWFXML**: Fields specific to the BWFXML format (IXML), which some audio files might contain. They are grouped into different sections, and the supported sections include the following:
  - "BWFXML/ASWG": Contains Audio Software Working Group (ASWG) metadata.
  - "BWFXML/BWF": Contains Broadcast Wave Format (BWF) metadata.
  - "BWFXML/USER": Contains user-defined metadata.

To retrieve the full list of available fields, use [ak.wwise.core.mediaPool.getFields](ak_wwise_core_mediapool_getfields.html). Fields under the BWFXML section are discovered dynamically when Wwise scans the audio files.

### Universal Category System Fields

The [Universal Category System (UCS)](https://universalcategorysystem.com/) is an attempt to standardize audio file naming and categorization to improve organization, searchability, and interoperability across different sound libraries and software. UCS fields are located under the BWFXML/ASWG and BWFXML/USER sections in the Media Pool:

- BWFXML/ASWG/category
- BWFXML/ASWG/subCategory
- BWFXML/ASWG/catId
- BWFXML/USER/CATID
- BWFXML/USER/CATEGORY
- BWFXML/USER/SUBCATEGORY