//this one-off program is intended to answer the question posted at:
//https://math.stackexchange.com/questions/445477/sigma-of-factorial-function
//to work out a sigma summation

#include <bits/stdc++.h>
using namespace std;

int main() {
	//maybe use a different value other than 0.5
	//could use a third loop that changes the value from 100 to something greater (maybe squaring it each time) to show convergence to a single value
	int sum;
	int x = 5;
	for(int i = 0; i <= x; i++) { //change x to sth not 100
		int i_copy = i; //to prevent modification of the counter (causing disruption of the loop)
		for(int j = 1; j < i; j++) i_copy *= j; //power factorial
		if(i_copy == 0) i_copy = 1; //since 0! is 1
		sum += pow(0.5,i_copy);
	}
	printf("%d",sum);
	return 0;
}