from app.Multivalued_Dictionary import MultiValuedDictionary
import io, sys
import unittest.mock


class IntegrationTestMultivaluedDictionary(unittest.TestCase):

    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def clearCapturedOutput(self):
        self.capturedOutput.truncate(0)
        self.capturedOutput.seek(0)

    def getCapturedOutputValue(self):
        value = self.capturedOutput.getvalue()
        self.clearCapturedOutput()
        return value

    def test_Keys(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'ADD baz bang'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), 'foo\nbaz\n')

    def test_Members(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'MEMBERS foo'.split()
        dictionary.members(command)
        self.assertEqual(self.getCapturedOutputValue(), 'bar\n')

        command = 'MEMBERS bad'.split()
        dictionary.members(command)
        self.assertEqual(self.getCapturedOutputValue(), "Error, key doesn't exits\n")

    def test_Add(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'ADD foo baz'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Error, Member already exists for the key\n')

    def test_Remove(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'ADD foo baz'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'REMOVE foo bar'.split()
        dictionary.remove(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Removed\n')

        command = 'REMOVE foo bar'.split()
        dictionary.remove(command)
        self.assertEqual(self.getCapturedOutputValue(), 'ERROR, Member does not exist in the key\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), 'foo\n')

        command = 'REMOVE foo baz'.split()
        dictionary.remove(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Removed\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), '(empty set)\n')

        command = 'REMOVE boom pow'.split()
        dictionary.remove(command)
        self.assertEqual(self.getCapturedOutputValue(), 'ERROR, key does not exist\n')

    def test_Removeall(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'ADD foo baz'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), 'foo\n')

        command = 'REMOVEALL foo'.split()
        dictionary.removeall(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Removed\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), '(empty set)\n')

        command = 'REMOVEALL foo'.split()
        dictionary.removeall(command)
        self.assertEqual(self.getCapturedOutputValue(), 'ERROR, key does not exist\n')

    def test_Clear(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'ADD bang zip'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), 'foo\nbang\n')

        dictionary.clear()
        self.assertEqual(self.getCapturedOutputValue(), 'Cleared\n')

        dictionary.keys()
        self.assertEqual(self.getCapturedOutputValue(), '(empty set)\n')

    def test_KEYEXISTS(self):
        dictionary = MultiValuedDictionary()

        command = 'KEYEXISTS foo'.split()
        dictionary.keyexists(command)
        self.assertEqual(self.getCapturedOutputValue(), 'False\n')

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'KEYEXISTS foo'.split()
        dictionary.keyexists(command)
        self.assertEqual(self.getCapturedOutputValue(), 'True\n')

    def test_MEMBEREXISTS(self):
        dictionary = MultiValuedDictionary()

        command = 'MEMBEREXISTS foo bar'.split()
        dictionary.memberexists(command)
        self.assertEqual(self.getCapturedOutputValue(), 'False\n')

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        command = 'MEMBEREXISTS foo bar'.split()
        dictionary.memberexists(command)
        self.assertEqual(self.getCapturedOutputValue(), 'True\n')

        command = 'MEMBEREXISTS foo baz'.split()
        dictionary.memberexists(command)
        self.assertEqual(self.getCapturedOutputValue(), 'False\n')

    def test_allMembers(self):
        dictionary = MultiValuedDictionary()

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        dictionary.allmembers()
        self.assertEqual(self.getCapturedOutputValue(), 'bar\n')

    def test_items(self):
        dictionary = MultiValuedDictionary()

        dictionary.items()
        self.assertEqual(self.getCapturedOutputValue(), '(empty set)\n')

        command = 'ADD foo bar'.split()
        dictionary.add(command)
        self.assertEqual(self.getCapturedOutputValue(), 'Added\n')

        dictionary.items()
        self.assertEqual(self.getCapturedOutputValue(), '1) foo : bar\n')


if __name__ == '__main__':
    """
    Testing the application end to end
    """
    unittest.main()
