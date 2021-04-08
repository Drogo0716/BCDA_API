# January 12, 2021
# This program reads the separate key files then writes them to a new file in the correct format for .csv conversion
# TO BE RAN AFTER 'SEPARATE_KEYS_JSON.py'
#######################################################################################################################
stack = []
quote = False
stop = False

# new = open('API_EoB_Data_Formatted(1).json', 'w')
new = open('API_EoB_Data_03162021_MAR29(Key1_Formatted_Step2).json', 'w')
new.write('[\n')
# with open('API_EoB_Data_01112021_NOV30(1).json', 'r') as f:

with open('EoB_Key1.json', 'r') as f:
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
new.write(']')
new.close()

#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key2_Formatted_Step2).json', 'w')
new.write('[\n')
with open('EoB_Key2.json', 'r') as f:
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
new.write(']')
new.close()

#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key3_Formatted_Step2).json', 'w')
new.write('[\n')

with open('EoB_Key3.json', 'r') as f:
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
new.write(']')
new.close()

#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key4_Formatted_Step2).json', 'w')
new.write('[\n')

with open('EoB_Key4.json', 'r') as f:
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
new.write(']')
new.close()


#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key5_Formatted_Step2).json', 'w')
new.write('[\n')

with open('EoB_Key5.json', 'r') as f:
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
new.write(']')
new.close()


#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key6_Formatted_Step2).json', 'w')
new.write('[\n')

with open('EoB_Key6.json', 'r') as f:
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
new.write(']')
new.close()


#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key7_Formatted_Step2).json', 'w')
new.write('[\n')


with open('EoB_Key7.json', 'r') as f:
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
new.write(']')
new.close()


#######################################################################################################################

stack = []
quote = False
stop = False

new = open('API_EoB_Data_03162021_MAR29(Key8_Formatted_Step2).json', 'w')
new.write('[\n')

with open('EoB_Key8.json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
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
                    new.write(char)
                    stack.pop()
            else:
                new.write(char)

f.close()
new.write(']')
new.close()

#######################################################################################################################
'''
stack = []
quote = False
stop = False

new = open('API_EoB_Data_03082021_MAR16(Key9_Formatted_Step2).json', 'w')
new.write('[\n')

with open('EoB_Key9.json', 'r') as f:
    for line in f:
        if stop:
            new.write(',\n')
            stop = False
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
                    new.write(char)
                    stack.pop()
            else:
                new.write(char)

f.close()
new.write(']')
new.close()
'''
