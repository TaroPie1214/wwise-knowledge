# Importing Base64 content to create a Sound SFX object

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing Base64 content to create a Sound SFX object

Creates a Source SFX object and an audio file source object and imports the specified base64 content as a WAV file.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"import": {

"files": [

{

"audioFileBase64": "Sine.wav|UklGRpgDAABXQVZFZm10IBAAAAABAAIARKwAABCxAgAEABAAZGF0YXQDAAAAAAAAjgKOAhoFGgWmB6YHMQoxCrkMuQw+Dz4PwRHBEUAUQBS6FroWMBkwGaAboBsLHgsecCBwIM4iziIkJSQlcydzJ7opuin4K/grLC4sLlgwWDB5MnkykDSQNJs2mzacOJw4kDqQOnk8eTxVPlU+JEAkQOVB5UGZQ5lDP0U/RddG10ZgSGBI2UnZSURLREueTJ5M6U3pTSRPJE9OUE5QZ1FnUXBScFJnU2dTTlROVCJVIlXlVeVVllaWVjVXNVfCV8JXPVg9WKVYpVj7WPtYPlk+WW9Zb1mNWY1ZmVmZWZJZkll4WXhZTFlMWQ1ZDVm8WLxYWFhYWOJX4ldaV1pXv1a/VhNWE1ZUVVRVhFSEVKNTo1OwUrBSq1GrUZZQllBwT3BPOU45TvNM80ycS5xLNUo1Sr9Iv0g6RzpHp0WnRQREBERUQlRClkCWQMo+yj7xPPE8DDsMOxo5GjkdNx03FDUUNQAzADPhMOEwuC64LoYshixKKkoqBSgFKLkluSVkI2QjCCEIIaUepR48HDwczBnMGVgXWBffFN8UYRJhEt8P3w9bDVsN0wrTCkkISQi+Bb4FMQMxA6MAowAW/hb+ifuJ+/z4/Phy9nL26fPp82PxY/Hf7t/uYOxg7OTp5Olt523n++T75I/ij+Ip4Cngyd3J3XHbcdsg2SDZ19bX1pfUl9Rg0mDSMtAy0A7ODs71y/XL58nnyePH48fsxezFAMQAxCHCIcJPwE/Air6KvtK80rwpuym7jrmOuQG4AbiEtoS2FbUVtbezt7NosmiyKbEpsfuv+6/drt2u0a3RrdWs1azqq+qrEasRq0qqSqqVqZWp8ajxqGCoYKjgp+CndKd0pxmnGafRptGmnKacpnmmeaZopmima6ZrpoCmgKanpqem4abhpi6nLqeNp42n/6f/p4KogqgYqRipwKnAqXqqeqpGq0arI6wjrBKtEq0SrhKuI68jr0WwRbB3sXexurK6sg20DbRwtXC14rbitmO4Y7jzufO5kruSuz+9P736vvq+wsDCwJfCl8J6xHrEaMZoxmPIY8hpymnKesx6zJbOls690L3Q7dLt0ibVJtVp12nXs9mz2QbcBtxh3mHewuDC4CnjKeOX5ZflCugK6IPqg+r/7P/sgO+A7wTyBPKL9Iv0FPcU95/5n/ks/Cz8uf65/g=="

}

]

}

}

],

"onNameConflict": "merge"

}

# 结果

{

"objects": [

{

"id": "{811AE2DB-9EA3-4749-A8B9-CB89588D1925}",

"import": {

"logs": [

{

"message": "Finalizing Importation...",

"severity": "Message"

}

],

"objects": [

{

"id": "{46295B27-A02A-4FAB-9BCB-69018995F41C}",

"name": "Sine"

},

{

"id": "{64C7AA03-7C5C-4554-A5E4-0866DDA133C1}",

"name": "Sine"

}

]

},

"name": "Default Work Unit"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。