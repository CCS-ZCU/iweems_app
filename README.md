#  tomeviz: interactive visualizations of latin embeddings

---
## Authors
* [see citation file]

## License
CC-BY-SA 4.0, see attached LICENSE.md

---
## Description

[What is the purpose of this repo? Is it related to any specific dataset or publication output?]

## Getting started

### To setup your python evnironment

```
git clone [url-of-the-git-file]
cd [name-of-the-repo]
python3 -m venv tomevizvenv
source tomevizvenv/bin/activatate
pip install -r requirements.txt
ipykernel install --user --name tomeviz_kernel
```

### To download the latest data
```
curl -L https://github.com/CCS-ZCU/noscemus_ETF/raw/master/data/vectors_dict_comp.pkl -o data/vectors_dict_comp_TEST.pkl
curl -L https://github.com/CCS-ZCU/noscemus_ETF/raw/master/data/coordinates3d_dict.pkl -o data/coordinates3d_dict.pkl
curl -L https://github.com/CCS-ZCU/noscemus_ETF/raw/master/data/filtered_vocab_df.json -o data/filtered_vocab_df.json
curl -L https://github.com/CCS-ZCU/noscemus_ETF/raw/master/data/metadata_table_long.json -o data/metadata_table_long.json

```


Go to `scripts` and run the notebooks

## How to cite

[once a release is created and published via zenodo, put its citation here]

## Ackwnowledgement

[This work has been supported by ...]
