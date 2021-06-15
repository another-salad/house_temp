from pathlib import Path


def get_secret(file_name: str) -> str:
    """Returns the contents of the docker secret file

    Args:
        file_name (str): the file name

    Returns:
        str: the docker secret
    """
    with open(Path("/run/secrets", file_name), "r", encoding='UTF-8') as secret:
        return secret.read()
