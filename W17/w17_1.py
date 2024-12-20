A = 0
B = 0
C = 0

instrPointer = 0
output = []
program = []

def ComboOperand(operand):
    global A, B, C
    match operand:
        case num if 0 <= num <= 3:
            return num
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            raise Exception("Using 7 as combo operand")
        case _:
            raise Exception("Combo operand not between 0-7")
        
def Op0adv(operand):
    global A
    A = int(A / (2**ComboOperand(operand)))
    IncrementInstruction()

def Op1bxl(operand):
    global B
    B = B^operand
    IncrementInstruction()

def Op2bst(operand):
    global B
    B = ComboOperand(operand) % 8
    IncrementInstruction()

def Op3jnz(operand):
    global A, instrPointer
    if A != 0:
        instrPointer = operand
    else:
        IncrementInstruction()

def Op4bxc(_):
    global B, C
    B = B^C
    IncrementInstruction()

def Op5out(operand):
    global output
    output.append(ComboOperand(operand) % 8)
    IncrementInstruction()

def Op6bdv(operand):
    global A, B
    B = int(A / (2**ComboOperand(operand)))
    IncrementInstruction()

def Op7cdv(operand):
    global A, C
    C = int(A / (2**ComboOperand(operand)))
    IncrementInstruction()

def IncrementInstruction():
    global instrPointer
    instrPointer = instrPointer + 2
        
def Operation(opcode, operand):
    match opcode:
        case 0:
            Op0adv(operand)
        case 1:
            Op1bxl(operand)
        case 2:
            Op2bst(operand)
        case 3:
            Op3jnz(operand)
        case 4:
            Op4bxc(operand)
        case 5:
            Op5out(operand)
        case 6:
            Op6bdv(operand)
        case 7:
            Op7cdv(operand)

def OutputToStr(output):
    result = ""
    for item in output:
        if result == "":
            result += str(item)
        else:
            result += "," + str(item)
    return result

with open("input.txt") as file:
    A = int(file.readline().strip().split(": ")[1])
    B = int(file.readline().strip().split(": ")[1])
    B = int(file.readline().strip().split(": ")[1])
    file.readline()
    program = file.readline().strip().split(": ")[1].split(",")

counter = 0
while instrPointer < len(program):
    counter += 1
    opcode = int(program[instrPointer])
    operand = int(program[instrPointer + 1])
    Operation(opcode, operand)

print(OutputToStr(output))