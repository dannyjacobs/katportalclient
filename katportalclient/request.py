###############################################################################
# SKA South Africa (http://ska.ac.za/)                                        #
# Author: cam@ska.ac.za                                                       #
# Copyright @ 2013 SKA SA. All rights reserved.                               #
#                                                                             #
# THIS SOFTWARE MAY NOT BE COPIED OR DISTRIBUTED IN ANY FORM WITHOUT THE      #
# WRITTEN PERMISSION OF SKA SA.                                               #
###############################################################################
"""Module defining the JSON-RPC request class used by websocket client."""

import uuid

import omnijson as json


class JSONRPCRequest(object):
    """
    Class with structure following the JSON-RPC standard.

        Parameters
        ----------
        method: str
            Name of the remote procedure to call.
        params: list
            List of parameters to be used for the remote procedure call.
    """

    id = ''
    method = ''
    params = None

    def __init__(self, method, params):
        self.jsonrpc = '2.0'
        self.id = str(uuid.uuid4().get_hex()[:10])
        self.method = method
        self.params = params

    def __call__(self):
        """Return object's attribute dictionary in JSON form."""
        return json.dumps(self.__dict__)

    def __str__(self):
        """Return a human readable string of the object"""
        return "{_class}: id: {_id}, method: {method}, params: {params}".format(
            _class=self.__class__,
            _id=self.id,
            method=self.method,
            params=self.params)
