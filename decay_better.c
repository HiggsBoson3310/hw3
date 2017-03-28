#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float delta_n_step(float n, float lambda, float dt);
float *single_decay(float N0, float lambda, float dt);
 
int main(){

	float N_0 = 100.0;
	float Lambda = 1.0/2.0;
	float Dt = 0.001;
	int k=100,i,j;
	float t_total = 5.0/Lambda;
	int n_points = (int)t_total/Dt;
	float *av = malloc(sizeof(float)*n_points);
	float *l_i = malloc(sizeof(float)*n_points);
	
	srand48(1);
	
	for(i=0; i<k; i++){
		
		l_i = single_decay(N_0, Lambda, Dt);
		if(i==0){
			for(j=0; j<n_points;j++){
				av[j] = l_i[j]/k;
			}
		}
		else{
	
			for(j=0; j<n_points;j++){
				av[j] += l_i[j]/k;
			}
		}

	}
	
	for (i=0; i<n_points; i++){
		printf("%f %f \n",av[i],i*Dt);	
	}

	
		
	return 0;
}

float delta_n_step(float n, float lambda, float dt){
	
	float rand_num = drand48();
	if(rand_num < lambda*n*dt){
		return -1.0;
	} else {
		return 0.0;
	}
}
	
float *single_decay(float N0, float lambda, float dt){

	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = N0;
	
	float *list_numbers = malloc(sizeof(float)*n_points);	
	
	printf("%f %f\n", t, n);
	
	for(i=0;i<n_points;i++){
		
		list_numbers[i] = n;
		t += dt;
		float delta_n = delta_n_step(n, lambda, dt);
		n +=delta_n;
		printf("%f %f\n", t, n);		
	}
	return list_numbers;
}
