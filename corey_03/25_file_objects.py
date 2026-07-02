# f = open('test_file.txt')

# print(f.name)
# print(f.mode)
# print(f.read())

# f.close()

"context manager"

# with open('test_file.txt', 'r') as f:
#     print(f.name)
#     print(f.mode)
#     print(f.read())

# print(f.closed)
# print(f.read())
# this will produce error the variable remains
# that doesnt mean u can read as f.closed is True its automatically closed

# so since its gonna closed the practice was store the file contents

# with open('test_file.txt', 'r') as f:
#     file_contents = f.read()

# print(file_contents)

# now read() whole data from file since its small file no issues
# use readlines() instead reading as whole it reads line by line

# with open('test_file.txt', 'r') as f:
#     file_lines = f.readlines()

# print(file_lines)

# as readlines() gonna read entire file line by line
# if you want to just read a line use readline()

# with open('test_file.txt', 'r')  as f:
#     first_line = f.readline()

# print(first_line)

# as it stopped at just reading 1 line read 2 lines
# with open('test_file.txt', 'r') as f:
#     first_line = f.readline()
#     second_line = f.readline()

# print(first_line, second_line, sep="", end="")

# this is the way to handle large files process each line
# with open('test_file.txt', 'r') as f:
#     for line in f:
#         print(line, end="")

# the difference between f.read() and this for line in f: print(line)
# it reads whole at once whereas readline() line by line make sure no memory overload

# f.read() we can also pass size so that it can read just those size characters
# with open('test_file.txt', 'r') as f:
#     print(f.read(100)) # by here 5 lines done
#     print(f.read(100)) # by here remaining lines done
#     print(f.read(100)) # no more to read so returns empty string

# now to use this size read efficiently we cant have hardcoded like 100
# also earlier we dont know the end of file may be we keep printing empty lines
# better way of implementation for this will be

# with open('test_file.txt', 'r') as f:
#     size_to_read = 100
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)

# file read think its like pointer
# we can tell where the pointer using f.tell()
# and we can move pointer to start using f.seek(0)
# not only start you can move to any position by passing it as param

# with open('test_file.txt', 'r') as f:
#     size_to_read  = 10
#     print(f.tell())
#     print(f.read(size_to_read))
#     print(f.tell())
#     print(f.read(size_to_read))
#     print(f.tell())
#     f.seek(0)
#     print(f.read(size_to_read))
#     print(f.tell())

# with open('test_file.txt', 'r') as f:
#     f.write("this produces error since file's not writable")

# now 'w' mode gonna overwrite ie delete whole existing data and write new one
# use it with caution make sure u dont overwrite
# with open('test_file2.txt', 'w') as f:
#     f.write("new file written")

# say we dont want to write anything but create just empty
# we can use same thing but dont do anything it will create new file
# with open('test_file3.txt', 'w') as f:
#     pass

# btw its dangerous to use over existing files
# as its gonna delete existing data
# with open('test_file2.txt', 'w') as f:
#     pass

# use write in same context block its gonna keep on writing
# by moving pointer its output will be 'testtest'
# with open('test_file2.txt', 'w') as f:
#     f.write('test')
#     f.write('test')

# say if we move pointer back to some existing data
# its going to overwrite as its op will be 'test' that written 2nd time
# as first time written test overwritted by 2nd one
# with open('test_file2.txt', 'w') as f:
#     f.write('test')
#     print(f.tell())
#     f.seek(0)
#     f.write('test')

# say if we dont overwrite all way just half
# it doesnt mean its gonna delete all existing ones after pointer
# as op of next one chnaged from test to rest
# with open('test_file2.txt', 'w') as f:
#     f.write('test')
#     f.seek(0)
#     f.write('r')

# lets see how to copy contents of one file to another
# with open('test_file.txt', 'r') as source:
#     with open('test_file_copy.txt', 'w')  as destination:
#         for line in source:
#             destination.write(line)

# we can also do opening stat on a single line sep by comma
# but its not quite readable if u want it u can

# lets try to copy an img
# with open('sample.jpg', 'r') as source:
#     with open('sample_copy.jpg', 'w') as dest:
#         for line in source:
#             dest.write(line)

# UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 593: character maps to <undefined>
# as in case of files we have to work with bytes

# with open('sample.jpg', 'rb') as source:
#     with open('sample_copy.jpg', 'wb') as dest:
#         for line in source:
#             dest.write(line)

# actually its not that safe to read lines
# to have more control use small chunks
# by this we can copy much safely since what if a line has so mcuh taht causes overflow
with open('sample.jpg', 'rb') as rf:
    with open('sample_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)