import pytest
import allure

@allure.step('Get API URL')
@pytest.fixture(scope='session')
def url():
    return 'https://jsonplaceholder.typicode.com'
