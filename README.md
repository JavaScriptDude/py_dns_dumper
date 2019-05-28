# py_dns_dumper
Very simple Python3 script for dumping DNS Resource Records

`python3 dns_dumper.py google.com`

Output example:
```Processing domain: google.com
checking: A: ✔
checking: AAAA: ✔
checking: AFSDB: -
checking: APL: -
checking: CAA: ✔
checking: CDNSKEY: -
checking: CDS: -
checking: CERT: -
checking: CNAME: -
checking: DHCID: -
checking: DLV: -
checking: DNAME: -
checking: DNSKEY: -
checking: DS: -
checking: HIP: -
checking: IPSECKEY: -
checking: KEY: -
checking: KX: -
checking: LOC: -
checking: MX: ✔
checking: NAPTR: -
checking: NS: ✔
checking: NSEC: -
checking: NSEC3: -
checking: NSEC3PARAM: -
checking: OPENPGPKEY: -
checking: PTR: -
checking: RRSIG: -
checking: RP: -
checking: SIG: -
checking: SMIMEA: (unknown)
checking: SOA: ✔
checking: SRV: -
checking: SSHFP: -
checking: TA: -
checking: TKEY: (not allowed)
checking: TLSA: -
checking: TSIG: (not allowed)
checking: TXT: ✔
checking: URI: -
Processing domain: www.google.com
checking: A: ✔
checking: AAAA: ✔
checking: AFSDB: -
checking: APL: -
checking: CAA: -
checking: CDNSKEY: -
checking: CDS: -
checking: CERT: -
checking: CNAME: -
checking: DHCID: -
checking: DLV: -
checking: DNAME: -
checking: DNSKEY: -
checking: DS: -
checking: HIP: -
checking: IPSECKEY: -
checking: KEY: -
checking: KX: -
checking: LOC: -
checking: MX: -
checking: NAPTR: -
checking: NS: -
checking: NSEC: -
checking: NSEC3: -
checking: NSEC3PARAM: -
checking: OPENPGPKEY: -
checking: PTR: -
checking: RRSIG: -
checking: RP: -
checking: SIG: -
checking: SMIMEA: (unknown)
checking: SOA: -
checking: SRV: -
checking: SSHFP: -
checking: TA: -
checking: TKEY: (not allowed)
checking: TLSA: -
checking: TSIG: (not allowed)
checking: TXT: -
checking: URI: -

DNS Records found for www.google.com:
 A:
 . 172.217.164.238
 AAAA:
 . 2607:f8b0:400b:800::200e
 CAA:
 . 0 issue "pki.goog"
 MX:
 . alt3.aspmx.l.google.com.
 . alt4.aspmx.l.google.com.
 . alt2.aspmx.l.google.com.
 . alt1.aspmx.l.google.com.
 . aspmx.l.google.com.
 NS:
 . ns4.google.com.
 . ns2.google.com.
 . ns3.google.com.
 . ns1.google.com.
 SOA:
 . ns1.google.com. dns-admin.google.com. 250191621 900 900 1800 60
 TXT:
 . "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
 . "facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
 . "docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
 . "v=spf1 include:_spf.google.com ~all"

DNS Records found for www.google.com:
 A:
 . 172.217.165.4
 AAAA:
 . 2607:f8b0:400b:80f::2004

```
