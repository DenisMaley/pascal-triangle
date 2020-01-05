NUM=4

install:
	docker build -t pascal-triangle .

pascal-triangle:
	docker run --rm -it pascal-triangle pascal-triangle -n $(NUM)