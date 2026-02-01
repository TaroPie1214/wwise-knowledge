# Wwise Project Database Sample

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Project Database Sample

The Wwise Project Database is a dynamic library that provides a memory-based database view of the current state of a Wwise project’s generated SoundBanks. All information available in the JSON metadata files produced when SoundBanks are generated is accessible in the Project Database.

All code presented in this section is available in a sample project in the `samples\WwiseProjectDatabase` directory.

There are two types of information in the database:

- The Metadata structures provide the raw information from the JSON files.
- The Ref classes allow access to information related to the metadata.

# Metadata Structures

The Metadata structures are defined exactly like the JSON files that describe the generated SoundBank metadata. No context is provided and the member names in these structures are identical to those in the JSON files.

The file definition begins with a `WwiseMetadataRootFile` object that defines the kind of optional root objects the file can declare. The structures expose the possible inner objects and values.

After they are loaded in memory, these structures provide a concise and clear representation of the generated SoundBanks.

Only one copy of this information is kept in memory in `WwiseRootDataStructure` and `WwisePlatformDataStructure` JSON files.

# Ref Classes

The Ref classes define each metadata object by its relation to related metadata. This class is helpful because the metadata in the generated SoundBanks minimizes duplicated information, and instead uses references to various data structures. For example, a media list references an Event ID, but the metadata for that media, such as the file location, is defined in the higher-level SoundBank metadata.

To reference an Event’s Switch Container value, a Ref class keeps a copy of a shared pointer to the file’s root and contains directions to locate the Switch Container, such as "this file, in the SoundBanks structure, the first SoundBank, the fourth declared Event, the third declared Switch Container."

The following code samples demonstrate how these classes work:

struct WwiseMetadataMediaAttributes : public WwiseMetadataMediaReference

{

WwiseDBString Language;

bool bStreaming;

WwiseMetadataMediaLocation Location;

bool bUsingReferenceLanguage;

WwiseDBShortId Align;

bool bDeviceMemory;

FWwiseMetadataMediaAttributes(FWwiseMetadataLoader& Loader);

private:

static WwiseMetadataMediaLocation LocationFromString(const WwiseDBString& LocationString);

};

struct WwiseMetadataMedia : public WwiseMetadataMediaAttributes

{

WwiseDBString ShortName;

WwiseDBString Path;

WwiseDBString CachePath;

WwiseDBShortId PrefetchSize;

FWwiseMetadataMedia(FWwiseMetadataLoader& Loader);

};

Here is a media example:

"Media": [

{

"Id": "274591330",

"Language": "English(US)",

"Streaming": "false",

"Location": "Loose",

"ShortName": "Hello.wav",

"Path": "Media/English(US)/27/274591330.wem",

"CachePath": "Voices/English(US)/Hello\_10C4C929.wem"

}

Essentially, the Ref classes provide context. Therefore, you can get information about the Switch Container as well as the class parents: the Event, the SoundBank, and the file.

Some referred types require additional information. For example, the platform information is divided into two complementary files: `ProjectInfo.json` and `PlatformInfo.json`, so the platform Ref contains two different structures. Similarly, some other referred types might reside in multiple locations. The Ref class attempts to accommodate these particularities.

Finally, the Ref classes provide additional utilities. If you pass the necessary global maps, you can get supplemental information alongside the Ref classes that are included in the specified Wwise object. For example, you can ask for the media requested in a particular Event’s definition, and it returns the media as Refs.

Because the Ref information is declared as the base and derived structs, in a Switch Container you can request all of the Event’s Switch Container values and get the siblings simultaneously. The same is true for other types of information contained in Events.

# AnyRef Class

At a higher level, the AnyRef class contains a pointer to any kind of Ref structure or a Null object. The AnyRef class contains the type and a shared pointer. There are limited operations available at the AnyRef level, such as retrieving the object’s Short ID, its GUID, and its name. For everything else, you can cast the boxed Ref object to its type.

# Accessing Information: WwiseProjectDatabase and WwiseDataStructure

The WwiseProjectDatabase handles queries through its access methods from the API.

Inside the Data structure, there are two structures:

- The **Root structure** contains basic information for each platform for a project’s structure:
  - The Platform list, which includes all available platforms for a project, even if they aren’t loaded.
  - The Language list.
- The **Platforms structure map** contains all of the project’s information for each platform.

The Data structure’s structs contain:

- A list of all loaded file names in the `GeneratedPlatformFiles` property.
- One unique copy of each parsed JSON file in the `JsonFiles` property.
- Refs for each accessible piece of data.

In addition, the Data structure allows templated access through functions such as `GetRef`.

The following code samples demonstrate how to determine whether a SoundBank is an Auto-Defined SoundBank:

bool IsAutoDefinedSoundBank(const char\* InSoundBankName)

{

//Init is usually only called once at the start of the application. It is here to show that it needs to be called for the Project Database to parse the SoundBanks.

[Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)("Path/To/GeneratedSoundBank", "Windows");

auto SoundBankRef = GetSoundBankRefString(const char\* InString);

if(SoundBankRef)

{

bool bIsUserDefined = IsUserBank(SoundBankRef);

DeleteSoundBankRef(SoundBankRef);

//If the SoundBank is not a User-Defined SoundBank, then it is an Auto-Defined SoundBank

return !bIsUserDefined;

}

return false;

};

# Building the Wwise Project Database

The Wwise Project Database binaries are available in the `\[Debug|Profile|Release]\bin` directory. To rebuild the application yourself, follow these steps:

## Windows

- Open the solution found in `samples\WwiseProjectDatabase` and build using the desired configuration.

# Creating Adapter Types

By default, the Project Database uses Adapter Types based on the standard C++ library. You can create your own Adapter Types. The following types can be created:

- WwiseArray
- WwiseGUID
- WwiseFuture
- WwiseJSONObject
- WwiseMap
- WwiseMultiMap
- WwisePair
- WwiseSet
- WwiseSharedPtr
- WwiseString
- WwiseTuple
- WwiseTask

Refer to the Standard Types to see which functions need to be created.

Next, create a file that defines all the WwiseDBTypes (For example, WwiseDBString) as the types you created. In `WwiseWrapperTypes.h`, include your new file. Make sure no other types are included .

[AK::Comm::Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)

AKSOUNDENGINE\_API AKRESULT Init(const AkCommSettings &in\_settings)