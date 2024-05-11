from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import requests
import pickle

# input variables
target = "anima"
subcorpus = "1501-1550"
topn = 20

# loading data
# Load the dataset of positions of all words in 3D space
path = "data/"
with open(path + "coordinates3s_dict.pkl", "rb") as f:
    coordinates3s_dict = pickle.load(f)#url = "https://raw.githubusercontent.com/CCS-ZCU/noscemus_ETF/master/data/coordinates3s_dict.pkl"
#resp = requests.get(url)
# coordinates3s_dict = pickle.loads(resp.content)

filtered_vocab_df = pd.read_json(path + "filtered_vocab_df.json")
# filtered_vocab_df = pd.read_json("https://raw.githubusercontent.com/CCS-ZCU/noscemus_ETF/master/data/filtered_vocab_df.json")
filtered_vocab_df.set_index("word", inplace=True)

with open(path + "vectors_dict_comp.pkl", "rb") as f:
    vectors_dict = pickle.load(f)
#url = "https://raw.githubusercontent.com/CCS-ZCU/noscemus_ETF/master/data/vectors_dict_comp.pkl"
#resp = requests.get(url)
#vectors_dict = pickle.loads(resp.content)

# selecting data on the basis of subcorporpus & target
xs, ys, zs, words = coordinates3s_dict[subcorpus]
word_dict = filtered_vocab_df.apply(lambda row: "wordcount: " + str(row[subcorpus]) + ", translation: " + row["transl"], axis=1).to_dict()

wordlist = [target] + [tup[0] for tup in vectors_dict[subcorpus].most_similar(target, topn=topn)]
idx = [word[0] for word in enumerate(words) if word[1] in wordlist] # find the positional indeces
wordlist_xs, wordlist_ys, wordlist_zs = xs[idx], ys[idx], zs[idx]

hover_text = [word + ": " + word_dict[word] for word in wordlist]



app = Dash(__name__)
server = app.server  # You can explicitly define server

app.layout = html.Div([
    html.H1(children='Interactive word embeddings', style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': key, 'value': key} for key in vectors_dict.keys()], value='1501-1550',
                 id='dropdown-selection'),
    dcc.Input(id="target-term", value="scientia", type="text"),
    html.Button(id='submit-button', n_clicks=1, children='Submit'),
    dcc.Graph(id='graph-content', style={'width': '100%', 'height': '100vh'})
])


@app.callback(
    Output('graph-content', 'figure'),
    Input('submit-button', 'n_clicks'),
    Input('dropdown-selection', 'value'),
    Input('target-term', 'value'),
)
def update_graph(n_clicks, subcorpus, target):
    # Update only when the submit button is pressed
    if n_clicks < 1:
        return dash.no_update
    xs, ys, zs, words = coordinates3s_dict[subcorpus]
    word_dict = filtered_vocab_df.apply(lambda row: "wordcount: " + str(row[subcorpus]) + ", translation: " + row["transl"], axis=1).to_dict()

    wordlist = [target] + [tup[0] for tup in vectors_dict[subcorpus].most_similar(target, topn=topn)]
    idx = [word[0] for word in enumerate(words) if word[1] in wordlist] # find the positional indeces
    wordlist_xs, wordlist_ys, wordlist_zs = xs[idx], ys[idx], zs[idx]

    hover_text = [word + ": " + word_dict[word] for word in wordlist]
    # define the figure object
    fig = go.Figure(data=go.Scatter3d(
        x=wordlist_xs,
        y=wordlist_ys,
        z=wordlist_zs,
        mode='markers',
        marker=dict(
            size=5,
            color='purple',
            opacity=0.3
        ),
        text=hover_text,  # use mapped hover text
        hoverinfo='text',  # ensure only the text field is displayed on hover
    ))

    fig.update_layout(
        title='Embeddings',
        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis'
        ),
        hovermode='closest',
        showlegend=False
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)