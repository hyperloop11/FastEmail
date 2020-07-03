# FastEmail
Send emails with attachments by a program that directly reads email addresses from a spreadsheet.
Before using make sure to have xlrd and pandas installed.
Instructions for installation:
```
pip install xlrd
```
```
pip install pandas
```
# Usage
1. Excel spreadsheet should be in same directory as this file. It should have emails under the heading 'EMAIL'
2. Change name of spreadsheet at line 8.
3. Add body at line 6.
4. Add sender's email-id at line 21.
5. Add sender's password at line 25.
6. Add name of attachment with e-mail at line 35,36.
