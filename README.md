# Scissors and Paste Database
## A Map of Reprinting and Reuse in the Anglophone Newspaper Press v.1.1.0

Version 1.1.0 currently maps reprinting and re-use in the following collections:

1. British Library 19th Century Newspapers, Part 1 (JISC)
2. Times Digital Archive (GALE CENGAGE)

Forthcoming collectons:

1. London Gazette
2. British Library 19th Century Newspapers, Part 2 (JISC)
3. Trove (National Library of Australia)
4. Papers Past (New Zealand)
5. Welsh Newspapers Online (National Library of Wales)

It was created using the [Scissors and Paste Console v.0.2.0](https://github.com/mhbeals/sap_console)

## Citation

Bibliometric data is time consuming to produce but benefits us all. Please remember to cite or acknowledge this and any other bibliometric data you use in your research. All data is hereby released CC-BY 4.0.

Beals. M. H. *Scissors and Paste Database: A Map of Reprinting and Reuse in the Anglophone Newspaper Press v.1.0.1*. 2 June 2017. Available at https://github.com/mhbeals/sap_reprints/.

## File Structure

### Inputs

#### Word Count Tables

The WCTables directory contains manifests of the word counts of each page and issue of the corpus. Each manifest contains a list with four entries

1. The page of the corpus
2. The word count of the page, as calculated using the OCR transcription
3. The issue that page belongs to
4. The word count of the issue, as calculated using the OCR transcription

These are used as part of the SAP Console in order to calculate the coverage of reused material on any given page or issue in the corpus. 

#### Raw Matching Reports

The RawMatchingReports directory contains manifests of reprints from the corpus. Each manifest contains a list of matches from a single year. The year relates the *source* or *earlier* text; the *target* or *later* text will be within 8 months. Manual testing suggested that matches more than 8 months apart were almost consistently always false positives, with some miscellany or advertising material. As the aim of this project is to identify reprinted news or time-sensitive material matches over 18 months have not been included. If you wish to replicate the matching procedure, or obtain matches over 8 months, the steps required to re-run the matching exercises are included below.

Each line represents two pages from the collection that contain a substantial amount of similar text. They were identified using Lou Bloomfield's [Copyfind](http://plagiarism.bloomfieldmedia.com/wordpress/software/copyfind/) plagiarism detection software using the following procedure:

1. Transform original page-level XML data from British Library into plaintext files using BL_TEXT.xsl
1. Transform original page-level XML data from Times Digital Archive into plaintext files using TDA_TEXT.xsl
2. Run plaintext files through Copyfind in overlapping eight-month sets using custom script files


#### Normalised Titles

Contains a list of XML-derived titles and Normalised titles. Used as part of the SAP Console in order to normalise results across multiple years and collections. There are two versions, one with underscores and hyphens (NormalisedTitles.tsv) and one without (NormalisedTitlesns.tsv).

### Outputs

#### Memes

The Memes directory contains manifests of text that appeared in multiple locations within the corpus. Each manifest contains a list of matches from a single month. The year relates the *earlier* text; *later* text will be within 21 days. Manual testing suggested that matches more than 21 days apart were almost consistently false positives, miscellany or advertising material. As the aim of this project is to identify reprinted news or time-sensitive material matches over 21 days have not been included. 

Testing also suggests that, with rare excepting, matches within the same periodical was consistently a false positive or advertising material. Therefore, matches from within the same periodical have not been included. 

Finally, as the titles tested do not consistently represent morning or evening editions, matches which have the same date of publication have not been included. Other "impossible" date combinations (such as reprinting in London and Aberdeen one day apart) have **not** been excluded at this stage.

The steps described above can be summarised as filtering out any matches that were

1. In the same title
2. Published on the same day
3. More than 200 days apart

The SAP Console also filtered out entries in which **none** of the following were true

4. The Overall Match was at least 160 Characters
5. The Left match was at least 90 Characters
6. The Right Match was at least 90 Characters

This reduced the likelihood of false positives based on small matches, but was more precise than the original Copyfind options allowed.

#### Directed Links

The DirectedLinks directory contains manifests of direct reprinting relationships within the corpus. Each manifest contains a list of matches from a single year. The year relates the *source* or *earlier* text; the *target* or *later* text will be within 21 days. 

Each line represents two pages from the collection that likely have a direct ancestor-descendent relationship. Although intermediary nodes likely exist, both listed pages are likely  on the same branch of the evolutionary tree. 

Matches were identified using the Reprint Mapper, now folded into the SAP Console, and derived from the filtered list, described in Memes.  For each *target*, the Mapper found the *source* with the highest Ovearll Match for each given *target*. If more than one source had the same Ovearll Match score, the earliest source was chosen.

**Provisos**

The SAP Console can only find the best match *within* the corpus. If two descedents of a source are present, but not their common ancestor, it will link the later to the earlier version, even if these actually represent two different branches. This false positive must be excluded manually by any historian using the Directed Links manifest, using contextual knowledge.

#### Evolutionary Dead Ends

Lists those pages that contain reused material, but which are not likely to have been the source for later instances; in other words, those not listed as a source in Directed Links.

#### Reuse Percentages

The following directories contain information about the absolute number of words or the relative percentage of words of reused material found in each page and issue of the corpus.  Using the full word count of each page (WCTables) and the highest words matched (RawMatchingReports) for each page, the SAP console created a series of manifest suggesting the level of reprinting and reuse in a given page or issue. Each directory contains a manifest of errors, or those pages deemed invalid owing to a negative or excessive (>100%) percentage being returned.

#### Issue Percentage

Contains monthly manifests of all issues that contain some duplicated or reused material and the minimum percentage of that issue that has been identified as originally appearing elsewhere.

#### Page Percentages

Contains monthly manifests of all pages that contain some duplicated or reused material and the minimum percentage of that issue that has been identified as originally appearing elsewhere.

#### Titles

Contains monthly manifests of all pages and issues that contain some duplicated or reused material and the minimum percentage of that issue that has been identified as originally appearing elsewhere. These are filtered by individual title.

#### Word Counts

Contains monthly manifests of all pages that contain some duplicated or reused material and the word count of the largest instance of reused material found of that issue that has been identified as originally appearing elsewhere. That is, if four matches were found (Memes), the highest score is deemed the minimum level of reuse identified.

### XML Datasets

In order to facilitate online usage, the data here has been converted into XML files, linking each page to its predecessors, contemporaries and successors. These can be downloaded here or viewed at the [Scissors and Paste website](http://scissorsandpaste.net/scissors-and-paste-o-meter/).
