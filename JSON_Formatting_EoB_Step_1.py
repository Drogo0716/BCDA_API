import os

stack = []
quote = False
stop = False

# new = open('API_EoB(1)_Data_Formatted.json', 'w')
new = open('API_EoB_Data_03162021_MAR29(Formatted_Step1).json', 'w')
new.write('{"Patients": [\n')
#new.write('[\n')
with open('API_EoB_Data_03162021_MAR29(1).json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
        for char in line:
            if char == '{' and len(stack) < 1:
                new.write(char)
                stack.append('{')
                for x in range(len(stack)):
                    new.write('    ')
            elif char == '{':
                if quote:
                    new.write(char)
                else:
                    stack.append(char)
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write(char)
                    for x in range(len(stack) + 1):
                        new.write('    ')
            elif char == '}' and len(stack) == 1:
                if quote:
                    new.write(char)
                else:
                    new.write(char)
                    stack.pop()
                    stop = True
                    break
            elif char == '}':
                if quote:
                    new.write(char)
                else:
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write((char))
                    stack.pop()
            else:
                new.write(char)

f.close()

with open('API_EoB_Data_03162021_MAR29(2).json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
        for char in line:
            if char == '{' and len(stack) < 1:
                new.write(char)
                stack.append('{')
                for x in range(len(stack)):
                    new.write('    ')
            elif char == '{':
                if quote:
                    new.write(char)
                else:
                    stack.append(char)
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write(char)  # + '\n')
                    for x in range(len(stack) + 1):
                        new.write('    ')
            elif char == '}' and len(stack) == 1:
                if quote:
                    new.write(char)
                else:
                    new.write(char)
                    stack.pop()
                    stop = True
                    break
            elif char == '}':
                if quote:
                    new.write(char)
                else:
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write((char))  # + '\n')
                    stack.pop()
            else:
                new.write(char)

f.close()

with open('API_EoB_Data_03162021_MAR29(3).json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
            #break
        for char in line:
            if char == '{' and len(stack) < 1:
                new.write(char)  # + '\n')
                stack.append('{')
                for x in range(len(stack)):
                    new.write('    ')
            elif char == '{':
                if quote:
                    new.write(char)
                else:
                    stack.append(char)
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write(char)  # + '\n')
                    for x in range(len(stack) + 1):
                        new.write('    ')
            elif char == '}' and len(stack) == 1:
                if quote:
                    new.write(char)
                else:
                    new.write(char)# + ',')#('\n' + char + ',')
                    stack.pop()
                    stop = True
                    break
            elif char == '}':
                if quote:
                    new.write(char)
                else:
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write((char))  # + '\n')
                    stack.pop()
            else:
                new.write(char)

f.close()

with open('API_EoB_Data_03162021_MAR29(4).json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
            #break
        for char in line:
            if char == '{' and len(stack) < 1:
                new.write(char)  # + '\n')
                stack.append('{')
                for x in range(len(stack)):
                    new.write('    ')
            elif char == '{':
                if quote:
                    new.write(char)
                else:
                    stack.append(char)
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write(char)  # + '\n')
                    for x in range(len(stack) + 1):
                        new.write('    ')
            elif char == '}' and len(stack) == 1:
                if quote:
                    new.write(char)
                else:
                    new.write(char)# + ',')#('\n' + char + ',')
                    stack.pop()
                    stop = True
                    break
            elif char == '}':
                if quote:
                    new.write(char)
                else:
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write((char))  # + '\n')
                    stack.pop()
            else:
                new.write(char)

f.close()

with open('API_EoB_Data_03162021_MAR29(5).json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
            #break
        for char in line:
            if char == '{' and len(stack) < 1:
                new.write(char)  # + '\n')
                stack.append('{')
                for x in range(len(stack)):
                    new.write('    ')
            elif char == '{':
                if quote:
                    new.write(char)
                else:
                    stack.append(char)
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write(char)  # + '\n')
                    for x in range(len(stack) + 1):
                        new.write('    ')
            elif char == '}' and len(stack) == 1:
                if quote:
                    new.write(char)
                else:
                    new.write(char)
                    stack.pop()
                    stop = True
                    break
            elif char == '}':
                if quote:
                    new.write(char)
                else:
                    # new.write('\n')
                    for x in range(len(stack)):
                        new.write('    ')
                    new.write((char))  # + '\n')
                    stack.pop()
            else:
                new.write(char)

f.close()
new.write(']}')
new.close()

