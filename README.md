# Companies data scraper 
One application for scraping data from <https://panoramafirm.pl/> and sending emails use defined email template.


## Create database 
```
$ python create_db.py
```

## Update smtp settings and email params
Possible to send emails from GMail SMTP Server (Google) \
Instruction for gmail config: \
https://www.siteground.com/kb/gmail-smtp-server/?gclid=Cj0KCQiAys2MBhDOARIsAFf1D1ecZSfRvG6ffbI5lChZ4F7t56jLweOioxqSCXVd3N563Sy3tFIfDo8aAtr5EALw_wcB

## Required changes in email_sender.py file
```
subject: str = '<subject of email>'
send_from: str = '<email>'

smtp.login('<email_login>', '<password>')
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


                             