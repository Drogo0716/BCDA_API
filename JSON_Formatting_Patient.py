# Denver Hancock
# February 1, 2021
# Phynet Health Systems
# This program reads the separate records from the Patient JSON then writes them to a new file in the correct format
#######################################################################################################################
stack = []
quote = False
stop = False

new = open('Patient_03162021_MAR29Formatted.json', 'w')
new.write('[\n')


for i in range(1, 6):
    print(i)
    with open(f'API_Patient_Data_03162021_MAR29({i}).json', 'r') as f:
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
new.write(']')
new.close()
