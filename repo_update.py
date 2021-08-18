from github import Github
import ckl_base
import datetime

def update_repo():
    database = ckl_base.db_server()
    mydb = database.connect()
    myres = database.select() #Calling Select Function to Fetch Data Tuples From DataBase
    html_code = database.generate_html(myres)
    date_time = str(datetime.datetime.now())
    #print(html_code)
    
    # Authenticate yourself -> g = Github("yourusername", "yourauthtoken")
    g = Github("yashash7", "GitHub4GHP#NY4")
    # Find your repository and path of README.md
    repo=g.get_user().get_repo("lumos")
    file = repo.get_contents("README.md")
    # Update README.md
    try:
        #Updating repo -> repo.update_file("file", "commit message", content, file.sha)
        commit_message = "Update Links' Base "+date_time
        #content = html_code
        repo.update_file("README.md", commit_message, html_code, file.sha, branch = "auto_update")
        print("Commit Successful!")
    except:
        print("An Error occured, Update Failed")
    #print(type(file))

#Driver
update_repo()
