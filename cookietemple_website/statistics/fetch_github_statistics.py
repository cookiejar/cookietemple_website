#!/usr/bin/env python3
from github import Github
import json


def fetch_ct_commits() -> None:
    """
    Fetch all commits to cookietemple repository.
    """
    token = "the_very_secret_token"
    g = Github(token)
    repo = g.get_repo('cookiejar/cookietemple')
    commits = repo.get_commits()
    commit_dict = dict()

    for commit in commits:
        if commit.commit is not None:
            commit_date = commit.commit.author.date
            date = str(commit_date).split(' ')[0]
            try:
                commit_dict[date] += 1
            except KeyError:
                commit_dict[date] = 1
    # sort the commit dict by date in ascending order
    commit_list = sorted(list(commit_dict.items()))
    # convert to dict for easier JSON dumping
    commit_dict = dict(commit_list)
    # sum up all commits made up to (including) a date
    sum_commits_until_date(commit_dict)
    # dump data to json file to plot at stats subpage
    write_commits_to_json(commit_dict)


def sum_commits_until_date(commits: dict) -> None:
    """
    For each date, calculate total sum of commits up to (and including) this date
    :param commits: The commit date associated with the number of total commits per date
    """
    key_list = list(commits.keys())
    for i in range(1, len(key_list)):
        commits[key_list[i]] += commits[key_list[i - 1]]


def write_commits_to_json(commits_per_day: dict) -> None:
    """
    Write the commits date and number to a local .json file
    """
    with open('commits_per_day.json', 'w', encoding='utf-8') as f:
        json.dump(commits_per_day, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    fetch_ct_commits()
