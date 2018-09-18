#include <stdio.h>
int main(void) {
    cudaDeviceProp prop;
    int count, i;

    cudaGetDeviceCount(&count);
    
    for (i = 0; i < count; i++) {
        cudaGetDeviceProperties(&prop, i);
        printf("%s\n", prop.name);
        printf("%d\n", prop.canMapHostMemory);
        printf("%d\n", prop.deviceOverlap);
        printf("%d\n", prop.multiProcessorCount);
        printf("%d\n", prop.integrated);
        printf("%d\n", prop.clockRate);
    }
}
