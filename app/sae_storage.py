from sae.storage import Bucket
from config import BUCKET_NAME, TARGET_FILE


def get_url():
    bucket = Bucket(BUCKET_NAME)
    # bucket.put()
    # bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn', metadata={'expires': '1d'})
    # attrs = bucket.stat(
    return bucket.generate_url(TARGET_FILE)


def write_storage(content):
    bucket = Bucket(BUCKET_NAME)
    bucket.delete_object(TARGET_FILE)
    bucket.put_object(TARGET_FILE, content)
