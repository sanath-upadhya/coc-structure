import decorations as d
from utils.Position import Position
from utils.Size import Size

position = Position(2,2)
size = Size(2,2)
purchase_cost = {"elixir":0,"gold":0,"gems":0,"dark_elixir":0}
c = d.PirateFlag()

print(c.size)
type_of_resource = c.purchase_cost.get_type_of_resource()
print(c.purchase_cost.get_type_of_resource())
print(c.purchase_cost.get_cost(type_of_resource))
print(c.purchased_by_user)
print(str(c.position.x) + str(c.position.y))

c.purchase_decoration(position)
print(str(c.position.x) + str(c.position.y))
print(c.purchased_by_user)