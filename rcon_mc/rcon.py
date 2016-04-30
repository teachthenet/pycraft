#!/usr/bin/env python
"""
 rcon.py - RCON protocol interface module
 Author:
   mrpaws
 Project Repo:
   https://github.com/mrpaws/python-rcon-mc
 Protocol:
   https://developer.valvesoftware.com/wiki/Source_RCON_Protocol
     -- adapted for use with minecraft, but a great starter
"""
import struct
from types import StringType, IntType
import lib.msocket as msocket


# Module Declarations:
NULL = '\x00'  # hex for C null terminator
MIN_PACKET_SIZE = 10  # 4(id)+4(type)+1(body)+1(empty string)
MIN_PACKET_ACTUAL_SIZE = 14  # 4(size) + 4(id)+4(type)+1(body)+1(empty string)
MAX_PACKET_SIZE = 4096  # just the way it is
# (4096 - 4(id) - 4(type) - 1(empty string) -1(body null-terminator)) = 4086
MAX_BODY_SIZE = 4086

# RCON command types:
SERVERDATA_RESPONSE_VALUE = 0
SERVERDATA_EXECCOMMAND = 2
SERVERDATA_AUTH_RESPONSE = 2
SERVERDATA_AUTH = 3

error = ""


class RconException(Exception):
    """For passing RCON module exceptions"""
    pass


class client:
    """Minecraft RCON protocol communication"""
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.error_stack = []
        self.id = 0
        self.authenticated = False
        assert type(self.host) is StringType, "{m}{h}".format(
            m="hostname is not a string:",
            h=self.host)
        assert type(self.port) is IntType, "{m}{p}".format(
            m="port is not a number:",
            p=self.port)
        assert type(self.password) is StringType, "password is not a string"
        try:
            self.connection = msocket.msocket(self.host, self.port)
        except(msocket.error) as ret_val:
            self._manage_rcon_error(ret_val)
            return False

    def _manage_rcon_error(self, ret_val):
        self.error_stack.append(ret_val)
        raise RconException(self.error_stack)

    def _connect(self):
        """private connect method"""
        try:
            con = self.connection.connect()
        except(msocket.error) as ret_val:
            if con is False:
                self._manage_rcon_error(ret_val)
                return False
        return True

    def _pack_data(self, type_name, msg):
        """private method for crafting RCON requests"""
        if not msg:
            msg = ""
        msg_len = len(msg)
        size = msg_len + MIN_PACKET_SIZE
        if msg_len > MAX_BODY_SIZE:
            self._manage_rcon_error("{m}\n{s}".format(
                m="Request message body too large. MAX=",
                s=str(MAX_BODY_SIZE)))
            return False
        try:
            request = "{s}{i}{t}{m}{n1}{n2}".format(
                s=struct.pack('<i', size),
                i=struct.pack('<i', self.id),
                t=struct.pack('<i', type_name),
                m=msg, n1=NULL, n2=NULL)
        except:
            self._manage_rcon_error("{m}\n{s}".format(
                m="Unable to pack data into TCP request: ",
                s=str(self.error_stack)))
            return False
        return request

    def _unpack_data(self, response):
        """private method to unpack the data and return the ascii message"""
        response_size = len(response)
        msg_size = response_size - MIN_PACKET_ACTUAL_SIZE
        if response_size == 0:
            self._manage_rcon_error("Zero length response from server")
            return False
        unpack_fmt = "{i}{m}{n}".format(i="<iii", m=str(msg_size), n="sxx")
        try:
            payload = struct.unpack(unpack_fmt, response)
        except(struct.error) as ret_val:
            self._manage_rcon_error(ret_val)
            return False
        size = payload[0]
        payload_id = payload[1]
        type_name = payload[2]
        msg = payload[3]
        return (payload_id, type_name, msg)

    def _send(self, type_name, msg):
        """private send method for handling the dirty work in
        sending a request"""
        if not self.connection:
            try:
                self._connect()
            except(error) as ret_val:
                return False
            return False
        try:
            request = self._pack_data(type_name, msg)
        except(error) as ret_val:
            return False
        try:
            response = self.connection.manage(request)
        except(msocket.error) as ret_val:
            self._manage_rcon_error(ret_val)
            return False
        if not response:
            self._manage_rcon_error("Empty response from server")
            return False
        try:
            response = self._unpack_data(response)
        except(error) as ret_val:
            return False
        return response

    def _authenticate(self):
        """private method to authenticate with server"""
        response = self._send(SERVERDATA_AUTH, self.password)
        if response[0] == -1:
            self._manage_rcon_error("Authentication failure")
            return False
        self.authenticated = True
        return True

    def send(self, msg):
        """API user function Sends a command to the RCON server,
        does not necessarily disconnect. Returns the response.
        """
        self.id = self.id + 1
        if not self.authenticated:
            try:
                self._authenticate()
            except IOError:
                return False

        try:
            print "*",SERVERDATA_EXECCOMMAND,msg
            response = self._send(SERVERDATA_EXECCOMMAND, msg)
        except IOError:
            return False

        response_msg = response[2]

        if response[0] == -1:
            self.authenticated = False
            try:
                self._authenticate()
            except IOError:
                return False
            try:
                response = self._send(SERVERDATA_EXECCOMMAND, msg)
            except IOError:
                return False
        return response_msg

    def disconnect(self):
        """hook into msocket to allow API users to easily disconnect"""
        try:
            self.connection.disconnect()
        except(msocket.error) as ret_val:
            self._manage_rcon_error(ret_val)
            return False
        return False

    def __del__(self):
        self.disconnect()
