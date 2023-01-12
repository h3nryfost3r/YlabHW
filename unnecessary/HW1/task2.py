def int32_to_ip(int32):
    ip = ""
    for i in range(4):
        ip = f".{int32%256}" + ip
        int32 //= 256
    return ip[1:]

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
