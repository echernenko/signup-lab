NOTE: suggest to not push anything for a sandbox Ubuntu box to this repo. Either edit via browser or push from main laptop. 
Be sure you have keys set up for github and remote is set:
```
git remote set-url origin git@github.com:echernenko/signup-lab.git
```

1. Create a new DigitalOcean Droplet: https://cloud.digitalocean.com/droplets
2. Login to droplet and create a new user to not work under root:
```
adduser --disabled-password --gecos "" worker
echo "{USER}:{PASSWORD}" | chpasswd
usermod -aG sudo {USER}
su - {USER}
```
3. create a folder in /home/{USER}/ called `code`. Navigate to it.
4. Clone the repo in question: 
```
git clone git@github.com:echernenko/signup-lab.git
chmod +x bootstrap.sh && ./bootstrap.sh
exit
su - worker
cd /home/{USER}/code/signup-lab
docker compose up -d --build
```
5. xx
