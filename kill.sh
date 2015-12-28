kill -9 $(ps fax | grep python | grep meta | sed -e 's/^[ \t]*//' | cut -d " " -f1)
