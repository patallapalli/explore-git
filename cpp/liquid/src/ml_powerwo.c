#include "math-lib.h"

double ml_power(int n1, int n2)
{
    result=n1;

    for(int i=0;i<n2;i++)
    {
        result*=n1;
    }

    return result;

}
