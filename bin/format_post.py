import sys

infile = open(sys.argv[1],'r')
out = open('post.txt', 'w')

line = infile.readline()

title = False

while line:

    parts = line.split("title: ")

    # get text
    if title and line != "---":
        text = infile.read()
        break


    # get title
    if(len(parts) > 1):
        title = parts[1].split('\n')[0]

    line = infile.readline()

out.write(text)
print title

infile.close()
out.close()
