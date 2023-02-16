from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, mode="r") as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        list = []
        for job in jobs:
            if job["industry"] not in list and job["industry"] != "":
                list.append(job["industry"])

        return list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list = [job for job in jobs if job["industry"] == industry]

    return list
