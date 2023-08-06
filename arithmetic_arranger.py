def arithmetic_arranger(problems, solve = False):

  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""

  #Error handling:

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    parts = problem.split()

    try:
      n1 = int(parts[0])
      n2 = int(parts[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    op = parts[1]

    if op not in "-+":
      return "Error: Operator must be '+' or '-'."

    if len(str(n1)) > 4 or len(str(n2)) > 4:
      return "Error: Numbers cannot be more than four digits."

    if op == "+":
      total = str(n1 + n2)
    elif op == "-":
      total = str(n1 - n2)

  #Formatting:
    #calculate length of lines
    max_length = max(len(str(n1)), len(str(n2)))
    align = max_length + 2
    
    #add spaces to each line
    top = str(n1).rjust(align)
    middle = op + str(n2).rjust(align-1)
    bottom = str(total).rjust(align)
    
    
    #generate correct number of dashes below problem statement 
    line = ""
    for i in range(align):
      line += "-"
    
    #append answer if necessary
    if problem != problems[-1]:
      first += top + "    "
      second += middle + "    "
      lines += line + "    "
      sumx += bottom + "    "
    else: 
      first += top 
      second += middle 
      lines += line 
      sumx += bottom 

  if solve:
    string += first + "\n" + second + "\n" + lines + "\n" + sumx
  else: 
    string += first + "\n" + second + "\n" + lines + "\n"

  return string

problems = []

while True:
  problem = ""

  operator = input("Add(+), Subt(-), or Done?")
  if operator.lower() == "done":
    break
  nu1 = input("Enter the first number:")
  nu2 = input("Enter the second number:")

  problem += f"{nu1} {operator} {nu2}"

  problems.append(problem)

s = input("solve?")
if s == "yes":
  print(arithmetic_arranger(problems))
elif s == "no":
  print(arithmetic_arranger(problems, solve = True))