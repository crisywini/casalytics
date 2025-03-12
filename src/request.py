import requests
from requests import Response


def get_info_by_page(page: int) -> Response:
    url = "https://search-service.fincaraiz.com.co/api/v1/properties/search"
    data = f"""
        {{
            "query": "",
            "variables": {{
                "rows": 21,
                "params": {{
                    "page": {page},
                    "order": 2,
                    "operation_type_id": 2,
                    "property_type_id": [
                        1,
                        2
                    ],
                    "currencyID": 4,
                    "m2Currency": 4,
                    "projects": false,
                    "locations": [
                        {{
                            "country": [
                                {{
                                    "name": "Colombia",
                                    "id": "858656c1-bbb1-4b0d-b569-f61bbdebc8f0",
                                    "slug": "country-48-colombia"
                                }}
                            ],
                            "name": "Armenia",
                            "location_point": {{
                                "coordinates": [
                                    -75.68052950793465,
                                    4.535830266737521
                                ],
                                "type": "point"
                            }},
                            "id": "0f4c7911-6b55-4242-9c67-4226b7478fa0",
                            "type": "CITY",
                            "slug": [
                                "city-colombia-63-001"
                            ],
                            "estate": {{
                                "name": "Quindio",
                                "id": "209f5ed2-e25b-4039-ad3c-ae18bfceb1a1",
                                "slug": "state-colombia-63-quindio"
                            }}
                        }}
                    ]
                }},
                "page": 1,
                "source": 10
            }}
        }}   
        """
    return  requests.post(url, data=data)

print(get_info_by_page(1))