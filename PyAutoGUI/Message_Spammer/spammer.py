import pyautogui as pa
import time

#For sending the message
print("Starting....")
time.sleep(3)
p=10
n=p;
while(n!=0):
    pa.typewrite("I hate you");
    pa.press("enter")
    print(n)
    n=n-1;

print("Done");

#For finding the location of option,unsend and confirm
print("Go to position 1\n")
time.sleep(3)
mousex1,mousey1=pa.position()
print(mousex1,mousey1)
print("Go to position 2\n")
time.sleep(3)
mousex2,mousey2=pa.position()
print(mousex2,mousey2)
print("Go to position 3\n")
time.sleep(3)
mousex3,mousey3=pa.position()
print(mousex3,mousey3)

#For deleting the messages
#For some reason only the first iteration works. Mouse clicking isnt proper
print("Deleting")
time.sleep(5)
n=p
while(n!=0):
    time.sleep(2)
    pa.leftClick(mousex1,mousey1)
    time.sleep(1)
    pa.leftClick(mousex2,mousey2)
    time.sleep(1)
    pa.leftClick(mousex3,mousey3)
    time.sleep(1)
    n=n-1
print("Done")
