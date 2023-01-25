#!/bin/bash
cd /app
echo "----- Now deployed web booting your repo ------ " 
git clone $REPO_URL ok && cd ok && pip3 install -U -r requirements.txt
gunicorn app:app & python3 -m InnexiaMusic
