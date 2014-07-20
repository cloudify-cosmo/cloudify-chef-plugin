########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
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


__author__ = 'dank'

import setuptools

<<<<<<< HEAD
PLUGIN_COMMONS_VERSION = '3.0'
PLUGIN_COMMONS_BRANCH = '3.0'
PLUGIN_COMMONS = 'https://github.com/cloudify-cosmo/cloudify-plugins-common' \
    '/tarball/{0}'.format(PLUGIN_COMMONS_BRANCH)
=======
from chef_plugin import get_version

>>>>>>> 1.0

setuptools.setup(
    zip_safe=False,
    name='cloudify-chef-plugin',
    version=get_version(),
    author='ilya',
    author_email='ilya.sher@coding-knight.com',
    packages=['chef_plugin'],
    license='LICENSE',
    description='Cloudify Chef plugin',
    install_requires=[
        'cloudify-plugins-common>=3.0',
        'requests',
    ],
    package_data={
        'chef_plugin': [
            'chef/handler/cloudify_attributes_to_json_file.rb',
            'VERSION'
        ]
    },
)
