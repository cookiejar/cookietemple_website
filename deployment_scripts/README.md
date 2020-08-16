1. SSH into server as root (if no user with superuser privileges exists)

2. Create an account with superuser privileges if not yet existing:
```bash
adduser cookietemple_dev

usermod -aG sudo cookietemple_dev

su cookietemple_dev
```

3. Enable firewall
```bash
ufw allow OpenSSH
ufw enable
```

4. Clone the code and start the deployment script! Ensure beforehand that the user account and the URL are still matching!
```bash
cd ~

git clone https://github.com/cookiejar/cookietemple_website
```
```bash
sudo bash cookietemple_website/deployment_scripts/setup.sh
```
