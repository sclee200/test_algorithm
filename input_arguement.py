import argparse

args = argparse.ArgumentParser()
args.add_argument('-x','--XValue', required=True)
args.add_argument('-y','--yValue', required=False)


argvar = vars(args.parse_args())

pass