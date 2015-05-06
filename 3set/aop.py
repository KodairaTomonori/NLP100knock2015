#coding: utf-8
# Jsonファイルの読み込み

if __name__ == "__main__":
  import json
  import sys
  
  file = open(sys.argv[1])
  
  for line in file:
    obj = json.loads(line)
    if isinstance(obj, list) or isinstance(obj, dict):
      orig = json.dumps(obj, ensure_ascii = False)
      print eval("u'''%s'''" % orig).encode('utf-8')
    else:
      print obj

  file.close()
