#include <iostream>
#include <cmath>
#include <boost/multi_array.hpp>
#include "../measure.h"

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: <type> <dim>" << std::endl;
        std::cerr << "type - 0 for row traversal, 1 for column traversal" << std::endl;
        std::cerr << "dim - pass matrix dimension (program will create 2D matrix dim x dim)" << std::endl;
        return 0;
    }

    auto type = std::atoi(argv[1]);
    size_t dim = static_cast<size_t>(std::sqrt(std::atof(argv[2])));

    boost::multi_array<int, 2> matrix(boost::extents[dim][dim]);

    // Fill matrix with some values
    for (auto i = 0; i < dim; ++i)
        for (auto j = 0; j < dim; ++j)
            matrix[i][j] = i + j;

    if (type == 0)
        measure(dim * dim, [&]() {
            long int sum = 0;
            for (auto i = 0; i < dim; ++i)
                for (auto j = 0; j < dim; ++j)
                    sum += matrix[i][j];
            return sum;
        });

    else
        measure(dim * dim, [&]() {
            long int sum = 0;
            for (auto j = 0; j < dim; ++j)
                for (auto i = 0; i < dim; ++i)
                    sum += matrix[i][j];
            return sum;
        });
}
