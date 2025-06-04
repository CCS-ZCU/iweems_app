[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15591687.svg)](https://doi.org/10.5281/zenodo.15591687)

# iWEEMS: Interactive Word Embeddings for Early Modern Science

This repository contains the source code of iWEEMS, an interactive web application for the visualization of 
Word Embeddings for Early Modern Science (WEEMS). The application allows users to explore semantic spaces 
derived from corpora of Early Modern Latin scientific texts. 

A more detailed description is available in `overview.py`

🔗 Public instance: https://ccs-lab.zcu.cz/iweems  
📄 WEEMS models: https://doi.org/10.5281/zenodo.15418943  
📚 Developed as part of the TOME project (LL2320).
---
## Authors
* [see citation file]

## License
CC-BY-SA 4.0, see attached LICENSE.md

---
## Technical details
On the server, the app is located in `/srv/webserver/apps/iweems_app`

The code of the app sits in the file `iweems-streamlist.py`.

It is configured to work well with our global `latin_venv` (`/srv/venvs/latin_venv`) python environment.

It can be executed by running commands in `iweems_run.sh`.

But the app should start automatically after reboot - see `/etc/systemd/system/iweems.service`

To update the app:
* make the changes in the code (`iweems-streamlit.py`)
* restart the app: `sudo systemctl restart iweems.service`

