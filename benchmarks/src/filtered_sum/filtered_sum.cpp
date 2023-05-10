#include <algorithm>
#include <iostream>
#include <random>
#include <vector>
#include "../measure.h"

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: <type> <n> <value>" << std::endl;
        std::cerr << "type - 0 for sorted, 1 for unsorted data" << std::endl;
        std::cerr << "n - size of array" << std::endl;
        return 0;
    }

    auto type = std::atoi(argv[1]);
    size_t n = std::stoull(argv[2]);

    std::vector<int> v;
    std::mt19937 gen;
    std::uniform_int_distribution<> rnd(0, 255);
    v.reserve(n);
    for (std::size_t i = 0; i < n; ++i)
        v.push_back(rnd(gen));

    auto f = [&]() {
        long int res = 0;
        for (int x: v)
            if (x >= 128)
                res += x;
        return res;
    };

    if (type == 0)
        std::sort(v.begin(), v.end());

    measure(n, f);
}