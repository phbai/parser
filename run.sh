docker run --name some-parser --link some-redis:redis -d -p 8000:8000 phbai/parser
docker run -i -t --rm --name some-parser -p 8000:8000 --link some-redis:redis parser /bin/bash