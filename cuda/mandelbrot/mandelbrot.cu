#include <stdlib.h>
#include <stdio.h>

__device__ int mandelbrot_point(float x, float y) {

    int max_iteration = 1000;
    int iteration;
    float a,b, new_a, new_b;
    a = 0.0f;
    b = 0.0f;
    new_a =0.0f;
    new_b =0.0f;
    iteration = 0;
    while (a*a + b*b <= 3.0f && iteration < max_iteration) {
        new_a = a*a - b*b + x;
        new_b = 2.0f*a*b + y;
        a = new_a;
        b = new_b;
        iteration++;
    }
    
    return (iteration == max_iteration ? 255 : iteration*10 % 255);
}

__global__ void compute_mandelbrot(int *pixels) {
    float x_center = -1.0f;
    float y_center =  0.0f;
    float x,y;
    int value;

    x = (float)x_center + 4.0f * (float)((float)blockIdx.x-(float)gridDim.x/2.0f) /(float)gridDim.x;
    y = (float)y_center + 4.0f * (float)((float)blockIdx.y-(float)gridDim.y/2.0f) /(float)gridDim.y;

    value = mandelbrot_point(x,y);

    pixels[blockIdx.x*3+blockIdx.y*gridDim.x*3] = value;
    pixels[blockIdx.x*3+blockIdx.y*gridDim.x*3+1] = value;
    pixels[blockIdx.x*3+blockIdx.y*gridDim.x*3+2] = value;
}

void print_mandelbrot(int *pixels, int width, int height ) {
    int i,j;
    for (i = 0; i < width; i++) {
        for (j = 0; j < height; j++) {
            if (pixels[i*3+width*j*3] == 255) printf("*");
            else printf(" ");
        }
        printf("|\n");
    }
}


int main(void) {
    int *pixels_dev;
    int *pixels;

    int width = 100;
    int height = 100;
    cudaEvent_t start, stop;

    dim3 grid(width, height);
    float elapsed;

    cudaMalloc((void **)&pixels_dev, sizeof(int) * width * height * 3);
    pixels = (int *)malloc(width*height*3*sizeof(int));

    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start,0);

    compute_mandelbrot<<<grid,1>>>(pixels_dev);
    cudaMemcpy(pixels, pixels_dev, width * height* 3 * sizeof(int), cudaMemcpyDeviceToHost);
    cudaEventRecord(stop,0);
    cudaEventSynchronize(stop);
    

    cudaEventElapsedTime(&elapsed, start, stop);
    printf("time: %f\n", elapsed);

    cudaEventDestroy(start);
    cudaEventDestroy(stop);
    print_mandelbrot(pixels, width, height);
}


