import click
import requests


@click.command()
@click.option('--token', required=True)
@click.option('--org', required=True)
@click.option('--per-page', required=True, type=int, default=100)
@click.option('--limit', required=False, type=int)
def get_repos(token, org, per_page, limit):
    result = []
    while True:
        resp = requests.get(
            'https://api.github.com/orgs/%s/repos' % org,
            headers={
                'authorization': 'token %s' % token,
                'user-agent': 'gpgh-app',
            },
            params={
                'sort': 'full_name',
                'per_page': per_page,
            },
        )
        if resp.status_code != 200:
            raise ValueError

        resp = resp.json()
        if not resp:
            break

        for repo in resp:
            result.append({
                'desc': repo['description'],
                'name': repo['name'],
                'lang': repo['language'],
            })

        if limit and len(result) >= limit:
            break

    for repo in result:
        click.echo(repo['name'])


if __name__ == '__main__':
    get_repos()
