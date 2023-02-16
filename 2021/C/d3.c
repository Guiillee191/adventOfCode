#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

#define printF(x) write(1, x, strlen(x))

int mode_1(char **nums, int size);
int mode_2(char **nums, int size);
char** split_by_char(char *string, char split, int *size);
char* oxygen(char **nums, int size, int p);
char* co2(char **nums, int size, int p);

int main(int argc, char *argv[]){
	
	char **nums=malloc(sizeof(char *));
	int n=0;
	
	if(argc!=3){
		printF("Num parametros incorrectos\n");
		exit(2);
	}
	if(atoi(argv[2])==0){
		printF("Segundo parametro incorrecto\n");
		exit(2);
	}
	
	int fd=open(argv[1], O_RDONLY);
	if(fd<0){
		printF("Error abriendo archivo\n");
		exit(2);
	}else{
		char peak;
		char *buff = malloc(1);
		int p_buff=0;
		
		
		while((read(fd, &peak, 1)) > 0){
			if(peak == '\n'){
				buff[p_buff]='\0';
				nums[n]=malloc(p_buff+1);
				strcpy(nums[n], buff);
				n++;
				nums=realloc(nums, (n+1)*sizeof(char *));
				p_buff=0;
				free(buff);
				buff = malloc(1);
			}else{
				buff[p_buff]=peak;
				p_buff++;
				buff=realloc(buff, p_buff+1);
			}
			
		}
		close(fd);
	}
	switch(atoi(argv[2])){
		case 1:
			printf("Solution: %d\n", mode_1(nums, n));
			break;
		case 2:
			printf("Solution: %d\n", mode_2(nums, n));
			break;
	}
	exit(1);
}

int mode_1(char **nums, int size){
	int ones=0;
	int zeros=0;
	unsigned long r=0;
	for(int i=0;i<12;i++){
		for(int j=0;j<size;j++){
			if(nums[j][i]=='0'){
				zeros++;
			}
			if(nums[j][i]=='1'){
				ones++;
			}
		}
		if(zeros<ones){
			r=r<<1;
			r++;
		}else{
			r=r<<1;
		}
		zeros=0;
		ones=0;
	}
	return r*((~r)&(0xFFF));
}

int mode_2(char **nums, int size){
	char *oxygen_char = oxygen(nums, size, 0);
	char *co2_char = co2(nums, size, 0);
	char *trash;
	
	printf("oxygen: %s, co2: %s\n", oxygen_char, co2_char); 
	return strtol(oxygen_char, &trash, 2)*strtol(co2_char, &trash, 2);
}

char* oxygen(char **nums, int size, int p){
	
	if(size==1){
		return *nums;
	}

	int ones=0;
	int zeros=0;
	char **one_list=malloc(sizeof(char *));
	char **zero_list=malloc(sizeof(char *));
	unsigned long r=0;
	char *tmp;
	
	
	for(int j=0;j<size;j++){
		if(nums[j][p]=='0'){
			zero_list[zeros]=malloc(strlen(nums[j])+1);
			strcpy(zero_list[zeros], nums[j]);
			zeros++;
			zero_list=realloc(zero_list, (zeros+1)*sizeof(char *));
		}
		if(nums[j][p]=='1'){
			one_list[ones]=malloc(strlen(nums[j])+1);
			strcpy(one_list[ones], nums[j]);
			ones++;
			one_list=realloc(one_list, (ones+1)*sizeof(char *));
		}
	}
	if(zeros>ones){
		tmp= oxygen(zero_list, zeros, p+1);
	}else{
		tmp= oxygen(one_list, ones, p+1);
	}
	free(zero_list);
	free(one_list);
	return tmp;
}

char* co2(char **nums, int size, int p){
	
	if(size==1){
		return *nums;
	}

	int ones=0;
	int zeros=0;
	char **one_list=malloc(sizeof(char *));
	char **zero_list=malloc(sizeof(char *));
	unsigned long r=0;
	char *tmp;
	
	for(int j=0;j<size;j++){
		if(nums[j][p]=='0'){
			zero_list[zeros]=malloc(strlen(nums[j])+1);
			strcpy(zero_list[zeros], nums[j]);
			zeros++;
			zero_list=realloc(zero_list, (zeros+1)*sizeof(char *));
		}
		if(nums[j][p]=='1'){
			one_list[ones]=malloc(strlen(nums[j])+1);
			strcpy(one_list[ones], nums[j]);
			ones++;
			one_list=realloc(one_list, (ones+1)*sizeof(char *));
		}
	}
	if(zeros>ones){
		tmp= co2(one_list, ones, p+1);
	}else{
		tmp= co2(zero_list, zeros, p+1);
	}
	free(zero_list);
	free(one_list);
	return tmp;
}
