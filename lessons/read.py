ipsum_file = open('files/ipsum.txt')

for line in ipsum_file:
    print(line.rstrip()) # rstrip strips out line breaks

ipsum_file.seek(0) # sets the start counter at char 50
    
lines = ipsum_file.readlines() # stores lines in a list
print(lines)

ipsum_file.seek(0) # sets the start counter at char 50
file_text = ipsum_file.read(100) # entire contents of file in string
print(file_text)

ipsum_file.close()

# alternate way to read files - auto closes file
def sequence_filter(line):
    return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))
