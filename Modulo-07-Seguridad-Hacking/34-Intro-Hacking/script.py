"""
Certificaciones:  ec-council, comptia
"""

import dns.resolver

def test():
    try:
        # ns: dns, A: ips
        objetivos = dns.resolver.query("cesarcancino.com", "ns")
        for objetivo in objetivos:
            print(objetivo)
    except Exception as e:
        print("No se pudo")
    

test()