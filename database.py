from logging import FileHandler
from discord.utils import find
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mynameisriju2021"
)

mycursor=mydb.cursor()
mycursor.execute("use simbot")
mycursor.execute("select phrase,n_phrase from statement")
list_phrase=list()
myresult=mycursor.fetchall()
dict1={}

gg=find(lambda x:x[0]=="gg",myresult)
print((gg[1]))