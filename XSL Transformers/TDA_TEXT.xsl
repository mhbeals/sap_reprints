<?xml version="1.0" encoding="UTF-8"?>
<xsl:output method="text" encoding="UTF-8" indent="yes"/>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">

	<xsl:template match="/">

<!-- Must be manually set to relevant folder of inputs -->

		<xsl:variable name="number"><xsl:number/></xsl:variable>
			<xsl:for-each select="collection(concat('TDA/1800s/', '?select=*.xml;recurse=no'))">
				<xsl:for-each select="issue">
					<xsl:for-each select="page">

<!-- Will sort output texts into directories by decade and sub directories by year -->

						<xsl:result-document method="text" href="TimesTexts/{substring(../metadatainfo/da/searchableDateStart,1,3)}0s/{substring(../metadatainfo/da/searchableDateStart,1,4)}/{substring(../metadatainfo/da/searchableDateStart,5,2)}/{substring(../metadatainfo/da/searchableDateStart,1,4)}.{substring(../metadatainfo/da/searchableDateStart,5,2)}.{substring(../metadatainfo/da/searchableDateStart,7,2)}_Times_0{substring(pageid,17,3)}.txt">

<!-- Create a plain-text file of the transcription, adding a space between words -->
						
							<xsl:for-each select="article">
								<xsl:for-each select="text">
									<xsl:for-each select="text.cr">
										<xsl:for-each select="p">
											<xsl:for-each select="wd">
												<xsl:value-of select="concat(.,' ')"/></xsl:for-each>
										</xsl:for-each>
									</xsl:for-each>
								</xsl:for-each>
							</xsl:for-each>				

<!-- Close output file -->
							
						</xsl:result-document>

<!-- Close input file -->
						
					</xsl:for-each>
				</xsl:for-each>
			</xsl:for-each>
			
		</xsl:template>

</xsl:stylesheet>
	



