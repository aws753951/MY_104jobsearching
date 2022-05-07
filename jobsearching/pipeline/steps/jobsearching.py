import requests
from bs4 import BeautifulSoup
import pandas as pd
from .step import Step

class JobSearching(Step):
    def process(self, data, inputs):
        colname = ['公司網址', '工作名稱', '公司名稱', '工作地點', '經歷', '學歷', '薪水', '刊登日期','工作描述']
        contents = []
        for i in range(1,2):
            url = inputs['url']
            r = requests.get(url)
            print(i)
            if r.status_code == requests.codes.ok:
                r.encoding = 'utf-8'
                soup = BeautifulSoup(r.text, 'html.parser')
                spans = soup.find_all('div', class_='b-block__left')[3:]
                for span in spans:
                    job_url = span.find('a').get('href')
                    job = span.find('a')
                    company = job.find_next('a')
                    details = span.find(class_='b-list-inline b-clearfix job-list-intro b-content')
                    where = details.find('li')
                    exp = where.find_next('li')
                    degree = exp.find_next('li')
                    descriptions = span.find(class_='job-list-item__info b-clearfix b-content')
                    salary = span.find(class_='b-tag--default')
                    date = span.find(class_='b-tit__date')
                    try:
                        contents.append([job_url, job.text, company.text, where.text, exp.text, degree.text, salary.text, date.text, descriptions.text])
                    except AttributeError:
                        print(job_url)
                        continue
        print(contents)
        return contents


        # df = pd.DataFrame(contents, columns=colname)
        # df.to_excel('jobs_investment.xlsx', index=False)

