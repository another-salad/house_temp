"""Base classes for Requester class tests"""
#pylint: disable=wrong-import-position, disable=wrong-import-position, disable=unused-argument
from copy import deepcopy
from sys import path
from requests import exceptions

from tests import BASE_TEST_KWARGS

path.append("..")
from common.exceptions import InvalidParameterError
from common.requester import Requester

class _TestCaseRequesterReturnValuesMixin:
    """Mixins for the Requester.request return values"""

    test_kwargs = BASE_TEST_KWARGS

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


class _TestCaseRequesterExceptionsMixin:
    """Mixins for the Requester.request Exceptions"""

    test_kwargs = BASE_TEST_KWARGS

    def test_requests_connection_error(self, post_mock):
        """Tests that the requests.exceptions.ConnectionError is caught"""
        post_mock.side_effect = exceptions.ConnectionError()
        try:

            Requester().request(**self.test_kwargs)

        except exceptions.ConnectionError:
            self.fail('Connection error not caught')

    def test_requests_invalid_url_error(self, post_mock):
        """Tests that the requests.exceptions.InvalidURL is caught"""
        post_mock.side_effect = exceptions.InvalidURL()
        try:

            Requester().request(**self.test_kwargs)

        except exceptions.ConnectionError:
            self.fail('InvalidURL error not caught')


class _TestCaseParameterMixin:
    """Mixins for input parameter test cases"""

    test_kwargs = BASE_TEST_KWARGS

    def test_invalid_param_exception_int(self):
        """Tests that an InvalidParameterError is raised when an unknown http method is supplied"""
        exception_kwargs = deepcopy(self.test_kwargs)
        exception_kwargs.update({"method": 3})
        with self.assertRaises(InvalidParameterError):
            Requester().request(**exception_kwargs)

    def test_invalid_param_exception_str(self):
        """Tests that an InvalidParameterError is raised when an unknown http method is supplied"""
        exception_kwargs = deepcopy(self.test_kwargs)
        exception_kwargs.update({"method": "testing"})
        with self.assertRaises(InvalidParameterError):
            Requester().request(**exception_kwargs)

    def test_invalid_param_exception_bool(self):
        """Tests that an InvalidParameterError is raised when an unknown http method is supplied"""
        exception_kwargs = deepcopy(self.test_kwargs)
        exception_kwargs.update({"method": True})
        with self.assertRaises(InvalidParameterError):
            Requester().request(**exception_kwargs)
