# overview.py
import streamlit as st

def app():
    st.markdown("""
    # iWEEMS: Interactive Word Embeddings for Early Modern Science

    This web app serves for interactive visualizations of a set of word embedding models 
    trained on Early Modern scientific prints in Latin available in [Noscemus Digital Sourcebook](https://zenodo.org/records/15040256).

    - Models: [Zenodo DOI](https://doi.org/10.5281/zenodo.14626412)
    - Based on: [TOME project](https://tome.flu.cas.cz)
    """)