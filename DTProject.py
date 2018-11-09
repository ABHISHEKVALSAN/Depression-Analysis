import os
import traceback
fileMap={\
"q"         : "q_mainA.txt",\
"q0"        : "q_mainB.txt",\
"q1"        : "q_subtance.txt",\
"q10"       : "q_medical.txt",\
"q100"      : "q_menstrual.txt",\
"q1001"     : "q_PMDD.txt",\
"q1000"     : "q_8Sx.txt",\
"q10000"    : "q_2year.txt",\
"q100000"   : "q_2week.txt",\
"q100001"   : "q_PDDSx.txt",\
"a"         : "a_main.txt",\
"a11"       : "a_substance.txt",\
"a101"      : "a_medical.txt",\
"a10011"    : "a_PMDD.txt",\
"a1000011"  : "a_PDD.txt",\
"a1000010"  : "a_UD.txt",\
"a1000001"  : "a_ISx.txt",\
"a1000000"  : "a_UD.txt",\
"aend"      : "aend.txt",\
}
tMap = {\
"q"         : ["q0","q1"],\
"q0"        : ["a","q1"],\
"q1"        : ["q10","a11"],\
"q10"       : ["q100","a101"],\
"q100"      : ["q1000","q1001"],\
"q1001"     : ["q1000","a10011"],\
"q1000"     : ["q10000","aend"],\
"q10000"    : ["q100000","q100001"],\
"q100000"   : ["a1000000","a1000001"],\
"q100001"   : ["a1000010","a1000011"],\
}
def prompt(query):
    print(query)
    global fileMap
    filename=fileMap[query]
    f=open(filename,"r")
    for i in f:
        print(i[:-1])
def ask(query):
    global tMap
    print(query)
    os.system("clear")
    if query[0]=="a":
        print("########## Result of your diagnosis ############")
        prompt(query)
    elif query[0]=="q":
        prompt(query)
        while True:
            try:
                x=int(input())
                ask(tMap[query][x])
                break
            except:
                print("Enter Valid options!!!")
def main():
    ask("q")

if __name__=="__main__":
    main()
