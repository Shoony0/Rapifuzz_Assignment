# Rapifuzz_Assignment Setup
Required Tools:
- Docker version 27.1.1 
- docker-compose version 1.29.2

### Clone the Repo and execute the command:
```bash
git clone https://github.com/Shoony0/Rapifuzz_Assignment.git
rm Rapifuzz_Assignment/mysql_data/delete.txt
cd Rapifuzz_Assignment/
```

### Setup The Django Env:
```bash
docker compose --env-file .env -f docker-compose.yml up --build --force-recreate --remove-orphans
```

### ROOT API URL
http://localhost:808/
