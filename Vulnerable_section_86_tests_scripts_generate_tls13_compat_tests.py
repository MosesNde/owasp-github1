 
 import sys
 import os
import abc
 import argparse
 import itertools
 from collections import namedtuple
 }
 
 
class TLSProgram(metaclass=abc.ABCMeta):
     """
     Base class for generate server/client command.
     """
     # pylint: disable=too-many-arguments
     def __init__(self, ciphersuite=None, signature_algorithm=None, named_group=None,
                  cert_sig_alg=None, compat_mode=True):
         self._cert_sig_algs.extend(
             [sig_alg for sig_alg in signature_algorithms if sig_alg not in self._cert_sig_algs])
 
    @abc.abstractmethod
     def pre_checks(self):
         return []
 
    @abc.abstractmethod
     def cmd(self):
         if not self._cert_sig_algs:
             self._cert_sig_algs = list(CERTIFICATES.keys())
 
    @abc.abstractmethod
     def post_checks(self):
         return []
 
 
class OpenSSLServ(TLSProgram):
     """
    Generate test commands for OpenSSL server.
     """
 
     NAMED_GROUP = {
     }
 
     def cmd(self):
        super().cmd()
        ret = ['$O_NEXT_SRV_NO_CERT']
        for _, cert, key in map(lambda sig_alg: CERTIFICATES[sig_alg], self._cert_sig_algs):
            ret += ['-cert {cert} -key {key}'.format(cert=cert, key=key)]
        ret += ['-accept $SRV_PORT']
 
         if self._ciphers:
             ciphersuites = ':'.join(self._ciphers)
                 map(lambda named_group: self.NAMED_GROUP[named_group], self._named_groups))
             ret += ["-groups {named_groups}".format(named_groups=named_groups)]
 
        ret += ['-msg -tls1_3 -num_tickets 0 -no_resume_ephemeral -no_cache']
         if not self._compat_mode:
             ret += ['-no_middlebox']
 
        return ' '.join(ret)
 
     def pre_checks(self):
         return ["requires_openssl_tls1_3"]
 
     def post_checks(self):
         return ['-c "HTTP/1.0 200 ok"']
 
 
class GnuTLSServ(TLSProgram):
     """
    Generate test commands for GnuTLS server.
     """
 
     CIPHER_SUITE = {
                 "requires_gnutls_next_no_ticket",
                 "requires_gnutls_next_disable_tls13_compat", ]
 
    def post_checks(self):
        return ['-c "HTTP/1.0 200 OK"']

     def cmd(self):
        super().cmd()
        ret = ['$G_NEXT_SRV_NO_CERT', '--http',
               '--disable-client-cert', '--debug=4']

        for _, cert, key in map(lambda sig_alg: CERTIFICATES[sig_alg], self._cert_sig_algs):
            ret += ['--x509certfile {cert} --x509keyfile {key}'.format(
                cert=cert, key=key)]
 
         priority_string_list = []
 
             priority_string_list.append('GROUP-ALL')
 
         priority_string_list = ['NONE'] + \
            sorted(priority_string_list) + ['VERS-TLS1.3']
 
         priority_string = ':+'.join(priority_string_list)
         priority_string += ':%NO_TICKETS'
 
         ret += ['--priority={priority_string}'.format(
             priority_string=priority_string)]
        ret = ' '.join(ret)
         return ret
 
 
class MbedTLSCli(TLSProgram):
     """
    Generate test commands for mbedTLS client.
     """
 
     CIPHER_SUITE = {
         'TLS_AES_128_CCM_8_SHA256': 'TLS1-3-AES-128-CCM-8-SHA256'}
 
     def cmd(self):
        super().cmd()
        ret = ['$P_CLI']
        ret += ['server_addr=127.0.0.1', 'server_port=$SRV_PORT',
                'debug_level=4']
        ret += ['ca_file={cafile}'.format(
            cafile=CERTIFICATES[self._cert_sig_algs[0]].cafile)]
 
         if self._ciphers:
             ciphers = ','.join(
         if self._named_groups:
             named_groups = ','.join(self._named_groups)
             ret += ["curves={named_groups}".format(named_groups=named_groups)]

        ret = ' '.join(ret)
         return ret
 
     def pre_checks(self):
         ret = ['requires_config_enabled MBEDTLS_DEBUG_C',
               'requires_config_enabled MBEDTLS_SSL_CLI_C',
                'requires_config_enabled MBEDTLS_SSL_PROTO_TLS1_3']
 
         if self._compat_mode:
                 'requires_config_enabled MBEDTLS_X509_RSASSA_PSS_SUPPORT')
         return ret
 
     def post_checks(self):
         check_strings = ["Protocol is TLSv1.3"]
         if self._ciphers:
         return ['-c "{}"'.format(i) for i in check_strings]
 
 
SERVER_CLASSES = {'OpenSSL': OpenSSLServ, 'GnuTLS': GnuTLSServ}
CLIENT_CLASSES = {'mbedTLS': MbedTLSCli}
 
 
 def generate_compat_test(client=None, server=None, cipher=None, named_group=None, sig_alg=None):
                                            signature_algorithm=sig_alg,
                                            cert_sig_alg=sig_alg)
 
    cmd = ['run_test "{}"'.format(name), '"{}"'.format(
        server_object.cmd()), '"{}"'.format(client_object.cmd()), '0']
     cmd += server_object.post_checks()
     cmd += client_object.post_checks()
     cmd += ['-C "received HelloRetryRequest message"']
                                            cert_sig_alg=cert_sig_alg)
     client_object.add_named_groups(server_named_group)
 
    cmd = ['run_test "{}"'.format(name), '"{}"'.format(
        server_object.cmd()), '"{}"'.format(client_object.cmd()), '0']
     cmd += server_object.post_checks()
     cmd += client_object.post_checks()
    cmd += ['-c "received HelloRetryRequest message"']
    cmd += ['-c "selected_group ( {:d} )"'.format(
        NAMED_GROUP_IANA_VALUE[server_named_group])]
     prefix = ' \\\n' + (' '*9)
     cmd = prefix.join(cmd)
     return '\n'.join(server_object.pre_checks() +
                      client_object.pre_checks() +
                      [cmd])
 

 SSL_OUTPUT_HEADER = '''#!/bin/sh
 
 # {filename}
                               CIPHER_SUITE_IANA_VALUE.keys(),
                               NAMED_GROUP_IANA_VALUE.keys(),
                               SIG_ALG_IANA_VALUE.keys()):
            yield generate_compat_test(client=client, server=server,
                                       cipher=cipher, named_group=named_group,
                                       sig_alg=sig_alg)
 
         # Generate Hello Retry Request  compat test cases
         for client, server, client_named_group, server_named_group in \
             itertools.product(CLIENT_CLASSES.keys(),
                               SERVER_CLASSES.keys(),
                               NAMED_GROUP_IANA_VALUE.keys(),
                               NAMED_GROUP_IANA_VALUE.keys()):
            if client_named_group != server_named_group:
                 yield generate_hrr_compat_test(client=client, server=server,
                                                client_named_group=client_named_group,
                                                server_named_group=server_named_group,