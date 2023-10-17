from scapy.all import *

def trace_route(ip_address):
    print("Current IP Address:", ip_address)
    
    found_ip_addresses = []
    for i in range(1, 28):
        pkt = IP(dst=ip_address, ttl=i) / UDP(dport=33434)
        try:
            # Send the packet and get a reply
            reply = sr1(pkt, verbose=0, timeout=10)
            if reply is None:
                # No reply
                break
            elif reply.type == 3:
                # We've reached our destination
                print("Done!", reply.src)
                break
            else:
                print(f"{i} hops away: {reply.src}")
                found_ip_addresses.append(reply.src)
        except Exception as ex:
            print("Error occured at {i} hops:")
            print(ex)
            break
    
    return found_ip_addresses