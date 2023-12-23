lines = []
with open("input2.txt","r") as file:
    lines = file.readlines()

first = True
output = []

for line in lines:
    line = line.strip()
    if "textbf" in line:
        if first:
            first = False
        else:
            output.append(f"\\end{{itemize}}")
        subsub, title = line.split("}")
        output.append(subsub.replace("textbf","subsection")+"}")
        output.append(f"\\textbf{{{title.replace("\\","")}}}")
        output.append(f"\\begin{{itemize}}")
    elif len(line):
        output.append("\\item "+line)

output.append(f"\\end{{itemize}}")

with open("output2.txt","w") as file:
    file.write("\n".join(output))