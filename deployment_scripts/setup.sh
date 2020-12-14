#!/bin/bash
# Reference:
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-dev nginx -y
sudo pip3 install virtualenv

virtualenv dpenv
source dpenv/bin/activate

sudo apt-get update
pip3 install gunicorn
make install

cp /home/cookietemple_dev/cookietemple_website/deployment_scripts/cookietemple_website.service \
/etc/systemd/system/cookietemple_website.service

sudo systemctl start cookietemple_website

sudo systemctl enable cookietemple_website

cp /home/cookietemple_dev/cookietemple_website/deployment_scripts/cookietemple_website \
/etc/nginx/sites-available/cookietemple_website

ln -s /etc/nginx/sites-available/cookietemple_website /etc/nginx/sites-enabled

sudo nginx -t

sudo systemctl restart nginx

sudo ufw delete allow 5000

sudo ufw allow 'Nginx Full'

sudo add-apt-repository ppa:certbot/certbot -y

sudo apt install python3-certbot-nginx -y

sudo certbot --nginx -d cookietemple.com -d www.cookietemple.com --non-interactive --agree-tos -m philipp_ehm@protonmail.com
