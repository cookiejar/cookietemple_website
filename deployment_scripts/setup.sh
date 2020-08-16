#!/bin/bash
# Reference:
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

apt-get update

pip3 install gunicorn

python3 setup.py clean --all install

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

apt install python3-certbot-nginx -y

certbot --nginx -d cookietemple.com -d www.cookietemple.com --non-interactive --agree-tos -m philipp_ehm@protonmail.com
