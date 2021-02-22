'''
An online shopping website contains one to many items on each page. To mimic the logic of the website, a programmer has a list of items and each item has its name, relevance, and price. After sorting the items by (name: 0, relevance: 1, price: 2), the programmer is trying to find out a list of items displayed in a chosen page. Given a list of items, the sort column, the sort order (0: ascending, 1: descending), the number of items to be displayed in each page, and a page number,

write an algorithm to determine the list of item names in the specified page while respecting the item's order (Page number starts at 0).

Input
The input consists of three arguments:

sortParameter: an integer representing the value used for sorting (0 for the name, 1 for relevance, 2 for price)

sortOrder: an integer representing the order of sorting (0 for ascending order and 1 descending order)

itemsPerPage: an integer representing the number of items per page

pageNumber: an integer representing the page number

numOfItems: an integer representing the number of items

items: a map of string as key representing the name and pair of integers as values representing the relevance, price

Output
Return a list of strings representing the item names on the requested page in the order they are displayed.

Constraints
1 <= numOfItems < 10^5

0 <= relevance, price < 10^8

0 <= pageNumber < 10

Note
itemsPerPage is always greater than 0, and is always less than the minimum of numOfItems and 20.

Examples
Example 1:
Input:
sortParameter = 1

sortOrder = 0

itemsPerPage = 2

pageNumber = 1

numOfItems = 3

items = [["item1", 10, 15], ["item2", 3, 4]. ["item3", 17, 8]]

Output: ["item3"]
Explanation:
There are 3 items.

Sort them by relevance(sortParameter = 1) in ascending order items = [["item2", 3, 4], ["item1", 10, 15], ["item3", 17, 8]].

Display up to 2 items on each page.

The page 0 contains 2 item names ["item2", "item1"] and page 1 contains only 1 item name ["item3"].

So, the output is "item3".
'''

class Solution():
    def fetchItemsToDisplay(self, sortParam: int, sortOrder: int, itemsPerPage: int, pageNumber: int, items):
        # What we are going to do is first just sort everything, then we are going to skip (itemsPerPage)*(pageNumber-1) items
        # O(nlogn) time complexity ( from sorting ), and O(n) space complexity (again from sorting).
        s = sorted(items, reverse=(True if sortOrder else False), key=lambda t: t[sortParam])
        return s[(itemsPerPage)*(pageNumber):(itemsPerPage)*(pageNumber + 1)]

s = Solution()
itemsToDisplay = s.fetchItemsToDisplay(1,0,2,0, [["item1", 10, 15], ["item2", 3, 4], ["item3", 17, 8]])
print(itemsToDisplay)