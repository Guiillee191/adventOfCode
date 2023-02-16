#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

#define printF(x) write(1, x, strlen(x))

typedef struct Carton{
	int nums[5][5];
}carton;

typedef struct Bingo{
	int *bolas;
	int num_bolas;
	carton *cartones;
	int num_cartones;
}bingo;

int mode_1(char **nums, int size);
int mode_2(char **nums, int size);
char** split_by_char(char *string, char split, int *size);


int main(int argc, char *argv[]){
	
	int n=0;
	bingo b;
	b.bolas = malloc(sizeof(int));
	b.cartones=malloc(sizeof(carton *));
	
	
	
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
		
		read(fd, &peak, 1);
		while(peak != '\n'){
			if(peak == ','){
				buff[p_buff]='\0';
				b.bolas[n]=atoi(buff);
				n++;
				b.bolas=realloc(b.bolas, (n+1)*sizeof(int *));
				p_buff=0;
				free(buff);
				buff = malloc(1);
			}else{
				buff[p_buff]=peak;
				p_buff++;
				buff=realloc(buff, p_buff+1);
			}
			read(fd, &peak, 1);
		}
		b.bolas[n]=atoi(buff);
		b.num_bolas=n;
		free(buff);
		
		read(fd, &peak, 1);
		n=0;
		p_buff=0;
		int k=0;
		char last_peak='a';
		char buff2[1000];
		while((read(fd, &peak, 1)) > 0){
			if(peak=='\n' && last_peak=='\n'){
				n++;
				k=0;
				b.cartones=realloc(b.cartones, (n+1)*sizeof(carton *));
			}else if(peak == '\n'){
				buff2[p_buff]='\0';
				sscanf(buff2, "%d %d %d %d %d", &b.cartones[n].nums[k][0], &b.cartones[n].nums[k][1], &b.cartones[n].nums[k][2], &b.cartones[n].nums[k][3], &b.cartones[n].nums[k][4]);
				k++;
				p_buff=0;
				//free(buff);
				//buff = malloc(1);
			}else{
				buff2[p_buff]=peak;
				p_buff++;
				//buff=realloc(buff, p_buff+1);
			}
			last_peak=peak;
		}
		close(fd);
	}
	/*
	switch(atoi(argv[2])){
		case 1:
			printf("Solution: %d\n", mode_1(nums, n));
			break;
		case 2:
			printf("Solution: %d\n", mode_2(nums, n));
			break;
	}*/
	exit(1);
}
