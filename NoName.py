import math

class NoName:
    def word(self,word):
        self.word = word.split('_')[0]
        self.tag = word.split('_')[1]
        
    def substring(self,sub):
        self.L = len(sub)
        self.words = []
        self.tag = []
        for word in sub:
            self.words.append(word.split('_')[0])
            self.tag.append(word.split('_')[1])
        self.f = 0
        self.c = 0
        self.t = 0
        
    def CValue_non_nested(self):
        self.CValue = math.log2(self.L) * self.f
    
    def CValue_nested(self):
        self.CValue = math.log2(self.L) * (self.f - 1/self.c * self.t)
        
    def substringInitial(self,f):
        self.c = 1
        self.t = f
        
    def revise(self,f,t):
        self.c += 1
        self.t += f - t