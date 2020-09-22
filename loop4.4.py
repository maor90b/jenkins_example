from time import sleep
import sys

if __name__=="__main__":
    inuser=int(sys.argv[1])
    for i in range(inuser):
    	print(i,i**3)
    	sleep(1)
