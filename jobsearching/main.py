import sys

sys.path.append('../')

from jobsearching.pipeline.steps.jobsearching import JobSearching
from jobsearching.pipeline.pipeline import Pipeline


def main():
    inputs = {
        'url': 'https://www.104.com.tw/jobs/search/?ro=0&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
    }

    steps = [
        JobSearching(),
    ]

    p = Pipeline(steps)
    p.run(inputs)

if __name__ == '__main__':
    main()