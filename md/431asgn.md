# asgn2

NOTE: Approx 900 words to the page (depending on section spacing, and accounting somewhat for references/etc.) Expect to write approx. 3600 words, unless some fancy formatting is included

NOTE 2: May be beneficial for andrew to title subsubsections... "paper goals/research q;paper discussion;contributions to the field"

## Abstract

- ~ 1-200 words summarising the introduction, and the contents of the paper
    - The importance and challenges of oral history archives
    - Ways in which to search through them
    - Methods of increasing recall (related to video archives, and generally)
        - re-ranking vs. document expansion via queries, why this can be useful
        - something cliche on how neural networks can be useful
    - This paper discusses...
        - Including xyz research
    - We then propose experiments (such as?) to [investigate abc], and determine def.

## Introduction

- Brief overview on the importance of serving informational needs
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

- What research questions did they set out
    - reiterate the video archive thing
        - importance of oral archives; maybe also address why one can't just use text archive versions (retaining integrity? Rather than relying on 100% accuracy of STT)
            - *don't* take a defensive stance lol

The first paper [being covered] sets out to develop a framework for information retrieval in video archives. More specifically, they aim to [solve the problem of/where] trawling through large amounts of video footage in order to find the answer to a specific query, by implementing an *Asking Questions* framework. [Overview on what this is; document expansion]. [This comes in two parts ]- Automatic Speech Recognition (ASR), and the Asking Questions framework itself. 

[Brief description of ASR and how they did it, what its based on. NOTE this is not the main focus of this assignment; however it's necessary for context as the AQ model is dependent on accurate STT technology to generate relevant data].

[Asking Questions Framework - what is an AQ framework? Why good? compare to QA framworks]. [A - AQ model; what this is built on, what they tested]. However, as mentioned in [[2]-(see section?),], such models are known to produce hallucinations. To help preserve the relevancy of generated questions, [authors] also implemented a Semantic Continuity (SC) model. This was achieved by building upon the [NN? thing] Sentence-BERT, with a training objective of [xyz]. [Brief overview on how training works?]. [In a nutshell, works by taking a context-question pair and calculating a distance. Based on (insert calculation). Lower distance = more relevant. Can then filter based on this value + a probability score].[They built 3 SC models, based on (training datasets go here)]. [How these SC models fit into the framework; evaluating relevance of questions in context? Pairs compared with a "ground truth" question to determine the effectiveness of the AQ models]. 

[How they evaluated]. [SC by using "reference" and N-1 (N being?) irrelevant questions; determine accuracy based on if the ref question has the lowest distance compared to irrelevant qs]. [AQ then tested based on SC filters]. [Results]

Overall, this paper contributed to the field by [demonstrating xyz; synthesizing THINGS and applying stuff to oral archives]. [Providing questions w/ associated timestamps while preserving the context of the original video (since not reliant on transcript?)]. [Musings on where this stuff may also apply]. [Maybe quickly note some shortcomings (foreshadowing lol)].

## Paper 2

Generating Clarifying Questions for Information Retrieval
- Basic overview; What their research questions were
	- How it relates to paper 1
		- Same context of document expansion; also generating questions (though the context is for general search, not limited to audio)
			- This is an alternative (or possibly... supplement?) To "list diversification" (which is the process of getting multiple contexts into top results (to hopefully better solve information needs w/in the first page because solves for multiple contexts))
		- Also expands on it bc has a user study to show the effectiveness of this method [NOTE: probably move this to the "research contributions" subsection]
- What they did; how they did it (and what their research was built on)
- Contributions to the field

## Paper 3

- doc2query--
(could also do doc2query--, which paper A is built on)

[Relatedness - d2q-- was a major inspiration for the archive tool thing.]
- what research questions did this paper have
    - NN-based *document* (not query) expansion?
        - note this is fairly early; pre-that ai boom c. 2021
    - as an alternative to reranking
        - reasonable? tradeoff of spd vs performance
- how this relates to paper A
    - it's the model that paper A is built on; adapted for video archive
        - why good for video?
- what was done
    - what tool did they build, what technologies were used to develop it
- contribution to the field
- shortcomings ()

## Future Research

Possibly a brief couple of sentences on general areas of interest

### Experiment 1

- what this experiment is investigating
    - scalability/generalisation to other datasets?
    - A: does the trained model work with video archives on other topics (eg?), [since the model is trained on a general podcast thing?]
        - if not, do other training datasets work well? Can we alter how we fine-tune?
    - (also potentially a user study to see whether this is practical;)
        - so could test both trained models for paper A on different datasets
- how one would go about investigating
    - based on filtering with the SC model? Is the SC model generalisable? [READ UP ON THIS]
    - would need to test on other document collections
        - possibly give one or 2 examples if possible
    - using manual judgement on a subset would be nice. We're using AI to test other AI; having a good control would be useful
        - if time-intensive to do; we're assuming unlimited budget and manpower here ;)
- what sort of results would be expected from this research

### Experiment 2

- what this experiment is investigating
    - POSSIBLY: look into the SC model's effectiveness
        - see if SC can be tweaked to get improved response. So basically we are either reducing garbage at one end, or the other
    - ALSO POSSIBLY: option B
- how one would go about investigating
- what sort of results would be expected from this research

## Conclusions

- Conclusions about the papers + the field.
- Identification of gaps in the field
- Briefly, the proposed experiments

