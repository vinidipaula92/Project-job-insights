from src.jobs import read


def get_unique_job_types(path):
    content = read(path)
    job_types = []
    for job in content:
        job_types.append(job["job_type"])
    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    content = [job for job in jobs if job["job_type"] == job_type]
    return content


def get_unique_industries(path):
    content = read(path)
    industries = []
    for job in content:
        if job["industry"] != "":
            industries.append(job["industry"])
    return list(set(industries))


def filter_by_industry(jobs, industry):
    content = [job for job in jobs if job["industry"] == industry]
    return content


def get_max_salary(path):
    content = read(path)
    max_salary = {
        int(job["max_salary"])
        for job in content
        if job["max_salary"].isdigit() and int(job["max_salary"]) > 0
    }
    return max(max_salary)


def get_min_salary(path):
    content = read(path)
    min_salary = {
        int(job["min_salary"])
        for job in content
        if job["min_salary"].isdigit() and int(job["min_salary"]) > 0
    }
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(job.get("min_salary")) is not int
        or type(job.get("max_salary")) is not int
        or job.get("min_salary") > job.get("max_salary")
        or type(salary) is not int
    ):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


# Referencia: https://www.w3schools.com/python/ref_dictionary_get.asp


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
