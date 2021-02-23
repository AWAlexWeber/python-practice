'''
A Company parses logs of online store user transactions/activity to flag fraudulent activity.

The log file is represented as an Array of arrays. The arrays consist of the following data:

<userid1> <userid2> <# of transactions>

For example:

345366 89921 45

Note: the data is space delimited

So, the log data would look like:

 345366 89921 45
 029323 38239 23
 ...
Write a function to parse the log data to find distinct users that meet or cross a certain threshold.

The function will take in 2 inputs:
logData: Log data in form an array of arrays

threshold: threshold as an integer

Output:
It should be an array of userids that are sorted.

If same userid appears in the transaction as userid1 and userid2, it should count as one occurrence, not two.

Example:
Input:
logData:

345366 89921 45
029323 38239 23
38239 345366 15
029323 38239 77
345366 38239 23
029323 345366 13
38239 38239 23
...
threshold: 3

Output: [029323, 345366, 38239]
Explanation:
Given the following counts of userids, there are only 3 userids that meet or exceed the threshold of 3.

345366: 4 times , 38239: 5 times, 029323: 3 times, 89921: 1 time
'''

from collections import defaultdict
from typing import List

class Solution():
    def transactionLogs(self, log_data: List[str], threshold: int) -> List[str]:
        d = defaultdict(lambda: 0)
        # O(n) space, O(n) time where n is size of log_data
        for log in log_data:
            user1, user2, num = (log.split(' '))
            if user1 == user2:
                d[user1] += 1
            else:
                d[user1] += 1
                d[user2] += 1

        output = list()
        # O(n) time/space
        for k in d.keys():
            if d[k] >= threshold:
                output.append(k)

        return sorted(output)