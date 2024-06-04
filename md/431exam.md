
| Question | Description                                    | Confidence |
| -------- | ---------------------------------------------- | ---------- |
| 1        | _Ranking functions_                            | 9          |
| 2        | ~~How worth is compression~~                   | 5          |
| 3        | Semi-structured indexing techniques, Precisoon | 7          |
| 4        | *Bias and precision*                           | 7          |
| 5        | Distributed Information Retrieval              | 6          |
| 6        | _TaaT/DaaT/SaaT, opinion question_             | 8          |

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

[ In case of general search engine like asgn 1, I would do x (specific implementation of x?), because of y]. [However this depends on use-case, algorithm A would be better in cases such as C because of reason R]. However, this probably depend on use-case. For example, in a case where users tend to input long queries with many terms, [use xyz].

## Question 1

#### A: [10] Describe and compare the following ranking functions used in information retrieval: TF-IDF, and BM25. In your comparison, consider factors such as: How documents are represented, how queries are represented, how relevance is calculated, and how they improve search result ranking.

- Both TF-IDF and BM25 are search functions used in ranking. As an overview, TF-IDF works by [x], whilst BM25 works by [y].
- [How docs are represented; i.e. what params are used? What addtl stuff we may need for the index?] Both of these functions require additional values to be stored in the index, assuming values are calculated at search time. TF-IDF requires term frequency and document frequency (or the inverse, if you're partially pre-calculating). BM25 requires both of these, with the addition of document length - as such, the index size will be slightly larger for BM25 when compared to TF-IDF.
- The way TF-IDF calculates relevance is relatively simple - [calc here]; i.e. the relevance for a given term in a document is taken as the frequency of that term, multiplied by the inverse frequency of that term over the entire collection. Comparatively, BM25 is more complex; [explanation/etc. what it does or picture of the damn thing]. It also contains several constants - [k1 k3 and b; representative of xy and z respectively; b being 'falloff' i.e. it devalues subsequent occurrences of a term (they will contribute less to the score until infinitesimal difference)]. These can be tuned to work better on different collections.
- TF-IDF improves upon basic term frequency weighting since it handles the issue of words that are frequent throughout the collection; words that are ubiquitous like "the", "and", etc. will have low relevance scores and as such won't influence ranking. Unfortunately there are still issues with this function for several reasons - one being that it doesn't take the 'context' of the query into account (i.e. whether documents are 'similar' to the query, taking context into account). BM25 in turn takes TF-IDF and combines it with features taken from vector space models; it improves upon search results from TF-IDF by [adding a representation of]. This means it's (theoretically) more likely to produce results similar to the query - though at the cost of a larger index size or being more computationally complex at index time, if rsv values are precalculated).

## Question 4

#### A: [4] what is the influence of a biased search engine on precision and recall?

[How a search engine may be biased]. [Influence of this on precision]. [Influence of this on recall]
Bias?
- Confirmation bias;
	- i.e. results being dependent on wording of queries; "benefits of x"; "is x good?" vs "is x bad?"; results may contain misinformation which could be either deliberate, or, more frequently nowadays, hallucinated. 
	- Recall may be affected if [certain things with low RSV, get culled from results list]
	- Precision may be negatively affected if irrelevant results are promoted in search results.

#### B: [6] Define and Describe Precision, Recall, and Mean Average Precision. Given a search engine that implements BM25, describe 3 techniques you might use to increase Mean Average Precision.

In information retrieval, Precision, Recall, and Mean Average Precision (MAP) are all metrics used to evaluate relevance functions. Precision can be described as the proportion of relevant documents in a set of results for a given query. Recall on the other hand can be described as the proportion of relevant documents found out of all relevant documents in a collection. MAP involves measuring the average precision of a search function across a set of queries, to get a more holistic estimate of how a function may be performing.

Three techniques that could be used to improve MAP for a search engine implementing BM25 are:
1. Tuning of BM25 parameters - in particular, [k1 and b] can be altered to work better for a given collection. 'Ideal' values for these parameters could be determined using e.g. a grid walk, to test a number of values.
2. a
3. b

## Question ...3?