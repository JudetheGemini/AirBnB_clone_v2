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
sed -i "25i \\\tserver {\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\t}" /etc/nginx/nginx.conf
sudo service nginx restart