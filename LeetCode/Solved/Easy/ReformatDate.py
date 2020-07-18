'''
1507. Reformat Date

Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
 

Example 1:

Input: date = "20th Oct 2052"
Output: "2052-10-20"
Example 2:

Input: date = "6th Jun 1933"
Output: "1933-06-06"
Example 3:

Input: date = "26th May 1960"
Output: "1960-05-26"

'''
class Solution:
    def reformatDate(self, date: str) -> str:
        # Splitting into subsets we can work with
        s = date.split(' ')
        output = ""
        output += s[2] + "-"

        mnth = {}
        mnth["Jan"] = "01"
        mnth["Feb"] = "02"
        mnth["Mar"] = "03"
        mnth["Apr"] = "04"
        mnth["May"] = "05"
        mnth["Jun"] = "06"
        mnth["Jul"] = "07"
        mnth["Aug"] = "08"
        mnth["Sep"] = "09"
        mnth["Oct"] = "10"
        mnth["Nov"] = "11"
        mnth["Dec"] = "12"
        
        output += mnth[s[1]] + "-"
        
        d1 = s[0][0:1]
        d2 = s[0][0:2]
        
        if d2.isdigit():
            return output + d2
        else:
            return output + "0" + d1