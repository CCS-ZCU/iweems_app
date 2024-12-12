#!/bin/bash
cd /home/tvrzj/Documents/Projects/tomeviz/
source .env/bin/activate
streamlit run totomeme.py --server.address localhost --server.port 8052 --browser.gatherUsageStats False