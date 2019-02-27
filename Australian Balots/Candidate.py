class Candidate:
  def __init__(self, name):
    self.name = name
    self.count = 0
  
  def increaseCount(self):
    self.count +=1
    
  def getCount(self):
    return self.count
    
  def getName(self):
    return self.name
  
  def println(self):
    print(self.name + str(self.count))
