# Miron-Insights
Simple python script to get Miron insights automatically

# Dependencies

Python3 and PyGithub:
`pip install PyGithub`

# How to use
Navigate to the folder Miron-Insights and run:

`python3 insights.py "token"`

Replace "username" and "password" with your info.

You should get something like this, in terminal:

`['Unique Views', 4, 8, 3, 5, 1, 0, 0]  
['Views Count', 59, 51, 18, 13, 4, 0, 0]  
['Unique Clones', 1, 0, 5, 1, 1, 0, 0]  
['Views Count', 59, 51, 18, 13, 4, 0, 0]`

It also generates a .csv file with the total. The csv file's name is current date and the results have 1 week timestamp.

# How to make a Token

Follow the link bellow:
[Token Documentation](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

Make sure to tick the "read" access.