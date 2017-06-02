#  Copyfind Script Creator v.0.0.4
#  M. H. Beals (2016) CopyfindScriptCreator v.0.0.4 [Software]
#  Available at https:# github.com/mhbeals/BL19thC_Reprints/tree/master/Scripts%20for%20Copyfind

#  MIT License

#  Copyright(c) 2016 M. H. Beals

#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files(the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions :

#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

start_year = 1800
end_year = 1899
counter = 1
end = 12
countery = 0
year = 0

# While we are before the final year
while year < end_year:
    
    # Set to new year
    year = start_year + countery
    
    # While we are within a single year
    while  counter <= end:
              
        # Start file text
        string = "Documents,50000\n"
        
        # Setting month attributes
        
        month1 = counter
        month2 = counter + 1
        month3 = counter + 2
        month4 = counter + 3
        month5 = counter + 4
        month6 = counter + 5
        month7 = counter + 6
        month8 = counter + 7
        
        month1 = "0" + str(month1)
                
        # Add report folder
        string += "ReportFolder,I:\\bl_ddata\\reports\\"
        string += str(year)
        string += "\\"
        string += (str(month1)[-2:])
        string += "\n"
            
        # Document folder 1
        string += "Document,1,I:\\BL_TXTS\\18"
        string += str(year)[2:3]
        string += "0s\\"
        string += str(year)
        string += "\\"
        string += (str(month1)[-2:])
        string += "\n"
        
        # Document folder 2
        if month2 <=12:
            month2 = "0" + str(month2)
            string += "Document,2,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month2[-2:]
            string += "\n"
        else:
            month2 = "0" + str(month2-12)
            newyear = year+1
            string += "Document,2,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month2[-2:]
            string += "\n"
            
        # Document folder 3
        if month3 <=12:
            month3 = "0" + str(month3)
            string += "Document,3,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month3[-2:]
            string += "\n"
        else:
            month3 = "0" + str(month3-12)
            newyear = year+1
            string += "Document,3,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month3[-2:]
            string += "\n"

        # Document folder 4
        if month4 <=12:
            month4 = "0" + str(month4)
            string += "Document,4,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month4[-2:]
            string += "\n"
        else:
            month4 = "0" + str(month4-12)
            newyear = year+1
            string += "Document,4,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month4[-2:]
            string += "\n"
            
        # Document folder 5
        if month5 <=12:
            month5 = "0" + str(month5)
            string += "Document,5,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month5[-2:]
            string += "\n"
        else:
            month5 = "0" + str(month5-12)
            newyear = year+1
            string += "Document,5,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month5[-2:]
            string += "\n"

        # Document folder 6
        if month6 <=12:
            month6 = "0" + str(month6)
            string += "Document,6,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month6[-2:]
            string += "\n"
        else:
            month6 = "0" + str(month6-12)
            newyear = year+1
            string += "Document,6,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month6[-2:]
            string += "\n"
            
        # Document folder 7
        if month7 <=12:
            month7 = "0" + str(month7)
            string += "Document,7,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month7[-2:]
            string += "\n"
        else:
            month7 = "0" + str(month7-12)
            newyear = year+1
            string += "Document,7,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month7[-2:]
            string += "\n"

        # Document folder 8
        if month8 <=12:
            month8 = "0" + str(month8)
            string += "Document,8,I:\\BL_TXTS\\18"
            string += str(year)[2:3]
            string += "0s\\"
            string += str(year)
            string += "\\"
            string += month8[-2:]
            string += "\n"
        else:
            month8 = "0" + str(month8-12)
            newyear = year+1
            string += "Document,8,I:\\BL_TXTS\\18"
            string += str(newyear)[2:3]
            string += "0s\\"
            string += str(newyear)
            string += "\\"
            string += month8[-2:]
            string += "\n"
                    
        # Scripting Attributes
        string += "PhraseLength,10,,\n"
        string += "WordThreshold,200,\n"
        string += "SkipLength,20,,\n"
        string += "MismatchTolerance,5,\n"
        string += "MismatchPercentage,50,\n"
        string += "BriefReport,0,,\n"
        string += "IgnoreCase,1,,\n"
        string += "IgnoreNumbers,1,,\n"
        string += "IgnoreOuterPunctuation,1,\n"
        string += "IgnorePunctuation,1,\n"
        string += "SkipLongWords,0,,\n"
        string += "SkipNonwords,0,,\n"
        string += "Locale,English,,\n"
        string += "PrepareForComparisons,\n"
        
        # Comparison List
        string += "Compare,1,1\n"
        string += "Compare,1,2\n"
        string += "Compare,1,3\n"
        string += "Compare,1,4\n"
        string += "Compare,1,5\n"
        string += "Compare,1,6\n"
        string += "Compare,1,7\n"
        string += "Compare,1,8\n"
        string += "Done,\n"
        
        # Write script file
        filename = "script_" + str(year) + "_" + str(month1[-2:]) + ".txt"
        filename.encode('cp1252')
        text_file = open(filename, "w")
        text_file.write(string)
        text_file.close()
        
        # Move onto next month counter
        counter += 1
        
        # Continue month loop
        
    # Reset month counter  
    counter = 1
    
    # Update year counter
    countery += 1
    
    # Continue year loop 
