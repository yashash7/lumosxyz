import mysql.connector
import datetime

class db_server:
    def __init__(self):
        self._user_name = "ul8a9buow3kovfwl"
        self._server = "bmm9nmdc8jkviblsmk1v-mysql.services.clever-cloud.com"
        self._pwd = "T5fBv04lvFp9hBV9W70b"
        self._db = "bmm9nmdc8jkviblsmk1v"

    def connect(self):
        #connecting to DB
        return mysql.connector.connect(user=self._user_name, password=self._pwd, host=self._server, database=self._db)
        #return mydb
    def select(self):
        connection = self.connect()
        mycursor = connection.cursor() #Create a Cursor Object
        mycursor.execute("SELECT * FROM linksarchive")#Execute the SQL Query
        result = mycursor.fetchall() #List of data tuples
        #print(myres) # List of Data Tuples
        connection.close() #Closing Database Connection
        return result
    #HTML Code Generator
    def generate_html(self, db_list):#HTML Code Generator
        db_list = self.select()
        #HTML Code
        html = '''
# Links' Base


<table>

<tr>
<th> Asset_Entry </th>
<th> Asset_URL </th>
<th> Remarks </th>
<tr>
'''
        loop = ''''''
        for i in range(len(db_list)):
            #asset_entry = myres[1]
            #asset_url = myres[2]
            #remarks = myres[3]
            loop += '''
<tr>
<td>'''+db_list[i][1]+'''</td>
<td><a href="'''+db_list[i][2]+'''">'''+db_list[i][2]+'''</a></td>
<td>'''+db_list[i][3]+'''</td>
</tr>
'''

        #Final Code
        html+=loop+'''
</table>
'''
        return html
