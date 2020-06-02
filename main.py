import os
import csv
import requests
from bs4 import BeautifulSoup
from save import save_to_file

os.system("clear")
#request to main page
alba_url = "http://www.alba.co.kr"
result = requests.get(alba_url)
brands = BeautifulSoup(result.text, "html.parser").find_all("ul", {"class":"goodsBox"})[1].find_all("li")

#each brand
for brand in brands[1:]:
  arr = []
  save = True
  company_tag = brand.a.find("span", {"class":"company"})
  if isinstance(company_tag, type(None)):
    continue
  company = company_tag.string
  company_url = brand.a["href"]
  res = requests.get(company_url)
  soup = BeautifulSoup(res.text, "html.parser")
  brand_jobs = soup.table.find_all("tr", {"class": ""})
  print("---", company)
  
  #each job
  for (i, job) in enumerate(brand_jobs[1:]):
    tmp = job.find("td", {"class":"local"})
    if isinstance(tmp, type(None)):
      save = False
      continue
    place = job.find("td", {"class":"local"}).get_text()
    title = job.find("td", {"class":"title"}).a.find("span", {"class":"company"}).string.strip()
    time = job.find("td", {"class":"data"}).get_text()
    pay = job.find("td", {"class":"pay"}).get_text()
    date = job.find("td", {"class":"regDate"}).get_text()
    arr.append({"index":i+1,"place":place, "title":title, "time":time, "pay":pay, "date":date})
  if save is True:
    save_to_file(arr, company)