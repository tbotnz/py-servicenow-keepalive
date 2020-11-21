import requests
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="servicenow instance keep alive")
    parser.add_argument(
                        '--instance',
                        action="store",
                        dest="instance_id",
                        help='instance id eg. dev12345',
                        required=True
                        )
    parser.add_argument(
                        '--username',
                        action="store",
                        dest="username",
                        help='username eg. admin',
                        required=True
                        )
    parser.add_argument(
                        '--password',
                        action="store",
                        dest="password",
                        help='password eg. 23123SDasdeqewe',
                        required=True
                        )
    parser.add_argument(
                        '--sysid',
                        action="store",
                        dest="user_sys_id",
                        help='sysid for username arg eg. 123cxzccxzxceq',
                        required=True
                        )
    results = parser.parse_args()
    url = f"https://{results.instance_id}.service-now.com/api/now/table/sys_user/{results.user_sys_id}"
    headers = {}
    response = requests.get(
                            url,
                            headers=headers,
                            data={},
                            auth=(results.username, results.password)
                            )
    res = json.loads(response.text)
    if response.status_code == 200 and res["result"]:
        print("servicenow instance keep alive: SUCCESS")
    else:
        print("servicenow instance keep alive: FAILURE")
