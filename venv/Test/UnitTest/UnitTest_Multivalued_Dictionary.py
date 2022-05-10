import io
import unittest.mock
from app.Multivalued_Dictionary import MultiValuedDictionary


class TestMultivaluedDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = MultiValuedDictionary()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_adding_member_successfully(self, mock_stdout):
        """
            Test Add member feature
        """
        command = 'ADD foo bar'.split(' ')
        self.dictionary.add(command)
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar'}})
        self.assertEqual(mock_stdout.getvalue(), 'Added\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handles_adding_existing_member(self, mock_stdout):
        """
            Test to throw an error if an existing member is added
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'ADD foo bar'.split(' ')
        self.dictionary.add(command)
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar'}})
        self.assertEqual(mock_stdout.getvalue(), 'Error, Member already exists for the key\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_removeall_keys_successfully(self, mock_stdout):
        """
            Test Removeall  feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar', 'baz'}
        command = 'REMOVEALL foo'.split(' ')
        self.dictionary.removeall(command)
        self.assertEqual(self.dictionary.multivalued_dictionary, {})
        self.assertEqual(mock_stdout.getvalue(), 'Removed\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_removeall_for_nonexisting_keys(self, mock_stdout):
        """
            Test to throw an error if a non-existing key is removed
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'REMOVEALL boo'.split(' ')
        self.dictionary.removeall(command)
        self.assertEqual(mock_stdout.getvalue(), 'ERROR, key does not exist\n')
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar'}})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_member_successfully(self, mock_stdout):
        """
            Test remove member feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar', 'baz'}
        command = 'REMOVE foo bar'.split(' ')
        self.dictionary.remove(command)
        self.assertEqual(mock_stdout.getvalue(), 'Removed\n')
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'baz'}})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_remove_non_existing_members(self, mock_stdout):
        """
            Test to throw an error if a non-existing member is removed
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar', 'baz'}
        command = 'REMOVE foo boo'.split(' ')
        self.dictionary.remove(command)
        self.assertEqual(mock_stdout.getvalue(), 'ERROR, Member does not exist in the key\n')
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar', 'baz'}})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_remove_non_existing_key(self, mock_stdout):
        """
            Test to throw an error if a non-existing key is removed
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar', 'baz'}
        command = 'REMOVE boo bar'.split(' ')
        self.dictionary.remove(command)
        self.assertEqual(mock_stdout.getvalue(), 'ERROR, key does not exist\n')
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar', 'baz'}})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_key_if_all_members_removed_successfully(self, mock_stdout):
        """
            Test to remove key if all members in that key are removed
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'REMOVE foo bar'.split(' ')
        self.dictionary.remove(command)
        self.assertEqual(mock_stdout.getvalue(), 'Removed\n')
        self.assertEqual(self.dictionary.multivalued_dictionary, {})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_keyexists_successfully(self, mock_stdout):
        """
                Test key exists feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'KEYEXISTS foo'.split(' ')
        self.dictionary.keyexists(command)
        self.assertTrue(mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_key_does_not_exists(self, mock_stdout):
        """
            Test key exists feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'KEYEXISTS boo'.split(' ')
        self.dictionary.keyexists(command)
        self.assertEqual(mock_stdout.getvalue(), 'False\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_memberexists_successfully(self, mock_stdout):
        """
            Test member exists feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'MEMBEREXISTS foo bar'.split(' ')
        self.dictionary.memberexists(command)
        self.assertTrue(mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_non_existing_member(self, mock_stdout):
        """
            Test member exists feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'MEMBEREXISTS bar bar'.split(' ')
        self.dictionary.memberexists(command)
        self.assertEqual(mock_stdout.getvalue(), 'False\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_member_successfully(self, mock_stdout):
        """
            Test member feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'MEMBERES foo'.split(' ')
        self.dictionary.members(command)
        self.assertEqual(mock_stdout.getvalue(), 'bar\n')
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar'}})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_non_existing_key(self, mock_stdout):
        """
            Test member if a non-existing key is passed as a param
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        command = 'MEMBERES boo'.split(' ')
        self.dictionary.members(command)
        self.assertEqual(mock_stdout.getvalue(), "Error, key doesn't exits\n")
        self.assertEqual(self.dictionary.multivalued_dictionary, {'foo': {'bar'}})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_keys_successfully(self, mock_stdout):
        """
            Test keys feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        self.dictionary.multivalued_dictionary['baz'] = {'bang'}
        self.dictionary.keys()
        self.assertEqual(mock_stdout.getvalue(), "foo\nbaz\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_zero_keys(self, mock_stdout):
        """
            Test zero existing keys
        """
        self.dictionary.multivalued_dictionary = {}
        self.dictionary.keys()
        self.assertEqual(mock_stdout.getvalue(), "(empty set)\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_allmembers_successfully(self, mock_stdout):
        """
            Test all members feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        self.dictionary.multivalued_dictionary['bang'] = {'bar'}
        self.dictionary.allmembers()
        self.assertEqual(mock_stdout.getvalue(), "bar\nbar\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_allmembers_with_no_members(self, mock_stdout):
        """
           Test all members to handle if no members exists
        """
        self.dictionary.multivalued_dictionary = {}
        self.dictionary.allmembers()
        self.assertEqual(mock_stdout.getvalue(), "(empty set)\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_items_successfully(self, mock_stdout):
        """
           Test Items feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        self.dictionary.items()
        self.assertEqual(mock_stdout.getvalue(), "1) foo : bar\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_items_with_no_items(self, mock_stdout):
        """
           Test Items feature if no items exists
        """
        self.dictionary.multivalued_dictionary = {}
        self.dictionary.items()
        self.assertEqual(mock_stdout.getvalue(), "(empty set)\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_clear_successfully(self, mock_stdout):
        """
           Test Clear feature
        """
        self.dictionary.multivalued_dictionary['foo'] = {'bar'}
        self.dictionary.clear()
        self.assertEqual(mock_stdout.getvalue(), "Cleared\n")
        self.assertEqual(self.dictionary.multivalued_dictionary, {})


if __name__ == '__main__':
    unittest.main()
