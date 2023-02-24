from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salary = 0
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            if int(job["max_salary"]) > salary:
                salary = int(job["max_salary"])

    return salary


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salary = 1000000000000000000000000
    for job in jobs:
        if job["min_salary"] != "" and job["max_salary"] != "invalid":
            if int(job["min_salary"]) < salary:
                salary = int(job["min_salary"])

    return salary


def validate_type(valor: Union[int, str]):
    if type(valor) == int:
        return True
    elif type(valor) == str:
        return valor.isdigit()
    else:
        return False


def validate_params(job: Dict, salary: Union[int, str]):
    if not validate_type(job["min_salary"]):
        raise ValueError

    if not validate_type(job["max_salary"]):
        raise ValueError

    if not validate_type(salary):
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    validate_params(job, salary)

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError

    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True
    else:
        return False


def validate_erro(job: Dict, salary: Union[int, str]):
    try:
        return matches_salary_range(job, salary)
    except ValueError:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    list = []
    for job in jobs:
        if validate_erro(job, salary):
            list.append(job)

    return list
