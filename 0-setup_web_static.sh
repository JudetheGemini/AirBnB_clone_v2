#!/usr/bin/env bash
# Script to setup web server for deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    ALX wan kill me
  </body>
</html>" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "25i \\\tserver {\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current/;\n\t}\t}" /etc/nginx/sites-available/default
sudo service nginx restart