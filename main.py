from symspellpy import SymSpell
import pkg_resources
import pandas as pd
import numpy as np
import re

df = pd.read_csv('Covid19Suspect_4attr.csv', encoding='utf-8')
df = df.dropna()


sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
)

# term_index is the column of the term and count_index is the column of the term frequency
sym_spell.load_dictionary(
    "./dataset/text/medical_abbreviations_wikipedia.txt", term_index=0, count_index=1)
sym_spell.load_dictionary(
    "./dataset/text/medical_abbreviations_medline.txt", term_index=0, count_index=1)
sym_spell.load_dictionary(
    "./dataset/text/medical_abbreviations_medicinenet.txt", term_index=0, count_index=1)
sym_spell.load_dictionary(
    "./dataset/text/medical_abbreviations_asha.txt", term_index=0, count_index=1)
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

df = pd.read_csv('Covid19Suspect_4attr.csv', encoding='utf-8')
df = df.dropna()

df['otherComorbidCleaned'] = df['otherComorbid'].apply(
    lambda x: sym_spell.lookup_compound(x, max_edit_distance=2)[0].term)

df.to_csv('Covid19Suspect_4attr_cleaned.csv', index=False)
