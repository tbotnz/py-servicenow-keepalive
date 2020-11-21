from json.decoder import JSONDecodeError
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
    user_url = f"https://{results.instance_id}.service-now.com/api/now/table/sys_user/{results.user_sys_id}"
    headers = {}
    response = requests.get(
                            user_url,
                            headers=headers,
                            data={},
                            auth=(results.username, results.password)
                            )
    br_url = f"https://{results.instance_id}.service-now.com/api/now/table/sys_script"
    data = {
        "client_callable": "false",
        "template": "",
        "access": "package_private",
        "action_insert": "true",
        "action_update": "true",
        "advanced": "true",
        "action_delete": "false",
        "change_fields": "false",
        "description": "",
        "action_query": "false",
        "when": "after",
        "sys_class_name": "sys_script",
       
        "is_rest": "false",
        "rest_method_text": "",
        "rest_service_text": "",
        "sys_domain": {
            "link": "https://"+results.instance_id+".service-now.com/api/now/table/sys_user_group/{link=https://"+results.instance_id+".service-n",
            "value": "{link=https://"+results.instance_id+".service-n"
        },
        "sys_name": "postman_rule",
        "sys_scope": {
            "link": "https://"+results.instance_id+".service-now.com/api/now/table/sys_scope/global",
            "value": "global"
        },
        "sys_created_by": "admin",
        "order": "100",
        "rest_method": "",
        "rest_service": "",
        "add_message": "false",
        "sys_mod_count": "7",
        "active": "true",
        "sys_overrides": "",
        "collection": "incident",
        "message": "",
        "priority": "100",
        "sys_domain_path": "/",
        "sys_tags": "",
        "script": "(function executeRule(current, previous /*null when async*/) {\r\n\tgs.info(\"webhook calling\");\r\n\t// Add your code here\r\n\r\n})(current, previous);",
        "abort_action": "false",
        "execute_function": "false",
        "filter_condition": "",
        "sys_package": {
            "link": "https://"+results.instance_id+".service-now.com/api/now/table/sys_package/global",
            "value": "global"
        },
        "condition": "",
        "rest_variables": "",
        "name": "keep-alive-rule",
        "role_conditions": "",
        "sys_policy": ""
    }
    requests.post(
                            br_url,
                            headers=headers,
                            json=data,
                            auth=(results.username, results.password)
                            )
    try:
        res = json.loads(response.text)
        if response.status_code == 200 and res.get("result", False):
            print("servicenow instance keep alive: SUCCESS")
        else:
            print("servicenow instance keep alive: FAILURE")
    except JSONDecodeError:
        print("servicenow instance keep alive: FAILURE")
