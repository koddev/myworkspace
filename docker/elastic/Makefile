.PHONY: config
config:
	rm -rf clickhouse01 clickhouse02 clickhouse03 clickhouse04


.PHONY: up
up:
	docker-compose up

.PHONY: up2
up2:
	docker compose -f docker-compose_cert.yml up

.PHONY: up3

up3:
	 
	docker network create elastic

	docker run  \
	--name "es01" \
	--net elastic \
	-p 9200:9200 \
	-p 9300:9300 \
	-e node.name="es1" \
	-e ES_JAVA_OPTS="-Xms4g -Xmx4g"\
	 docker.elastic.co/elasticsearch/elasticsearch:8.8.2 
 


.PHONY: start
start:
	docker-compose start

.PHONY: stop
stop:
	docker-compose stop

.PHONY: down
down:
	docker-compose down

.PHONY: down2
down2:
	docker compose -f docker-compose_cert.yml down -v
