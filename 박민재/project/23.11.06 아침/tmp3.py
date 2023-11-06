c = [[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]]
_c = c[0]
__c = _c[1]["name"]
#__c = _[1]["age"] + _c[0]["age"] + _c[2]["age"]
print(__c)
