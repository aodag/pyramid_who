import unittest

class ForbiddenChallengeDeciderTests(unittest.TestCase):

    def _getFUT(self):
        from pyramid_who.classifiers import forbidden_challenger
        return forbidden_challenger

    def _callFUT(self, environ, status, headers):
        return self._getFUT()(environ, status, headers)

    def test_conforms_to_IChallengeDecider(self):
        from repoze.who.interfaces import IChallengeDecider
        self.assertTrue(IChallengeDecider.providedBy(self._getFUT()))

    def test_miss(self):
        self.assertFalse(self._callFUT({}, '200 OK', ()))

    def test_hit(self):
        self.assertTrue(self._callFUT({}, '403 Forbidden', ()))
