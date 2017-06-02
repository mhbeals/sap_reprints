# Scripts for Copyfind 64.4.1.4

These scripts replicate the reprint indentification undertaken for the *Scissors and Paste Project*. 

## Five-Year-Sets

The years 1800-1830 were originally processed using 5-year increments. However, testing at 1880 suggested that the corpus size had become too large to efficiently process at this resolution.

## One-Month-Sets

The one-month sets differ from the original five-year sets in the following regards:

* The 'originals' being examined are restricted to a single month
* The possible reprints are from the succeeding eight months, continuing into the following year where appropriate

This results in a **smaller* number number of [raw matches](https://github.com/mhbeals/BL19thC_Reprints/tree/master/Raw%20Matching%20Reports). However, as eight months is greater than the 200 days prescribed by the [Reprint Mapper](https://github.com/mhbeals/ReprintMapper), the resulting [formatted matches](https://github.com/mhbeals/BL19thC_Reprints/tree/master/Formatted%20Matching%20Reports) will be the same.

These sets were made using the python script copyfindscriptcreator.py
