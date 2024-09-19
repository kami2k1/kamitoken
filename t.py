from cryptography.fernet import Fernet
import hashlib
import base64

def generate_key_from_password(password):
    """Tạo một khóa mã hóa từ mật khẩu bằng hàm băm."""
    # Thêm muối ngẫu nhiên vào hàm băm
    salt = b"xem cc "  # Thay đổi giá trị muối nếu cần
    # Băm mật khẩu kết hợp với muối
    hashed_password = hashlib.sha256(password.encode() ).digest()  # Sử dụng digest để có bytes
    # Chuyển đổi băm thành khóa Fernet bằng cách mã hóa base64
    key = base64.urlsafe_b64encode(hashed_password[:32])  # Đảm bảo có độ dài 32 byte
    return key

def encrypt_message(message, key):
    """Mã hóa một tin nhắn."""
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode('utf-8')


def decrypt_message(encrypted_message, key):
    """Giải mã một tin nhắn."""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Mật khẩu
password = "kami"

# Tạo khóa mã hóa từ mật khẩu
key = generate_key_from_password(password)
print("Khóa:", key)

# Tin nhắn cần mã hóa
message = "Đây là tin nhắn cần mã hóa."

# Mã hóa tin nhắn
encrypted_message = encrypt_message(message, key)

# In tin nhắn mã hóa
print("Tin nhắn mã hóa:", str(encrypted_message))

# Giải mã tin nhắn
decrypted_message = decrypt_message(encrypted_message, key)

# In tin nhắn giải mã
print("Tin nhắn giải mã:", decrypted_message)