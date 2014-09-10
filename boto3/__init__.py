# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import logging

from boto3.session import Session


__author__ = 'Amazon Web Services'
__version__ = '0.0.1'


# The default Boto3 session; autoloaded when needed.
DEFAULT_SESSION = None

def setup_default_session(**kwargs):
    """
    Set up a default session, passing through any parameters to the session
    constructor. There is no need to call this unless you wish to pass custom
    parameters, because a default session will be created for you.
    """
    global DEFAULT_SESSION
    DEFAULT_SESSION = Session(**kwargs)

def _get_default_session():
    """
    Get the default session, creating one if needed.

    :rtype: boto3.session.Sesssion
    :return: The default session
    """
    if DEFAULT_SESSION is None:
        setup_default_session()

    return DEFAULT_SESSION

def client(service):
    """
    Create a low-level service client by name using the default session.

    :type service: string
    :param service: The name of a service, e.g. 's3' or 'ec2'

    :return: Service client instance
    """
    return _get_default_session().client(service)

def resource(service):
    """
    Create a resource service client by name using the default session.

    :type service: string
    :param service: The name of a service, e.g. 's3' or 'ec2'

    :return: Resource client instance
    """
    return _get_default_session().resource(service)

# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('boto3').addHandler(NullHandler())