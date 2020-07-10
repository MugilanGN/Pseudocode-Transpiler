# Pseudocode-Compiler
Compiles pseudocode into python. It isn't a traditional compiler as it uses regular expressions to evaluate statements. In fact Im assuming that the correct term is "Transcompiler" as the pseudocode you enter has a pythonic structure

## How to use

Inside the Pseudocode folder, there will be three files. The file known as **enter.txt** will be the one where you type your pseudocode. After typing your Pseudocode save the text file.

Next, run the **Compiler.py** program. This will compile the pseudocode in the enter.txt file, and it will save the generated python code in the **Compiled.py**

The Compiler.py will immediately run Compiled.py after creating it. This means that your pseudocode program will get executed automatically after compiling.

If you want to store or edit the generated Python code, you can look inside **Compiled.py**, where it will be written to.

## Syntax

The language is case sensitive. All keywords must be capitalized. Indenting doesnt matter. There are no delimiters either (semicolon in java, etc). Due to being built on top of Python, anything not in the below documentation can be emulated using Python syntax. One key use of this is for comparisons and list operations.

The delimiters are not needed as there are closing statements for all the block statements (IF, WHILE, FOR, ETC). These closing statements (ENDIF, ENDWHILE, NEXT) are **extremely important**. Never forget them or else the program won't work.

In every pseudocode program, there must be a **STOP** statmement at the very end to signify that the program is finished. Without it there will be list index errors sent.

### Syntax Guide

 #### Input and Output:

  - INPUT x 
  - OUTPUT x

   ```sh
   INPUT X
   OUTPUT var
   OUTPUT "hello"
   ```
#### IF statements:
  - IF condition THEN
  - ELSE
  - ENDIF
  
  ```sh
  IF x < 3 THEN
    OUTPUT X
  ELSE
    OUTPUT x*2
  ENDIF
  ```
  
  #### Process-type blocks:

  ```sh
  x = x + 1
  y = x / 2
  ```
  
  #### While loops:

  - WHILE condition DO
  - ENDWHILE
  
  ```sh
  WHILE x < 5 DO
    OUTPUT x
  ENDWHILE
  ```
  #### For loops:
   
  - FOR var <- start TO end
  - NEXT var
  
  ```sh
  FOR i <- 1 TO 5
    OUTPUT i
  NEXT i
  ```

