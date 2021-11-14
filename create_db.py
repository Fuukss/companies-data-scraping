"""

Create the companies table in application database

"""
import sqlite3

con = sqlite3.connect('application.db')

cur = con.cursor()
# Create table

cur.execute('''CREATE TABLE companies
               (id integer primary key AUTOINCREMENT, category_name text, subcategory_name text, company_name text,
                email_address text, web_address text, phone_number text, 
                UNIQUE (company_name, email_address) ON CONFLICT IGNORE)''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
