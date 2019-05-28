 #!/usr/bin/python3
from __future__ import print_function
# http://python-future.org/compatible_idioms.html

#########################################
# .: dns_dumper.py :.
# Grab DNS records for a domain for all current Resource Record Types
# Source: https://en.wikipedia.org/wiki/List_of_DNS_record_types
# .: Sample :.
# python3 dns_dumper.py google.com
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/py_dns_dumper
# Licence: https://opensource.org/licenses/MIT
# TODO: (none)
#########################################

import sys, dns.resolver, time
argv=sys.argv[1:]
domain = argv[0]
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
DNS_REC_TYPES='A|AAAA|AFSDB|APL|CAA|CDNSKEY|CDS|CERT|CNAME|DHCID|DLV|DNAME|DNSKEY|DS|HIP|IPSECKEY|KEY|KX|LOC|MX|NAPTR|NS|NSEC|NSEC3|NSEC3PARAM|OPENPGPKEY|PTR|RRSIG|RP|SIG|SMIMEA|SOA|SRV|SSHFP|TA|TKEY|TLSA|TSIG|TXT|URI'.split('|')

dns_answers={}
def dump_dns(type):
    try:
        answers = my_resolver.query(domain, type)
        print('type: %s: %s' % (type, u'\u2714'))
        dns_answers[type] = answers
    except dns.resolver.NXDOMAIN:
        _exit('Invalid domain: %s' % domain)
    except Exception as e:
        if isinstance(e, dns.resolver.NoAnswer) \
           or isinstance(e, dns.resolver.NoNameservers):
            print('type: %s: -' % (type))
        elif isinstance(e, dns.rdatatype.UnknownRdatatype):
            print('type: %s: ?' % (type))
        elif isinstance(e, dns.resolver.NoMetaqueries):
            print('type: %s: (not allowed)' % (type))
        else:
            raise e
        

    time.sleep(0.25)

def _exit(msg):
    print('{}'.format(msg))
    sys.exit(1)
    
for type in DNS_REC_TYPES:
    dump_dns(type)


print('\n DNS Records found for %s:' % domain)
found_types = list(dns_answers.keys())
found_types.sort()
for type in found_types:
    print('type: %s:' % type)
    for rdata in dns_answers[type]:
        print(' . {}'.format(rdata))

print("~")