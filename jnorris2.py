#
import sys
x = 0
count = len(sys.argv)

if(count==1):
	prompt = "jsh: "
if(count==2):
	if(sys.argv[1]=="-"):
		prompt =""
	else:
		prompt = sys.argv[1] +":"

print(prompt)
for line in sys.stdin:
	if 'exit' == line.rstrip():
		break
	print(*line.split(),sep = "\n")
	print(prompt)
    

