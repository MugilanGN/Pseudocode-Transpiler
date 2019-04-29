import re,os

def identify(text):
    
    global indent

    if_re = re.compile(r'^IF\s(.+)\sTHEN$')
    endif_re = re.compile(r'^ENDIF$')
    else_re = re.compile(r'^ELSE$')
    elif_re = re.compile(r'^ELSE\sIF\s(.+)\sTHEN$')
    
    output_re = re.compile(r'^OUTPUT\s(.+)')
    input_re = re.compile(r'^INPUT\s(.+)')
    
    while_re = re.compile(r'^WHILE\s(.+)\sDO$')
    endwhile_re = re.compile(r'^ENDWHILE$')

    for_re = re.compile(r'^FOR\s(.+)\s<-\s(.+)\sTO\s(.+)')
    next_re = re.compile(r'^NEXT$')

    repeat_re = re.compile(r'^REPEAT$')
    until_re = re.compile(r'^UNTIL\s(.+)')

    if re.search(if_re,text):

        #Searches for IF statements (Starters)
        
        statement = re.search(if_re,text).group(1)
        statement = indent * "  " + "if("+statement+"):"
        
        indent += 1

        return statement
        
    elif re.search(endif_re,text):
        
        #Searches for ENDIF statements (Stoppers)
        
        indent -= 1
        
        #statement = indent * "  " + re.search(endif_re,text).group()
        #not needed as endif wont be needed for a python conversion. The None will be ignored by write()

        return None

    elif re.search(else_re,text):

        #Searches for ELSE statements (Pseudo-Starters)
        
        statement = re.search(else_re,text).group()
        statement = (indent-1) * "  " + "else:"

        return statement

    elif re.search(output_re,text):
        
        #Searches for OUTPUT statements (Regulars)
        
        statement = re.search(output_re,text).group(1)
        statement = indent * "  " + "print("+statement+")"

        return statement

    elif re.search(while_re,text):
        
        #Searches for While statements (Starters)
        
        statement = re.search(while_re,text).group(1)
        statement = indent * "  " + "while(" + statement + "):"
        
        indent += 1

        return statement

    elif re.search(endwhile_re,text):
        
        #Searches for ENDWHILE statements (Stoppers)
        
        indent -= 1

        return None
    
    elif re.search(input_re,text):
         
        #Searches for INPUT statements (Regulars)
        
        statement = re.search(input_re,text).group(1)
        statement = indent * "  " + statement + " = check(input())"

        return statement

    elif re.search(next_re,text):
        
        #Searches for NEXT statements (Stoppers)
        
        indent -= 1

        return None

    elif re.search(for_re,text):
        
        #Searches for FOR statements (Starters)
        
        var = re.search(for_re,text).group(1)
        low = re.search(for_re,text).group(2)
        high = re.search(for_re,text).group(3)
        
        statement = indent * "  " + "for " + var + " in range(" + low + ","+ high + "):"
        
        indent += 1

        return statement

    elif re.search(elif_re,text):

        #Searches for ELSE IF statements (Pseudo-Starters)
        
        statement = re.search(elif_re,text).group(1)
        statement = (indent-1) * "  " + "elif (" + statement + "):"
        
        return statement  

    elif re.search(repeat_re,text):
        
        #Searches for REPEAT statements (Starters)
        
        statement = re.search(repeat_re,text).group()
        
        statement = indent * "  " + "while True:"
        
        indent += 1

        return statement

    elif re.search(until_re,text):
        
        #Searches for UNTIL statements (post-Stoppers)
        
        statement = re.search(until_re,text).group(1)
        
        statement = indent * "  "+ "if ("+ statement + "):\n" + (indent+1) * "  " + "break"
        
        indent -= 1
        
        return statement
        
    else:

        #Anything not fitting syntax will get stored. Can be used for Initializing
        
        statement = (indent * "  "+text)

        return statement

def read(count):

    compiler = os.path.realpath(__file__)
    
    self_path = re.compile(r'(.+)Compiler.py')
    
    path = re.search(self_path,compiler).group(1) + "enter.txt"

    file1 = open(path,"r")

    v = file1.readlines()

    file1.close()

    read_filter = re.compile(r'^\s*(.*)$')
    
    if re.search(read_filter,v[count]):
        x = re.search(read_filter,v[count]).group(1)
        return x
    else:
        return None
    
def write(lines):
    
    file = open("compiled.py","a")
    
    for line in lines:
        file.write(line+" \n") 
    file.close()

def main():
    
    global indent,lines,check

    file = open("compiled.py","w")
    file.write("\n")
    file.close()
    
    indent = 0
    lines = []
    filtered = ""
    count = 0
    
    check = """
def check(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if(s == "True"):
                return True
            elif(s == "False"):
                return False
            else:
                return(s)
                """
                
    
    lines.append(check)
    
    while filtered != "STOP":
        
        text = read(count)
        filtered = identify(text)
        
        if (filtered != "STOP" and filtered != None): 
           lines.append(filtered)
        else:
            pass

        count+= 1
        
    lines.append("r = input() #line that halts execution so program won't close")

    write(lines)

    import Compiled
        
main()
