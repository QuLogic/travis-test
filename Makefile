
all: sassc

sassc: sassc.o
	gcc --coverage -o sassc sassc.o

sassc.o: sassc.c
	gcc --coverage -c -o sassc.o sassc.c

clean:
	rm *.o sassc

test: sassc
	./sassc -h

.PHONY: all clean test

