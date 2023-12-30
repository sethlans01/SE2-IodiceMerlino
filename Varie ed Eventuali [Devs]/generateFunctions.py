lines = []
with open("input.txt","r") as file:
    lines = file.readlines()

state = 0
output = []

for line in lines:
    line = line.strip()
    match state:
        case 0:
            #function name
            if len(line) == 0:
                continue #emptry line
            else:
                output.append("\\textbf{"+line+"}\\\\\n")
                state = 1
        case 1:
            #function description
            if len(line) == 0:
                continue #emptry line
            else:
                output.append(line+"\\\\\n")
                state = 2
        case 2:
            #function params and returns
            if len(line) == 0:
                output.append("\\\\\n")
                state = 0
            else:
                values = line.split(":")
                print(values)
                output.append("\\textit{"+values[0]+"}:"+values[1]+"\\\\\n")

with open("output.txt","w") as file:
    file.writelines(output)