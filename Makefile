
all: sassc

sassc: sassc.o
	gcc --coverage -o sassc sassc.o

sassc.o: sassc.c
	gcc --coverage -c -o sassc.o sassc.c

clean:
	rm *.o sassc

test: sassc
	echo -en 'travis_fold:start:sassc\r'
	./sassc -h
	echo -en 'travis_fold:end:sassc\r'

.PHONY: all clean test

