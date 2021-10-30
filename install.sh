#! /bin/bash

pip3 install -r requirements.txt
sudo cp chainalysis.service /etc/systemd/system/
