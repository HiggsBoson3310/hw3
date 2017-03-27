#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define PI 3.14159
int main(void){
	int a=1;
	int b=2;
	if(a>b){
		printf("a is greater tha b: a=%d, b=%d\n", a,b);
	}
	a=1;
	b=1;
	if(a<b){
		printf("b is greater tha b: a=%d, b=%d\n", a,b);	
	}
	else{
		printf("a is equal or grater than b \n");
	}
	printf("A loop with do-while structure\n");
	a=0;
	b=10;
	do{
		printf("a=%d, b=%d\n",a,b);
		a++;
	} while(a<b);
	return 0;
/*
	
	char name[256];
	char lastname[256];
	char fullname[256];
	int year;
	printf("Garbage in string name %s\n",name);
	printf("Garbage in string lastname %s\n",lastname);
	strcpy(name,"George");
	strcpy(lastname,"Gershwin");
	printf("After inialization: %s %s\n",name, lastname);
	year = 1965;
	sprintf(fullname, "%s, %s; Born %d", lastname, name, year);
	printf("Final string: %s\n", fullname);


	int i;
	int *array_int;
	int n_points = 10;
	array_int = malloc(n_points * sizeof(int));
	if(!array_int){
		printf("There is something wrong with the code\n");		
		exit(1);	
	}
	printf("Memory starts at %p\n", array_int);
	printf("Allocation went OK. Initializing...\n");
	for(i=0;i<n_points;i++){
		array_int[i] = i*2;
		printf("%d\n",array_int[i]);
	}
	printf("Let's see what happens if I go beyond the allocated space...\n");
	array_int[n_points] = n_points*2;
	printf("%d\n", array_int[n_points]);
	printf("OK.");
	printf("and if I go far away?\n");
	array_int[n_points*10000] = n_points*10000*2;
	printf("%d\n",array_int[n_points*10000]);
	

	int list[10];
	int i;
	printf("Content b4 initialization\n");
	for(i=0;i<10;i++){
		printf("%d\n",list[i]);
	}
	for(i=0;i<10;i++){
		list[i] = i*2;
	}
	printf("Content after initialization\n");
	for(i=0;i<10;i++){
		printf("%d\n",list[i]);
	}	
	
	int i;
	float radius;
	float volume;
	float surface;
	radius = 0.0;
	volume = 0.0;
	surface = 0.0;
	printf("Radius Surface Volume\n");
	for(i=0; i<12 ; i++){
		radius = i;
		surface = 4.0*PI*pow(radius,2.0);
		volume = (radius*surface)/3.0;
		printf("%f %f %f\n", radius, surface, volume);
	}

	char s[100] = "La respuesta es: ";
	int i = 42;
	float x = 42.0;
	double y = 42.0;
	printf("%s %d %f %e\n",s,i,x,y);	


	int a,b,c;
	float d,e,f;
	a = 1;
	b = 10;
	c = pow(a,b);
	d = 1.0;
	e = 10.0;
	f = pow(e,f);
	printf("%d %d %d \n",a,b,c);
	printf("%f %f %f \n",d,e,f);
	return 0;*/
}
