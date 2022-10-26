def punt(a):
# define punctuation
   punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~–'''

   my_str = a

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
   no_punct = ""
   for char in my_str:
       if char not in punctuations:
          no_punct = no_punct + char
   d=no_punct
    # display the unpunctuated string
   import mysql.connector
#from cleverclod console you get the credentials
   mydb = mysql.connector.connect(
    host='hostname',
    user ='username',
    passwd='pwd',
    database='db'
    )
   mycursor = mydb.cursor()

   mycursor.execute("SELECT * FROM marvel")

   myresult = mycursor.fetchall()
   mycursor.execute("SELECT * FROM eng")

   myresult2 = mycursor.fetchall()


   for x in myresult:
      if x[1].lower().replace(' ','').strip()==d.strip().lower().replace(' ',''):
          return x[2]
      
          

   for f in myresult2:
      if f[1].lower().replace(' ','').strip()==d.strip().lower().replace(' ',''): 
             return f[2]


              
              
              


