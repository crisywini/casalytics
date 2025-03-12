import json

import pytest
from src.request import get_info_by_page, save_json_file


def test_get_all_info():
    # Given

    page = 1

    # When
    response = get_info_by_page(page)

    hits = response.json()['hits']['hits']

    # Then
    assert response.status_code == 200


def test_save_json():
    # Given
    page = 1
    response = get_info_by_page(page)
    file_name = "page1.json"

    # When
    save_json_file(file_name, response)

    # Then
    with open(file_name, "r") as file:
        data = json.load(file)

    assert data['hits']['hits'] is not None