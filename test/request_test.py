import pytest
from src.request import get_info_by_page


def test_get_all_info():
    # Given

    page = 1

    #When
    response = get_info_by_page(page)

    hits = response.json()['hits']['hits']

    #Then
    assert response.status_code == 200