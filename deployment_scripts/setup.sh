#!/bin/bash
# Reference:
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

apt-get update

apt-get install python-pip python-dev nginx -y

pip3 install virtualenv

cd ~

git clone https://github.com/cookiejar/cookietemple_website

cd cookietemple_website

virtualenv dpenv

source dpenv/bin/activate

pip3 install gunicorn

python setup.py clean --all install

cp /home/cookietemple_dev/cookietemple_website/deployment_scripts/cookietemple_website.service \
/etc/systemd/system/cookietemple_website.service

systemctl start cookietemple_website

systemctl enable cookietemple_website

cp /home/cookietemple_dev/cookietemple_website/deployment_scripts/cookietemple_website \
/etc/nginx/sites-available/cookietemple_website

ln -s /etc/nginx/sites-available/cookietemple_website /etc/nginx/sites-enabled

nginx -t

systemctl restart nginx

ufw delete allow 5000

ufw allow 'Nginx Full'

add-apt-repository ppa:certbot/certbot -y

apt install python-certbot-nginx -y

certbot --nginx -d cookietemple.com -d www.cookietemple.com --non-interactive --agree-tos -m philipp_ehm@protonmail.com
