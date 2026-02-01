# AkMemoryArena 的配置和调整

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

AkMemoryArena 的配置和调整

AkMemoryArena 是 Wwise 声音引擎使用的自定义内存分配器。您可以利用它的各种设置来管理其预留的内存。声音引擎会使用多个 AkMemoryArena。为此，可根据项目需要对其进行适当调整，来大幅提升声音引擎整体的内存利用效率。

- [AkMemoryArena 概述](goingfurther_memoryarenas.html#goingfurther_memoryarenas_overview)
- [AkMemoryArenaSettings](goingfurther_memoryarenas.html#goingfurther_memoryarenas_settings)
- [AkMemoryArenaSettings 分配回调](goingfurther_memoryarenas.html#goingfurther_memoryarenas_callbacks)
- [有关 AkMemoryArena 配置的建议](goingfurther_memoryarenas.html#goingfurther_memoryarenas_recommendations)

# AkMemoryArena 概述

作为通用的内存分配器，AkMemoryArena 会根据内存分配大小将其归入不同的内存堆（Small、Medium、Large 或 Huge）。

Small 分配是指 256 字节以内的分配。此阈值不可配置。这些分配会归入 Small-Block Allocator (SBA) 内存堆。SBA 基于由固定大小的内存块构成的跨度管理各项分配。这样方便对内存碎片做统一的处理。各个跨度的大小可自行配置。这些跨度的分配基于父级 Medium 或 Large 内存堆。在初始化 SBA 时，会为其设定初始内存区域。这样可降低 SBA 内存堆中的分配所用的开销。通常，AkMemoryArena 中各种规模的内存分配都需要 16 字节的开销（用于存储分配元数据）。不过，初始区域内的 SBA 分配并不需要这样的开销。比如，若普通 SBA 跨度为 16 KiB (Kibibyte)，并被配置为处理 64 字节的分配，则该跨度可处理约 200 个 80 字节的内存块。不过，若在初始区域内分配同样的 16 KiB 跨度，则其可处理约 250 个 64 字节的内存块。

Medium 分配是指 256 ~ `AkMemoryArenaSettings::uAllocSizeLarge` 字节的分配；Large 分配是指 `AkMemoryArenaSettings::uAllocSizeLarge` ~ `AkMemoryArenaSettings::uAllocSizeHuge` 字节的分配。Medium 和 Large 分配所用的内存堆采用基于 Two-level segregated fit (TLSF) 的算法。如此一来，这些内存堆便可以相当于 O(1) 的性能进行分配和释放。这些内存堆采用 Good-fit 分配策略来决定要将分配放在哪里。不过，跟原始的 TLSF 算法不同，AkMemoryArena 所用的 TLSF 内存堆还允许随着内存需求的增加请求获取新的内存跨度，而不要求新的内存跨度跟其他内存跨度是连续的。另外，在释放所有相关内存后，TLSF 内存堆也会释放内存。在请求执行 Medium 或 Large 分配时，TLSF 内存堆会先尝试查找初始 Base 内存跨度中可用的内存块；若无可用内存块，则尝试查找已映射的 Medium 或 Large 跨度中可用的内存块。若仍未找到可用的内存块，则请求在 Huge 分配堆中获取新的跨度，并添加到 Medium 或 Large 跨度列表。同样地，在跨度没有任何分配时，其将被视为 Unused。在 Unused 跨度达到一定数量后，它们会被释放给系统。

Huge 分配是指大到无法归入 Medium 或 Large 内存堆的分配。这些分配放在单独的跨度中，并且不与其他分配共用内存。另外，Huge 跨度的内存不会被重复使用或缓存。也就是说，一旦相关内存被释放，跨度就会马上被释放。

# AkMemoryArenaSettings

AkMemoryMgr 包含一系列初始化设置，方便配置声音引擎所用的不同 AkMemoryArena。除非另有说明，否则下述值的大小不需要是 2 的幂。

- `AkMemoryArenaSettings::bEnableSba` – 决定是否要激活 SBA。若未激活，则将所有 Small 分配视为 Medium 分配，并发送到 TLSF 内存堆。在默认情况下，Media AkMemoryArena 会禁用此选项，因为 Media 分配对 SBA 来说通常太大。
- `AkMemoryArenaSettings::uSbaInitSize` – SBA 内存堆的初始内存区域的大小（字节）。因为减少了内存分配开销，所以此初始区域中的分配占用空间较少。
- `AkMemoryArenaSettings::uSbaSpanSize` – SBA 内存堆所用各个内存跨度的大小（字节）。您可以将其设为较大的值来略微提升系统性能，但可能会因内存未被使用而造成更多内存浪费。注意，该值必须是 2 的幂。
- `AkMemoryArenaSettings::uSbaMaximumUnusedSpans` – 决定在释放之前最多可有多少个在 SBA 内存堆初始内存区域以外分配的 SBA 跨度处于未使用状态。
- `AkMemoryArenaSettings::uTlsfInitSize` – TLSF 内存堆所用初始 Base 内存跨度的大小（字节）。
- `AkMemoryArenaSettings::uTlsfSpanSize` – 为 Medium 分配创建的每个辅助内存跨度的大小（字节）。若请求执行的分配（需要获取新的跨度）大于该值，则将请求分配的大小舍入为该值的下一倍数。
- `AkMemoryArenaSettings::uTlsfLargeSpanSize` – 为 Large 分配创建的每个辅助内存跨度的大小（字节）。若请求执行的分配（需要获取新的跨度）大于该值，则将请求分配的大小舍入为该值的下一倍数。
- `AkMemoryArenaSettings::uTlsfSpanOverhead` – 在为 TLSF 请求获取新的跨度时从请求执行的 Huge 分配减去的字节数。
- `AkMemoryArenaSettings::uTlsfMaximumUnusedMediumSpans` – 决定在释放之前最多可有多少个用于 Medium 分配的跨度处于未使用状态。
- `AkMemoryArenaSettings::uTlsfMaximumUnusedLargeSpans` – 决定在释放之前最多可有多少个用于 Large 分配的跨度处于未使用状态。
- `AkMemoryArenaSettings::uAllocSizeLarge` – 决定分配要达到多少字节才会被归为 Large 分配。所有小于该值但大于 256 字节的分配都将被视为 Medium 分配。注意，若该值大于 uAllocSizeHuge，则不会将任何分配归为 Large 分配。
- `AkMemoryArenaSettings::uAllocSizeHuge` – 决定分配要达到多少字节才会被归为 Huge 分配。
- `AkMemoryArenaSettings::uMemReservedLimit` – 决定此 AkMemoryArena 最多可预留多少内存（字节）。若 Huge 内存堆尝试请求获取的内存超过该限值，则返回 nullptr，且 `fnMemAllocSpan` 不会被调用。
- `AkMemoryArenaSettings::fnMemAllocSpan` – 在 Huge 内存堆要实施新的分配时执行的用户提供的回调（包括请求从 TLSF 内存堆获取新的跨度）。
- `AkMemoryArenaSettings::fnMemFreeSpan` – 在 Huge 内存堆释放分配时执行的用户提供的回调（包括从 TLSF 内存堆释放跨度）。

以下示例代码展示了在默认情况下会如何初始化 AkMemoryMgr 的 AkMemoryArenaSettings。您可以在此基础上根据自身需要对 AkMemoryArenaSettings 做进一步的设置：

[AkMemSettings](struct_ak_mem_settings.html) memSettings;

for ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) eArenaType = [AkMemoryMgrArena\_Primary](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4cada4fb0aaa502bf0b4481e825e20127be); eArenaType < [AkMemoryMgrArena\_NUM](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca6d04cd32dae8081d7af43611f5f67ab6); eArenaType++)

{

[AK::MemoryArena::AkMemoryArenaSettings](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings.html)& arenaSettings = memSettings.[memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)[eArenaType];

// 为所有设置设定默认值

arenaSettings.[bEnableSba](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_ae6e2a5d134dcc17e2560db12032efdae.html#ae6e2a5d134dcc17e2560db12032efdae) = true;

arenaSettings.[uSbaInitSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a38a3458e0df1124c2fe1adce95a65da5.html#a38a3458e0df1124c2fe1adce95a65da5) = 0;

arenaSettings.[uSbaSpanSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a37b90d5f6b49be36850ec06438077ea1.html#a37b90d5f6b49be36850ec06438077ea1) = 16384;

arenaSettings.[uSbaMaximumUnusedSpans](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_abb44a42ccd21315a44b276d4fa2cb648.html#abb44a42ccd21315a44b276d4fa2cb648) = 1;

arenaSettings.[uTlsfInitSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a84025d5b4c90a8d3921c28cd9b7b517c.html#a84025d5b4c90a8d3921c28cd9b7b517c) = 2 \* 1024 \* 1024;

arenaSettings.[uTlsfSpanSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a61be009fb1b18dd0ea983eb873998d60.html#a61be009fb1b18dd0ea983eb873998d60) = 2 \* 1024 \* 1024;

arenaSettings.[uTlsfLargeSpanSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_ae3530381c708848afa239a5b4161aed1.html#ae3530381c708848afa239a5b4161aed1) = 8 \* 1024 \* 1024;

arenaSettings.[uTlsfSpanOverhead](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_af54775ab16bddad12d14d0e6bc4cbdf0.html#af54775ab16bddad12d14d0e6bc4cbdf0) = 128; // 对于 Large 分配，std::malloc 似乎产生了 128 B 的开销

arenaSettings.[uTlsfMaximumUnusedMediumSpans](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a331f90c6905a828d5ec4434d5530b56d.html#a331f90c6905a828d5ec4434d5530b56d) = 1;

arenaSettings.[uTlsfMaximumUnusedLargeSpans](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a926578aa4de0d8d4085afa51ac8559b9.html#a926578aa4de0d8d4085afa51ac8559b9) = 1;

arenaSettings.[uAllocSizeLarge](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a9630470020e7dcf088b3a5e189b96d76.html#a9630470020e7dcf088b3a5e189b96d76) = UINT\_MAX;

arenaSettings.[uAllocSizeHuge](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a1f1ce618bd9b5b544354a93a47d1580e.html#a1f1ce618bd9b5b544354a93a47d1580e) = 4 \* 1024 \* 1024;

arenaSettings.[uMemReservedLimit](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a07814e5a7e2d552f7c8d4e880e121e9a.html#a07814e5a7e2d552f7c8d4e880e121e9a) = 0;

arenaSettings.[fnMemAllocSpan](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a5da5a8e3af77f520ee46bdcc97fce372.html#a5da5a8e3af77f520ee46bdcc97fce372) = [AKPLATFORM::AllocSpan](namespace_a_k_p_l_a_t_f_o_r_m_a8607b18eaea4aa3fdfa581caee18970a.html#a8607b18eaea4aa3fdfa581caee18970a);

arenaSettings.[fnMemFreeSpan](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a5bbf92ce6096b998829fa7622489db95.html#a5bbf92ce6096b998829fa7622489db95) = [AKPLATFORM::FreeSpan](namespace_a_k_p_l_a_t_f_o_r_m_a9bb64f59357062f99eb67c179ab1daba.html#a9bb64f59357062f99eb67c179ab1daba);

}

// ... 不过...

// 在初始化 Primary 内存堆时要使用较大的 uTlsfInitSize 和 uSbaInitSize，

// 因为几乎所有项目都会有大量数据传入其中

memSettings.[memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)[[AkMemoryMgrArena\_Primary](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4cada4fb0aaa502bf0b4481e825e20127be)].[uSbaInitSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a38a3458e0df1124c2fe1adce95a65da5.html#a38a3458e0df1124c2fe1adce95a65da5) = 2 \* 1024 \* 1024;

memSettings.[memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)[[AkMemoryMgrArena\_Primary](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4cada4fb0aaa502bf0b4481e825e20127be)].[uTlsfInitSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a84025d5b4c90a8d3921c28cd9b7b517c.html#a84025d5b4c90a8d3921c28cd9b7b517c) = 8 \* 1024 \* 1024;

// Media 内存堆不应激活 SBA

memSettings.[memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)[[AkMemoryMgrArena\_Media](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4caf034292470314618cda8b900728cf644)].[bEnableSba](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_ae6e2a5d134dcc17e2560db12032efdae.html#ae6e2a5d134dcc17e2560db12032efdae) = false;

// 若采用 Optimized（即 Release）配置，则不应初始化 Profiler 分配区

#if defined(AK\_OPTIMIZED)

memSettings.[memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)[[AkMemoryMgrArena\_Profiler](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca08ef70af1290299d43fafa826b9de574)].[fnMemAllocSpan](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a5da5a8e3af77f520ee46bdcc97fce372.html#a5da5a8e3af77f520ee46bdcc97fce372) = nullptr;

memSettings.[memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)[[AkMemoryMgrArena\_Profiler](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca08ef70af1290299d43fafa826b9de574)].[fnMemFreeSpan](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a5bbf92ce6096b998829fa7622489db95.html#a5bbf92ce6096b998829fa7622489db95) = nullptr;

#endif

# AkMemoryArenaSettings 分配回调

对于 `AkMemoryArenaSettings::fnMemAllocSpan` 和 `AkMemoryArenaSettings::fnMemFreeSpan` ，回调具有以下要求和行为：

- `fnMemAllocSpan` 只需返回指向所请求大小的内存分配的指针。返回的分配对所返回内存的对齐没有任何要求，也不需要跟之前的其他内存分配是连续的。
- `fnMemFreeSpan` 只需释放给定地址的内存。
- 只使用之前通过 `fnMemAllocSpan` 返回的地址对 `fnMemFreeSpan` 进行调用。size 参数跟最初请求分配时所用的值相同。
- 在执行 `fnMemAllocSpan` 的过程中，可将任意值写入到 `out_userData` 中。该值将作为 `in_userData` 参数提供给与 `fnMemFreeSpan` 对等的调用。

回调的实现可以非常灵活。比如，可使用以下代码来实现：

void\* [AllocSpan](namespace_a_k_p_l_a_t_f_o_r_m_a8607b18eaea4aa3fdfa581caee18970a.html#a8607b18eaea4aa3fdfa581caee18970a)(size\_t size, size\_t\* out\_userData)

{

return std::malloc(size);

}

void [FreeSpan](namespace_a_k_p_l_a_t_f_o_r_m_a9bb64f59357062f99eb67c179ab1daba.html#a9bb64f59357062f99eb67c179ab1daba)(void\* address, size\_t size, size\_t in\_userData)

{

std::free(address);

}

Advanced Profiler 中的 Memory Arenas 选项卡会列出当前分配的所有跨度以及与回调返回值匹配的各个跨度的地址和 userData 值。这样尤其方便在结合使用其他调试和性能分析工具的时候进行调试。

## 有关 AkMemoryArena 配置的建议

我们已对 AkMemoryMgr 管理的 AkMemoryArena 的默认设置做了优化，以便将初始预留内存控制在较低水平，并避免出现其他一些重大错误。不过，还是建议根据自身项目的需要对其中的大部分设置加以调节。合理的调节可显著优化 Wwise 中预留的内存、游戏引擎的总计预留内存以及 Wwise 的 CPU 处理性能。 为此，不妨参考以下建议来找到最适合自己项目的设置方案：

- **为 Primary 和 Media 内存区设置 `AkMemoryArenaSettings::uTlsfInitSize` 以使其符合典型的内存用量或整体内存预算。**通常，较大的 Base 跨度可让 TLSF 算法实现更好的内存碎片处理性能。另外，还可尝试使用单个跨度来监控是否超出了内存预算（通过检查有没有发出获取辅助内存跨度的请求）。这样还有助于制定整个应用程序的内存预算，因为项目启动时的系统总计预留内存能更好地反映长时间运行后的系统总计预留内存。
- **为 Primary AkMemoryArena 设置 `AkMemoryArenaSettings::uSbaInitSize` 以使其符合游戏当中的一般 SBA 预留要求。**借助 Advanced Profiler 中的 Memory Arenas 选项卡，可评估游戏当中的一般 SBA Reserved 需求，或确定一个较高的水位并设置 `uSbaInitSize` 以与之保持一致。通过将其设为较大的值，可将更多 SBA 内存分配放在初始内存区域中并减少各项内存分配的开销。另外，这样还可减少 TLSF 内存堆中分配的 SBA 跨度，并减少 Primary TLSF 内存堆中长时间产生的碎片。
- **或者：将 `AkMemoryArenaSettings::uTlsfInitSize` 设为较小的值以便回收内存并用于其他系统。**若有游戏场景会直接释放大量内存，而且内存碎片只会造成很小的影响，最好调低 Primary 或 Media 内存区的 `uTlsfInitSize` 以便将内存用于其他系统。
- **或者：将 `AkMemoryArenaSettings::uTlsfMaximumUnusedMediumSpans` 设为较大的值来确定内存预留水位。**在默认情况下，会将 `uTlsfMaximumUnusedMediumSpans` 和 `uTlsfMaximumUnusedLargeSpans` 设为 1 以便及时回收未使用的内存。您可以将其临时设为较高的值，确保在分配之后不会释放跨度，以此确定自己的内存预留水位。
- **使用 Large 内存分配来减少内存碎片。**在默认情况下，会禁用 Large 内存分配。但在有些情况下，可能要让特定大小的分配在物理上相互独立，以减少长时间产生的系统碎片。为此，不妨做些尝试以确定合理的 `uAllocSizeLarge` 和 `uTlsfLargeSpanSize` 值。这可能会增加前期的总计预留内存，因为有更多跨度中的内存不被使用，不过可以减少总体产生的内存碎片。注意，在有可用空间的情况下，Medium 和 Large 分配都会在 Base 跨度中执行。
- **将 `AkMemoryArenaSettings::uAllocSizeHuge` 设为较小的值以减少内部的碎片。**因为 Huge 分配是独立的，所以其不受内部内存碎片影响。若可控制因频繁调用 `fnMemAllocSpan` 和 `fnMemFreeSpan` 额外产生的 CPU 成本和外部碎片，那么最好调低 Huge 分配的认定阈值以便将更多内存归入到该类别中。
- **设置 `AkMemoryArenaSettings::uTlsfSpanOverhead` 以使其与 `fnMemAllocSpan` 实现中的分配元数据大小保持一致。**若 `fnMemAllocSpan` 实现所创建的内存分配本身需要一些元数据，请估算相应元数据的大小并调高 uTlsfSpanOverhead 以与之保持一致。该值用于略微减小请求获取的 TLSF 跨度的大小，以确保 `fnMemAllocSpan` 的分配映射预期数量的内存。比如，TLSF 跨度的大小应当为 2.00 MiB（2097152 字节），实际映射的内存可能为 2.02 MiB（2113536 字节），因为需要使用额外的内存页来存储内存分配元数据。不过，若预计需要 128 字节的元数据，则可将 uTlsfSpanOverhead 设为该值，以便从请求的 TLSF 跨度大小中减去对应量值。在本例中，请求的 TLSF 跨度大小为 2097024 字节，最终会刚好映射 2.00 MiB 的内存，从而减少物理内存的浪费。

[AK::MemoryArena::AkMemoryArenaSettings::uTlsfInitSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a84025d5b4c90a8d3921c28cd9b7b517c.html#a84025d5b4c90a8d3921c28cd9b7b517c)

AkUInt32 uTlsfInitSize

**Definition:** [AkMemoryArenaTypes.h:67](_ak_memory_arena_types_8h_source.html#l00067)

[AK::MemoryArena::AkMemoryArenaSettings::uAllocSizeHuge](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a1f1ce618bd9b5b544354a93a47d1580e.html#a1f1ce618bd9b5b544354a93a47d1580e)

AkUInt32 uAllocSizeHuge

**Definition:** [AkMemoryArenaTypes.h:75](_ak_memory_arena_types_8h_source.html#l00075)

[AkMemSettings::memoryArenaSettings](struct_ak_mem_settings_ad938c0122f4ed866a1ae1c459812d597.html#ad938c0122f4ed866a1ae1c459812d597)

AK::MemoryArena::AkMemoryArenaSettings memoryArenaSettings[AkMemoryMgrArena\_NUM]

Configuration of memory arenas for default memory allocator. For more information,...

**Definition:** [AkMemoryMgrModule.h:166](_ak_memory_mgr_module_8h_source.html#l00166)

[AK::MemoryArena::AkMemoryArenaSettings::uSbaMaximumUnusedSpans](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_abb44a42ccd21315a44b276d4fa2cb648.html#abb44a42ccd21315a44b276d4fa2cb648)

AkUInt32 uSbaMaximumUnusedSpans

**Definition:** [AkMemoryArenaTypes.h:65](_ak_memory_arena_types_8h_source.html#l00065)

[AK::MemoryArena::AkMemoryArenaSettings::uTlsfMaximumUnusedMediumSpans](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a331f90c6905a828d5ec4434d5530b56d.html#a331f90c6905a828d5ec4434d5530b56d)

AkUInt32 uTlsfMaximumUnusedMediumSpans

**Definition:** [AkMemoryArenaTypes.h:71](_ak_memory_arena_types_8h_source.html#l00071)

[AK::MemoryArena::AkMemoryArenaSettings::uTlsfLargeSpanSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_ae3530381c708848afa239a5b4161aed1.html#ae3530381c708848afa239a5b4161aed1)

AkUInt32 uTlsfLargeSpanSize

**Definition:** [AkMemoryArenaTypes.h:69](_ak_memory_arena_types_8h_source.html#l00069)

[AK::MemoryArena::AkMemoryArenaSettings](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings.html)

**Definition:** [AkMemoryArenaTypes.h:61](_ak_memory_arena_types_8h_source.html#l00060)

[AK::MemoryArena::AkMemoryArenaSettings::uSbaSpanSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a37b90d5f6b49be36850ec06438077ea1.html#a37b90d5f6b49be36850ec06438077ea1)

AkUInt32 uSbaSpanSize

**Definition:** [AkMemoryArenaTypes.h:64](_ak_memory_arena_types_8h_source.html#l00064)

[AK::MemoryArena::AkMemoryArenaSettings::bEnableSba](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_ae6e2a5d134dcc17e2560db12032efdae.html#ae6e2a5d134dcc17e2560db12032efdae)

bool bEnableSba

**Definition:** [AkMemoryArenaTypes.h:62](_ak_memory_arena_types_8h_source.html#l00062)

[AK::MemoryArena::AkMemoryArenaSettings::fnMemAllocSpan](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a5da5a8e3af77f520ee46bdcc97fce372.html#a5da5a8e3af77f520ee46bdcc97fce372)

AkAllocSpan fnMemAllocSpan

**Definition:** [AkMemoryArenaTypes.h:79](_ak_memory_arena_types_8h_source.html#l00079)

[AK::MemoryArena::AkMemoryArenaSettings::uMemReservedLimit](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a07814e5a7e2d552f7c8d4e880e121e9a.html#a07814e5a7e2d552f7c8d4e880e121e9a)

AkUInt32 uMemReservedLimit

**Definition:** [AkMemoryArenaTypes.h:77](_ak_memory_arena_types_8h_source.html#l00077)

[AkMemSettings](struct_ak_mem_settings.html)

**Definition:** [AkMemoryMgrModule.h:149](_ak_memory_mgr_module_8h_source.html#l00148)

[AK::MemoryArena::AkMemoryArenaSettings::uAllocSizeLarge](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a9630470020e7dcf088b3a5e189b96d76.html#a9630470020e7dcf088b3a5e189b96d76)

AkUInt32 uAllocSizeLarge

**Definition:** [AkMemoryArenaTypes.h:74](_ak_memory_arena_types_8h_source.html#l00074)

[AkMemoryMgrArena\_Primary](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4cada4fb0aaa502bf0b4481e825e20127be)

@ AkMemoryMgrArena\_Primary

**Definition:** [AkMemoryMgrModule.h:131](_ak_memory_mgr_module_8h_source.html#l00131)

[AK::MemoryArena::AkMemoryArenaSettings::uTlsfSpanOverhead](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_af54775ab16bddad12d14d0e6bc4cbdf0.html#af54775ab16bddad12d14d0e6bc4cbdf0)

AkUInt32 uTlsfSpanOverhead

**Definition:** [AkMemoryArenaTypes.h:70](_ak_memory_arena_types_8h_source.html#l00070)

[AkMemoryMgrArena\_Profiler](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca08ef70af1290299d43fafa826b9de574)

@ AkMemoryMgrArena\_Profiler

**Definition:** [AkMemoryMgrModule.h:133](_ak_memory_mgr_module_8h_source.html#l00133)

[AKPLATFORM::FreeSpan](namespace_a_k_p_l_a_t_f_o_r_m_a9bb64f59357062f99eb67c179ab1daba.html#a9bb64f59357062f99eb67c179ab1daba)

AkForceInline void FreeSpan(void \*address, size\_t size, size\_t in\_userData)

**Definition:** [AkMemoryMgrFuncs.h:42](_platforms_2_windows_2_ak_memory_mgr_funcs_8h_source.html#l00042)

[AkMemoryMgrArena\_NUM](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4ca6d04cd32dae8081d7af43611f5f67ab6)

@ AkMemoryMgrArena\_NUM

**Definition:** [AkMemoryMgrModule.h:135](_ak_memory_mgr_module_8h_source.html#l00135)

[AK::MemoryArena::AkMemoryArenaSettings::uTlsfSpanSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a61be009fb1b18dd0ea983eb873998d60.html#a61be009fb1b18dd0ea983eb873998d60)

AkUInt32 uTlsfSpanSize

**Definition:** [AkMemoryArenaTypes.h:68](_ak_memory_arena_types_8h_source.html#l00068)

[AK::MemoryArena::AkMemoryArenaSettings::uTlsfMaximumUnusedLargeSpans](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a926578aa4de0d8d4085afa51ac8559b9.html#a926578aa4de0d8d4085afa51ac8559b9)

AkUInt32 uTlsfMaximumUnusedLargeSpans

**Definition:** [AkMemoryArenaTypes.h:72](_ak_memory_arena_types_8h_source.html#l00072)

[AkMemoryMgrArena\_Media](_ak_memory_mgr_module_8h_a166fce11fcaf8c6c3ccaf6f00182dc4c.html#a166fce11fcaf8c6c3ccaf6f00182dc4caf034292470314618cda8b900728cf644)

@ AkMemoryMgrArena\_Media

**Definition:** [AkMemoryMgrModule.h:132](_ak_memory_mgr_module_8h_source.html#l00132)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AKPLATFORM::AllocSpan](namespace_a_k_p_l_a_t_f_o_r_m_a8607b18eaea4aa3fdfa581caee18970a.html#a8607b18eaea4aa3fdfa581caee18970a)

AkForceInline void \* AllocSpan(size\_t size, size\_t \*out\_userData)

**Definition:** [AkMemoryMgrFuncs.h:37](_platforms_2_windows_2_ak_memory_mgr_funcs_8h_source.html#l00037)

[AK::MemoryArena::AkMemoryArenaSettings::uSbaInitSize](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a38a3458e0df1124c2fe1adce95a65da5.html#a38a3458e0df1124c2fe1adce95a65da5)

AkUInt32 uSbaInitSize

**Definition:** [AkMemoryArenaTypes.h:63](_ak_memory_arena_types_8h_source.html#l00063)

[AK::MemoryArena::AkMemoryArenaSettings::fnMemFreeSpan](struct_a_k_1_1_memory_arena_1_1_ak_memory_arena_settings_a5bbf92ce6096b998829fa7622489db95.html#a5bbf92ce6096b998829fa7622489db95)

AkFreeSpan fnMemFreeSpan

**Definition:** [AkMemoryArenaTypes.h:80](_ak_memory_arena_types_8h_source.html#l00080)