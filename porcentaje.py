import random
import sys
def main(infilename, outfilename, ratio):
    with open(infilename) as infile:
        with open(outfilename, 'w') as outfile:
            for line in infile:
                if random.random()<=ratio:
                    outfile.write(line)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.argv[0]} <infilename> <outfilename> <ratio>")
        exit(1)
    infilename = "quijote.txt"
    outfilename = "quijote_s05.txt"
    ratio = 0.1
    main(infilename, outfilename, ratio)

