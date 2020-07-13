import subprocess
import sys

def reorder(tags):
    return [tags[0], tags[5], tags[4], tags[1], tags[2], tags[3]]

with open(sys.argv[1], 'r') as in_f, open(sys.argv[1] + ".tmp", 'w') as temp_f:
    for line in in_f:
        fields = line.split()
        tags = fields[0].split(".")
        reordered_tags = reorder(tags)
        new_line = ".".join(reordered_tags) + "\t" + "\t".join(fields[1:]) + "\n"
        temp_f.write(new_line)
    subprocess.call(["sort", "-o", sys.argv[1] + ".sorted", sys.argv[1] + ".tmp"])

def get_cell(line):
   tags = line.split("\t")[0].split(".")
   return ".".join([tags[0], tags[1], tags[2]])

with open(sys.argv[1] + ".sorted", 'r') as in_f:
    current_cell = None
    output = ""
    for line in in_f:
        this_cell = get_cell(line)
        if current_cell != this_cell:
            if current_cell != None:
                with open(current_cell, 'w') as f:
                    f.write(output)
            current_cell = this_cell
            output = line
        else:
            output += line
        
    with open(current_cell, 'w') as f:
        f.write(output)
        
        
