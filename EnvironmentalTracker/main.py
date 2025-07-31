# conversion of showers to the gallons of water it uses
# (5 min shower * 2 --> 10 gals of water as seen in example)
showersToWater = 2
print("This is an environmental tracker !")
numShowers = int(input("How many showers have you taken this week? "))
showerTime = int(input("How long are your showers usually ? "))
totalShowerTime = numShowers*showerTime*showersToWater
print("You've used about {} gallons of water this week".format(totalShowerTime))
