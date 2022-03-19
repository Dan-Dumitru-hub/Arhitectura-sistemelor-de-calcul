#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
 
void BMMultiply(int n, double** a, double** b, double** c)
{
    int bi=0;
    int bj=0;
    int bk=0;
    int i=0;
    int j=0;
    int k=0;
    // TODO: set block dimension blockSize
    int blockSize=100; 
 
    for(bi=0; bi<n; bi+=blockSize)
        for(bj=0; bj<n; bj+=blockSize)
            for(bk=0; bk<n; bk+=blockSize)
                for(i=0; i<blockSize; i++)
                    for(j=0; j<blockSize; j++)
                        for(k=0; k<blockSize; k++)
                            c[bi+i][bj+j] += a[bi+i][bk+k]*b[bk+k][bj+j];
}
 
int main(void)
{
    int n;
    double** A;
    double** B;
    double** C;
    int numreps = 10;
    int i=0;
    int j=0;
    struct timeval tv1, tv2;
   // struct timezone tz;
    double elapsed;
    // TODO: set matrix dimension n
    n = 500;
    // allocate memory for the matrices
 
    // TODO: allocate matrices A, B & C
    ///////////////////// Matrix A //////////////////////////
    // TODO ...
    A=malloc(sizeof(double*)*n);

    if(!A){
        printf("errorA\n");
    return 0;}

    for(i=0;i<n;i++)
    {A[i]=malloc(sizeof(double)*n);

 if(!A[i]){
        printf("errorA%d\n",i);
    return 0;}
    }
    ///////////////////// Matrix B ////////////////////////// 
    // TODO ...
  B=malloc(sizeof(double*)*n);
  if(!B){
        printf("errorB\n");
    return 0;}

    for(i=0;i<n;i++)
    {B[i]=malloc(sizeof(double)*n);

 if(!B[i]){
        printf("errorB%d\n",i);
    return 0;}}
    ///////////////////// Matrix C //////////////////////////
    // TODO ...
  C=malloc(sizeof(double*)*n);
  if(!C){
        printf("errorC\n");
    return 0;}

    for(i=0;i<n;i++)
    {C[i]=malloc(sizeof(double)*n);

 if(!C[i]){
        printf("errorC%d\n",i);
    return 0;}}
    // Initialize matrices A & B
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            A[i][j] = 1;
            B[i][j] = 2;
        }
    }
 
    //multiply matrices
 
    printf("Multiply matrices %d times...\n", numreps);
    for (i=0; i<numreps; i++)
    {
        gettimeofday(&tv1, NULL);
        BMMultiply(n,A,B,C);
        gettimeofday(&tv2, NULL);
        elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
    }
    printf("Time = %lf \n",elapsed);
 
    //deallocate memory for matrices A, B & C
    // TODO ...
 
    return 0;
}