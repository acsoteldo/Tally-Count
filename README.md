# Tally Count

### hw

Write a Python function tally(v) to count the votes in a simple first-past-the-post
election and to report the outcome.

The function takes a single parameter ‘v’ that represents a list of the votes cast, each
vote being indicated by the candidate’s name. For example, the first three votes below
are for Anne, Bob and Clare, respectively

["Anne", "Bob", "Clare", "Dan", "Anne", "Bob", "Anne", "Clare",
"Anne", "Clare", "Bob", "Clare", "Anne", "Bob"]


We assume that candidates’ names are distinct.

The function should print the candidates’ names in alphabetical order and give the total
number of votes received by each.

The function should also print the name of the candidate who received the greatest
number of votes. In the event of a tie, one of the candidates with the greatest number of
votes should be chosen at random and deemed the winner. You may import the random
package for this question.



if v is ["Anne", "Bob", "Clare", "Dan", "Anne", "Bob", "Anne", "Clare", "Anne", "Clare", "Bob", "Clare", "Anne", "Bob"], the function will output the following:

```
Anne: 4
Bob: 4
Clare: 5
Winner: Clare
```
