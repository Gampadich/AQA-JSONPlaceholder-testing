import allure
import requests

@allure.epic('API test')
@allure.feature('API Get test')
@allure.story('Get /posts test')
def test_get_all(url):
    result = requests.get(f'{url}/posts')
    assert result.status_code == 200
    print(result.json())
