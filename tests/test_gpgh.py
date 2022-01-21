import operator
from unittest import mock

import gpgh

__all__ = (
    'TestGetRepos',
    'TestLoadPulls',
    'TestFilterNone',
    'TestGetTop',
    'TestCountAttr',
)


class TestGetRepos:
    def test_ok(self):
        org = mock.Mock()
        org.get_repos.return_value = repos = [1, 2, 3]

        assert gpgh.get_repos(org) == repos


class TestLoadPulls:
    def test_empty(self):
        assert gpgh.load_pulls([]) == []

    def test_ok(self):
        repo1 = mock.Mock()
        repo1.get_pulls.return_value = [1, 2]
        repo2 = mock.Mock()
        repo2.get_pulls.return_value = [3, 4, 5]

        repos = gpgh.load_pulls([repo1, repo2])
        assert len(repos) == 2
        assert repos[0].pulls == [1, 2]
        assert repos[0].pulls_count == 2
        assert repos[1].pulls == [3, 4, 5]
        assert repos[1].pulls_count == 3


class TestFilterNone:
    def test_empty(self):
        assert gpgh.filter_none([], 'attr1') == []

    def test_ok(self):
        obj1 = mock.Mock(lang='python')
        obj2 = mock.Mock(lang=None)
        obj3 = mock.Mock(lang='java')
        assert gpgh.filter_none([obj1, obj2, obj3], 'lang') == [obj1, obj3]


class TestGetTop:
    def test_empty(self):
        assert gpgh.get_top(
            [],
            top_by=operator.attrgetter('attr1'),
            top_num=10,
        ) == []

    def test_getattr_ok(self):
        obj1 = mock.Mock(value=13)
        obj2 = mock.Mock(value=9)
        obj3 = mock.Mock(value=15)
        assert gpgh.get_top(
            [obj1, obj2, obj3],
            top_by=operator.attrgetter('value'),
            top_num=2,
        ) == [obj3, obj1]

    def test_getitem_ok(self):
        obj1 = ('value', 13)
        obj2 = ('value', 9)
        obj3 = ('value', 15)
        assert gpgh.get_top(
            [obj1, obj2, obj3],
            top_by=operator.itemgetter(1),
            top_num=2,
        ) == [obj3, obj1]


class TestCountAttr:
    def test_ok(self):
        obj1 = mock.Mock(lang='python')
        obj2 = mock.Mock(lang='python')
        obj3 = mock.Mock(lang='java')
        obj4 = mock.Mock(lang='python')
        obj5 = mock.Mock(lang='ruby')

        assert gpgh.count_attr([obj1, obj2, obj3, obj4, obj5], 'lang') == {
            'python': 3,
            'java': 1,
            'ruby': 1,
        }
