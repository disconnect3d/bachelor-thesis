#include <iostream>
#include <cmath>
#include <chrono>
#include "../measure.h"

struct PaddedList {
    char padding[59];
    struct PaddedList* next;
};

// ustawienie wyrównania do jednego bajtu
#pragma pack(1)
struct PackedList {
    char padding[59];
    struct PackedList* next;
    char fill[5];
};
// ustawienie wyrównania na domyślne
#pragma pack()


template <typename ListType>
void benchmark(std::size_t n) {
    ListType* list = new ListType[n];

    std::cerr << sizeof(ListType) << " " << (char*)&list[1] - (char*)list << std::endl;
    for(int i=0; i<n-1; ++i)
        list[i].next = &list[i+1];
    list[n-1].next = list;

    ListType* ptr = list;
measure(n, [&]() {
        for (auto i = 0; i < n; ++i)
            ptr = ptr->next;
        return ptr-list;
    });

//    std::cerr << "List: " << list << ", ptr: " << ptr << std::endl;

    delete [] list;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: <type> <n>" << std::endl;
        std::cerr << "type - 0 for PaddedList, 1 for PackedList data" << std::endl;
        std::cerr << "n - number of nodes" << std::endl;
        return 0;
    }

    auto type = std::atoi(argv[1]);
    size_t n = std::stoull(argv[2]);

    if (type == 0)
        benchmark<PaddedList>(n);
    else
        benchmark<PackedList>(n);
}
