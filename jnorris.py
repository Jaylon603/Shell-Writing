#prompt the user for a line of input, split that input into words and print them out separately, and then repeat until the user types the line "exit" or EOF is received.
import sys
x = 0
for line in sys.stdin:
	if 'exit' == line.rstrip():
		break
	print(*line.split(),sep = "\n")
    
print("Exit succesful")
