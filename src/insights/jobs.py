from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        list = [job for job in jobs]
        return list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    list = []
    for job in jobs:
        if job["job_type"] not in list:
            list.append(job["job_type"])

    return list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list = [job for job in jobs if job["job_type"] == job_type]

    return list
