<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">

	<xsl:output method="text" encoding="UTF-8" indent="yes"/>	

	<xsl:template match="/">

<!-- Must be manually set to relevant folder of inputs -->

		<xsl:for-each select="collection(concat('XMLS/', '?select=*.xml;recurse=yes'))">
			<xsl:for-each select="BL_newspaper">

<!-- Will sort output texts into directories by decade and sub directories by year -->

				<xsl:result-document method="text" href="Texts/{substring(BL_page/issue_metadata/normalisedDate,1,3)}0s/{substring(BL_page/issue_metadata/normalisedDate,1,4)}/{substring(BL_page/issue_metadata/normalisedDate,6,2)}/{BL_page/issue_metadata/normalisedDate}_{replace(BL_page/title_metadata/title,' ','')}_{BL_page/pageImage/pageSequence}.txt">

<!-- Create a plain-text file of the transcription, adding a space between words -->

					<xsl:for-each select="BL_page">
						<xsl:for-each select="pageText/pageWord"><xsl:value-of select="concat(.,' ')"/></xsl:for-each>
					</xsl:for-each>
					
<!-- Close output file -->
					
				</xsl:result-document>
				
<!-- Close input file -->
				
			</xsl:for-each>
		</xsl:for-each>

	</xsl:template>
	
</xsl:stylesheet>