
### General Notes
- Due May 6?
- Approx 2k words
- Worth 15% (weighted less for initial submission)
- Shape & scope can be discussed; what to in/exclude, formulation of aims also w/ supervisor. Just not the writing itself

#### Content as per guidelines
- brief lit review
- rationale behind 'plan of action' (note: this may not be as clear-cut as we're working more data-first?)
- Main aims of the project for ~1/2 page at end of introduction
- Consider including figures if/where necessary

---
## Outline 2 (+ Aims)

###  General overview of problem
(in the style of an abstract (sort of) (for now))
- What is a linear ref/ Hg38, why is it so important
	- Single consensus sequence (determined to be representative;)
	- With improvements to sequencing technologies (meaning we can make T2T); can fill in gaps 
		- In particular long-read sequencing; covers SVs/seg duplications/etc.

### Intro the topic
- Enter pangenomes
	- outline what the HPRC set out to do; information about the release (how many, who, selection criteria)
- Possibly include a graph in this section...
- How they differ from a linear reference:
	- graph format, nodes/edges/paths instead of a linear consensus format
	- means we can represent multiple variants more easily; also makes it e.g. easier to grow
	- also means that we can better represent regions with tricky-to-align features
		- e.g. SVs, segmental duplications, etc.
			- why?
- However, such a drastic move between formats means there's a need to adapt or build workflows around this.
	- [keep this point generic for now; expand later]

#### Continuing: more about pangenomes
- Some tools already exist, and have been used in studies already
- Tools for building;
	- Lead-in to the HPRC; what they're doing, where the project's at, where it's going (and the end goal; in summary though...)
- TO GO HERE: some examples of pangenomes (& their tools) being used
	- e.g. utility paper; used pangenomes to identify [variants/insertions] not present in the reference genome.
		- this also highlights how pangenomes support better diversity, since most of this was done on populations currently underrepresented in the current reference.
		- This is also particularly useful for previously difficult variants (e.g. SVs)
			- for example: look at T2T vs. hg38 - identified ~200Mbp of gaps x
	- Non-human worth a mention too possibly
		- tomato pangenome (read this; check book for ref); discovered tons of SVs relevant for propagation/etc/etc. Made possible with the pangenome + long-read sequencing
	- Potentially; pangenomes in GWASs?
		- currently not enough sequencing data (yet)
			- but yes we can (theoretically?practically?) Improve GWAS results for non-european populations; since not reliant on linear reference opens the field for gwas (how? Several papers mention this but *which* ones and *what do they say*)
		- Doing a GWAS beyond the base level would open up to looking @ associations with complex allelles (see tomato pangenome above)
			- Could then better predict e.g. risk burden; therefore beneficial for precision medicine. 
			- Especially useful for underrepresented populations; same/similar variants could have different effects between different populations [ref diversity paper which talks about this]

### Problems

- HOWEVER: eukaryotic pangenomes are a new [field/thing/etc.], so naturally this comes with some issues
	- there are potential issues w/ pangenomes - one is that there's no one way to assess the quality of a pangenome - graphs made with different tools may look completely different, and not be necessarily better or worse than one or the other (cite the review or one of its sources)
		- Field is settling on consistent formats as it matures
	- issues with adoption (see above); even now, people are still using Hg37 (despite the fact that the most recent release was *11 years ago*)
		- there's a high cost to switching; though several good tools already exist, there are still many gaps in terms of software available for analysis on/with pangenomes.
			- this means researchers need to make their own; results in a lot of tools to bridge the gap that may not be reliably maintained (not sure where I'm going with this)
			- (An aside) also may be useful to talk about tools for bridging the gap? But not necessarily relevant
			- New data structure (graphs) means that workflows are completely different - this also means new formats. Some tools/pipelines still rely on linear-based formats. Reduces the advantages to using a pangenome pipeline bc the benefits disappear [WORD THIS BETTER]
	- Overall, lacking in gud pipelines for analysis with pangenomes, THEREFORE-

### Aims

Overall, the goal of this project is to establish a robust workflow for carrying out one or more common analysis tasks, utilising the human pangenome. Ideally the outcome of this project will aid in more accurate identification of variants associated with altered risk burden for disease conditions; this will be particularly beneficial for populations underrepresented in the current linear reference genome. To that end, we are investigating the state of existing software in the field, [in order to assess performance...?]. 

Several tools already exist for building and working with pangenomes. [Tools for building pangenomes mentioned above - due to the complexity/etc of building a good pangenome, not focusing on pangenome *building* tools].  [Some of the [popular?] tools for working with pangenomes include the vg suite, odgi, and [any othe examples? go here]]. The vg toolkit is a suite of software tools [developed by] which has the capacity to [do things like mapping, etc... potentially mention who made vg as it might be important]. [Other tools?].  [And will be used as a starting point for this investigation into mapping/etc]. [Working at a gene scale].

Additionally, we will be investigating visualisation tools. Although visualisation is not strictly necessary for analysis, it can be beneficial in helping comprehension of what a graph may be doing, or assessing graph build quality. It may also be useful to visualise alignment data, such as read depth. As such, it's important for good visualisation tools to be available. Visualising pangenomes in a 2D space comes with additional challenges, and large graphs may become incredibly convoluted. This is especially apparent when attempting to visualise highly repetitive regions, such as SVs and segmental duplications. Currently, there are two [3?] commonly used software tools for visualising pangenomes - Bandage [src], and seqTubeMap [src].  [Note that older tools exist?Not maintained]. Both of these tools are good at providing an overview of a graph, but as mentioned do not scale well to larger graphs. The features of these tools are also fairly limited - it would be beneficial if these tools were able to (for example) colour or otherwise represent data based on alignment information. Therefore, we are also investigating ways to better represent pangenome graphs visually, using these tools as a starting point.


---
### General Structure

(copied from book; fri apr 26)

- the motivating problem
	- describe hg38; where it's used (ubiquitously); why it's used (1-2 good sentences)
		- define linear-based genome
	- some specific problems w/ hg38 and/or linear-based references in general
		- issues with diversity (be specific)
			- where hg38 comes from (1 individual of european ancestry)
			- SVs? [GET LITERATURE FOR THIS + other issues]
- Introduction to pangenomes:
	- Describe what a pangenome is & how it differs from a linear-based reference
		- What are the benefits of this? Especially wrt known problems with linear
			- Give specific examples + ref. how pangenomes have worked to solve some of these [CHECK PRC papers for src/starting point]
		- What are some current known issues of pangenomes?
			- Unsolved problems from linear (can probaby leave this out of introduction esp. if not relevant)
			- *this is a lead-in to thesis topic* -->
-  Issues of adoption
	- There's a cost associated with switching to new workflows: see people still using hg37 (any source for this? would be useful)
		- Needs to be worth the cost; new tools need to be available (or old ones need to be adapted to work with graph-based)
	- To that end, we are:
		- a.) doing an assessment of the state of (some) of the tools currently available for graph-based genomes
			- is this comparative?
		- b.) looking at mapping (?)
			- why this is/may be a challenge with graph-based over linear genomes
			- what specifically we're looking ay
			- (I think I had something here but had to help a student and lost my train of thought..)
		- c.) looking at visualisation tools
			- challenges w/ visualisation
			- graphs with large SVs can be confusing to look at
			- challenging to make a readable graph with larger segments of the reference (ref [link goes here])
			- to that end: looking at the state of current tools
				- investigating avenues to improve visualisation
					- (Q: how do we assess this quantitatively? If it's something no tool can do yet, should be easy but if we're *improving* something this may be tricky?)
- Some less specific (but not *too* vague) overarching statement on the overall goals of what's being done here; and to what benefit.