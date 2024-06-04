
| Question | Description                                    | Confidence |
| -------- | ---------------------------------------------- | ---------- |
| 1        | Ranking functions                              | 9          |
| 2        | How worth is compression                       | 5          |
| 3        | Semi-structured indexing techniques, Precisoon | 7          |
| 4        | Bias and precision                             | 7          |
| 5        | Distributed Information Retrieval              | 6          |
| 6        | TaaT/DaaT/SaaT, opinion question               | 8          |

Reformat this in word when it comes to submission
## Question 6

#### A: [1] - Define TaaT, DaaT, and SaaT

All three of these are terms describing ways of processing queries.  
TaaT (Term at a time) processing involves processing the postings lists for a query one term at a time. An array of accumulators is used to store and update the rsv values for each document, and is updated for each postings list processed.
DaaT (Document at a time), on the other hand, is where all postings lists for the terms in a query are processed at the same time. The rsv is calculated for each document, one at a time.
Finally, SaaT (Score at a time) involves loading all postings lists for a query into memory, and then processing lists by decreasing order of *impact* (i.e., which list has the maximum possible influence on the final rsv scores).

#### B: [6] - Give an advantage and disadvantage of each of TaaT, DaaT, and SaaT

One advantage of TaaT is [easy to implement? Don't need to get whole index/postings list into array therefore Accum array is smaller], however [b - possibly something to do with the problems inherent in working with skip lists; if you do a merge then memory access is different and you lose the advantages of a linear search (there are solutions for this)].
A benefit of using DaaT is that [very fast if we can optimise, since its implicitly an AND search we can search based on the shortest list, doing SLS; shortest more skips/can also keep only top-k; no sorting or accumulator needed]. [One possible disadvantage; with specific *implementations of DaaT (WAND, etc)* requires impact to be determined at indexing time - ie there is a tradeoff since potentially larger index size].
SaaT is useful in that it processes the most influential postings first, meaning we can decide to stop after an arbitrary amount of time and still have sufficiently good results for a given query. On the other hand, accumulator initialisation tends to be slow since we need to load the entire postings list into memory (though there are ways around this such as breaking the list into pages).

#### C: [3] If you were to implement a search engine, such as that in your assignment, which approach would you use and why? 

[ In case of general search engine like asgn 1, I would do x (specific implementation of x?), because of y]. [However this depends on use-case, algorithm A would be better in cases such as C because of reason R]. However, this probably depend on use-case. For example, in a case where users tend to input long queries with many terms, 

## Question 1

y