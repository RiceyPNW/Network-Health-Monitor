import json
import subprocess
import logging
import ipaddress

logging.basicConfig(
    filename="ping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ask for and validate Test Server IP
while True:
    userTestServer = input("Enter the Test Server IP Address: ").strip()

    try:
        validated_ip = ipaddress.ip_address(userTestServer)
        userTestServer = str(validated_ip)
        break

    except ValueError:
        print("Enter a valid IP Address.")


try:
    with open("hosts.json", "r") as file:
        data = json.load(file)
        logging.info("File was successfully found.")

except FileNotFoundError:
    print("File not found.")
    logging.error("File not found.")

except json.JSONDecodeError:
    print("JSON is invalid.")
    logging.error("JSON is invalid.")

else:
    results = []

    for host in data:

        # Replace Test Server address with user-entered IP
        if host["name"] == "Test Server":
            host["address"] = userTestServer

        pingResults = {
            "name": "",
            "address": "",
            "status": ""
        }

        print(host["name"], "-", host["address"])

        pingResults["name"] = host["name"]
        pingResults["address"] = host["address"]

        try:
            ping = subprocess.run(
                ["ping", host["address"], "-n", "2"],
                capture_output=True,
                text=True
            )

        except FileNotFoundError:
            print("Ping could not be run.")
            logging.error("Ping could not be run.")
            continue

        if ping.returncode == 0:
            status = "Reachable"
            logging.info(
                f"{host['name']} ({host['address']}) is Reachable"
            )

        else:
            status = "Unreachable"
            logging.warning(
                f"{host['name']} ({host['address']}) is Unreachable"
            )

        print(f"Status: {status}\n")

        pingResults["status"] = status
        results.append(pingResults)

    with open("results.json", "w") as jsonFile:
        json.dump(results, jsonFile, indent=4)