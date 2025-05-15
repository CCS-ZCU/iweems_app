# overview.py
import streamlit as st

def app():
    st.markdown("""
    # iWEEMS: Interactive Word Embeddings for Early Modern Science

    This web app serves as an interactive visualization of the [WEEMS](https://zenodo.org/records/15418943) (Word Embeddings for Early Modern Science) models, a series of word vector models trained on two corpora of Early Modern Latin texts:

    * [Noscemus Digital Sourcebook](https://doi.org/10.5281/zenodo.15040256) - a corpus of digitized Early modern scientific texts in Latin
    * [EMLAP](https://doi.org/10.5281/zenodo.14765294) -  a corpus of digitized Early Modern Latin Alchemical Prints
    
    In addition to that, for comparison, we also implement two other word embedding models based on [LASLA](https://www.lasla.uliege.be/cms/c_8508894/fr/lasla?id=c_8508894) (a representative selection of Classical Latin texts) and OperaMaiora (a corpus of philosophical and religious works written by Thomas Aquinas in the 13th century, comprising some 4.5 million words), which are publicly available from [here](https://embeddings.lila-erc.eu/#topnav).
    
    In total, we offer 4 temporal models based on NOSCEMUS, 8 discipline-specific models derived from NOSCEMUS, 1 model trained on the EMLAP corpus, and two pretrained models inherited from other resources:
    
    * NOSCEMUS - 1501-1550
    * NOSCEMUS - 1551-1600
    * NOSCEMUS - 1601-1650
    * NOSCEMUS - 1651-1700
    * NOSCEMUS - Alchemy/Chemistry
    * NOSCEMUS - Astronomy/Astrology/Cosmography
    * NOSCEMUS - Biology
    * NOSCEMUS - Geography/Cartography
    * NOSCEMUS - Mathematics
    * NOSCEMUS - Medicine
    * NOSCEMUS - Meteorology/Earth sciences
    * NOSCEMUS - Physics
    * EMLAP
    * LASLA
    * Opera Maiora
    
    We trained the models on textual data previously preprocessed and automatically morphologically annotated using scripts in the following GitHub repositories:
    
    * [NOSCEMUS_ETL](https://github.com/CCS-ZCU/noscemus_ETL)
    * [EMLAP_ETL](https://github.com/CCS-ZCU/EMLAP_ETL)
    
    The training textual data have the form of automatically lemmatized and morphologically annotated Latin sentences. From these sentences, we filter morphologically annotated nouns (NOUN), verbs (VERB), adjectives (ADJ), and proper names (PROPN), as they tend to be semantically most relevant.
    
     We further refine the vocabulary by calculating raw word frequencies across subcorpora. Specifically, 2,000 most frequent (lemmatized) words from each subcorpus are extracted, yielding a [NOTICE: outdated] vocabulary size of 6643 unique words. Words with less than 5 occurrences are excluded, reducing the vocabulary to 6,005 unique lemmas (ensuring overlap for model alignment).
    
    The models are trained using the FastText algorithm:
    
    * Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching Word Vectors with Subword Information. Transactions of the Association for Computational Linguistics, 5, 135–146. https://doi.org/10.1162/tacl_a_00051
     
    And we employ the same parametrization as used in this paper:
    
    * Sprugnoli, R., Moretti, G., & Passarotti, M. (2020). Building and Comparing Lemma Embeddings for Latin. Classical Latin versus Thomas Aquinas. Italian Journal of Computational Linguistics, 6(1). https://doi.org/10.5281/ZENODO.4618000
    This standardization makes our vectors directly comparable to those generated for LASLA and OperaMaiora.

    """)