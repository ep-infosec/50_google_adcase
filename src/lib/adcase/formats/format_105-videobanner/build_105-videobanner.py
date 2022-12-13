# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Executes a build process for a format.
"""
import os
from lib.adcase import helper as f
# pylint: disable=line-too-long


def build(req):
  """Builder for this format.

  Args:
    req: flask request

  Returns:
    Json containing the creative data
  """
  current_path = os.path.dirname(__file__)

  errors = []
  v = {}
  tdir = "/tmp/" + f.get_tmp_file_name()
  index = f.file_get_contents(current_path + "/index_105-videobanner.html")

  ext = f.get_ext(req.files["videofile"].filename)
  if ext != "mp4":
    return {"errors": ["Only mp4 files allowed"]}

  f.save_file(req.files["videofile"], tdir + "/video.mp4")

  return {"errors": errors, "dir": tdir, "index": index, "vars": v}
