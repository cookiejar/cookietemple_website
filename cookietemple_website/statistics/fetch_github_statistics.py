#!/usr/bin/env python3
from github import Github
from collections import OrderedDict
import json


def fetch_ct_commits() -> None:
    """
    Fetch all commits to cookietemple repository.
    """
    token = "the_very_secret_token"
    g = Github(token)
    repo = g.get_repo('cookiejar/cookietemple')
    commits = repo.get_commits()
    commit_dict = OrderedDict()

    for commit in commits:
        if commit.commit is not None:
            commit_date = commit.commit.author.date
            date = str(commit_date).split(' ')[0]
            try:
                commit_dict[date] += 1
            except KeyError:
                commit_dict[date] = 1
    write_commits_to_json(commit_dict)


def write_commits_to_json(commits_per_day: OrderedDict) -> None:
    """
    Write the commits date and number to a local .json file
    """
    with open('commits_per_day.json', 'w', encoding='utf-8') as f:
        json.dump(commits_per_day, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    fetch_ct_commits()

