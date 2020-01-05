NUM=4
DIVIDER=2

install:
	docker build -t pascal-triangle .

pascal-triangle:
	docker run --rm -it pascal-triangle pascal-triangle -n $(NUM)

sierpinski-triangle:
	docker run --rm -it pascal-triangle sierpinski-triangle -n $(NUM) -d $(DIVIDER)