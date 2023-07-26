#!/usr/bin/env python3
from decimal import *

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, quantity=1):
    for i in range(quantity):
      self.items.append(title)
    
    self.last_transaction = price * quantity
    self.total += price*quantity

  def apply_discount(self, discount=20):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = round(self.total * (1 - discount/100))
      print(f'After the discount, the total comes to ${self.total}.')

  def void_last_transaction(self):
    self.items.pop()
    self.total -= self.last_transaction


