run-dev-historical:
	cp historical.settings.env settings.env
	uv run python run.py

run-dev-live:
	cp live.settings.env settings.env
	uv run python run.py

build:
	docker build -f Dockerfile -t candles .

run: build
	docker run -it \
		--network redpanda_network \
		-e KAFKA_BROKER_ADDRESS=redpanda:9092 \
		candles
