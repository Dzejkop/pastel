# C++ - using python to compile files into executables

## Spoiler alert
![Funny image saying "it was absolutely useless. Thanks"](http://i.imgur.com/cL3cnbr.png)

But I did for fun anyways ¯\\\_(ツ)\_/¯

## What is it and how does it work?
The `parse.py` is a simple python script which parses a .cpp (doesn't actually have to be a .cpp file, but it should be for compilation reasons) file (first argument) and looks for macroes such as this one: `COMPILE_IN_DATA_FILE(var_name, "path_to_file");`, it extracts the `var_name` and `path_to_file`. The script will then read the contents of every `path_to_file` file and encode it as a byte array in a .s file (name specified by the second argument).

You, the user, can then compile both files together and voilà - static linking of random files.

**Now.**

You may ask:

**ＷＨＹ　ＷＯＵＬＤ　ＡＮＹＯＮＥ　ＤＯ　ＴＨＩＳ？**

To which I say:

![](http://media.giphy.com/media/K6VhXtbgCXqQU/giphy.gif)

# How do I use it?

Be warnded it's: **only tested on Linux**

## Requirements
1. Python3
1. g++

## Usage
1. Run `python3 parse.py src.cpp asm.s` command where `src.cpp` is your cpp source file, and `asm.s` will be a generated assembly file.
1. Compile the original and generated files together.
1. Preferably remove the generated files.

## Example (works on files in the repo)
```
> python3 parse.py source.cpp temp.s
> g++ temp.s source.cpp -o O
> rm temp.s
> ./O
```
