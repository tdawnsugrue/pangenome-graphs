# Overleaf can suck my dick

NOTE: Approx 900 words to the page (depending on section spacing, and accounting somewhat for references/etc.) Expect to write approx. 3600 words, unless some fancy formatting is included

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
        - harder to summarise; harder to parse unlike text-based
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
- An overview of what they did
    - big-picture
        - developed an asking questions model
            - based on [extant tools go here]
            - what it does, how it does it
        - Whittled down questions using a semantic continuity model
            - based on d2q-- (cite); whose purpose is [1 sentence].
            - SC model determines what to keep from the AQ model (d2q-style stuff tends to hallucinate [cite]); Aims to keep questions relevant
    - how they did it (broadly what technologies; add in math explanation if need to pad) [see above]
- Their contribution to the field
    - made a thing to more easily search video archives by providing 'questions' and timestamps where subject of q is a'd
- briefly, some shortcomings
    - anything addressed in future research section

## Paper 2

Generating Clarifying Questions for Information Retrieval
- ababa

## Paper 3

- doc2query
(could also do doc2query--, which paper A is built on)
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

