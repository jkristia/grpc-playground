

Start db
```bash
docker compose -f server/db/docker-compose.yml up
```


run
docker run --name pgres --rm -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5432:5432 -v ./pgres_data:/var/lib/postgresql/data -d postgres

connect cli
docker exec -it pgres psql -U postgres


docker pull dpage/pgadmin4
docker run -p 80:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=admin' \
    -e 'PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION=True' \
    -e 'PGADMIN_CONFIG_LOGIN_BANNER="Authorised users only!"' \
    -e 'PGADMIN_CONFIG_CONSOLE_LOG_LEVEL=10' \
    -d dpage/pgadmin4
