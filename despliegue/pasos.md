installar docker 


sudo apt-get remove -y docker-compose

sudo curl -L "https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

```bash
/usr/local/bin/docker-compose up -d
/usr/local/bin/docker-compose ps
```