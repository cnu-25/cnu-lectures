#include <math.h>
#include <stdio.h>

int main(void) {
    const int N = 20;
    int i, target;
    double value;
    void *targets[] = {&&loop, &&end};

    value = 0.0;
    i = 1;
    loop:
    value += sqrt(i);
    i += 1;
    target = i > N;
    goto *targets[target];
    end:
    printf("%f\n", value);

    return 0;
}
