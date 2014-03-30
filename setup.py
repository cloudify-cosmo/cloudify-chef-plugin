__author__ = 'dank'

import setuptools

COSMO_CELERY_VERSION = "0.3"
COSMO_CELERY_BRANCH = "develop"
COSMO_CELERY = "https://github.com/CloudifySource/cosmo-celery-common/tarball/{0}".format(COSMO_CELERY_BRANCH)

setuptools.setup(
    zip_safe=False,
    name='cloudify-chef-plugin',
    version='0.3',
    author='ilya',
    author_email='ilya.sher@coding-knight.com',
    packages=['chef_plugin'],
    license='LICENSE',
    description='Cloudify Chef plugin',
    install_requires=[
        "cosmo-celery-common",
        "requests",
    ],
    package_data={
        'chef_plugin': ['chef/handler/cloudify_attributes_to_json_file.rb']
    },
    dependency_links=["{0}#egg=cosmo-celery-common-{1}".format(COSMO_CELERY, COSMO_CELERY_VERSION)]
)
