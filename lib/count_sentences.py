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

  def is_sentence(self):
    if self._value == "":
      return False
    elif self._value[-1] == ".":
      return True
    return False
  
  def is_question(self):
    if self._value == "":
      return False
    elif self._value[-1] == "?":
      return True
    return False
  
  def is_exclamation(self):
    if self._value == "":
      return False
    elif self._value[-1] == "!":
      return True
    return False
    
  def count_sentences(self):
    newval = self._value.replace("!", ".").replace("?",".")
    sen_list = newval.split(".")
    acc = 0
    for sen in sen_list:
      if len(sen) > 0:
        acc += 1
    return acc



    
