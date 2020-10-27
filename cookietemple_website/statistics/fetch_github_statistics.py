#!/usr/bin/env python3
from github import Github
import json

# token needed for authentication at github
token = "the_very_secret_token"
g = Github(token)
repo = g.get_repo('cookiejar/cookietemple')


def fetch_ct_pr_stats() -> None:
    """
    Fetch number of closed and open pull requests to the cookietemple repository per day
    """
    pull_requests = repo.get_pulls('all')

    open_pr_dict = dict()
    closed_pr_dict = dict()

    for pr in pull_requests:
        pr_is_closed = pr.state == 'closed'
        # add the creation date of each pr
        pr_created_date = pr.created_at
        created_date = str(pr_created_date).split(' ')[0]
        # if pr is already closed, add a closed date
        if pr_is_closed:
            pr_closed_date = pr.closed_at
            closed_date = str(pr_closed_date).split(' ')[0]
            try:
                closed_pr_dict[closed_date] += 1
            except KeyError:
                closed_pr_dict[closed_date] = 1
        # for each pr, add its creation date, so it counts to open PRs
        try:
            open_pr_dict[created_date] += 1
        except KeyError:
            open_pr_dict[created_date] = 1

    # sort the open and closed prs by date in ascending order
    open_pr_list = sorted(list(open_pr_dict.items()))
    closed_pr_list = sorted(list(closed_pr_dict.items()))
    # convert to dict for easier JSON dumping
    open_pr_dict = dict(open_pr_list)
    closed_pr_dict = dict(closed_pr_list)
    # sum up all closed prs made up to (including) a date
    sum_until_date(closed_pr_dict)
    # dump data to json file to plot at stats subpage
    write_to_json(open_pr_dict, 'open_prs')
    write_to_json(closed_pr_dict, 'closed_prs')


def fetch_ct_commits() -> None:
    """
    Fetch all commits to cookietemple repository.
    """
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
    sum_until_date(commit_dict)
    # dump data to json file to plot at stats subpage
    write_to_json(commit_dict, actions='commits')


def sum_until_date(gh_data: dict) -> None:
    """
    For each date, calculate total sum of actions up to (and including) this date
    :param gh_data: The fetched github data containing dates associated with number of actions (like prs or commits)
    """
    key_list = list(gh_data.keys())
    for i in range(1, len(key_list)):
        gh_data[key_list[i]] += gh_data[key_list[i - 1]]


def write_to_json(actions_per_day: dict, actions: str) -> None:
    """
    Write the actions date and number to a local .json file
    """
    with open(f'{actions}_per_day.json', 'w', encoding='utf-8') as f:
        json.dump(actions_per_day, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    #fetch_ct_commits()
    fetch_ct_pr_stats()
