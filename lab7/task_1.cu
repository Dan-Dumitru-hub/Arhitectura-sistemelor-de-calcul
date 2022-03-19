#include <stdio.h>
#include "utils/utils.h"

// ~TODO 3~
// Modify the kernel below such as each element of the 
// array will be now equal to 0 if it is an even number
// or 1, if it is an odd number
__global__ void kernel_parity_id(int *a, int N) {
    unsigned int i = threadIdx.x + blockDim.x * blockIdx.x;

    // Avoid accessing out of bounds elements
    printf("aici %d i %d ai",i,a[i]);
    if(i<N)
    if (a[i] %2) 
        
        a[i]=1;
    
    else 
    a[i]=0;

}

// ~TODO 4~
// Modify the kernel below such as each element will
// be equal to the BLOCK ID this computation takes
// place.
__global__ void kernel_block_id(int *a, int N) {
unsigned int i = threadIdx.x + blockDim.x * blockIdx.x;

a[i]=i / blockDim.x; 





}

// ~TODO 5~
// Modify the kernel below such as each element will
// be equal to the THREAD ID this computation takes
// place.
__global__ void kernel_thread_id(int *a, int N) {
unsigned int i = threadIdx.x + blockDim.x * blockIdx.x;

a[i]=threadIdx.x; 

}

int main(void) {
    int nDevices;

    // Get the number of CUDA-capable GPU(s)
    cudaGetDeviceCount(&nDevices);

    // ~TODO 1~
    // For each device, show some details in the format below, 
    // then set as active device the first one (assuming there
    // is at least CUDA-capable device). Pay attention to the
    // type of the fields in the cudaDeviceProp structure.
    //
    // Device number: <i>
    //      Device name: <name>
    //      Total memory: <mem>
    //      Memory Clock Rate (KHz): <mcr>
    //      Memory Bus Width (bits): <mbw>
    // 
    // Hint: look for cudaGetDeviceProperties and cudaSetDevice in
    // the Cuda Toolkit Documentation. 
    for (int i = 0; i < nDevices; ++i) {
    cudaDeviceProp prop;
    cudaGetDeviceProperties(&prop, i);
    printf("Device Number: %d\n", i);
    printf("  Device name: %s\n", prop.name);
    printf("  Memory Clock Rate (KHz): %d\n",
           prop.memoryClockRate);
    printf("  Memory Bus Width (bits): %d\n",
           prop.memoryBusWidth);
    printf("  Peak Memory Bandwidth (GB/s): %f\n\n",
           2.0*prop.memoryClockRate*(prop.memoryBusWidth/8)/1.0e6);
  }
    

    // ~TODO 2~
    // With information from example_2.cu, allocate an array with
    // integers (where a[i] = i). Then, modify the three kernels
    // above and execute them using 4 blocks, each with 4 threads.
    // Hint: num_elements = block_size * block_no (see example_2)
    //
    // You can use the fill_array_int(int *a, int n) function (from utils)
    // to fill your array as many times you want.
    const size_t block_size = 4;
    const int num_elements =4 *4;


    int *host_array=0;
    int *device_array_a = 0;


    const int num_bytes = num_elements * sizeof(int);
    cudaMalloc((void **) &device_array_a, num_bytes);
    host_array = (int *) malloc(num_bytes);



for (int i = 0; i < num_elements; ++i) {
        host_array[i] =  i;
    }
size_t blocks_no = num_elements / block_size;


  cudaMemcpy(device_array_a, host_array, num_bytes, cudaMemcpyHostToDevice);



    // ~TODO 3~
    // Execute kernel_parity_id kernel and then copy from 
    // the device to the host; call cudaDeviceSynchronize()
    // after a kernel execution for safety purposes.
    //
    // Uncomment the line below to check your results

kernel_parity_id<<<blocks_no, block_size>>>(device_array_a ,num_elements );
cudaMemcpy(host_array, device_array_a, num_bytes, cudaMemcpyDeviceToHost);
    check_task_1(3, host_array); 

    // ~TODO 4~
    // Execute kernel_block_id kernel and then copy from 
    // the device to the host;
    //
    // Uncomment the line below to check your results





kernel_block_id<<<blocks_no, block_size>>>(device_array_a ,num_elements );
cudaMemcpy(host_array, device_array_a, num_bytes, cudaMemcpyDeviceToHost);
    check_task_1(4, host_array); 

    // ~TODO 5~
    // Execute kernel_thread_id kernel and then copy from 
    // the device to the host;
    //
    // Uncomment the line below to check your results

kernel_thread_id<<<blocks_no, block_size>>>(device_array_a ,num_elements );
cudaMemcpy(host_array, device_array_a, num_bytes, cudaMemcpyDeviceToHost);
    check_task_1(5, host_array); 

    // TODO 6: Free the memory
    free(host_array);
    
    cudaFree(device_array_a);
    
    return 0;
}