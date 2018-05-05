#include <vector>
#include <algorithm>
int ProductOfHighest(std::vector<int> intVector) {
    std::sort(intVector.begin(), intVector.end());
    int factorOne = intVector.at(intVector.size() - 1);
    int factorTwo = intVector.at(intVector.size() - 2);
    int finalProduct = factorOne * factorTwo;
    return finalProduct;
}
//Before you vote, make sure to consider all the factors
