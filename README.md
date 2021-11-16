# Companies data scraper 
One application for scraping data and sending emails.


## Create database 
```
$ python create_db.py
```

## Update smtp login and email params
```
# File email_sender.py
smtp.login('<email_login>', '<password>')

msg['Subject'] = '<Subject>'
msg['From'] = '<email>'
```

## Update email template 
```
# template/html_template.py
```
## Run app 
```
$ python main.py
```

#### Menu options:
1 - display categories\
2 - display subcategories\
3 - scrap random count categories\
4 - display random count of records from database\
5 - send random count of emails to potential clients\
6 - exit


                             