import nest
import unittest


class UnitTests(unittest.TestCase):

    def test_get_extra_keys_list(self):
        hierarchy_list = ['currency', 'country', 'city']
        json = [
            {'country': 'US', 'city': 'Boston', 'currency': 'USD', 'amount': 100},
            {'country': 'FR', 'city': 'Paris', 'currency': 'EUR', 'amount': 20},
            {'country': 'FR', 'city': 'Lyon', 'currency': 'EUR', 'amount': 11.4},
            {'country': 'ES', 'city': 'Madrid', 'currency': 'EUR', 'amount': 8.9},
            {'country': 'UK', 'city': 'London', 'currency': 'GBP', 'amount': 12.2},
            {'country': 'UK', 'city': 'London', 'currency': 'FBP', 'amount': 10.9}
        ]
        self.assertEqual(nest.get_extra_keys_list(hierarchy_list, json), ['amount'])

    def test_update(self):
        original_dict = {'EUR': {'ES': {'Madrid': [{'amount': 8.9}]}}}
        new_dict = {'EUR': {'FR': {'Lyon': [{'amount': 11.4}], 'Paris': [{'amount': 20}]}}}
        result = {'EUR': {'ES': {'Madrid': [{'amount': 8.9}]},'FR': {'Lyon': [{'amount': 11.4}], 'Paris': [{'amount': 20}]}}}
        self.assertEqual(nest.update(original_dict, new_dict), result)

    def test_list_to_nested_dict(self):
        input_key_list = ['USD', 'US', 'Boston']
        remainder_dict = {'amount': 100}
        result = {'USD': {'US': {'Boston': [{'amount': 100}]}}}
        self.assertEqual(nest.list_to_nested_dict(input_key_list, remainder_dict), result)

    def test_regroup_json_data(self):
        hierarchy_list = ['currency', 'country', 'city']
        json = [
            {'country': 'US', 'city': 'Boston', 'currency': 'USD', 'amount': 100},
            {'country': 'FR', 'city': 'Paris', 'currency': 'EUR', 'amount': 20},
            {'country': 'FR', 'city': 'Lyon', 'currency': 'EUR', 'amount': 11.4},
            {'country': 'ES', 'city': 'Madrid', 'currency': 'EUR', 'amount': 8.9},
            {'country': 'UK', 'city': 'London', 'currency': 'GBP', 'amount': 12.2},
            {'country': 'UK', 'city': 'London', 'currency': 'FBP', 'amount': 10.9}
        ]
        extra_keys_list = ['amount']
        result = {'EUR':
                      {'ES': {'Madrid': [{'amount': 8.9}]},
                       'FR': {'Lyon': [{'amount': 11.4}], 'Paris': [{'amount': 20}]}},
                  'FBP': {'UK': {'London': [{'amount': 10.9}]}},
                  'GBP': {'UK': {'London': [{'amount': 12.2}]}},
                  'USD': {'US': {'Boston': [{'amount': 100}]}}}
        self.assertEqual(nest.regroup_json_data(json, hierarchy_list, extra_keys_list), result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

