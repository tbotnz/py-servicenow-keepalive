# py-servicenow-keepalive
python based command line utility for keeping dev servicenow instance alive

### Usage
```python3 servicenow-keepalive.py --instance XXXXXXXXXXXXXXX --username XXXXXXXXXXXXXXX --password XXXXXXXXXXXXXXX --sysid XXXXXXXXXXXXXXX```

### Simple 6 Hour Crontab
```0 */6 * * * /usr/bin/python3 /home/XXXXXXXXXXXXXXX/py-servicenow-keepalive/servicenow-keepalive.py --instance XXXXXXXXXXXXXXX --username XXXXXXXXXXXXXXX --password XXXXXXXXXXXXXXX --sysid XXXXXXXXXXXXXXX >/dev/null 2>&1```
