# GekiChuMai × PMS — Beginner / Normal

**[Open or import this table](https://sehun-joo.github.io/gekichumai-pms-beginner/)**

229 PMS charts across 100 songs appearing in maimai, CHUNITHM or ONGEKI. Includes 30 charts at Lv20 or below (including two provisional ratings) and 14 five-button PMS charts. The scope is the normal PMS table's **Lv1–45 and 45+**, matching the [Pump collection](https://sehun-joo.github.io/pump-pms-normal/). The upper levels are challenging; use the Lv1–20 browser filter to start.

Add the public page URL to your player's difficulty-table settings. Browser filters do not change imports: the player receives all 229 charts. Only metadata is hosted; obtain playable files using the credited package and chart links. External downloads have not all been tested.

## Sources and matching

Checked **2026-10-12**. All categories were considered, not only Variety:

- [maimai Japanese official data](https://maimai.sega.jp/data/maimai_songs.json): 1,602 records.
- [CHUNITHM Japanese official data](https://chunithm.sega.jp/storage/json/music.json): 1,759 records.
- [ONGEKI Japanese official data](https://ongeki.sega.jp/assets/json/music/music.json): 1,109 records.
- [PMS Database normal records](https://pmsdatabase.github.io/pmsdatabase/pmsdatabase_score.json): 7,291 charts.
- Discovery cross-checks: [Japanese BMSまとめ crossover list](https://w.atwiki.jp/laser_bm/pages/86.html), [Japanese ONGEKI BMS download list](https://aki-memo.net/2023/04/16/bms-songs-list-added-to-ongeki/), [CHUNITHM Touhou list](https://wikiwiki.jp/chunithmwiki/ジャンル別楽曲一覧/東方Project), and individual Japanese wiki pages linked in the catalog.
- [OTOGE DB](https://github.com/zvuc/otoge-db) deleted-song archives were also compared (53 maimai, 161 CHUNITHM, 109 ONGEKI records). No additional verified normal-PMS matches resulted; matches such as Realize were different artists/songs.

`game-catalog.json` retains deduplicated title, artist, category and source metadata from all three official feeds. `source-normal.json` preserves the full normal PMS snapshot. `catalog.json` records reviewed chart hashes, official game evidence, aliases and version notes. Matching was reviewed by title **and artist**, with additional searches for title variants. Future builds use these reviewed hashes, not unreviewed substring matches.

## Touhou and version differences

The playable set includes **Calamity Fortune (14/35/43), Little "Sister" Bitch (28/40/45), Wizdomiot (29/30/43), and Yakumo >>JOINT STRUGGLE (31)**. Touhou is a separate browser filter. A shared Touhou source melody is not sufficient for inclusion: the arrangement must match, or be the explicitly identified original of a later remake.

**星の器～STAR OF ANDROMEDA**, Imperishable Night 2006, Satori ～3rd EyEs and Armageddon were checked and remain visible in coverage, but have no rated normal chart in the selected snapshot. Star of Andromeda's checked PMS records are insane-table ●8/●9/●12, outside this table. The normal Lv29 **Andromeda by hurirai is unrelated** and is excluded. Coverage is not a claim that easier charts cannot exist elsewhere.

Original BMS versions of later Sega-game remakes are included and explicitly labeled: felys / -final remix-, Flesvelka / La Flesvelka, Yakumo / 2019 Update, Velaciela / Hyper Mix, Akasagarbha / -reincarnate-, and EVERGREEN. Audio is not asserted to be identical. Artist aliases such as Junk / 高嶺愛花 and BACO / フロン were checked. Aeventyr is matched to Äventyr.

Same-title collisions were rejected, including Apollo (xelloscope vs TJ.hangneil), seagull, Colorful, Odin (しらいし vs Gram), METATRON (OptiU vs SHIKI), and 竹 (LU vs 立秋). Different covers/remixes of 魔理沙は大変なものを盗んでいきました, 鳥の詩 and Henceforth were not silently treated as the licensed versions. Unknown `?` difficulty rows and raw old chart-header levels are not used.

The normalized-rating supplements are mopemope Normal Lv22 and Hyper Lv40. Their original records in `supplemental-charts.json` come from the [upstream excluded table](https://pmsdatabase.github.io/excluded_pmsdatabase/excluded_pmsdatabase_score.json), BGA gore category; comments explicitly retain the corrected 20→22 and 39→40 ratings. Cutter also has two explicitly provisional supplements, described below. No excluded charts are automatically included.

## Fresh local-database audit (2026-10-12)

Read-only SQLite queries examined 20,549 PMS records (16,528 unique MD5 hashes), including five-button charts stored in mode 9. All records with a `.pms` extension were checked regardless of database mode; none were outside mode 9. The song-information database supplied density, peak density, long-note and lane counts. Broader title/alias candidates, near-spelling matches, and all 30 hashes absent from the three PMS source tables were reviewed.

This found **Cutter by EmoCosine (ONGEKI)**: **3? / five-button / 88 notes** and **11? / nine-button Easy / 150 notes**. Both local files were MD5-verified. Their BOFXVI headers declare levels 3 and 11; neither has a numeric normalized rating in the excluded source. They are labeled with `?` in the player table, not represented as upstream-normalized levels. Both are 140.937 seconds, constant 160 BPM, with no long notes; database peak densities are 2 and 3 respectively. The source excludes these charts under the BGA-gore category.

Older L9 variants are marked corrected upstream, Pure Ruby variants withdrawn, and old felys variants have no usable normalized ratings. These were not added as fresh beginner ratings. Star of Andromeda remains outside the normal range. Database paths and the full private audit remain local; only public chart metadata and derived verification statistics are committed.

## Rebuild

Python 3, standard library only:

```sh
python build.py --base-url https://sehun-joo.github.io/gekichumai-pms-beginner
```

GitHub Pages deploys `dist` through the included workflow on each main-branch push. Source refreshes and new hash selections are intentional manual changes; builds never silently fetch new songs. Retain source dates and review artist/version identity when updating.

Original PMS titles, levels, hashes, credits, comments and links are preserved for normal-table rows. Supplemental comments explain the source category and rating. No audio, chart files or local library paths are published. This independent fan table is not affiliated with SEGA, Andamiro or the source maintainers. Japanese-series presence does not guarantee availability in each regional/current release. Coverage is limited to the reviewed sources.
