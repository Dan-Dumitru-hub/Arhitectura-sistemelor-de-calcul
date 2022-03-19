
#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdint.h>     
#include <stdlib.h>
#include <time.h>



int main(int argc, char* argv[])
{

int i,j,k;
int N=500;//daca il fac mai mare imi da segfault
double c[N][N],a[N][N],b[N][N];

srand(time(NULL));

for(i=0;i<N;i++){
double *ptr=&(a[i][0]); // 2 adunari si o inmultire
for (j=0;j<N;j++) {
   *ptr = rand();                
   ptr++;               // N adunari in numere intregi
}}

for(i=0;i<N;i++){
double *ptr=&(b[i][0]); // 2 adunari si o inmultire
for (j=0;j<N;j++) {
   *ptr = rand();                
   ptr++;               // N adunari in numere intregi
}}


time_t now = time(0);


 clock_t timpInitial, timpFinal ;
  timpInitial = clock() ;



for(int x=0;x<10;x++){
    for(i = 0; i < N; i++){
  double *orig_pa = &a[i][0];
  for(j = 0; j < N; j++){
    double *pa = orig_pa;
    double *pb = &b[0][j];
    register double suma = 0;
    for(k = 0; k < N; k++){
      suma += *pa * *pb;
      pa++;
      pb += N;
    }
    c[i][j] = suma;
  }
}}
   timpFinal = clock() ;
  printf("dif ijk=%ld",(timpFinal-timpInitial)/ CLOCKS_PER_SEC);

now = time(0);
for(int x=0;x<10;x++){
    for(k = 0; i < N; i++){
  double *orig_pa = &a[i][0];
  for(i = 0; j < N; j++){
    double *pa = orig_pa;
    double *pb = &b[0][j];
    register double suma = 0;
    for(j = 0; k < N; k++){
      suma += *pa * *pb;
      pa++;
      pb += N;
    }
    c[i][j] = suma;
  }
}}
  
  printf("\ndif kij=%ld",time(0)-now);


now = time(0);
for(int x=0;x<10;x++){
    for(i = 0; i < N; i++){
  double *orig_pa = &a[i][0];
  for(k = 0; j < N; j++){
    double *pa = orig_pa;
    double *pb = &b[0][j];
    register double suma = 0;
    for(j = 0; k < N; k++){
      suma += *pa * *pb;
      pa++;
      pb += N;
    }
    c[i][j] = suma;
  }
}}
  
  printf("\ndif ikj=%ld",time(0)-now);





    return 0;
}

