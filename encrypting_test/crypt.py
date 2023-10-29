from cryptography.fernet import Fernet

class lock:
    def __init__(self) -> None:
        pass

    

class convert:
    def __init__(self,file) -> None:
        self.path = file
        self.toBeConverter = self.converted()
    def converted(self):
        l = []
        with open(self.path , "r") as file:
            for i in file.read():
                l.append(i)
        m = []
        for i in l:
            m.append(ord(i))
        n = []
        for i in m:
            n.append(bytes(i))            
        print(n)

# ----------main program------------

if __name__ == "__main__":
    a = convert("encrypting_test/crypt.txt")
    a.converted()
    pass