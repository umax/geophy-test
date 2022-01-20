import click

import gpgh


@click.command(help='Show top GitHub repos and its langs of organization.')
@click.option('--token', required=True, help='Your GitHub API token.')
@click.option('--org', required=True, help='GitHub organization ID.')
@click.option('--top-repos', required=True, type=int,
              help='Number of repositories to show')
@click.option('--top-langs', required=True, type=int,
              help='Number of languages to show for each repo.')
def print_metrics(token, org, top_repos, top_langs):
    pass


if __name__ == '__main__':
    print_metrics()
