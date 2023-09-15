#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def pun_check(self, char):
    if self._value == "":
      return False
    elif self._value[-1] == char:
      return True
    return False

  def is_sentence(self):
    return self.pun_check(".")
  
  def is_question(self):
    return self.pun_check("?")
  
  def is_exclamation(self):
    return self.pun_check("!")
    
  def count_sentences(self):
    newval = self._value.replace("!", ".").replace("?",".")
    sen_list = newval.split(".")
    acc = 0
    for sen in sen_list:
      if len(sen) > 0:
        acc += 1
    return acc



    
