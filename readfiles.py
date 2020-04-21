"""Read Json file."""
import json

# jsonファイルを読み込みjsonを返却


def read_json_file(file_path):
    """Read Json File.

    Args:
        file_path: 入力ファイルパス

    Returns:
        output- 読み込んだファイルをJson形式
    """
    json_open = open(file_path, 'r')
    json_load = json.load(json_open)

    return json_load
