from src.sorting import sort_by


def data_jobs_sort_by_criteria():
    return [
        {
            "max_salary": 82162,
            "min_salary": 44587,
            "date_posted": "2020-05-08",
        },
        {
            "max_salary": 103279,
            "min_salary": 94715,
            "date_posted": "2020-05-05",
        },
        {
            "max_salary": 212901,
            "min_salary": 125410,
            "date_posted": "2020-04-28",
        },
        {
            "max_salary": 35000,
            "min_salary": 20000,
            "date_posted": "2020-05-07",
        },
    ]


def test_sort_by_criteria():
    content = data_jobs_sort_by_criteria()

    for criteria in ["max_salary", "min_salary", "date_posted"]:
        sort_by(content, criteria)

        if criteria == "min_salary":
            assert content[0][criteria] <= content[1][criteria]
            assert content[1][criteria] <= content[2][criteria]
            assert content[2][criteria] <= content[3][criteria]
        elif criteria == "max_salary":
            assert content[0][criteria] >= content[1][criteria]
            assert content[1][criteria] >= content[2][criteria]
            assert content[2][criteria] >= content[3][criteria]
        else:
            assert content[0][criteria] >= content[1][criteria]
            assert content[1][criteria] >= content[2][criteria]
            assert content[2][criteria] >= content[3][criteria]
