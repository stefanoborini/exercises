int main(void) {
    unsigned char *dev_buffer;
    unsigned int *dev_histogram;

    cudaEvent_t start, stop;

    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    cudaEventRecord(start, 0);

    cudaMalloc( (void **)&dev_buffer, 1024*sizeof(unsigned char));
    cudaMemcpy( dev_buffer, buffer, 1024*sizeof(unsigned char), cudaMemcpyHostToDevice);

    cudaMalloc( (void **)&dev_histogram, 256*sizeof(unsigned int));
    cudaMemset( dev_histogram, 0, 256*sizeof(unsigned int));
    kernel<<<>>>()

