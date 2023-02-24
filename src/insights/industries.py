from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    list = []
    for job in jobs:
        if job["industry"] not in list and job["industry"] != "":
            list.append(job["industry"])

    return list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list = [job for job in jobs if job["industry"] == industry]

    return list
