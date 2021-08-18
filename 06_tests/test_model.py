"""
  Aaron's MLOps and DevSecOps Baseline Project
  Copyright (C) 2021  Aaron Elliott

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as published
  by the Free Software Foundation, either version 3 of the License, or
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

  You may contact Aaron Elliott at mraarone@yahoo.com.
"""

import requests
import json


def pretty_print_request(request):
    print(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "-----------Request----------->",
            request.method + " " + request.url,
            "\n".join("{}: {}".format(k, v) for k, v in request.headers.items()),
            request.body,
        )
    )


def pretty_print_response(response):
    print(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "<-----------Response-----------",
            "Status code:" + str(response.status_code),
            "\n".join("{}: {}".format(k, v) for k, v in response.headers.items()),
            response.text,
        )
    )


def test_model():
    url = "http://localhost:8000/predict"

    # Additional headers.
    headers = {"Content-Type": "application/json"}

    # Body
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.8,
        "petal_length": 1.9,
        "petal_width": 0.4,
    }

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body["prediction"] == "setosa"

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)
