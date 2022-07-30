from bs4 import BeautifulSoup
import requests
import json
import datetime

OPENDOTA_URL = 'https://api.opendota.com/api'

DEFAULT_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "_ga=GA1.2.1568616352.1658875198",
    "referer": "https://github.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}


def get_file_name():
    dt = datetime.datetime.now()
    return dt.strftime('%Y-%m-%d')


def save_to_json(cont):
    with open(f"{get_file_name()}.json", 'w') as f:
        f.write(cont)


def save_to_py(json_):
    json_ = json.loads(json_)

    content = f"import requests\nimport json\nOPENDOTA_URL='https://api.opendota.com/api'\n"
    content += "DEFAULT_HEADERS={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','cookie':'_ga=GA1.2.1568616352.1658875198','referer':'https://github.com/','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}"

    for tag in json_.keys():
        class_name = tag.replace(' ', '_')
        class_name = class_name[0].upper() + class_name[1:]
        content += f"class {class_name}():\n"

        for scheme in json_[tag]:
            func_name = ''
            paths = scheme['path'].split('/')
            for i in range(1, len(paths)):
                if '{' in paths[i]:
                    continue

                func_name += f"_{paths[i]}"

            variables = 'self, '
            for param in scheme['params']:
                variables += f"{param}=None, "

            variables = variables[:len(variables) - 2]
            content += f"    def {scheme['method']}{func_name}({variables}):\n"
            content += f"        \"\"\"\n        {scheme['description']}\n        \"\"\"\n"

            data = "{"
            for param in scheme['params']:
                data += f"'{param}': {param}, "
            data += '}'

            content += f"        data={data}\n        response = requests.{scheme['method']}(f\"{{OPENDOTA_URL}}{scheme['path']}\", header=DEFAULT_HEADERS, data=data)\n        return response.json()\n"

    with open(f"{get_file_name()}.py", 'w') as f:
        f.write(content)


def get_opendota_apis():
    response = requests.get(OPENDOTA_URL, headers=DEFAULT_HEADERS)

    response = response.json()
    paths = response['paths']
    result = {}

    for path in paths:
        data = paths[path]
        tag = ''

        method = list(data)[0]
        params = []

        if len(data[method]['tags']) > 1:
            print(f"이 새끼 두개임 {data[method]['tags']}")
        else:
            tag = data[method]['tags'][0]

        if 'parameters' in data[method]:
            for param in data[method]['parameters']:
                params.append(param['name'])

        responses = {}
        if 'responses' in data[method]:
            responses = data[method]['responses']

        desc = ''
        if 'description' in data[method]:
            desc = data[method]['description']

        obj = {
            'method': str(method),
            'path': str(path),
            'params': params,
            'response': responses,
            'description': desc,
        }

        if tag in result:
            result[tag].append(obj)
        else:
            result[tag] = []
            result[tag].append(obj)

    return result


def get_opendota_apis_from_file():
    content = ''
    with open(f"{get_file_name()}.json", "r") as f:
        for line in f.readlines():
            content += line

    return json.loads(content)


if __name__ == '__main__':
    # result = get_opendota_apis()

    result = get_opendota_apis_from_file()

    # save_to_json(json.dumps(result))
    save_to_py(json.dumps(result))
