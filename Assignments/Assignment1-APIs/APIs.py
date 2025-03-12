import requests
import json

api_url = "https://api.github.com/repos/devkapilbansal/Github-API-Testing"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

rows, cols = (10, 3)
star_array =  [ [0]*cols for i in range(rows)]
i = 0

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value

        #print(i, j)
        #print(star_array[i][j], star_array[i][j+1], star_array[i][j+2])
        #star_array[i][j] = key
        #print(star_array[i][j], star_array[i][j+1])
        #print(star_array)
        #star_array[i][j] = value
        #j+=1
        #star_array[i][j] = value
        #print(i, j)
        #print(star_array[i][j-1], star_array[i][j])
        #print(star_array)
        #print(value)
        if key == 'open_issues_count':
            #j+=1
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/fivethirtyeight/data"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1
        

api_url = "https://api.github.com/repos/censusreporter/censusreporter"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/nprapps/app-template"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/guardian/frontend"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/BloombergGraphics/whatiscode"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/CreateJS/SoundJS"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/photonstorm/phaser"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/acekyd/made-in-nigeria"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1


api_url = "https://api.github.com/repos/EFForg/action-center-platform"
issues_api_url = api_url + "/issues/1"

response = requests.get(api_url)
issue_response = requests.get(issues_api_url)

response = response.json()
issue_response = issue_response.json()

for key, value in response.items():
    if key == 'full_name' or key == 'stargazers_count' or key == 'open_issues_count':
        if key == 'full_name':
            star_array[i][0] = value

        if key == 'stargazers_count':
            star_array[i][1] = value
            
        if key == 'open_issues_count':
            if value > 0:
                for key, value in issue_response.items():
                    if key == 'title':
                        star_array[i][2] = value
            i+=1

#print(star_array)


""" -------------------------------------------------
ansible/ansible, 50751
Bug Issue:
[BUG] Issue with module XYZ
...
-------------------------------------------------- """



print('-------------------------------------------------')
i = 0
while (i < 10):
    print(star_array[i][0], ", ", star_array[i][1])
    print('Bug Issue:')
    print (star_array[i][2])
    print('...')
    print('-------------------------------------------------')
    i += 1