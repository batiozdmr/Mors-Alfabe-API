import json

import requests

from apps.common.mors.mors import mors_encrypt


def api(message):
    result_mors_key = mors_encrypt(message.upper())

    params = {
        'command': result_mors_key,
    }

    result = requests.post('http://ik.olleco.net/morse-api/', params)
    res = json.loads(result.text)

    return res

