#!/bin/bash
cd /app
echo "----- Now deployed web booting your repo ------ " 
git clone https://github.com/Team-Deadly/Music && cd Music && pip3 install -U -r requirements.txt
gunicorn app:app & python3 -m InnexiaMusic
