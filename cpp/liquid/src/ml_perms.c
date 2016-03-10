#include "math-lib.h"

int ml_perms(int n1, int n2){
      
    
int s=1,n=1,k=1,i,j,a;

  for (j=1;j<=(n1-(n1-n2));j++)
     {
       s=s*n1;
       n1--;
     }

   return s;
}
