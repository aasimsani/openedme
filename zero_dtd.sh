
kill -9 $(ps aux | grep "opened_me.py" | awk '{print $2}')

nohup python3 opened_me/opened_me.py &