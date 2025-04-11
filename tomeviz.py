import dash
from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import plotly.graph_objects as go
from gensim.models import KeyedVectors

import pandas as pd
import requests
import pickle
import numpy as np

import argparse  # Import argparse for command-line arguments

# input variables
target = "anima"
subcorpus = "1501-1550"
topn = 20

# loading data
# Load the dataset of positions of all words in 3D space
path = "data/"
with open(path + "coordinates3d_dict.pkl", "rb") as f:
    coordinates3d_dict = pickle.load(f)

filtered_vocab_df = pd.read_json(path + "filtered_vocab_df_v0-1.json")
filtered_vocab_df.set_index("word", inplace=True)

with open(path + "vectors_dict_comp_v0-1.pkl", "rb") as f:
    vectors_dict = pickle.load(f)

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

app = Dash(__name__)
server = app.server  # You can explicitly define server

app.layout = html.Div([
    html.H1(children='tomeviz: Interactive word embeddings for Latin', style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': key, 'value': key} for key in vectors_dict.keys()], value='1501-1550',
                 id='dropdown-selection'),
    dcc.Input(id="target-term", value="scientia", type="text"),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    dcc.Slider(
        id='topn-slider',
        min=5,
        max=100,
        step=1,
        value=20,  # Default value
        marks={i: str(i) for i in range(5, 101, 10)},  # Marks every 10 steps
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    dcc.Graph(id='graph-content', style={'width': '100%', 'height': '100vh'})
])


@app.callback(
    Output('graph-content', 'figure'),
    [Input('submit-button', 'n_clicks'),
     State('dropdown-selection', 'value'),
     State('target-term', 'value'),
     State('topn-slider', 'value')]  # Add slider value as State
)
def update_graph(n_clicks, subcorpus, target, topn):
    if n_clicks < 1:  # If submit-button has not been clicked yet, do not update
        return dash.no_update

    xs, ys, zs, words = coordinates3d_dict[subcorpus]
    word_dict = filtered_vocab_df.apply(lambda row: "<br>wordcount: " + (
        str(row[subcorpus]) if subcorpus in filtered_vocab_df.columns else "NA") + "<br>translation: " + row["transl"],
                                        axis=1).to_dict()

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


if __name__ == '__main__':
    # Argument parsing to check for the 'onip' flag
    parser = argparse.ArgumentParser(description='Run Dash app publicly or locally.')
    parser.add_argument('--onip', action='store_true', help='Run the app publicly.')
    args = parser.parse_args()

    if args.onip:
        # Run to be public and bind to IPv6 as well
        app.run(debug=True, host='::', port=8050)
    else:
        # Run locally (default)
        app.run(debug=True, host='::', port=8050)