
all: sassc

sassc: sassc.o

sassc.o: sassc.c

test: sassc
	./sassc -h

