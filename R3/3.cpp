#include <vector>
template<typename T> std::vector<std::vector<T>> r3(const std::vector<T>& e) {
    std::vector<std::vector<T>> res(e.size());
    for (size_t i = 0; i < res.size(); ++i) {
        size_t j = res.size() - i - 1; const T& x = e[j];
        const T& y = e[j ? j - 1 : e.size() - 1]; T z = x;
        res[i].resize(x); for (T& t : res[i]) { t = z; z += y; }
    }
    return res;
}
