#!/usr/bin/env python3
from github import Github
import json

# token needed for authentication at github
token = "the_very_secret_token"
g = Github(token)
repo = g.get_repo('cookiejar/cookietemple')


def fetch_ct_pr_issue_stats(gh_item: str) -> None:
    """
    Fetch number of closed and open pull requests to the cookietemple repository per day
    :param gh_item Either Issue or PR indicating the sort of data to be collected
    """
    stats = repo.get_pulls('all') if gh_item == 'pr' else repo.get_issues(state='all')
    open_stats_dict = dict()
    closed_stats_dict = dict()

    for stat in stats:
        if gh_item == 'issue' and stat.pull_request:
            continue
        stat_is_closed = stat.state == 'closed'
        stat_created_date = stat.created_at
        created_date = str(stat_created_date).split(' ')[0]
        # if issue/pr is already closed, add a closed date
        if stat_is_closed:
            stat_closed_date = stat.closed_at
            closed_date = str(stat_closed_date).split(' ')[0]
            try:
                closed_stats_dict[closed_date] += 1
            except KeyError:
                closed_stats_dict[closed_date] = 1
        # for each issue/pr, add its creation date, so it counts to open issues/prs
        try:
            open_stats_dict[created_date] += 1
        except KeyError:
            open_stats_dict[created_date] = 1

    open_stat_per_date = dict()
    for stat in stats:
        if gh_item == 'issue' and stat.pull_request:
            continue
        if stat.state == 'closed':
            stat_created_date = stat.created_at
            created_date = str(stat_created_date).split(' ')[0]
            stat_closed_date = stat.closed_at
            closed_date = str(stat_closed_date).split(' ')[0]
            for date in open_stats_dict.keys():
                if created_date <= date < closed_date:
                    try:
                        open_stat_per_date[date] += 1
                    except KeyError:
                        open_stat_per_date[date] = 1

    # sort the open and closed issues/prs by date in ascending order
    open_stat_list = sorted(list(open_stat_per_date.items()))
    closed_stat_list = sorted(list(closed_stats_dict.items()))
    # convert to dict for easier JSON dumping
    open_stats_dict = dict(open_stat_list)
    closed_stats_dict = dict(closed_stat_list)
    # sum up all closed issues/prs made up to (including) a date
    sum_until_date(closed_stats_dict)
    # dump data to json file to plot at stats subpage
    write_to_json(open_stats_dict, f'open_{gh_item}s')
    write_to_json(closed_stats_dict, f'closed_{gh_item}s')


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
    fetch_ct_commits()
    fetch_ct_pr_issue_stats(gh_item='issue')
    fetch_ct_pr_issue_stats(gh_item='pr')
