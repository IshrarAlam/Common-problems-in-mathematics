from collections import defaultdict
def freqQuery(queries):
    output_array=[]
    wd=defaultdict(int)
    fd=defaultdict(int)
    for command,value in queries:
        if command==1:
            fd[wd[value]]=max(0,fd[wd[value]]-1)
            wd[value]+=1
            fd[wd[value]]+=1
            #print(dict(wd),dict(fd))
        elif command==2:
            if wd[value]:
                fd[wd[value]]=max(0,fd[wd[value]]-1)
                wd[value]=max(0,wd[value]-1)
                fd[wd[value]]+=1
           # print(dict(wd),dict(fd))
        else:
            if fd[value]:
                output_array.append(1)
            else:
                output_array.append(0)
           # print(dict(wd),dict(fd)) 
    return output_array

if __name__ == '__main__':
    testcase=open("test case.txt")
    cases=testcase.readlines()
    queries = []
    for case in cases:
        queries.append(list(map(int, case.strip().split())))
    ans = freqQuery(queries)
    solution=open("solution.txt")
    sol=solution.readlines()
    expected=[]
    for s in sol:
        expected.append((int(s.strip())))
    print(ans==expected)
