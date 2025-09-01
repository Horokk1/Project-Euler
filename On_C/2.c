#include <stdio.h>
#define N 4000000

int main() {
    int result = 2;
    int current = 2;
    int previous = 1;
    int tmp;
    while (1) {
        tmp = current;
        current = previous + current;
        previous = tmp;
        if (current > N) {
            break;
        }
        if (current % 2 == 0) {
            result += current;
        }
    }

    printf("%d", result);

    return 0;
}
