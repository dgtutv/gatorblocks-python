import json
print("please enter classes in order from 1-1 to 2-4")
classes = []
for i in range(8):
    classes+=[str(input())]
with open('classes.txt', 'w') as filehandle:
    json.dump(classes, filehandle)
