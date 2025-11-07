import json
import os.path
from pprint import pprint

from openapi_client.api import app as openapi_app

from slurm_rest_api_client import Client
from slurm_rest_api_client.api.openapi import get_openapi_json

from slurm_prometheus_exporter.modify_schema import modify_schema

def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description='update Slurm OpenAPI schema from server'
    )

    parser.add_argument('url', type=str, help='OpenAPI schema downlaod URL')
    parser.add_argument('-o', '--output',
                        type=str,
                        required=True,
                        help='Output file')
    parser.add_argument('--no-versionize',
                        action='store_false',
                        dest='versionize',
                        default=True,
                        help='Don\'t modify schema to split Slurm API versions')
    parser.add_argument('--no-update-client',
                        action='store_false',
                        dest='update_client',
                        default=True,
                        help='Don\'t update Slurm API client')

    args = parser.parse_args()

    client = Client(base_url=args.url)

    print(f'Load schema from {args.url}')

    response = get_openapi_json.sync_detailed(client=client)

    schema = json.loads(response.content)

    if args.versionize:
        print('Modify schema to handle specific API versions')

        modify_schema(schema)

    print(f'Write output {args.output}')

    with open(args.output, 'w') as f:
        json.dump(schema, f, indent=2)
        f.write('\n')

    if args.update_client:
        command = 'generate'
        if os.path.isdir('slurm-rest-api-client/slurm_rest_api_client'):
            command = 'update'

        print(f'{command.capitalize()} client package')

        openapi_app([
            command,
            '--meta=setup',
            f'--path={args.output}',
            '--custom-template-path=openapi/templates'
        ])

if __name__ == '__main__':
    main()
