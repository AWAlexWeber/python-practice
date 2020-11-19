'''
1169. Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''

from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        trans_list = [[x for x in trans.split(",")] for trans in transactions]
        transactions_by_name = defaultdict(list)
        for x in trans_list:
            transactions_by_name[x[0]].append(x[1:])
        res = []
        for name, values_list in transactions_by_name.items():
            for values in values_list:
                time, amount, city = values
                if int(amount) > 1000:
                    res.append(','.join([name, time, amount, city]))
                else:
                    for other_values in values_list:
                        otime, _, ocity = other_values
                        if ocity != city and abs(int(time) - int(otime)) <= 60:
                            res.append(','.join([name, time, amount, city]))
                            break
        return res