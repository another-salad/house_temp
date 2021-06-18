"""Test cases for the Requester class and its methods"""

from unittest import mock, main, TestCase

from tests.base_requester_tests import _TestCaseRequesterExceptionsMixin, _TestCaseRequesterReturnValuesMixin, _TestCaseParameterMixin, \
    _TestCaseReturnValuesHTTPErrorMixin

default_mock = mock.Mock(status_code=200, content=b'{"foo": "bar"}')
non_200_mock = mock.Mock(status_code=500, text='foo')


@mock.patch("requests.post", return_value=default_mock)
class TestCaseRequesterReturnValuesPost(_TestCaseRequesterReturnValuesMixin, TestCase):
    """Return value test cases for requests.post method"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.test_kwargs = super().test_kwargs | {"method": 1}


@mock.patch("requests.get", return_value=default_mock)
class TestCaseRequesterReturnValuesGet(_TestCaseRequesterReturnValuesMixin, TestCase):
    """Return value test cases for requests.get method"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.test_kwargs = super().test_kwargs | {"method": 0}


@mock.patch("requests.post", return_value=default_mock)
class TestCaseRequesterExceptionsPost(_TestCaseRequesterExceptionsMixin, TestCase):
    """Exceptions test cases for requests.post method"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.test_kwargs = super().test_kwargs | {"method": 1}


@mock.patch("requests.get", return_value=default_mock)
class TestCaseRequesterExceptionsGet(_TestCaseRequesterExceptionsMixin, TestCase):
    """Exceptions test cases for requests.get method"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.test_kwargs = super().test_kwargs | {"method": 0}


class TestCaseInvalidParameters(_TestCaseParameterMixin, TestCase):
    """Invalid params test cases"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)


@mock.patch("requests.get", return_value=non_200_mock)
class TestCaseHTTPNonOKGet(_TestCaseReturnValuesHTTPErrorMixin, TestCase):
    """Non HTTP 200 response cases for requests.get method"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.test_kwargs = super().test_kwargs | {"method": 0}


@mock.patch("requests.post", return_value=non_200_mock)
class TestCaseHTTPNonOKPost(_TestCaseReturnValuesHTTPErrorMixin, TestCase):
    """Non HTTP 200 response cases for requests.post method"""

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.test_kwargs = super().test_kwargs | {"method": 1}


if __name__ == '__main__':
    main()
