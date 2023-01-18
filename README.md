# Semantic Data Curation
Introducing semantics is a unique technique in data curation.  Semantics acts as a glue by defining the data model and relationships before and after the data processing.  Curation handles data duplication and improves data quality. It disambiguates the data items. Multiple labels are unified and classified based on the trained model corpora, and semantically equivalent terms are identified.
Example: {Fever, Fiver, FVR, Feever, Fevere\} = {Fever}.

To handle the misspelled English words, The \textbf{\textit{SymSpell's}} own corpus is used, which consists of the intersection of the large Ngram datasets from google Ngram with wordlists generated from **hunspell** dictionary files. The proposed semantic data curation is pipelined as shown in Figure \ref{fig:3}. For the clinical abbreviations, we generated the word corpus of clinical abbreviations. The corpus was web scrapped from Wikipedia's Page on List of Medical Abbreviations. To get the curated semantic data of the original corpus, we then run a **Garbe_SymSpell_201** and **Symspell check** algorithm using the intersections of both the corpus and subsequently achieving the semantic data curation at the initial level of RDF data processing. 


This repository contains the source code for the Semantic Data Curation for healthcare data. 

## Installation

`pip install -r requirements.txt`

## Usage

`python main.py`

## License


This work is submitted to a **Connection Science Taylor and Francsis Jouranl** and is currenty under review. 
