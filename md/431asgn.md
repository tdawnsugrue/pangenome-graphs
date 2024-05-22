# asgn2

NOTE: Approx 900 words to the page (depending on section spacing, and accounting somewhat for references/etc.) Expect to write approx. 3600 words, unless some fancy formatting is included

NOTE 2: May be beneficial for andrew to title subsubsections... "paper goals/research q;paper discussion;contributions to the field"

NOTE 3: *Clarifying* questions useful bc "relevant" questions that were generated serve as the "documents/results" for paper A.
## Abstract

- Document expansion in IR; particularly query generation and its use.

Document expansion is a [thing in IR] that can [help retrieval efficiency] by [eg altering term frequency/etc]. One form of this is query generation, in which [models predict queries for a document based on context, and query log data]. Video archive collections [pose a unique problem for IR in that] - [needs to be transformed via eg ASR - additionally xyz]. In this [report/paper], we [discuss PAPERNAME], which [made a tool to generate questions for videos + relevant timestamps while preserving integrity of original content]. [Additionally/to back this], we also overview [paper b], which [demonstrates utility of *clarifying* questions in search/IR]. [Paper C] also discusses [some shortcomings of seq2seq models eg d2q], [and presents a tool to improve results of such models w/ denoising/semantic filters]. Finally, we outline two experiments to build on the contributions of these [papers], [evaluation into the practical benefits of AQ for video collections], and [extended use case of paper A usability].

## Introduction

- Brief overview on the importance of serving informational needs

Perhaps more important than [serving relevant documents] is [resolving informational needs]. [If doc big, may contain large amounts of irrelevant content that the user is not interested in], [which makes in-document search important in these cases]. Such is the case when searching collections of video footage, as [difficult to accurately skim - may lose context, etc.].

[In paper], [authors addressed this issue; identifying these such challenges]. They also note that [in the case where information is sensitive/context more important, so retaining integrity is consequently important (reword this)]. To address this, they developed [a tool] which [generates questions associated w/ timestamp for context where this question is answered]. This [involves 2 things, ASR and the AQ model]. [The AQ model is based on d2q-- [cite]]

- Specific database type/s
    - challenges that come with video archives
        - harder to su- An overview of what they did
    ​￼- big-picture
        ​￼- developed an asking questions model
            - based on [extant tools go here]
            - what it does, how it does it
        ​￼- Whittled down questions using a semantic continuity model
            - based on d2q-- (cite); whose purpose is [1 sentence].
            - SC model determines what to keep from the AQ model (d2q-style stuff tends to hallucinate [cite]); Aims to keep questions relevant
    - how they did it (broadly what technologies; add in math explanation if need to pad) [see above]
​￼- Their contribution to the field
    - made a thing to more easily search video archives by providing 'questions' and timestamps where subject of q is a'd
​￼- briefly, some shortcomings
    - anything addressed in future research sectionmmarise; harder to parse unlike text-based
- Brief intro on query generation
    - and how it can be used to assist in meeting users info needs
        - link prompting paper
        - and maybe 2012 paper...
- Intro the 3 papers; 1 sentence each.

## Paper 1



The first paper [being covered] sets out to develop a framework for information retrieval in video archives. More specifically, they aim[/their research questions were] to [solve the problem of/where] trawling through large amounts of video footage in order to find the answer to a specific query, by implementing an *Asking Questions* framework. [Overview on what this is; document expansion]. [This comes in two parts ]- Automatic Speech Recognition (ASR), and the Asking Questions framework itself. 

[Brief description of ASR and how they did it, what its based on. NOTE this is not the main focus of this assignment; however it's necessary for context as the AQ model is dependent on accurate STT technology to generate relevant data].

[Asking Questions Framework - what is an AQ framework? Why good? compare to QA framworks]. [A - AQ model; what this is built on, what they tested]. However, as mentioned in [[2]-(see section?),], such models are known to produce hallucinations. To help preserve the relevancy of generated questions, [authors] also implemented a Semantic Continuity (SC) model. This was achieved by building upon the [NN? thing] Sentence-BERT, with a training objective of [xyz]. [Brief overview on how training works?]. [In a nutshell, works by taking a context-question pair and calculating a distance. Based on (insert calculation). Lower distance = more relevant. Can then filter based on this value + a probability score].[They built 3 SC models, based on (training datasets go here)]. [How these SC models fit into the framework; evaluating relevance of questions in context? Pairs compared with a "ground truth" question to determine the effectiveness of the AQ models]. 

[How they evaluated]. [SC by using "reference" and N-1 (N being?) irrelevant questions; determine accuracy based on if the ref question has the lowest distance compared to irrelevant qs]. [AQ then tested based on SC filters]. [Results]

Overall, this paper contributed to the field by [demonstrating xyz; synthesizing THINGS and applying stuff to oral archives]. [Providing questions - shortcomings ()w/ associated timestamps while preserving the context of the original video (since not reliant on transcript?)]. [Musings on where this stuff may also apply]. [Maybe quickly note some shortcomings (foreshadowing lol)].

## Paper 2

Generating Clarifying Questions for Information Retrieval
- Basic overview; What their research questions were
    - Overview:
        - discusses the usefulness of clarifications in information retrieval
            - Main research questions were; investigating the usefulness of asking clarifying questions (done via user studies); and addressing the *challenges* of *generating* questions.
	- How it relates to paper 1
		- Same context of document expansion; also generating questions (though the context is for general search, not limited to audio)
			- This is an alternative (or possibly... supplement?) To "list diversification" (which is the process of getting multiple contexts into top results (to hopefully better solve information needs w/in the first page because solves for multiple contexts))
		- Also expands on it bc has a user study to show the effectiveness of this method [NOTE: probably move this to the "research contributions" subsection]
- What they did; how they did it (and what their research was built on)
    - (briefly intro both, and then jump into below)
    - 2 main points:
        - A: discussed the usefulness of clarification/clarifying questions in general; investigated via several user studies to determine utility.
            - Study 1 determined that users reported appreciating the feature; do want to note this was a *very* small study; only 5 individuals lol... (they did a second one with 24)
            - Study 2 large scale online experiment using Bing; 2m users 1 week; 48.57% increased "engagement" compared with previously found that providing clarifying questions improved ctr significantly; showing that AQ is something worth looking into
        - B: Generated models for query generation
            - rule-based slot-filling algorihm
	            - Based on the realisation/assumption that most questions fit one of 4 templates; implemented a template completion model
				- found this generally produced appropriate questions
            - weakly supervised text generation algorithm
	            - encodes query; with k aspects, (using an arbitrary ) then feeds into a decoder which __generates questions__. 
	            - *weak supervision* in this case is the templatePOSSIBLY: look into the SC model's effectiveness
        - see if SC can be tweaked to get improved response. So basically we are either reducing garbage at one end, or the other
        ​￼- Maybe also speed improvements for the model? Not relevant for archives specifically, but would be useful for open collections
	        - Since filtering models (see d2q-- are often expensive @ indexing time...)
	- ALSO ALSO could see how filtering eg in A & C affects query reformulation? Not sure on this one really... just an idea.
    - ALSO POSSIBLY: option B-completion model discussed above.
	            - Outputs of this are *noisy*. So implements a "Query Clarification Maximisation" model (reward-function-ish) to remove noise e.g. common training questions, etc.
		            - Give a brief? (2-3 sentence) overview of how this works?
	- Requires query reformulation data (lack of this is part of the reason why this corner of IR is not so well studied); in this case they used reformulation data from bing search query logs in a 1.5y period (US market)
	- Their conclusions
		- Showed that this can be useful; still many areas for improvement
			- Looking at the tables provided in this paper; clarifications were evaluated as majority "fair" though ~1/5-1/4 were "good"
- Contributions to the field
    - Another (possibly older?) Question/clarification generation model, based on query reformulation data, which produces satisfactory results
	    - Were able to evaluate w/ human annotation; do user studies to find that this is actually useful.
    - this is particularly useful in contexts where e.g. query is complex, or on an interface where user is working with a small-screen/voice-only interface (i.e., the benefits of list diversification are limited as the user has much less space for a list of results)
    - Have identified areas for further study
	    - Based on the limitations of *this* study

## Paper 3

doc2query--
- what this paper covers
	- 1-2 sentences; building on top of seq2seq models which are used for document expansionwhat tool did they build, what technologies were used to develop it
- what research questions did this paper have
    - Addresses problems with seq2seq models when used for IR
	    - Namely, hallucination and index inflation
		- Seeks to solve this 
	- Shows that filtering via a relevance model results in higher (+ faster) IR efficiency; built on top of doc2query [CITE and possibly briefly discuss what doc2query is]
- how this relates to paper A
    - This is relevant to paper A in that it was one of the major inspirations for that paper [CITE] - in fact, paper A builds on top of this concept
	    - Both with a.) general topic of doc expansion via query generation, and b.) use of a seq2seq model to do it
    - Possibly related to paper B?
	    - Both use seq2seq; both implement some kind of noise reduction strategy.
- what was done
    - Built doc2query--; which (basically) adds a filtering phase to the original doc2query (in turn built on top of T5)
	    - Describe the 2 phases - note same [theoretical] model as [paper A].
		    - Generates questions; not all may be relevant (this is discussed briefly only; ref. og d2q paper citations)hat this experiment is investigating
	- ALT: do a user study on the ￼￼actual￼￼ effectiveness of working with an Asking Questions model - want to see if this improves retrieval effectiveness in a "practical scenario". Paper a builds a nice tool but doesn't really do any quantitative "are user information needs being met" sort of study.
​￼- how one would go about investigating
    ​￼- This could be done by either (or both of) A: annotation study (like B; based on likely queries) where generated questions are ranked as relevant
	    - Based on whether the question is related to the information need of their information query, AND whether the attached timestamp is relevant to both the generated question and info need.
	    - Since multiple models are used, could do separate tests on multiple of these; which would mean you could assess the SC independently (e.g. if you did a separate study of the questions prior to filtering via SC; can compare the two.)
	​￼- If done with a different collection (which is more frequently used; and/or more freely available so we can collect more data), could do a study similar to B to determine whether improves
		- Difficult to do at scale for a number of reasons, since this isn't e.g. internet search CTR may not be particularly useful...
​￼- what sort of results would be expected from this research
	- Option A, we would expect to obtain a dataset reporting on the effectiveness of questions generated and kept by the model used in paper A (rather than "X% of questions were relevant based on our filtering model")
	- Depending on the setup, we could then also identify weak points of the model (i.e. if it has problems, is it failing on a specific type of query?)
		    - Filtering: runs gen'd questions through a relevance filter [INSERT R FN], with arbitrary threshold *t*. Questions w/ threshold < t are discarded as irrelevant
- contribution to the field
	- Showed that seq2seq results (which are shown to be useful) can be improved by implementing a filtering model
		- This increases retrieval effectiveness AND reduces index size relative to unfiltered; both of which are good for [REASONS].
		- Opens the field to further research since seq2seq are used throughout IR atm (see A, B)

## Future Research

Possibly a brief couple of sentences on general areas of interest
- Note some obvious shortcomings of the discussed papers

### Experiment 1

- what this experiment is investigating
	- ALT: do a user study on the *actual* effectiveness of working with an Asking Questions model - want to see if this improves retrieval effectiveness in a "practical scenario". Paper a builds a nice tool but doesn't really do any quantitative "are user information needs being met" sort of study.
- how one would go about investigating
    - This could be done by either (or both of) A: annotation study (like B; based on likely queries) where generated questions are ranked as relevant
	    - Based on whether the question is related to the information need of their information query, AND whether the attached timestamp is relevant to both the generated question and info need.
	    - Since multiple models are used, could do separate tests on multiple of these; which would mean you could assess the SC independently (e.g. if you did a separate study of the questions prior to filtering via SC; can compare the two.)
	- If done with a different collection (which is more frequently used; and/or more freely available so we can collect more data), could do a study similar to B to determine whether improves
		- Difficult to do at scale for a number of reasons, since this isn't e.g. internet search CTR may not be particularly useful...
- what sort of results would be expected from this research
	- Option A, we would expect to obtain a dataset reporting on the effectiveness of questions generated and kept by the model used in paper A (rather than "X% of questions were relevant based on our filtering model")
	- Depending on the setup, we could then also identify weak points of the model (i.e. if it has problems, is it failing on a specific type of query?)

### Experiment 2

- what this experiment is investigating
    - Problem with the collection accessibility; I think? USHMM is open-access (haven't tried) but the other one is limited to a small set of countries/institutions, so possibly not so good for a large-scale study (and also means that results can't be shared easy - problematic for e.g. replication)- Conclusions about the papers + the field.
	- I
    - However this is also an OPPORTUNITY! If we work on another collection, it enables a portion of the previous experiment AND enables us to test how well the model generalises to other collections. (Whether at base, or if we want to do a little bit of tweaking to get it to work...)
- how one would go about investigating
	- Probably want to grab a similar (but different and open-access) collection of video; ideally also with transcriptions already. If not can try to use the ASR that paper A used.
		- Also would need a preexisting search function (i,e. extant audience), this is unfortunately a limitation as not many such collections exist. But in an ideal scenario...
	- Do a study on this; implement the question interface (or even just the document expansion?)
		- How does the AQ model do with generating questions? What portion are kept by the SC model/s? If we incorporate this into the first experiment, do users find a noticable improvmeent
			- Alternatively, not doing the user study means we wouldn't need a collection with preexisting searchability; makes this experiment somewhat easier to do (though more impractical to evaluate on a practical level).
- what sort of results would be expected from this research
	- Would expect to get info on [how well works for a different dataset.] Would then be able to use this as a jumping-off point for further research
		- Tweaks to model? What kind of tweaks would work well? Either to get a generalised model (unlikely) or an idea of what kind of retraining is necessary to adapt the model to different collections.
		- If we can do this on an open-source dataset, means we could get more easily accessible data (that's also relevant to the problem?) Meaning there's more resources available for any researchers wanting to continue research in this field.

## Conclusions

In conclusion, looked at the utility of query generation and question answering as a form of [document expansion/search-timestamping-whatever], and its utility in [improving efficiency of IR]. In particular, [looked at case study where this could be applied as [point highlighting??] for video archives], [a topic made difficult by relative lack of data].

Furthermore, we identified [points of interest for further study] - namely, [summary of experiment sections]. [Overall statement of how many avenues still to be studied in this area]; [these experiments may help pave the way for future work].

