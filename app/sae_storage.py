from sae.storage import Bucket

def get_url():
    bucket = Bucket('bucket')
    # bucket.put()
    # bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn', metadata={'expires': '1d'})
    # attrs = bucket.stat()
    bucket.put_object('1.txt', 'hello, world')
    return bucket.generate_url('1.txt')


