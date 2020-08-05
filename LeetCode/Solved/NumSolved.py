import fnmatch, os

dir = "C:/Users/Vested/PycharmProjects/python-practice/LeetCode/Solved/"

easyNum = len(fnmatch.filter(os.listdir(dir+"/Easy/"), '*.py'))
mediumNum = len(fnmatch.filter(os.listdir(dir+"/Medium/"), '*.py'))
hardNum = len(fnmatch.filter(os.listdir(dir+"/Hard/"), '*.py'))

print("Easy: " + str(easyNum))
print("Medium: " + str(mediumNum))
print("Hard: " + str(hardNum))
print("Total: " + str((easyNum + mediumNum + hardNum)))