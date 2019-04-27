# Pseudocode-Compiler
Compiles pseudocode into python. It isn't a traditional compiler as it uses regular expressions to evaluate statements.

## How to use

Inside the Pseudocode folder, there will be three files. The file known as **enter.txt** will be the one where you type your pseudocode. After typing your Pseudocode save the text file.

Next, run the **Compiler.py** program. This will compile the pseudocode in the enter.txt file, and it will save the generated python code in the **Compiled.py**

The Compiler.py will immediately run Compiled.py after creating it. This means that your pseudocode program will get executed automatically after compiling.

If you want to store or edit the generated Python code, you can look inside **Compiled.py**, where it will be written to.

## Syntax

The language is case sensitive. All keywords must be capitalized. Indenting doesnt matter. There are no delimiters either (semicolon in java, etc). Due to being built on top of Python, anything not in the below documentation can be emulated using Python syntax. One key use of this is for comparisons and list operations.

The delimiters are not needed as there are closing statements for all the block statements (IF, WHILE, FOR, ETC). These closing statements (ENDIF, ENDWHILE, NEXT) are **extremely important**. Never forget them or else the program won't work.

In every pseudocode program, there must be a **STOP** statmement at the very end to signify that the program is finished. Without it there will be list index errors sent.

### If statements 
  **IF condition THEN** - if statement where condition can be "x > 5", "5!=6", etc

  **ELSE IF condition THEN** - Else if where condition is an argument. Can be used as many times as needed in one IF block

  **ELSE** - else statement

  **ENDIF** - ends and if statement

### For statements
  
  **FOR i = x TO y** - i is the variable being incremented. x is the starting value, and y is the end value. As python code it would look like           for i in range(x,y)
  
  **NEXT** - Ends the for statement just like how ENDIF ends an if statement. Anything after this is outside the FOR statement block
  
### While statements
  
  **WHILE condition DO** - A while loop is started where everything following the statement till the ENDWHILE is within the WHILE block
                        Condition is just another condition like x>6
   
  **ENDWHILE** - Closes the WHILE loop
  
### REPEAT statements

  **REPEAT** - starts the repeat loop
  
 **UNTIL** condition - closes the REPEAT loop once the condition has been satisfied. Substitute condition with something like x > 6
  
### Other statements
  
  **OUTPUT x** - x is the value to be outputted. x can be a variable, string, boolean, float, etc. Ex: **OUTPUT "hello"**, **OUTPUT True**
  
  **INPUT x** - x is the name of the variable which is going to be inputted. The compiled version of **INPUT x** will be **x 
            = eval(input())** 

