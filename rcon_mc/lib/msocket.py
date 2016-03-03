#!/usr/bin/env python
"""
 msocket.py - low level network interface
 Author:
   mrpaws
 Project Repo:
   https://github.com/mrpaws/python-rcon-mc
"""

import socket
import select
from types import StringType, IntType

error = ""


class MSocketError(Exception):
    pass


class msocket:
    """Manage client connections"""
    def __init__(self, host, port, *timeout):
        self.host = host
        self.port = port
        self.connection = False
        if timeout:
            self.timeout = timeout[0]
        else:
            self.timeout = 1
        self.error_stack = []
        assert type(self.host) is StringType, "{m}{h}".format(
            m="hostname is not a string:", h=self.host)
        assert type(self.port) is IntType, "{m}{p}".format(
            m="port is not a number:", p=self.port)
        assert type(self.timeout) is IntType, "{m}{t}".format(
            m="timeout is not a number:", t=self.timeout)

    def _manage_socket_error(self, ret_val):
        if self.connection:
            self.connection.close()
        self.connection = None
        self.error_stack.append(ret_val)
        raise MSocketError(str(self.error_stack))

    def connect(self):
        """Resolve remote host and connect however possible (IPV6 compat)"""
        if self.connection:
            return self.connection
        for con in socket.getaddrinfo(self.host,
                                      self.port,
                                      socket.AF_UNSPEC,
                                      socket.SOCK_STREAM):
            addr_fam, sock_type, proto, canonical_name, server_addr = con
            try:
                self.connection = socket.socket(addr_fam, sock_type, proto)
            except socket.error as ret_val:
                self._manage_socket_error(ret_val)
                continue
            try:
                self.connection.settimeout(self.timeout)
            except(socket.error) as ret_val:
                self._manage_socket_error(ret_val)
                continue
            try:
                self.connection.connect(server_addr)
            except(socket.error) as ret_val:
                self._manage_socket_error(ret_val)
                continue
            if not self.connection:
                continue
            break
        else:
            self.connection = False
            raise MSocketError("{m}\n{e}".format(m="Unable to Connect",
                                                 e=str(self.error_stack)))
        return True

    def disconnect(self):
        """Disconnect from remote host"""
        if self.connection:
            self.connection.close()
            self.connection = False
            return self.connection

    def send(self, packet):
        """issue a packet to the socket (sent as received)"""
        if not self.connection:
            try:
                self.connect()
            # this needs more thorough testing, seeing as there isn't
            except(error) as ret_val:
                self._manage_socket_error(ret_val)
                return False

        try:
            self.connection.send(packet)
        except(socket.error) as ret_val:
            return False
        return True

    def receive(self, *buflen):
        """Read responses from the socket and return them as received.
           Runs as a blocking socket.
        """
        not_ready = 0
        packet = ""
        if not buflen:
            buflen = 1024  # rather arbitrary read amount
        packet_size = 0
        while True:
            if self.connection is not None or False:
                rdy = select.select([self.connection.fileno()], [], [], .3)[0]
                if rdy:
                    try:
                        cpacket = self.connection.recv(buflen)
                        if not cpacket:
                            break
                    except(socket.error) as ret_val:
                        self._manage_socket_error(ret_val)
                        return False
                    cpacket_size = len(cpacket)
                    packet_size = packet_size + cpacket_size
                    if packet_size > 0:
                        packet = packet + cpacket
                    else:
                        packet = cpacket
                    continue
                else:
                    not_ready = not_ready + 1
                    if not_ready > 2:
                        break
            break
        return packet

    def manage(self, packet):
        """High level whamadyne function for sending and
        receiving a message. Does not explicitily disconnect"""

        try:
            self.connect()
        except(error):
            print error
            return False
        try:
            self.send(packet)
        except(error):
            print error
            return False
        try:
            response = self.receive()
        except(error):
            print error
            return False
        return response
