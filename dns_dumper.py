 #!/usr/bin/python3
from __future__ import print_function
# http://python-future.org/compatible_idioms.html

#########################################
# .: dns_dumper.py :.
# Grab DNS records for a domain for all current Resource Record Types
# Source: https://en.wikipedia.org/wiki/List_of_DNS_record_types
# .: Sample :.
# python3 dns_dumper.py google.com,www.google.com
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/py_dns_dumper
# Licence: https://opensource.org/licenses/MIT
# TODO: (none)
#########################################

import sys, dns.resolver, time

def _exit(msg):
    print('{}'.format(msg))
    sys.exit(1)

argv=sys.argv[1:]
if not len(argv) == 1:
    _exit('Invalid arguments. Only one arg is required, a comma separated list of domains')

domains = list(map(lambda s: s.strip(),argv[0].split(',')))

my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
DNS_REC_TYPES='A|AAAA|AFSDB|APL|CAA|CDNSKEY|CDS|CERT|CNAME|DHCID|DLV|DNAME|DNSKEY|DS|HIP|IPSECKEY|KEY|KX|LOC|MX|NAPTR|NS|NSEC|NSEC3|NSEC3PARAM|OPENPGPKEY|PTR|RRSIG|RP|SIG|SMIMEA|SOA|SRV|SSHFP|TA|TKEY|TLSA|TSIG|TXT|URI'.split('|')


def get_dns_recs(domain, type):
    try:
        answers = my_resolver.query(domain, type)
        print('checking: %s: %s' % (type, u'\u2714'))

        return list(map(lambda a: \
                a.exchange if type == 'MX' else \
                a.address if type in ['A', 'AAAA'] else \
                a
            , answers)
        )
    except dns.resolver.NXDOMAIN:
        _exit('Invalid domain: %s' % domain)
    except Exception as e:
        if isinstance(e, dns.resolver.NoAnswer) \
           or isinstance(e, dns.resolver.NoNameservers):
            print('checking: %s: -' % (type))
        elif isinstance(e, dns.rdatatype.UnknownRdatatype):
            print('checking: %s: (unknown)' % (type))
        elif isinstance(e, dns.resolver.NoMetaqueries):
            print('checking: %s: (not allowed)' % (type))
        else:
            raise e

        return None
        

    time.sleep(0.1)

answer_list = []
for domain in domains:
    print('Processing domain: %s' % domain)
    dns_answers={}
    for type in DNS_REC_TYPES:
        answers = get_dns_recs(domain, type)
        if answers is not None:
            dns_answers[type] = answers
    answer_list.append(dns_answers)

for dns_answers in answer_list:
    print('\nDNS Records found for %s:' % domain)
    found_types = list(dns_answers.keys())
    found_types.sort()
    for type in found_types:
        print(' %s:' % type)
        for rdata in dns_answers[type]:
            print(' . {}'.format(rdata))
            try:
                print(' . (address) {}'.format(rdata.address))
            except:pass
            try:
                print(' . (exchange) {}'.format(rdata.exchange))
            except:pass

print("~")
