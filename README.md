# Network Health Monitor

A simple Python network monitoring tool that reads hosts from a JSON file, pings each host, logs the results, and saves the latest status to a JSON output file.

## Features

- Reads hosts from `hosts.json`
- Validates a user-provided test server IP address
- Pings each host using the Windows `ping` command
- Reports hosts as `Reachable` or `Unreachable`
- Logs results with timestamps
- Saves results to `results.json`
- Handles missing or invalid JSON files
- Handles errors if the ping command cannot run
