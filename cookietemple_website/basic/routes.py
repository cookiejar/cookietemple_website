from flask import render_template, redirect, url_for
import json

from cookietemple_website.basic import bp


@bp.route('/')
def root():
    return redirect((url_for('basic.index')))


@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/templates')
def dev():
    return render_template('templates.html')


@bp.route('/join')
def join():
    return render_template('join.html')


@bp.route('/stats')
def stats():
    with open('commits_per_day.json', 'r') as file:
        commits = json.load(file)
    with open('open_prs_per_day.json', 'r') as file:
        open_prs = json.load(file)
    with open('closed_prs_per_day.json', 'r') as file:
        closed_prs = json.load(file)
    return render_template('stats.html', commits_data=json.dumps(commits, default=lambda x: x.__dict__),
                           open_pr_data=json.dumps(open_prs, default=lambda x: x.__dict__), closed_pr_data=json.dumps(closed_prs, default=lambda x: x.__dict__))


@bp.route('/code_of_conduct')
def code_of_conduct():
    return render_template('code_of_conduct.html')


@bp.route('/ourstory')
def story():
    return render_template('ourstory.html')


@bp.route('/showoff')
def showoff():
    return render_template('showoff.html')
