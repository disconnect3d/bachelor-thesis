#include <iostream>
#include <random>
#include <thread>
#include <vector>
#include "../measure.h"

int main(int argc, char *argv[]) {
    if (argc != 4) {
        std::cerr << "Usage: <type> <n> <threads_count>" << std::endl;
        std::cerr << "type - 0 for near, 1 for far" << std::endl;
        std::cerr << "n - size of data" << std::endl;
        std::cerr << "threads_count - number of threads that will be used" << std::endl;
        return 0;
    }

    auto type = std::atoi(argv[1]);
    size_t n = std::stoull(argv[2]);
    auto threads_count = std::atoi(argv[3]);

    std::mt19937 gen;
    std::uniform_int_distribution<> rnd(0, 255);
    std::vector<int> v;
    v.reserve(n);

    /* fill with some values */
    for (std::size_t i = 0; i < n; ++i)
        v.push_back(rnd(gen));

    int res[500];

    volatile int *near_pointers[] = {res, res + 1, res + 2, res + 3, res + 4, res + 5, res + 6, res + 7};
    volatile int *far_pointers[] = {res, res + 64, res + 128, res + 192, res + 256, res + 320, res + 384, res + 448};
    //const int threads_count = 8;
    const int pointers_count = 8;

    auto f = [&](volatile int **result_pointers) {
        auto th = [](volatile int *result, int *first, int *last) {
            *result = 0;
            while (first != last) {
                int x = *first++;
                *result += x % 2;
            }
        };

        std::vector<std::thread> threads;
        const auto elements_per_thread = n / threads_count;
        const auto rest_elements = n % threads_count;
        decltype(n) data_index_start = 0;

        for (int thread_index = 0; thread_index < threads_count; ++thread_index) {
            auto do_elements = elements_per_thread;

            if (thread_index < rest_elements)
                do_elements += 1;

            decltype(n) data_index_end = data_index_start + do_elements + 1;
            threads.push_back(
                    std::thread{th, result_pointers[thread_index], v.data() + data_index_start,
                                v.data() + data_index_end}
            );
            data_index_start = data_index_end;
        }

        for (auto &t: threads)
            t.join();

        auto sum = 0;
        for (auto i = 0; i < pointers_count; ++i)
            sum += *result_pointers[i];
        return sum;
    };

    if (type == 0)
        measure(n, [&]() {
            return f(near_pointers);
        });
    else
        measure(n, [&]() {
            return f(far_pointers);
        });
}
