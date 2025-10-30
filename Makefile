IMAGE_NAME = cxeli-dzagli-picker

# იმიჯის ასაშენებელი ბრძანება
build:
	docker build -t $(IMAGE_NAME) .

# აპლიკაციის გაშვების ბრძანება
run: build
	docker run --rm -it --net=host $(IMAGE_NAME)

.PHONY: build run
