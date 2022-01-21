import operator

import click
import github

import gpgh


@click.command(help='Show top GitHub repos and its langs of organization.')
@click.option('--token', required=True, help='Your GitHub API token.')
@click.option('--org-id', required=True, help='GitHub organization ID.')
@click.option('--repos-num', required=True, type=int,
              help='Number of repositories to show')
@click.option('--langs-num', required=True, type=int,
              help='Number of languages to show for each repo.')
def get_metrics(token, org_id, repos_num, langs_num):
    client = github.Github(token, per_page=100)
    org = client.get_organization(org_id)

    print('fetching repos...')
    repos = gpgh.get_repos(org)
    print('fetched %s repos' % len(repos))

    print('fetching pull requests...')
    repos = gpgh.load_pulls(repos)
    repos = gpgh.filter_none(repos, 'language')

    repos = gpgh.get_top(
        repos,
        top_by=operator.attrgetter('pulls_count'),
        top_num=repos_num,
    )
    print(f'Top {len(repos)} repos (by pull requests):')
    for repo in repos:
        print(f'{repo.name} [{repo.pulls_count} pulls]')

    langs = gpgh.count_attr(repos, 'language')
    langs = gpgh.get_top(
        langs.items(),
        top_by=operator.itemgetter(1),
        top_num=langs_num,
    )

    print(f'Top {len(langs)} langs:')
    for lang, repos in langs:
        print(f'{lang} [{repos} repos]')


if __name__ == '__main__':
    get_metrics()
