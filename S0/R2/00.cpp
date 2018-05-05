#include <limits>
#include <vector>
template<typename T> auto pmax2(const std::vector<T>& es) {
    T max1 = std::numeric_limits<T>::min(), max2 = max1;
    for (const T& e : es) {
        if (e > max1) { max2 = max1; max1 = e; }
        else if (e > max2) { max2 = e; }
    }
    return max1 * max2;
}
