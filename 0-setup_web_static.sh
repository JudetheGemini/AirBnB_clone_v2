#!/usr/bin/env bash
# Script to setup web server for deployment
sudo apt-get update
sudo apt-get nginx
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "25i \\\tserver {\tlocation /hbnb_static {\talias /data/web_static/current/;\t}\t}" /etc/nginx/nginx.conf
sudo service nginx restart