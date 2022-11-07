import paramiko
import random
import concurrent.futures

####  config  ####
special_account = "admin"
special_port    = "443"
special_timeout = 90
workersnumber   = 64

#pkey = paramiko.Ed25519Key.from_private_key_file("./id_rsa")
pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
#### #### #### ####

# Retrieve a single page and report the URL and contents
def check_host(host):
    print(f"Try to connect with {host}:{special_port}")
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    try:
        client.connect(host, username=special_account, pkey=pkey, port=special_port, timeout=special_timeout, banner_timeout=special_timeout)
        stdin , stdout, stderr = client.exec_command("hostname")
        f = open("report.txt", "w")
        f.write(f"{host} says {stdout.read()}")
        f.close()
        quit()
    except:
        print(f"Host {host}:{special_port} is not available")

with open("Armenia.txt") as f:
    Lines = f.readlines()
    for line in Lines:
        print(f"Process new line: {line}")
        host_list = []

        # Get border IPs
        ip1 = line.split()[0].strip()
        ip2 = line.split()[1].strip()

        # Build full ip list
        ip1s = ip1.split('.')
        ip2s = ip2.split('.')
        for x in range(int(ip1s[2]), int(ip2s[2]) + 1):
            for y in range(1, 256):
                host_list.append(f"{ip1s[0]}.{ip1s[1]}.{x}.{y}")
        random.shuffle(host_list)

        # We can use a with statement to ensure threads are cleaned up promptly
        with concurrent.futures.ThreadPoolExecutor(max_workers=workersnumber) as executor:
            # Start the load operations and mark each future with its URL
            future_to_host = {executor.submit(check_host, host): host for host in host_list}
            for future in concurrent.futures.as_completed(future_to_host):
                future.result()
