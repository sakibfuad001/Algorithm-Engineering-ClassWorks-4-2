import numpy
import random


def fileWrite(filepath1, filepath2, n):
    file1=open(filepath1, "w+")
    file2=open(filepath2, "w+")
    for j in range(n):
        for k in range(n):
            item1=str(random.randint(0,1000000))+" "
            file1.write(str(item1))
            
            item2=str(random.randint(0,1000000))+" "
            file2.write(str(item2))
        file1.write("\n")
        file2.write("\n")
    file1.close()
    file2.close()
    
def main():
    n=int(input("Enter N: "))
    for i in range(1,n,1):
        pow_i=2**i
        filepath1="C:/Users/sakib/.spyder-py3/inputfolder/mat_one_"+str(pow_i)+".txt"
        filepath2="C:/Users/sakib/.spyder-py3/inputfolder/mat_two_"+str(pow_i)+".txt"
        #numpy.random.random((i,i))
        #list=[[random.random() for j in range(i)] for k in range(i)]
        fileWrite(filepath1,filepath2, pow_i)
        
if __name__=="__main__":
    main()