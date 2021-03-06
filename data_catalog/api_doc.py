#
# Copyright (c) 2015 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Endpoint serving Data Catalog's Swagger documentation.
"""

import os
import json

from flask_restful import Resource


class ApiDoc(Resource):
    """
    Imports Swagger 2.0 json from file and creates endpoint with imported data.
    """

    def __init__(self):
        super(ApiDoc, self).__init__()
        json_path = os.path.join(os.path.dirname(__file__), '../api_doc.json')
        with open(json_path) as api_doc:
            self.data = json.load(api_doc)

    def get(self):
        """
        Flask-Restful HTTP GET.
        """
        return self.data
