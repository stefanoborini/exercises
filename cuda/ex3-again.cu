#include <stdio.h>
#define N 10

__global__ void add(int *a, int * b, int *c) {
    c[blockIdx.x] = a[blockIdx.x] + b[blockIdx.x];
}

int main(void) {
    int a[N], b[N], c[N];
    int *dev_a, *dev_b, *dev_c;
    int i;

    printf("%d\n", cudaMalloc( (void **)&dev_a, sizeof(int)*N));
    cudaMalloc( (void **)&dev_b, sizeof(int)*N);
    cudaMalloc( (void **)&dev_c, sizeof(int)*N);
 
    for (i = 0; i < N; i++) {
        a[i] = i;
        b[i] = 2*i;
    } 
    
    cudaMemcpy(dev_a, a, N*sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(dev_b, b, N*sizeof(int), cudaMemcpyHostToDevice);

    add<<<N,1>>>(dev_a, dev_b, dev_c);
    
    cudaMemcpy(c, dev_c, N*sizeof(int), cudaMemcpyDeviceToHost);
  
    for (i = 0; i < N; i++) {
        printf("%d %d %d\n", a[i],b[i],c[i]);
    } 
     
    cudaFree((void *)dev_a);
    cudaFree((void *)dev_b);
    cudaFree((void *)dev_c);

}
