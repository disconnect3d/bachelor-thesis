#include <algorithm>
#include <iostream>
#include <vector>
#include "../measure.h"


struct particle {
    int x, y, z;
    int dx, dy, dz;
};

using particle_aos = std::vector<particle>;

particle_aos create_particle_aos(int n) {
    particle_aos res;
    res.reserve(n);
    for (int i = 0; i < n; ++i)
        res.push_back({i, i + 1, i + 2, i + 3, i + 4, i + 5});
    return res;
}

struct particle_soa {
    std::vector<int> x, y, z;
    std::vector<int> dx, dy, dz;
};

particle_soa create_particle_soa(int n) {
    particle_soa res;
    res.x.reserve(n);
    res.y.reserve(n);
    res.z.reserve(n);
    res.dx.reserve(n);
    res.dy.reserve(n);
    res.dz.reserve(n);
    for (int i = 0; i < n; ++i) {
        res.x.push_back(i);
        res.y.push_back(i + 1);
        res.z.push_back(i + 2);
        res.dx.push_back(i + 3);
        res.dy.push_back(i + 4);
        res.dz.push_back(i + 5);
    }
    return res;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: <type> <n>" << std::endl;
        std::cerr << "type - 0 for aos, 1 for soa" << std::endl;
        std::cerr << "n - size of data" << std::endl;
        return 0;
    }

    auto type = std::atoi(argv[1]);
    size_t n = std::stoull(argv[2]);

    if (type == 0) {
        auto ps = create_particle_aos(n);

        measure(n, [&]() {
            long int res = 0;
            for (const auto &particle: ps)
                res += particle.x + particle.y + particle.z;
            return res;
        });
    }
    else {
        auto ps = create_particle_soa(n);

        measure(n, [&]() {
            long int res = 0;
            for (std::size_t i = 0; i < n; ++i)
                res += ps.x[i] + ps.y[i] + ps.z[i];
            return res;
        });
    }
}
