def military_time(time):
    
    if 'pm' in time:
      if time[:2] == '12':
        return time.replace('pm','')
      else:
        return str(int(time.replace('pm',''))+12)
    else:
      if time[:2] == '12':
        return str(int(time.replace('am',''))-12)
      else:
        return time.replace('am','')

class Menu:
  
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = military_time(start_time)
    self.end_time = military_time(end_time)
  
  def __repr__(self):
    return '{0} menu is available from {1} to {2}'.format(self.name,self.start_time,self.end_time)
  
  def calculate_bill(self,purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items.get(item)
    return total
  
  
class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return 'located at {}'.format(self.address)
  
  def available_menus(self,time):
    available_menus = []
    time = military_time(time)
    for menu in self.menus:
      print(time)
      print(menu.start_time,menu.end_time)
      print(time >= menu.start_time , time <= menu.end_time)
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
 

class Business:
  
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
    
  
  
brunch = Menu('Brunch',{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},'11am','4pm')

early_bird = Menu('Early-bird',{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},'3pm','6pm')

dinner = Menu('Dinner',{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},'5pm','11pm')

kids = Menu('Kids',{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},'11am','9pm')

arepas_menu = Menu("Take a' Arepa",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},'10am','8pm')

flagship_store = Franchise('1232 West End Road',[brunch,early_bird,dinner,kids])

new_installment = Franchise('12 East Mulberry Street',[brunch,early_bird,dinner,kids])

arepas_place = Franchise('189 Fitzgerald Avenue',[arepas_menu])

business = Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])
