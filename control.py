#!/usr/bin/python3
import sys
import argparse
import bg
from linedraw import *
import ntpath


def main(args = sys.argv[1:]):
    parser = argparse.ArgumentParser()

    parser.add_argument("--boxtest","-b",
                       help = "run the box test",
                       action = "store_true")

    parser.add_argument("--plot","-p",
                       help = "plot file on plotter",
                       action = "store_true")

    parser.add_argument("--draw","-d",
                       help = "draw file ",
                       action = "store_true")

    parser.add_argument("--file", "-f",
                        help="input file must be in images folder",
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument("--int_value",
                        help="display a square of a given number",
                        type=int)

    parser.add_argument("--draw-contours", "-dc",
                        help="number of contours",
                        type=int,
                        default=2)

    parser.add_argument("--repeat-contours", "-rc",
                        help="number of repeats of the contours",
                        type=int,
                        default=1)

    parser.add_argument("--repeat-hatch", "-rh",
                        help="number of repeats of the hatch",
                        type=int,
                        default=1)

    parser.add_argument("--draw-hatch","-dh",
                        help="density of hatch",
                        type=int,
                        default=16)


    args = parser.parse_args(args)


    # running the box test
    if args.boxtest:
        bg.bg.box()

    if args.file is not None:
        fileName=ntpath.basename(args.file.name)
        print ("working with file %s" % (args.file.name))
        print ("must be in images folder..")
        print ("filename only: %s" % (fileName))

        if args.plot == False:
            image_to_json(fileName, draw_contours=args.draw_contours, draw_hatch=args.draw_hatch, repeat_contours=args.repeat_contours, repeat_hatch=args.repeat_hatch)
            if args.draw:
                print("try to show you the result")
                lines = vectorise(fileName, draw_contours=args.draw_contours, draw_hatch=args.draw_hatch, repeat_contours=args.repeat_contours, repeat_hatch=args.repeat_hatch)
                draw(lines)
        else:
            print("running plot")
            bg.bg.plot_file(args.file.name)



if __name__ == '__main__':
    main()






