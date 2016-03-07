#include "shunting-yard.h"
#include <iostream>
#include <string>

using namespace std;

int main(int agrc, char *argv[]){
	string response;
	string input;

    cin>>input;
    double actual = calculator::calculate(input.c_str());

	cout<<": "<<actual<<endl;
}
