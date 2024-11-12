try:
    f=open(r'C:/python/assign 10.py/sample.txt')
    try:
        content=f.read()
        print(content)
    finally:
        f.close()
except FileNotFoundError:
    print("file not found") 