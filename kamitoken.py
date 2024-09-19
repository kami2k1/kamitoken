from cryptography.fernet import Fernet
import hashlib , base64
from datetime import datetime
import json
class kamitoken:
   
    def __init__(self, key : str = "kami" , time : int = 300  ) -> None:
      
        self.key = self.getkey(key)
        self.time = time *60
    def getkey (self ,  passwd : str ): 
        # get key from passwd 
        has_passwd = hashlib.sha256(passwd.encode()).digest()
        key_enc = base64.urlsafe_b64encode(has_passwd[:32])
        return key_enc

    def encode (self, User : str ):
        data = {
            "user": User,
            "time": int(datetime.now().timestamp())
        }
        enc = Fernet(self.key)
        kami = str(data)
       
        data_enc = enc.encrypt(kami.encode())
        return data_enc.decode("utf-8")
    def get_time(self,time  : int ):
            now = int(datetime.now().timestamp())
            kq  = now - time
            print(kq)
            if  kq>= self.time:
                return False 
            else:
                return True
    def decode( self, data : str):
        try:
            key_en = Fernet(self.key)
            data_decode = key_en.decrypt(data).decode()
            data = data_decode.replace("'", '"')           # data_decode = {'user': 'kami@123.com', 'time': 1726709984}
            data = json.loads(data)
            now = int(datetime.now().timestamp())
            if self.get_time(int(data['time'])):
                return True , data['user']
            else:
                return False, 0




        except Exception as e :
            print("lỗi tại ", e )
            return False , 0

    # async def endcode(user : str ):



    # async def decode(data : str):

