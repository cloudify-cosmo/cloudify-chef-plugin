########
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

import os
import shutil

from path import path

from puppet_plugin.tests.system_tests import resources


def copy_blueprint(workdir, blueprint_dir_name, blueprints_dir=None):
    blueprint_path = path(workdir) / blueprint_dir_name
    shutil.copytree(get_blueprint_path(blueprint_dir_name, blueprints_dir),
                    str(blueprint_path))
    return blueprint_path


def get_blueprint_path(blueprint_name, blueprints_dir=None):
    resources_dir = os.path.dirname(resources.__file__)
    blueprints_dir = blueprints_dir or os.path.join(resources_dir,
                                                    'blueprints')
    return os.path.join(blueprints_dir, blueprint_name)
