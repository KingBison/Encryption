from random import randint

class Encryption_Key:

    


    def __init__(self):
        set_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        self.key = []
        
        for i in range(len(set_characters)):
            if len(characters)>1:
                rand = randint(0,len(characters)-1)
            else:
                rand = 0
            self.key.append([set_characters[i], characters[rand]])
            characters = characters[0:rand] + characters[rand+1:len(characters)]



    def getKey(self):
        return self.key

    def saveKey(self, key_name):
        f = open(key_name + ".txt","w+")
        add = ""
        for i in self.key:
            add += i[0] + i[1]
        f.write(add)

    def subKeyFromTxt(self,key_name):
        try:
            f = open(key_name + ".txt","r")
            f = f.read()
            self.key = []
            set_num = 0
            for i in range(int((len(f))/2)):
                self.key.append([f[set_num],f[set_num+1]])
                set_num+=2
            

        except:
            print("No Key Found")
            
        


        


    


