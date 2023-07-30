import math

def cakes(recipe, available):
    count = {}
    for key in recipe.keys():
        if available.get(key) != None:
            count[key] = math.floor(available.get(key)/recipe[key])
        else:
            return 0
    return min(count.values())


# must return 2
# print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
# must return 0
# print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))

# Wrong result for 
# recipe {'pears': 38, 'butter': 14, 'crumbles': 22} and 
# available ingredients {'crumbles': 2563, 'oil': 8502, 'milk': 4545, 'cocoa': 7892, 'pears': 1200, 'butter': 563, 'flour': 3036, 'apples': 6336, 'sugar': 3705, 'chocolate': 2639}
# 32 should equal 31
print(cakes({'pears': 38, 'butter': 14, 'crumbles': 22}, {'crumbles': 2563, 'oil': 8502, 'milk': 4545, 'cocoa': 7892, 'pears': 1200, 'butter': 563, 'flour': 3036, 'apples': 6336, 'sugar': 3705, 'chocolate': 2639}))