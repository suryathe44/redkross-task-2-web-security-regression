import csv
import json
from pathlib import Path

CASES = list(csv.DictReader((Path(__file__).parents[1] / "data/local_api_test_cases.csv").open(encoding="utf-8")))

def test_assigned_api_cases(client):
    """Execute the five individual cases supplied for intern 2418."""
    for case in CASES:
        payload = json.loads(case["payload"]) if case["payload"] else None
        # The supplied CSV uses a human-readable placeholder for API-04.
        # Expand it into the actual 500-character test value.
        if case["test_id"] == "API-04":
            payload = {"display_name": "x" * 500}
        if case["test_id"] == "API-01":
            response = client.get(case["path"])
        else:
            response = client.post(case["path"], json=payload)
        expected = case["expected_status"]
        if expected == "200_or_documented":
            assert response.status_code == 200, f"{case['test_id']}: {response.get_json()}"
        else:
            assert response.status_code == int(expected), f"{case['test_id']}: {response.get_json()}"


def test_profile_trims_whitespace(client):
    response = client.post("/profile", json={"display_name": "  Rohan  "})
    assert response.status_code == 200
    assert response.get_json()["display_name"] == "Rohan"


def test_profile_rejects_unexpected_fields(client):
    response = client.post("/profile", json={"display_name": "Rohan", "is_admin": True})
    assert response.status_code == 400


def test_profile_rejects_non_object_json(client):
    response = client.post("/profile", data='["not", "an", "object"]', content_type="application/json")
    assert response.status_code == 400
