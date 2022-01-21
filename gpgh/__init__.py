import collections
import concurrent.futures

__all__ = (
    'get_repos',
    'load_pulls',
    'filter_none',
    'count_attr',
)


def get_repos(org):
    """
    Get organization repositories.
    """

    return list(org.get_repos())


def load_pulls(repos):
    """
    Load pull requests for each repo in parallel.
    """

    def fetch_pulls(repo):
        repo.pulls = list(repo.get_pulls())
        repo.pulls_count = len(repo.pulls)
        return repo

    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(fetch_pulls, repo) for repo in repos]
        for future in concurrent.futures.as_completed(futures):
            result.append(future.result())

    return result


def filter_none(iterable, attr):
    """
    Return only objects with non nullable attr.
    """

    return [obj for obj in iterable if getattr(obj, attr) is not None]


def get_top(iterable, top_by=None, top_num=None):
    """
    Return top objects (by attr value) from collection.
    """

    return sorted(iterable, key=top_by, reverse=True)[:top_num]


def count_attr(iterable, attr):
    """
    Count attr value for each object from iterable.
    """

    result = collections.defaultdict(int)
    for obj in iterable:
        result[getattr(obj, attr)] += 1

    return result
