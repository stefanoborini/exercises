#include <stdio.h>

#define N 10000
__global__ void add(int **a, int **b, int **c) {
    int x = blockIdx.x;
    int y = blockIdx.y;
    c[x*gridDim.x] = a[x][y] + b[x][y];
}
int main(void) {
    int a[N][N], b[N][N], c[N][N];
    int **dev_a, **dev_b, **dev_c;

    cudaMalloc( (void ***) &dev_a, N*N*sizeof(int));
    cudaMalloc( (void ***) &dev_b, N*N*sizeof(int));
    cudaMalloc( (void ***) &dev_c, N*N*sizeof(int));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            a[i][j] = i*j;
            b[i][j] = i*j;
        }
    }

    cudaMemcpy( dev_a, a, N*N*sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy( dev_b, b, N*N*sizeof(int), cudaMemcpyHostToDevice);
    
    dim3 grid(N,N);
    add<<<grid,1>>>(dev_a,dev_b,dev_c);
    
    cudaMemcpy(c, dev_c, N*N*sizeof(int), cudaMemcpyDeviceToHost);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf ("%d + %d = %d\n", a[i][j], b[i][j], c[i][j]);
        }
    }

    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_c);

    return 0;
}
