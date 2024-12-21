#Every button can be navigated to with 2 buttons from the dir pad in the level above, followed by a press of A.

NUM_PAD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ['X',0,'A']
]
DIR_PAD = [
    ['X', '^', 'A'],
    ['<', 'v', '>']
]

NUM_PAD_DICT = {
    '7': [0, 0],
    '8': [0, 1],
    '9': [0, 2],
    '4': [1, 0],
    '5': [1, 1],
    '6': [1, 2],
    '1': [2, 0],
    '2': [2, 1],
    '3': [2, 2],
    '0': [3, 1],
    'A': [3, 2]
}

DIR_PAD_DICT = {
    '^': [0, 1],
    'A': [0, 2],
    '<': [1, 0],
    'v': [1, 1],
    '>': [1, 2]
}

snippet_count_dict = dict()
new_snippet_count_dict = dict()
snippet_cache = dict()


def GetDirPadInstructionsForNumPad(numCode: str) -> list:
    curSnippet = ""
    result = []
    i = 0
    curPos = NUM_PAD_DICT['A']
    while i < len(numCode):
        curSnippet = ""
        targetPos = NUM_PAD_DICT[numCode[i]]
        diff = [targetPos[0] - curPos[0], targetPos[1] - curPos[1]]
        swap = False
        if diff[1] < 0 and curPos[0] == 3 and targetPos[1] == 0:
            swap = True
        if diff[0] > 0 and curPos[1] == 0 and targetPos[0] == 3:
            swap = True
        if swap:
            #Right
            if diff[1] > 0:
                curSnippet += '>' * abs(diff[1])
            #Up
            if diff[0] < 0:
                curSnippet += '^' * abs(diff[0])
            #Left
            if diff[1] < 0:
                curSnippet += '<' * abs(diff[1])
            #Down
            if diff[0] > 0:
                curSnippet += 'v' * abs(diff[0])
        else:
            #Left
            if diff[1] < 0:
                curSnippet += '<' * abs(diff[1])
            #Down
            if diff[0] > 0:
                curSnippet += 'v' * abs(diff[0])
            #Up
            if diff[0] < 0:
                curSnippet += '^' * abs(diff[0])
            #Right
            if diff[1] > 0:
                curSnippet += '>' * abs(diff[1])
        
        curSnippet += 'A'
        result.append(curSnippet)
        i += 1
        curPos = targetPos
    return result

def calculateNextLevelDirSnippet(snippet:str) -> list:
    result = []
    i = 0
    curPos = DIR_PAD_DICT['A']
    while i < len(snippet):
        curSnippet = ""
        targetPos = DIR_PAD_DICT[snippet[i]]
        diff = [targetPos[0] - curPos[0], targetPos[1] - curPos[1]]
        swap = False
        if diff[1] < 0 and curPos[0] == 0 and targetPos[1] == 0:
            swap = True
        if diff[0] < 0 and curPos[1] == 0 and targetPos[0] == 0:
            swap = True
        if swap:
            #Down
            if diff[0] > 0:
                curSnippet += 'v' * abs(diff[0])
            #Right
            if diff[1] > 0:
                curSnippet += '>' * abs(diff[1])
            #Left
            if diff[1] < 0:
                curSnippet += '<' * abs(diff[1])
            #Up
            if diff[0] < 0:
                curSnippet += '^' * abs(diff[0])
        else:
            #Left
            if diff[1] < 0:
                curSnippet += '<' * abs(diff[1])
            #Down
            if diff[0] > 0:
                curSnippet += 'v' * abs(diff[0])
            #Up
            if diff[0] < 0:
                curSnippet += '^' * abs(diff[0])
            #Right
            if diff[1] > 0:
                curSnippet += '>' * abs(diff[1])
        curSnippet += 'A'
        result.append(curSnippet)
        i += 1
        curPos = targetPos
    return result

def getSnippet(snippet: str) -> list:
    cacheSnippet(snippet)
    return snippet_cache[snippet]
    
def cacheSnippet(snippet: str):
    if snippet not in snippet_cache:
        snippet_cache[snippet] = calculateNextLevelDirSnippet(snippet)
    
def incrementSnippetCount(count_dict: dict, snippet: str, amount):
    cacheSnippet(snippet)
    count_dict[snippet] = count_dict.get(snippet, 0) + amount

ans = 0
with open("input.txt") as file:
    for line in file:

        numCode = line.strip()
        numVal = int(numCode[:-1])

        snippet_count_dict = dict()
        new_snippet_count_dict = dict()

        numPadSnippets = GetDirPadInstructionsForNumPad(numCode)
        for s in numPadSnippets:
            incrementSnippetCount(snippet_count_dict, s, 1)
        
        iteration = 1
        while iteration <= 25:
            for snippet in snippet_count_dict.keys():
                newSnippets = getSnippet(snippet)
                for newSnippet in newSnippets:
                    incrementSnippetCount(new_snippet_count_dict, newSnippet, snippet_count_dict[snippet])
            snippet_count_dict = dict(new_snippet_count_dict)
            new_snippet_count_dict = dict()
            iteration += 1
        
        length = 0
        for snippet in snippet_count_dict.keys():
            length += len(snippet) * snippet_count_dict[snippet]
        ans += length * numVal

print(ans)
