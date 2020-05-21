"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# YOUR CODE HERE
read_file = open('foo.txt', 'r')
print(read_file.read())
read_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
# YOUR CODE HERE
write_file = open('bar.txt', 'w')
write_file.write("Long, long time ago \nI can still remember how that music \nused to make me smile\nand I knew if I had the chance\nI could make those people dance\nand maybe they'd be happy for awhile")
write_file.close()