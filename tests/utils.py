import imagehash
from PIL import Image
from loguru import logger

def compare_to_screenshots(path,path2):
    hash = imagehash.average_hash(Image.open(path))
    hash2 = imagehash.average_hash(Image.open(path2))
    return hash == hash2


def log(text, STATUS='info'):
    if STATUS=='info':
        logger.info(text)
    else:
        logger.error(text)

