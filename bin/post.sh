title=$(python format_post.py $1)
scp post.txt thousan2@thousandonestories.com:~/post.txt
wp @thousand post create /home/thousan2/post.txt --post_title="$title" --post_status=draft --user=edwardk
