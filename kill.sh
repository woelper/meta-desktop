kill -9 $(ps fax | grep python | grep meta | cut -d " " -f1)
