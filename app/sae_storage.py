from sae.storage import Bucket
from config import BUCKET_NAME, TARGET_FILE


def get_url():
    bucket = Bucket('bucket')
    # bucket.put()
    # bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn', metadata={'expires': '1d'})
    # attrs = bucket.stat()
    bucket.put_object('1.txt', 'hello, world')
    return bucket.generate_url('1.txt')


def write_storage(content):
    bucket = Bucket(BUCKET_NAME)
    bucket.delete_object(TARGET_FILE)
    bucket.put_object(TARGET_FILE, content)
    return bucket.generate_url(TARGET_FILE)
