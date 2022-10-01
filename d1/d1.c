#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

#define printF(x) write(1, x, strlen(x))

int mode_1(int **depth, int size);

int mode_2(int **depth, int size);

int main(int argc, char *argv[]){
	
	int *depth=malloc(sizeof(int));
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
				depth[n]=atoi(buff);
				n++;
				depth=realloc(depth, (n+1)*sizeof(int));
				p_buff=0;
				free(buff);
				buff = malloc(1);
			}else{
				buff=realloc(buff, p_buff+2);
				buff[p_buff]=peak;
				p_buff++;
			}
			
		}
		close(fd);
	}
	switch(atoi(argv[2])){
		case 1:
			mode_1(&depth, n);
			break;
		case 2:
			mode_2(&depth, n);
			break;
	}
	

	exit(1);
}

int mode_1(int **depth, int size){
	int c=0;
	for(int i=1;i<size;i++){
		if((*depth)[i-1]<(*depth)[i]){
			c++;
		}
	}
	printf("%d\n", c);
}

int mode_2(int **depth, int size){
	int c=0;
	for(int i=3;i<size;i++){
		if(((*depth)[i-3]+(*depth)[i-2]+(*depth)[i-1])<((*depth)[i-2]+(*depth)[i-1]+(*depth)[i])){
			c++;
		}
	}
	printf("%d\n", c);
}

