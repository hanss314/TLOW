#include <iostream>
int main() {
	int weAreNumberOne = 1;
	int numberTwo = 1;
	while (1 == 1) {
		std::cout << weAreNumberOne << std::endl << numberTwo << std::endl;
		weAreNumberOne = weAreNumberOne + numberTwo;
		numberTwo = numberTwo + weAreNumberOne;
	}
}