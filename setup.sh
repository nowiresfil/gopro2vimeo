#!/bin/bash
PACKAGE_LIST="apt-transport-https ca-certificates curl gnupg openssl"
DOCKER_LIST="docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
sudo apt update && sudo apt upgrade -y
sudo apt install $PACKAGE_LIST

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/debian trixie stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install $DOCKER_LIST
# add pi user to docker group
sudo usermod -aG docker $USER

git clone https://github.com/nowiresfil/gopro2vimeo.git

cd gopro2vimeo/mediamtx
python -m venv .venv
source .venv/bin/activate
pip install requests PyYAML
cd ..
python setup-mediamtx.py
