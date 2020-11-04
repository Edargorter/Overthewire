#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>


#define e(); if(((unsigned int)ptr & 0xff000000)==0xca000000) { setresuid(geteuid(), geteuid(), geteuid()); execlp("/bin/sh", "sh", "-i", NULL); }

void print(unsigned char *buf, int len)
{
        int i;

        printf("[ ");
        for(i=0; i < len; i++) printf("%x ", buf[i]); 
        printf(" ]\n");
}

int main()
{
        unsigned char buf[512];
        unsigned char *ptr = buf + (sizeof(buf)/2);
        unsigned int x;

        while((x = getchar()) != EOF) {
				printf("%hd\n", x);
                switch(x) {
                        case '\n': 
							print(buf, sizeof(buf)); 
							continue; 
							break;

                        case '\\': 
							printf("%hhn\n", ptr);
							ptr--; 
							break; 

                        default: 
							e(); 
							if(ptr > buf + sizeof(buf)) 
								continue; 
							ptr++[0] = x; 
							break;
                }
        }
        printf("All done\n");
}

/**
 
[ 0 0 0 0 1 0 0 0 a8 81 fd f7 0 d0 ff f7 3b 6d fe f7 0 c0 ff f7 0 10 0 0 1 0 0 0 fc 6c fe f7 0 d0 ff f7 0 0 0 0 18 d6 ff ff 4b 72 fe f7 f0 da ff f7 60 87 fd f7 1 0 0 0 1 0 0 0 0 0 0 0 8c 57 ff f7 0 0 0 0 0 0 0 0 5c d5 ff f7 e8 d5 ff ff 8 d6 ff ff 0 0 0 0 8c 57 ff f7 5c d5 ff f7 8 d6 ff ff ac c4 fd f7 dc c2 fd f7 3d 4f fe f7 61 60 e3 f7 ff 82 4 8 0 0 0 0 3c c3 fd f7 0 0 0 0 0 c0 fd f7 40 0 0 0 2 0 0 0 7d 82 4 8 24 dc ff f7 bc 26 e2 f7 0 d0 ff f7 c4 6c e2 f7 1 0 0 0 60 84 fd f7 94 56 fe f7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 60 84 fd f7 3 0 0 0 30 d6 ff ff 71 ea b1 7 2e 4e 3d f6 d4 6e e2 f7 34 fc e2 f7 b6 e ff f7 0 d0 ff f7 77 4 fe f7 5c d5 ff f7 f0 da ff f7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 d6 8 0 0 90 84 fd f7 a8 81 fd f7 d4 82 4 8 74 4 e3 f7 5c 82 4 8 1 0 0 0 0 0 2 0 86 30 ff f7 2 0 0 0 0 d0 ff f7 74 d7 ff ff f0 da ff f7 30 d7 ff ff 1a 59 fe f7 e0 d6 ff ff 5c 82 4 8 e8 d6 ff ff 94 da ff f7 0 0 0 0 90 84 fd f7 1 0 0 0 0 0 0 0 1 0 0 0 38 d9 ff f7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 21 0 0 0 9 0 0 0 4d 0 0 0 0 0 0 0 74 d7 ff ff e8 d6 ff ff e0 d6 ff ff d4 82 4 8 38 d9 ff f7 0 0 0 0 c2 0 0 0 0 91 eb f7 ff ff ff ff e d7 ff ff 34 fc e2 f7 e3 5f e5 f7 4d 0 0 0 7d 30 2c 0 1 0 0 0 a9 83 4 8 fd d8 ff ff 2f 0 0 0 0 a0 4 8 22 87 4 8 1 0 0 0 d4 d7 ff ff dc d7 ff ff 9d 61 e5 f7 c4 d3 fc f7 0 d0 ff f7 db 86 4 8  ]

**/
