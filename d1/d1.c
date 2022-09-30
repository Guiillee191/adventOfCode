#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

#define printF(x) write(1, x, strlen(x))

int main(int argc, char *argv[]){
	
	int *depth=malloc(sizeof(int));
	int n=0;
	
	if(argc!=2){
		printF("Num parametros incorrectos\n");
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
	
	int c=0;
	for(int i=1;i<n;i++){
		//printf("%d\n", depth[i]);
		if(depth[i-1]<depth[i]){
			c++;
		}
	}
	printf("%d\n", c);

//exit(1);
}
