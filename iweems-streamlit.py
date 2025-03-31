import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pickle

# page title
st.write('''
# iWEEMS: Interactive Word Embeddings for Early Modern Science

''')

# loading data
# Load the dataset of positions of all words in 3D space
path = "data/"
with open(path + "coordinates3d_dict.pkl", "rb") as f:
    coordinates3d_dict = pickle.load(f)

filtered_vocab_df = pd.read_json(path + "filtered_vocab_df_v0-1.json")
filtered_vocab_df.set_index("word", inplace=True)

with open(path + "vectors_dict_comp_v0-1.pkl", "rb") as f:
    vectors_dict = pickle.load(f)

# streamlit interactive elements for data selection
subcorpus = st.selectbox('What subcorpus are you interested in:', [key for key in vectors_dict.keys()])
target = st.text_input('What word are you interested in:', value='anima')
topn = st.slider('Select the number of nearest neighbours:', min_value=5, max_value=100, value=20)

def plot_gen(subcorpus, target, topn, coordinates3d_dict, filtered_vocab_df, vectors_dict):
    # selecting data on the basis of subcorpus & target
    xs, ys, zs, words = coordinates3d_dict[subcorpus]
    word_dict = filtered_vocab_df.apply(
        lambda row: "<br>wordcount: " + (
            str(row[subcorpus]) if subcorpus in filtered_vocab_df.columns else "NA") + "<br>translation: " + row["transl"],
        axis=1
    ).to_dict()

    nns_tuples = vectors_dict[subcorpus].most_similar(target, topn=topn)
    wordlist = [target] + [tup[0] for tup in nns_tuples]
    sim_scores = [str(1)] + [str(np.round(tup[1], 2)) for tup in nns_tuples]
    idx = [word[0] for word in enumerate(words) if word[1] in wordlist]  # find the positional indices
    wordlist_xs, wordlist_ys, wordlist_zs = xs[idx], ys[idx], zs[idx]

    hover_text = []
    for word, sim in zip(wordlist, sim_scores):
        if word in word_dict.keys():
            hover_text.append(word + word_dict[word] + "<br>similarity to target ({0}): {1}".format(target, sim))
        else:
            hover_text.append(
                word + "<br>wordcount: NA<br>translation: NA<br>similarity to target ({0}): {1}".format(target, sim))

    # define the figure object
    fig = go.Figure(data=go.Scatter3d(
        x=wordlist_xs,
        y=wordlist_ys,
        z=wordlist_zs,
        mode='markers+text',
        marker=dict(
            size=5,
            color='purple',
            opacity=0.3
        ),
        text=wordlist,
        hovertext=hover_text,  # use the prepared hover text mapping
        hoverinfo='text',
        textposition='top center',  # Ensures all texts are positioned consistently
        textfont=dict(
            size=12  # Uniform font size
        )
    ))

    fig.update_layout(
        title='Embeddings',
        scene=dict(
            xaxis=dict(title='', showgrid=False, showline=False, showticklabels=False, zeroline=False,
                        showbackground=False,
                        linecolor='rgba(0,0,0,0)'),
            yaxis=dict(title='', showgrid=False, showline=False, showticklabels=False, zeroline=False,
                        showbackground=False,
                        linecolor='rgba(0,0,0,0)'),
            zaxis=dict(title='', showgrid=False, showline=False, showticklabels=False, zeroline=False,
                        showbackground=False,
                        linecolor='rgba(0,0,0,0)'),
            bgcolor='rgba(255,255,255,0)'
        ),
        paper_bgcolor='rgba(255,255,255,255)',  # set the color of the area around the axes
        plot_bgcolor='rgba(255,255,255,255)',  # set the color of the entire chart
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=0),
        hovermode='closest',
        showlegend=False,
        uniformtext_minsize=12,
        uniformtext_mode='hide'  # Force minimum text size without displaying all labels
    )

    return fig

# Show the plot
try:
    st.plotly_chart(plot_gen(subcorpus, target, topn, coordinates3d_dict, filtered_vocab_df, vectors_dict))
except:
    st.write(f"The word **{target}** is not in our corpus!")
