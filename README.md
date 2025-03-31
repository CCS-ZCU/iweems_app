#  tomeviz: interactive visualizations of latin embeddings

---
## Authors
* [see citation file]

## License
CC-BY-SA 4.0, see attached LICENSE.md

---
## Description
On the server, the app is located in `/srv/webserver/apps/iweems_app`

The code of the app sits in the file `iweems-streamlist.py`.

It is configured to work well with our global `latin_venv` (`/srv/venvs/latin_venv`) python environment.

It can be executed by running commands in `iweems_run.sh`.

But the app should start automatically after reboot - see `/etc/systemd/system/iweems.service`

To update the app:
* make the changes in the code (`iweems-streamlit.py`)
* restart the app: `sudo systemctl restart iweems.service`

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

### To run the app:
 ensure that you use the right python environment:
```bash
souce tomevizvenv/bin/activatate
```
To run your app locally:
```
python tomeviz.py
```
To run it on the IP, (1) change the IP address of you machine in tomeviz.py and then (2) run:
```
python tomeviz --onip
```

# Deployment with heroku

We have also deployed the app using heroku. Once you create a new version, (1) commit it using git,
(2) login interactively to heroku (`heroku login`) and (3) push it to heroku git (`git push heroku master`)
)



## How to cite

[once a release is created and published via zenodo, put its citation here]

## Ackwnowledgement

[This work has been supported by ...]
