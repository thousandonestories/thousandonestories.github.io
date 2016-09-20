---
layout: post
tags: 
- tutorial
title: How to easily share Jekyll posts to Wordpress
---
wanna 

```bash
    title=$(python format_post.py $1)
    scp post.txt thousan2@thousandonestories.com:~/post.txt
    wp @thousand post create /home/thousan2/post.txt --post_title="$title" --post_status=draft --user=edwardk
```

```python
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
```

