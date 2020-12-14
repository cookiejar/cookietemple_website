from cookietemple_website.statistics.fetch_github_statistics import (fetch_ct_commits, fetch_ct_pr_issue_stats)
from cookietemple_website.statistics.fetch_discord_statistics import fetch_cookiejar_server_member

"""
The main script to fetch all statistics of cookietemple once per day!
"""
if __name__ == '__main__':
    fetch_ct_commits()
    fetch_ct_pr_issue_stats(gh_item='issue')
    fetch_ct_pr_issue_stats(gh_item='pr')
    fetch_cookiejar_server_member()
