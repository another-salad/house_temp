"""Test cases for the Requester class and its methods"""
#pylint: disable=wrong-import-position, disable=unused-argument

from unittest import TestCase, mock, main

from sys import path
path.append("..")
from common.requester import Requester


@mock.patch("common.requester.Requester.request", return_value=tuple([False, {"foo": "bar"}]))
class TestCaseRequesterReturnTypes(TestCase):
    """Test cases for the Requester class and its methods"""

    test_kwargs = {"method": 1, "uri": "0.0.0.0"}

    def test_request_return_tuple(self, mocked_output):
        """Tests a tuple is returned from requester method"""
        actual_result = Requester().request(**self.test_kwargs)
        self.assertIsInstance(actual_result, tuple)

    def test_request_return_tuple_len(self, mocked_output):
        """Tests the returned tuple has a len of 2"""
        actual_result = Requester().request(**self.test_kwargs)
        self.assertEqual(len(actual_result), 2)

    def test_request_first_value_bool(self, mocked_output):
        """Tests the first return value is a bool"""
        actual_result = Requester().request(**self.test_kwargs)[0]
        self.assertIsInstance(actual_result, bool)

    def test_request_second_value_dict(self, mocked_output):
        """Tests the second return value is a dictionary"""
        actual_result = Requester().request(**self.test_kwargs)[1]
        self.assertIsInstance(actual_result, dict)

if __name__ == '__main__':
    main()
