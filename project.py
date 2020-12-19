from cryptography.fernet import Fernet


def generatePassKey():
    key = Fernet.generate_key()
    print(key)
    print(bytes(key))
    abc = open("PasswordKey.key", 'wb')
    abc.write(key)
    abc.close()


generatePassKey()


def getMyKey():
    abc = open("PasswordKey.key", 'rb')
    key = abc.read()
    abc.close()
    return key


getMyKey()


def getContentFromUser():
    return input("Enter the Content you want to Encrypt in your python Script")


def encryptMessage(message_normal):
    key = getMyKey()
    k = Fernet(key)
    encrypted_Message = k.encrypt(message_normal)
    return encrypted_Message


encryptMessage(b"Hey there")


def decryptMessage(message_secret):
    key = getMyKey()
    k = Fernet(key)
    decrypted_Message = k.decrypt(message_secret)
    return decrypted_Message


decryptMessage(b'zb1AXmBxvwLI2MHhe-oBwRu_mdFM74ijqoStWy8hrTE=')
