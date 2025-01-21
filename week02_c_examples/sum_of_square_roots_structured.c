#include <math.h>
#include <stdio.h>

double sum_of_square_roots(int N) {
    int i;
    double value;

    value = 0.0;
    for(i = 1;i <= N;i++) {
        value += sqrt(i);
    }

    return value;
}

int main(void) {
    const int N = 20;
    double value;

    value = sum_of_square_roots(N);
    printf("%f\n", value);

    return 0;
}
