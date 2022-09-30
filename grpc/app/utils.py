import os
from typing import Dict


def get_files_with_content(dir: str) -> Dict[str, bytes]:
    """ Returns files in given directory (not recursive) with their content
    Args:
        dir (str): directory to retrieve files. Must exists.
            Can be single file. In that case file itself will be returned

    Returns:
        Dict[str, bytes]: dict with filenames mapped to their content as byres
    """
    if not os.path.exists(dir):
        return {}

    if os.path.isfile(dir):
        with open(dir, 'rb') as f:
            return {os.path.basename(dir): f.read()}

    result = {}
    for entry in os.listdir(dir):
        fname = os.path.join(dir, entry)
        if os.path.isfile(fname):
            with open(fname, 'rb') as f:
                result[entry] = f.read()

    return result
