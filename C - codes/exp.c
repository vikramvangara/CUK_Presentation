#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

float a,b;
float a1,b1;
int main()

{
int c,len;
float p,q;
double **V,**P,**theta;

c = 16;
len = 100;
V = loadtxt("./data/V.dat",2,2);
P = loadtxt("./data/P.dat",2,1);

a = sqrt(c/V[0][0]);
b = sqrt(c/V[1][1]);

printf("The value of a is %lf\n",a);
printf("The value of b is %lf\n",b);


p = 1/pow(P[0][0],2);
q = 1 - (16*p);

a1=sqrt(1/p);
b1=sqrt(1/q);

printf("The value of p = %lf\n",p);
printf("The value of q = %lf\n",q);

theta = linspace(0,2*M_PI,len);
savetxt(theta,"theta.dat",len,1);

save_a();
save_b();
save_a1();
save_b1();
save_pa();
save_pb();
save_pc();
save_pd();

return 0;
}
void save_a(){
    FILE * fptr;
    fptr = fopen("./data/a.dat","w");
    fprintf(fptr,"%lf",a);
    fclose(fptr);
}
void save_b(){
    FILE * fptr;
    fptr = fopen("./data/b.dat","w");
    fprintf(fptr,"%lf",b);
    fclose(fptr);
}
void save_a1(){
    FILE * fptr;
    fptr = fopen("./data/a1.dat","w");
    fprintf(fptr,"%lf",a1);
    fclose(fptr);
}
void save_b1(){
    FILE * fptr;
    fptr = fopen("./data/b1.dat","w");
    fprintf(fptr,"%lf",b1);
    fclose(fptr);
}
void save_pa(){
    FILE * fptr;
    fptr = fopen("./data/pa.dat","w");
    fprintf(fptr,"%lf",a);
    fprintf(fptr,"\n");
    fprintf(fptr,"%lf",b);
    fclose(fptr);
}
void save_pb(){
    FILE * fptr;
    fptr = fopen("./data/pb.dat","w");
    fprintf(fptr,"%lf",-a);
    fprintf(fptr,"\n");
    fprintf(fptr,"%lf",b);
    fclose(fptr);
}
void save_pc(){
    FILE * fptr;
    fptr = fopen("./data/pc.dat","w");
    fprintf(fptr,"%lf",-a);
    fprintf(fptr,"\n");
    fprintf(fptr,"%lf",-b);
    fclose(fptr);
}
void save_pd(){
    FILE * fptr;
    fptr = fopen("./data/pd.dat","w");
    fprintf(fptr,"%lf",a);
    fprintf(fptr,"\n");
    fprintf(fptr,"%lf",-b);
    fclose(fptr);
}


