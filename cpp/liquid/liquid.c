#include "shunting-yard.h"
#include <stdio.h>
#include <string.h>

int main(int agrc, char *argv[]){
	double result;
	char input[100];
	int i,j;
	while(1)
	{
		scanf("%s", input);
		if(strcmp(input,"Q")==0)
			break;
		
		for(i=0;input[i]!='\0';i++)
			if(input[i]==' ')
				for(j=i;input[j]!='\0';j++)
					input[j]=input[j+1];
		
    	Status response = shunting_yard(input, &result);
		printf(">> %f\n", result);
	}
	return 0;
}