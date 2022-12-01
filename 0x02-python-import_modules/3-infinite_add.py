#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    results = 0
    for i in range(1, len(sys.argv)):
        results += int(sys.argv[i])
    print("{}".format(results))
