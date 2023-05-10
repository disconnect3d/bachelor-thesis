/* Modified version of usingstdcpp2015: measure function.
 *
 * Copyright 2015 Joaquin M Lopez Munoz.
 * Distributed under the Boost Software License, Version 1.0.
 * (See accompanying file LICENSE_1_0.txt or copy at
 * http://www.boost.org/LICENSE_1_0.txt)
 */

#include <iostream>
#include <algorithm>
#include <array>
#include <chrono>
#include <numeric>

template <int iterations=50, typename Size, typename F>
void measure(Size n, F f) {
    using namespace std::chrono;
    volatile decltype(f()) res{0}; /* to avoid optimizing f() away */

    high_resolution_clock::time_point t1, t2;

    std::array<long double, iterations> timings;


    for(auto i=0; i<iterations; ++i) {
        t1 = high_resolution_clock::now();
        res += f();
        t2 = high_resolution_clock::now();
        timings[i] = (long double)(t2 - t1).count() / (long double)n;
    }
    std::cerr << "result value used against compiler optimization - ignore this: " << res << std::endl;

    for(int i=0; i<iterations-1; ++i)
        std::cout << timings[i] << ",";
    std::cout << timings[iterations-1] << std::endl;
}
