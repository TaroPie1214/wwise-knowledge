# Importing regions into your project

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [Working with the Media Pool](00-Working-with-the-Media-Pool.md) > Importing regions into your project

## Importing regions into your project

You can select and import regions of an audio file in the Audio Preview/Region
Selector in the Media Pool. Regions are a selected portion of an audio file. You can
select and import one or more regions. You can also select regions from markers in the
waveform.

When you import a region, the entire audio file is imported to the Project Originals
folder. Objects are created in the project at the Object destination with the region
selected in the Source Editor. When you import more than one region, each region is
saved with a number appended to the Object name. For example, if you import three
regions from the same file, each region is saved as an object with "\_01", "\_02", and
"\_03" appended to the object name.

The following image shows three selected regions in a waveform.

![](../../../../images/media_pool_regions.png)

### Selecting regions

To select regions, do one of the following:

- Click the starting point of the region you want to select and drag to
  the end point of the desired region.
- Hold **Ctrl** or **Shift** and select multiple regions.
- If your file has markers, you can select a marker as a region by
  clicking the marker name.
- Select the **Auto Select Detected
  Regions** icon.

  Wwise automatically detects regions in WAV files based on the energy
  and silence and uses heuristics to determine regions of interest. This
  is particularly useful when an audio file contains several takes or
  variations of the same type of sound. For example, the detected regions
  can be imported into a Random Container in just a few steps, reducing
  the amount of work necessary to prepare the files.
- Right-click the waveform of a file in the Audio Preview/Region
  Selector pane and select **Select All Detected
  Regions**.

### Deselecting regions

To deselect regions, do one of the following:

- Right-click a region and select either **Deselect
  Region** or **Deselect All
  Regions**.
- Press **Esc**.

### Importing regions from the Results pane

If you are importing directly into an existing Sound SFX object in your project,
you can import the detected regions as audio sources. If you are importing the
detected regions into your Default Work Unit, you can select to import them as
either Sound SFX or Sound Voice objects.

1. In the Results pane, right-click a single file, or select more than
   one file and right-click, and then select **Import
   Detected Region(s) to <selected Container in the Project
   Explorer>** or **Import Detected
   Region(s) to 'Default Work Unit'**.
2. Select the type of object to import as.

Wwise automatically detects regions in WAV files based on the energy and silence
and uses heuristics to determine regions of interest. This is particularly useful
when an audio file contains several takes or variations of the same type of sound.
For example, the detected regions can be imported into a Random Container in just a
few steps, reducing the amount of work necessary to prepare the files.

### Importing regions from the Audio Preview/Region Selector pane

To import regions into your project, select a region or regions and then do one of
the following:

- Click **Regions(#)**. The region or
  regions are displayed in the Audio File Importer dialog.
- Right-click a region and then select **Add Regions
  in Audio File Importer**. The regions are added to the
  Audio File Importer.
- Right-click a region and then select **Import
  Selected Region(s) to <folder selected in Project
  Explorer>**. The Objects are added to the folder that you
  have selected in the Project Explorer.
- Right-click a region and then select **Import
  Selected Region(s) to 'Default Work Unit'**. The Objects
  are added to the Default Work Unit in the Project Explorer.
- Press and hold the drag icon in a region and then drag and drop it in
  a Container in the Project Explorer. If you have more than one region
  selected, they will all be included in the drag and drop.

---