# Rapifuzz_Assignment Setup
Required Tools:
- Docker version 27.1.1 
- docker-compose version 1.29.2

### Clone the Repo and go to **Rapifuzz_Assignment/drf** foldet:
```bash
git clone https://github.com/Shoony0/Rapifuzz_Assignment.git
cd Rapifuzz_Assignment/drf
```

### Setup The Django Env:
```bash
docker compose --env-file .env -f docker-compose.yml up --build --force-recreate --remove-orphans
```

### ROOT API URL
http://localhost:808/
