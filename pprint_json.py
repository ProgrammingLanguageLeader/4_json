import json
import argparse


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except IOError:
        return None


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(
        description='A simple program that pretty prints JSON from file'
    )
    argument_parser.add_argument(
        'filepath',
        help='A path to the json file'
    )

    arguments = argument_parser.parse_args()
    input_file_path = arguments.filepath
    parsed_data = load_data(input_file_path)
    pretty_print_json(parsed_data)
