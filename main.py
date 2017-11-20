import json
import sys

print("Hello")
json_input = '{ "rate_of_climbing": 18.4, "speed_factor": 520}'
json_data = ''.join([line.strip() for line in open('log.json')])
for i in range(1,10):
    print(i)
    # try:
    #     print(json.loads(json.dumps(sys.stdin.read())))
    # except (ValueError, KeyError, TypeError):
    #     print("error value: " + str(ValueError) + " error key: " + str(KeyError) + " error type: " + str(KeyError))
try:
    decoded = json.loads(json_input)
    print (json.dumps(decoded, sort_keys=True, indent=4))
    print ("JSON parsing example: ", decoded['rate_of_climbing'])
    print ("Complex JSON parsing example: ", decoded['speed_factor'])

    _data = json.loads(json_data)
    print(json.dumps(_data, sort_keys=True, indent=4))

except (ValueError, KeyError, TypeError):
    print ("JSON format error")

# print (json.dumps({'4': 5, '6': 7}, sort_keys=True,
#     indent=4, separators=(',', ': ')))
# a=json.dumps( json.loads( sys.stdin.read() ))
# print(a)
print(i)