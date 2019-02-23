# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:00:41 2018

@author: sakib
"""
from math import ceil, log
import numpy
import matplotlib.pyplot as plt
import time
from threading import Thread
global resultParallel
resultParallel=[]

class MultiplyThread(Thread):
    def __init__(self,q, r, total_N, mat_one, mat_two):
        Thread.__init__(self)
        self.q=q
        self.r=r
        self.total_N=total_N
        self.mat_one=mat_one
        self.mat_two=mat_two
#        print(mat_one, mat_two)
    def run(self):
#        print("hi")
        global resultparallel
        for i in range(int(self.q),int(self.r)):
            for j in range(int(self.total_N)):
                for k in range(int(self.total_N)):
                    resultParallel[i][j]+=self.mat_one[i][k]*self.mat_two[k][j]
#                    print("hello")
#                    print(resultParallel[i][j])
           
    
def parallelMatrixMultiply(mat_one, mat_two):
    
    n=len(mat_one)
    total_N=n
    global resultParallel
    resultParallel=[[0 for i in range(n)] for j in range(n)]
    half=int(n/2)
#    print(half)
    resultParallel[0][0]=1
    threadOne=MultiplyThread(0,half,total_N, mat_one, mat_two)
    threadTwo=MultiplyThread(half,n,total_N, mat_one, mat_two)
    threadOne.start()
    threadTwo.start()
    threadOne.join()
    threadTwo.join()
    
    return resultParallel
    
    
    
def graphCreate(filePath):
    listA=[] 
    listB=[]
    file=open(filePath, "r")
    for line in file:
        number_strings=line.split()
        i=0
        for n in number_strings:
            if i%2==0:
                listA.append(int(n))
            else:
                listB.append(int(n))
            i+=1
    file.close()
#    print(listA)
#    print(listB)
    plt.plot(listA, listB)
    plt.show()
    
def readfile(filename):
    mat_one=[]
    file = open(filename, "r")
    #print(numberLines)
    for line in file:
        number_strings=line.split()
        numbers=[int(n) for n in number_strings]
        mat_one.append(numbers)
    file.close()
    return mat_one

def writeFile(filename, variable):
    file = open(filename, "a")
    file.write(str(variable))
    file.close()
    
def appendFile(filename, variable):
    file = open(filename, "a")
    file.write(str(variable))
    file.close()
        

 #naive_matrix_multiplication       
def naiveMatrixMultiplication(mat_one, mat_two):
    n = len(mat_one)
    result=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat_one[i][k] * mat_two[k][j]
    return result

#adding_two_matrix   
def addTwoMatrix(mat_one, mat_two):
    n = len(mat_one)
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = mat_one[i][j] + mat_two[i][j]
    return result

#subtracting_two_matrix
def subTwoMatrix(mat_one, mat_two):
    n = len(mat_one)
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = mat_one[i][j] - mat_two[i][j]
    return result

def strassenCalc(mat_one, mat_two):
    n=len(mat_one)
    if n <2:
        return naiveMatrixMultiplication(mat_one, mat_two)
    
    half_n=int(n/2)
    
    mat_one11 = [[0 for j in range(half_n)] for i in range(half_n)]
    mat_one12 = [[0 for j in range(half_n)] for i in range(half_n)]
    mat_one21 = [[0 for j in range(half_n)] for i in range(half_n)]
    mat_one22 = [[0 for j in range(half_n)] for i in range(half_n)]

    mat_two11 = [[0 for j in range(half_n)] for i in range(half_n)]
    mat_two12 = [[0 for j in range(half_n)] for i in range(half_n)]
    mat_two21 = [[0 for j in range(half_n)] for i in range(half_n)]
    mat_two22 = [[0 for j in range(half_n)] for i in range(half_n)]

    resultMatOne = [[0 for j in range(half_n)] for i in range(half_n)]
    resultMatTwo = [[0 for j in range(half_n)] for i in range(half_n)]
    
    for i in range(half_n):
        for j in range(half_n):
            mat_one11[i][j] = mat_one[i][j]            
            mat_one12[i][j] = mat_one[i][j + half_n]   
            mat_one21[i][j] = mat_one[i + half_n][j]    
            mat_one22[i][j] = mat_one[i + half_n][j +half_n] 

            mat_two11[i][j] = mat_two[i][j]           
            mat_two12[i][j] = mat_two[i][j + half_n]   
            mat_two21[i][j] = mat_two[i + half_n][j]    
            mat_two22[i][j] = mat_two[i + half_n][j + half_n] 
                
    #  m1 to m7:
    resultMatOne = addTwoMatrix(mat_one11, mat_one22)
    resultMatTwo = addTwoMatrix(mat_two11, mat_two22)
    m1 = strassenCalc(resultMatOne,resultMatTwo) 
    resultMatOne = addTwoMatrix(mat_one21, mat_one22)      
    m2 = strassenCalc(resultMatOne, mat_two11) 

    resultMatTwo = subTwoMatrix(mat_two12, mat_two22) 
    m3 = strassenCalc(mat_one11, resultMatTwo) 

    resultMatTwo = subTwoMatrix(mat_two21, mat_two11)
    m4 =strassenCalc(mat_one22, resultMatTwo) 
    
    resultMatOne =addTwoMatrix(mat_one11, mat_one12)     
    m5 = strassenCalc(resultMatOne, mat_two22) 

    resultMatOne = subTwoMatrix(mat_one21, mat_one11) 
    resultMatTwo = addTwoMatrix(mat_two11, mat_two12)     
    m6 = strassenCalc(resultMatOne, resultMatTwo) 

    resultMatOne = subTwoMatrix(mat_one12, mat_one22)
    resultMatTwo = addTwoMatrix(mat_two21, mat_two22)     
    m7 = strassenCalc(resultMatOne, resultMatTwo) 

    
    c12 =addTwoMatrix(m3, m5) 
    c21 = addTwoMatrix(m2, m4) 

    resultMatOne = addTwoMatrix(m1, m4) 
    resultMatTwo = addTwoMatrix(resultMatOne, m7) 
    c11 = subTwoMatrix(resultMatTwo, m5)

    resultMatOne =addTwoMatrix(m1, m3)
    resultMatTwo = addTwoMatrix(resultMatOne, m6) 
    c22 = subTwoMatrix(resultMatTwo, m2) 

    #merge
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(half_n):
        for j in range(half_n):
            result[i][j] = c11[i][j]
            result[i][j + half_n] = c12[i][j]
            result[i + half_n][j] = c21[i][j]
            result[i + half_n][j + half_n] = c22[i][j]
    return result

def strassen(mat_one, mat_two):
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(mat_one)
    m = nextPowerOfTwo(n)
    matOneP = [[0 for i in range(m)] for j in range(m)]
    matTwoP = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            matOneP[i][j] = mat_one[i][j]
            matTwoP[i][j] = mat_two[i][j]
    resultP = strassenCalc(matOneP, matTwoP)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = resultP[i][j]
    return result

    
    
def main():
    #print("Hi")
    filenameNTimeNaive="C:/Users/sakib/.spyder-py3/outputfolder/n_vs_time_naive.txt"
    filenameNTimeStrassen="C:/Users/sakib/.spyder-py3/outputfolder/n_vs_time_strassen.txt"
    filenameNTimeParallel="C:/Users/sakib/.spyder-py3/outputfolder/n_vs_time_parallel.txt"
    filenameWrite ="C:/Users/sakib/.spyder-py3/outputfolder/result.txt"
    for i in range(1,11,1):
        pow_i=2**i
        print(pow_i)
        
        filenameMatOne="C:/Users/sakib/.spyder-py3/inputfolder/mat_one_"+str(pow_i)+".txt"
        filenameMatTwo="C:/Users/sakib/.spyder-py3/inputfolder/mat_two_"+str(pow_i)+".txt"
        
        mat_one=readfile(filenameMatOne)
        mat_two=readfile(filenameMatTwo)
#        print("matrixOne:")
#        print_matrix(mat_one)
#        
#        print("matrixTwo:")
#        print_matrix(mat_two)
        
        
        
        #naive
        start_time_naive = time.perf_counter_ns()
        result=naiveMatrixMultiplication(mat_one, mat_two)
        process_time_naive = time.perf_counter_ns()-start_time_naive
        
        textToWrite = "Proces for time of naive matrix multiplication "+str(pow_i)+"*"+str(pow_i)+": "+str(process_time_naive)+"ns\n"
        appendFile(filenameWrite,textToWrite)
        
#        print("Resultant_Matrix_Naive")
#        print_matrix(result)
        
        time_n_text=str(pow_i)+" "+str(process_time_naive)+"\n"
        appendFile(filenameNTimeNaive,time_n_text)
        
        
        #strassen
        start_time_strassen = time.perf_counter_ns()
        strassenMat=strassen(mat_one, mat_two)
        process_time_strassen = time.perf_counter_ns()-start_time_strassen
        
        textToWrite2 = "Proces time of strassen's matrix multiplication: "+str(pow_i)+"*"+str(pow_i)+": "+str(process_time_strassen)+"ns\n"
        appendFile(filenameWrite,textToWrite2)
        
        time_n_text=str(pow_i)+" "+str(process_time_strassen)+"\n"
        appendFile(filenameNTimeStrassen,time_n_text)
         
#        print("Resultant_Matrix_Strassen")
#        print(strassenMat)
        
        
        
        
        #parallel
        start_time_parallel = time.perf_counter_ns()
        pr=parallelMatrixMultiply(mat_one, mat_two)
        process_time_parallel = time.perf_counter_ns()-start_time_parallel
        
        textToWrite3 = "Proces time of parallel matrix multiplication: "+str(pow_i)+"*"+str(pow_i)+": "+str(process_time_parallel)+"ns\n"
        appendFile(filenameWrite,textToWrite3)
        
        time_n_text=str(pow_i)+" "+str(process_time_parallel)+"\n"
        appendFile(filenameNTimeParallel,time_n_text)
#        print("parallel")
#        print(pr)
#        print("Resultant_Matrix_Parallel")
#        print(resultNumpy)
        #dfifferences
        diff_naiv_strassen=process_time_naive-process_time_strassen
        diff_naiv_parallel=process_time_naive-process_time_parallel
#        print(diff_naiv_strassen)
        textToDiff="Difference between Naive and Strassen's: "+str(diff_naiv_strassen)+"\n"+"Difference between Naive and Parallel: "+str(diff_naiv_parallel)+"\n"
        appendFile(filenameWrite, textToDiff)
        print(pow_i)
    #naiveNvsTime
    print("N vs Time Graph for Naive Solution:")
    graphCreate(filenameNTimeNaive)
    #Stressen
    print("N vs Time Graph for Strassen's Solution:")
    graphCreate(filenameNTimeStrassen)
    
    print("N vs Time Graph for Parallel Solution:")
    graphCreate(filenameNTimeParallel)
    
    
    
if __name__ == "__main__":
    main()
    
    