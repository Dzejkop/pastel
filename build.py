from subprocess import call
import os
import sys

if len(sys.argv) != 4:
    print ("Invalid number of arguments")
    exit()

data_header_template = """.globl %(name)s
.section .rodata
.p2align 5
.type %(name)s, "object"
.size %(name)s, %(size)d
%(name)s:
"""

data_part_template = "    .byte %(data)d\n"

def write_symbol_name(symbol_name, size, target_file):
    target_file.write(data_header_template % {'name': symbol_name, 'size' : size})

def write_symbol_data(symbol_name, data, target_file):
    for byte in data:
        target_file.write(data_part_template % {'data': byte})

def write_symbol(symbol_name, symbol_data, target_file):
    write_symbol_name(symbol_name, len(data), target_file)
    write_symbol_data(symbol_name, data, target_file)

def read_whole_file(path):
    with open(path, 'rb') as f:
        return f.read()

source_file_name = sys.argv[1]
data_file_name = sys.argv[2]
data_var_name = sys.argv[3]

temp_asm = "temp_asm.s"
temp_asm_object = "temp_asm.o"

cl_command = "g++"

temp = open(temp_asm, "w")

data = read_whole_file(data_file_name)

with open(temp_asm, "w") as temp_asm_file:
    write_symbol("data", data, temp_asm_file)

print("Compiling")

call([cl_command, "-c", temp_asm, "-o", temp_asm_object])
call([cl_command, temp_asm_object, source_file_name, "-O3", "-o", "O"])

#call("%(cl)s -c %(asm)s -o %(output)s" % {'cl' : cl_command, 'asm' : temp_asm, 'output' : temp_asm_object})
#call("%(cl)s %(asm_obj)s %(src)s -o %(output)s" % {'cl' : cl_command, 'asm_obj' : temp_asm_object, 'output' : "O"})

os.remove(temp_asm)
os.remove(temp_asm_object)

print ("Done")
