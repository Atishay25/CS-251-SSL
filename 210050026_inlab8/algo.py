import math
import re

##########
#### SEARCH FOR TODO and fix


# Anything following "//" is a comment until end of line
commentPat = re.compile(r'//.*')

# Grab anything within $...$. Make sure to use 
mathPat =  re.compile(r'\$(.*?)\$')

#All id-like words, including optional leading '\' and 
# field access sequences 
# Examples: abc,  foo.length, \xxx
wordPat = re.compile(r'([a-z\.A-Z_\\]+)')

#Take a set of all the unique symbols in opsToTex's keys. 
#Like this r'[<=>.]+'   etc. 
opPat = re.compile(r'([<=>\-\+\!]+|\.{2,3})')
#opPat = re.compile(r'\s*(==)\s*|\s*(<-)\s*|(\s*<=\s*)|(\s*<\s*)|(\s*->\s*)|(\s*>=\s*)|(\s*!=\s*)|(\s*\.\.\s*)|(\s*\.\.\.\s*)|(\s*=\s*)|(\s*>s*)')

# A line of the form "proc myfunc(a, b)".
procPat = re.compile(r'^(proc) ([a-zA-Z\-\+]+)\s*?\((.*)\)')

keywordsToTex = {
    'for'    : r'\For'        ,     'if'     : r'\If'          , 
    'end'    : r'\End'        ,     'then'   : r'\Then'        , 
    'while'  : r'\While'      ,     'do'     : r'\Do'          ,  
    'to'     : r'\To'         ,     'by'     : r'\By'          , 
    'downto' : r'\Downto'     ,     'repeat' : r'\Repeat'      , 
    'until'  : r'\Until'      ,     'elseif' : r'\Elseif'      ,
    'elsif'  : r'\Elseif'     ,     'return' : r'\Return'      , 
    'error'  : r'\Error'      ,     'nil'    : r'\const{nil}'  , 
    'true'   : r'\const{true}',     'false'  : r'\const{false}'
}

opsToTeX = {
    '<-' : r'\leftarrow' ,      '->' : r'\rightarrow',      '==' : r'\isequal' ,
    '<=' : r'\leq'       ,      '>=' : r'\geq'        ,      '>' : '>'          , 
    '<' : '<'            ,      '!=' : r'\neq'       ,      '=' : r'\eq'       , 
    '...' : r'\threedots',      '..' : r'\twodots'
}

def processLine(line):
    # TODO
    #print("line : ", line)
    # Split line into content part and comment part
    # Comments are always to the right, but are optional
    # return processContent(content) + processComment(comment)
    splittedLine = re.split("//",line)
    if len(splittedLine) > 2:
        for i in range(2,len(splittedLine)):
            splittedLine[1] += " // " + splittedLine[i]
        return processContent(splittedLine[0]) + processComment(splittedLine[1])
    if len(splittedLine) == 2:
        return processContent(splittedLine[0]) + processComment(splittedLine[1])
    else:
        return processContent(line)


def processContent(content):
    # TODO
    # Treat the entire content as if it is already in math mode
    # processProc if it matches a proc line
    # Otherwise,
    # Treat the entire content as if it is already in math mode.
    # If there are any embedded '$...$' fragments, then strip the dollar signs
    # out.
    # Prepend '\zi' to the returned line, unless content matches a proc declaration

    if(procPat.search(content) == None):
        content = processOps(content)
        content = processWords(content)
        content = "\zi" + content
        return content
    else :
        return re.sub(procPat, processProc, content)


def processProc(lineMatch):
    # TODO
    funcHeader = "\Procname{\\"
    funcHeader += lineMatch.group(1) + '{' + lineMatch.group(2) + "}("
    funcHeader += processWords(lineMatch.group(3))
    funcHeader += ")}"
    return funcHeader

def processMath(mathPart):
    # TODO
    if type(mathPart) == str:
        pass
    else:
        mathPart = mathPart.group(0)
    mathPart = mathPart.replace('$','')
    mathPart = re.sub(opPat, processOp, mathPart)
    mathPart = re.sub(wordPat, processWord, mathPart)
    return mathPart
    # call processOps(processWords) on the matching part.

def processWords(fragment):
    # TODO
    # call re.sub with wordPat and processWord
    return re.sub(wordPat, processWord, fragment)

def processWord(wordMatch):
    final_line = ""
    for i in wordMatch.groups():
        if(i[0] == "\\"):
            final_line += i
        elif i.count('.') > 0:
            num_b = i.count('.') + 1
            attr = "\\attri"
            words = i.split('.')
            for j in range(num_b-1):
                attr += 'b'
            for word in words:
                attr += "{" + word + '}'
            final_line += attr
        elif i in keywordsToTex.keys():
            final_line += keywordsToTex[i]
        else:
            final_line += "\id{" + i + '}'
    return final_line

    # TODO
    # Handle four cases. 
    #   Word starts with '\' ... return word untouched
    #   Word has embedded '.'. Convert "abc.def.ghi" to "\attribbb{abc}{def}{ghi}"
    #            The number of 'b's following attrib should equal the number of dots
    #   Word belongs to keywords (see testalgo.py for all keywords). Replace with latex substitute
    #   Otherwise replace with "\id{word}"

def processOps(fragment):
    return re.sub(opPat, processOp, fragment)

def processOp(opMatch):
    new_op = ""
    for i in opMatch.groups():
        if i in opsToTeX.keys():
            new_op = '$' + opsToTeX[i] + '$'
            return new_op
    
    return '$' + opMatch.group(0) + '$'
    #TODO
    # replace op with matching latex equivalent if any, and surround with '$'
    # That is, '==' becomes '$\isequal$', but '===' remains unchanged.


def processComment(comment):
    #TODO
    #Treat comment as if it is in text mode, but all embedded math expressions must be translated
    #by processMath
    # See testalgo.py for expected behaviour
    return "\Comment " + re.sub(mathPat, processMath, comment)


def main(filename):
    with open(filename) as f:
        print(r'\begin{codebox}')
        for line in f:
            line = line.rstrip()
            print(processLine(line))
        print(r'\end{codebox}')

def usage():
    print("""
algo.py <file.algo>
Translates a pseudocode algorithm to LaTeX's clrscode3e environment. 
The format is a simplification of that environment, the objective being to 
not have to introduce math-mode or have special keywords like \For and \If 

Keywords: 
- Loops: for, to, by, downto, do, while, repeat, until
- Selection: if, then, else, elseif/elsif
- Jumps: return, error, goto
- Constants: nil, true, false

do/end blocks are required for indent/dedent, but do not appear in final output

Operators like <-, !=, ==, <= etc are replaced by the LaTeX equivalents.

Example:

proc insertion-sort(A, B)
   for j <- 2 to A.length do
      key <- A[j] // Insert $A[j]$ into the sorted sequence $A[1 .. j-1]$
      i <- j - 1
      while i > 0 and A[i] > key do
         A[i+1] <- A[i]
         i <- i - 1
      end
      A[i+1] <- key
   end
   if x == 3 then do
      {{Do something special}}
   end
end

""")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(sys.argv[1])
    
   
