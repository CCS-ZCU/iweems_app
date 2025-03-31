#!/bin/bash
source /srv/venvs/latin_venv/bin/activate # .env/bin/activate
cd /srv/webserver/apps/iweems_app/
nohup streamlit run iweems-streamlit.py --server.address localhost --server.port 8052 --browser.gatherUsageStats False