#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

#define printF(x) write(1, x, strlen(x))

int mode_1(char **instructions, int size);
int mode_2(char **instructions, int size);
char** split_by_char(char *string, char split, int *size);

int main(int argc, char *argv[]){
	
	char **instructions=malloc(sizeof(char *));
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
				instructions[n]=malloc(p_buff+1);
				strcpy(instructions[n], buff);
				n++;
				instructions=realloc(instructions, (n+1)*sizeof(char *));
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
			printf("%d", mode_1(instructions, n));
			break;
		case 2:
			printf("%d", mode_2(instructions, n));
			break;
	}
	

	exit(1);
}

int mode_1(char **instructions, int size){
	int depth=0;
	int h_position=0;
	for(int i=0; i<size; i++){
		int size=0;
		char **l = split_by_char(instructions[i], ' ', &size);
		if(strcmp("forward", l[0])==0){
			h_position+=atoi(l[1]);
		}else if(strcmp("up", l[0])==0){
			depth-=atoi(l[1]);
		}else if(strcmp("down", l[0])==0){
			depth+=atoi(l[1]);
		}
	}
	return depth*h_position;
}

int mode_2(char **instructions, int size){
	int depth=0;
	int h_position=0;
	int aim=0;
	for(int i=0; i<size; i++){
		int size=0;
		char **l = split_by_char(instructions[i], ' ', &size);
		if(strcmp("forward", l[0])==0){
			h_position+=atoi(l[1]);
			depth+=aim*(atoi(l[1]));
		}else if(strcmp("up", l[0])==0){
			aim-=atoi(l[1]);
		}else if(strcmp("down", l[0])==0){
			aim+=atoi(l[1]);
		}
	}
	return depth*h_position;
}

char** split_by_char(char *string, char split, int *size){
	char **r=malloc(sizeof(char *));
	char *token=strtok(string, &split);
	*size=0;
	if(token!=NULL){
		while(token!=NULL){
			r[*size]=malloc(strlen(token)+1);
			strcpy(r[*size], token);
			(*size)++;
			r=realloc(r, ((*size)+1)*sizeof(char *));
			token=strtok(NULL, &split);
		}
	}
	return r;
}

