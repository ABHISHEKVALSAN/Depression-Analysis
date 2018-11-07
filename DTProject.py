import os
import traceback
fileMap={\
"q"     : "q_mainA.txt",\
"q0"    : "q_mainB.txt",\
"q1"    : "q_subtance.txt",\
"q10"   : "q_medical.txt",\
"q100"  : "q_menstrual.txt",\
"a"     : "a_main.txt",\
"a11"   : "a_substance.txt",\
"a101"  : "a_medical.txt",\
"aend"  : "aend.txt"
}
tMap = {\
"q"         : ["q0","q1"],\
"q0"        : ["a","q1"],\
"q1"        : ["q10","a11"],\
"q10"       : ["q100","a101"],\
"q100"      : ["aend","aend"],\
}
def prompt(query):
    global fileMap
    filename=fileMap[query]
    f=open(filename,"r")
    for i in f:
        print(i)
def ask(query):
    global tMap
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
