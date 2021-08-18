from github import Github
from ckl_base import *
import datetime

def update_repo():
    database = db_server()
    mydb = database.connect()
    myres = database.select() #Calling Select Function to Fetch Data Tuples From DataBase
    html_code = database.generate_html(myres)
    date_time = str(datetime.datetime.now())
    #print(html_code)
    
    # Authenticate yourself -> g = Github("yourusername", "yourauthtoken")
    g = Github("yashash7", "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")
    # Find your repository and path of README.md
    repo=g.get_user().get_repo("lumos")
    file = repo.get_contents("README.md")
    # Update README.md
    try:
        #Updating repo -> repo.update_file("file", "commit message", content, file.sha)
        commit_message = "Update Links' Base "+date_time
        #content = html_code
        repo.update_file("README.md", commit_message, html_code, file.sha, branch = "main")
        print("Commit Successful!")
    except:
        print("An Error occured, Update Failed")
    #print(type(file))

#Driver
update_repo()
