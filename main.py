class Stacks():
  def __init__(self):
    self.item=[]

  def push(self, p):
    self.item.append(p)

  def pop(self):
    return self.item.pop()
  
  def is_empty(self):
    return self.item == []

  def peek(self, p):
    if not self.is_empty():
      return self.item[-1]
  
  def get_stack(self):
    return self.item




=====================
function to match if the parenthesis are closed.
=====================

def is_match(top, inpt):
  if inpt == "}" and top == "{":
    return True

  if inpt == ")" and top == "(":
    return True
 

  if inpt == "]" and top == "[":
    return True
 



def is_paran(string):
  s = Stacks()
  is_balanced=True
  count=0

  while count < len(string) and is_balanced:
    paran = string[count]
    if paran in "{([":
      s.push(paran)
      #print(s.item)
    else:
      if s.is_empty() :
        print('hey')
        is_balanced = False
      else:
        top = s.pop()
        #print(s.item)
       # print(top)
        #print (count)
        if not is_match(top, paran):
          is_balanced = False

    count+=1
  
  if s.is_empty and is_balanced:
    return True
    
  else:
    return False



print (is_paran("([{}])"))  # can give any string to check, Can also use "input" to take user inputs
