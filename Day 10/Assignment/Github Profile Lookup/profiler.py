import requests as rq
import json

class Github_Profiler:
    def __init__(self):
        self.api_url = "https://api.github.com/users/"

    def profile_user(self, username):
        url = self.api_url + username

        response = rq.get(url)

        user_data = json.loads(response.text)
        status = response.status_code

        return user_data, status 
    
    def profile_repos(self, username):
        url = self.api_url + username + "/repos"

        response = rq.get(url)

        repo_data = json.loads(response.text)
        status = response.status_code

        return repo_data, status 
    

def main():
    profiler = Github_Profiler()
    
    user = input("Enter the GitHub Username :")
    user_data, status = profiler.profile_user(user)
    # print(status)
    if status == 200:
        print("\n" + user + " Found on Github!")
        print("\n"+ "-"*15 + " Basic User Details " + "-"*15)
        print("\n   Official Name: ", user_data['name'])
        print("   ID : ", user_data['id'])
        print("   Followers : ", user_data['followers'])
        print("   Following : ", user_data['following'])
        print("   Public Repositories : ", user_data['public_repos'])

        repo_data, status = profiler.profile_repos(user)

        if status == 200:
            print("\n"+ "-"*15 +"Public Repository Details" + "-"*15)
            for i, repo in enumerate(repo_data):
                print("\n   Repository : ", i+1)

                print("\tName : ", repo['name'])
                print("\tDescription : ", repo['description'])
                print("\tURL : ", repo['html_url'])
                print("\tDate Created : ", repo['created_at'])
                print("\tStars : ", repo['stargazers_count'])
                print("\tForks : ", repo['forks'])

        else:
            print("[ERROR] : Can't Fetch "+user+" repository data due to some reason!")

    else:
        print("[ERROR] : Can't Fetch "+user+" Profile data due to some reason!")



if __name__ == "__main__":
    main()

