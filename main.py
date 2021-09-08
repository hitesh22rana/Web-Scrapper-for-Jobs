from bs4 import BeautifulSoup
import requests
import time
import lxml

# Filtering out some information

print("Put some skills that you are not familiar with")
unfamiliar_skills = list(map(str,input("> ").split()))


print("Filtering out :",end = " ")
for item in unfamiliar_skills:
    print(item,end = " ")
print(" ")

# Skills Checker

def check(skills):
    for item in unfamiliar_skills:
        if item in skills:
            return False
            break
        else:
            continue
    return True

# job Finder

def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')

    jobs = soup.find_all("li",class_ = "clearfix job-bx wht-shd-bx")

    # To avoid empty white spaces we can use replace method

    for index,job in enumerate(jobs):
        published_date = job.find("span",class_ = "sim-posted").span.text

        # Checking for the published date
        if "few" in published_date:
            company_name = job.find("h3",class_ = "joblist-comp-name").text.replace(' ','')
            
            # Bringing the skills requirement
            skills = job.find("span",class_ = "srp-skills").text.replace(' ','')

            # For more information

            more_info = job.header.h2.a["href"]
            skills_check = check(skills)

            if(skills_check == True):
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"company name : {company_name.strip()}")
                    f.write("\n")
                    f.write("\n")
                    f.write(f"Required Skills : {skills.strip()}")
                    f.write("\n")
                    f.write("\n")
                    f.write(f"More Info : {more_info}")
            print(f"File Saved : {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)
