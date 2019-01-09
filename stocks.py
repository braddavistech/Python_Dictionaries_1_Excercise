purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]


stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak", "GE": "General Electric" }

def stock_value():
  total = 0
  companyOwned = []
  for item in purchases:
    name = stockDict.get(item[0])
    print("I purchased " + str(item[1]) + " shares of " + name + " stock for " + str(item[3]) + " on " + item[2] + ".")
    total += item[1] * item[3]
    notIn = 1
    for companyName in companyOwned:

      if item[0] == companyName[0]:
        print("inside")
        oldName = companyOwned.index(companyName)
        temp = [companyName, item]
        companyOwned[oldName] = temp
        notIn = 0
    if notIn == 1:
      companyOwned.append(item)
  for itemInOwned in companyOwned:
    if itemInOwned is list:
      for newItem in itemInOwned:
        print("inside list")
        print(newItem)
    else:
      coName = stockDict.get(itemInOwned[0])
      print("----------" + str(itemInOwned[0][0]) + "----------")
      print(itemInOwned)
  print("Total value of stocks purchased is $" + str(total) + ".")



stock_value()