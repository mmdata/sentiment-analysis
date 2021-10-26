import subprocess
from datetime import datetime
import json
import os
## run this file from app-root to generate __build_info.py

appConfig = json.loads(open(('./appconfig.json'), 'r').read())['appConfig']

git_ref = ''

if git_ref == '':
    with subprocess.Popen('git rev-parse --short=9 HEAD'.split(),
                          stdout=subprocess.PIPE) as process:
        output, error = process.communicate()
        git_ref = output.decode('utf-8').replace('\n', '')

path = './src/app/__build_info.py'
with open(path, 'w') as file:

    json_file = json.dumps(
        {
            'version': appConfig['version'],
            'lastCommit': git_ref,
            'buildTimestamp': datetime.now().isoformat(),
            'serviceName': appConfig['clientIdentifier']
        },
        ensure_ascii=True,
        indent=4)

    file.write(
        "# Note:\n# DO NOT MODIFY OR COMMIT\n# this file is auto-generated\n\nbuild_info = {}"
        .format(json_file))
    file.close()

print('[info] created {}'.format(path))