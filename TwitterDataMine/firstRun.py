import os

def firstRun(path):
    #check if file with keys exists
    if(os.path.isfile(path)):
        return True
    else:
        print("File does not exist. Please enter Twitter keys.")
        ck = input("consumer key> ")
        cs = input("consumer secret> ")
        at = input("access token> ")
        ats = input("access secret> ")

        f = open(path,'w')
        f.write(ck+"\n")
        f.write(cs+"\n")
        f.write(at+"\n")
        f.write(ats+"\n")

    #if not create one and ask for keys
    

   
