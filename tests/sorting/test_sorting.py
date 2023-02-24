import pytest
from datetime import date
from src.pre_built.sorting import sort_by


@pytest.fixture
def list():
    return [
        {
            "date_posted": date.fromisoformat("2020-05-07"),
            "min_salary": 1500,
            "max_salary": 2000,
        },
        {
            "date_posted": date.fromisoformat("2020-05-10"),
            "min_salary": 4000,
            "max_salary": 5000,
        },
        {
            "date_posted": date.fromisoformat("2020-05-09"),
            "min_salary": 2000,
            "max_salary": 3000,
        },
        {
            "date_posted": date.fromisoformat("2020-05-08"),
            "min_salary": 1000,
            "max_salary": 2500,
        },
    ]


def test_sort_by_criteria(list):

    sort_by(list, "min_salary")
    assert list[0]["min_salary"] == 1000

    sort_by(list, "max_salary")
    assert list[0]["max_salary"] == 5000

    sort_by(list, "date_posted")
    assert list[0]["date_posted"] == date.fromisoformat("2020-05-10")
