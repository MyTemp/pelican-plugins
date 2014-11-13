import unittest
from __init__ import CommonMarkReader


class SmokeTest(unittest.TestCase):
    EXPECTED_METADATA = {'key1': 'value1',
                         'key2': 'value2'}
    EXPECTED_HTML = '''<div>
<div>
<h2>header</h2>
<p>paragraph</p>
</div>
<div>
<p>paragraph</p>
</div>
</div>
'''

    def setUp(self):
        self.reader = CommonMarkReader({})
        self.content, self.metadata = self.reader.read('./test.md')

    def testMetadataShouldBeParsed(self):
        self.assertEqual(self.metadata, self.EXPECTED_METADATA)

    def testMarkdownInBlockTagsShouldBeParsed(self):
        self.assertEqual(self.content, self.EXPECTED_HTML)
