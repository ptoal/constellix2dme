#!/usr/bin/env python3
# Python script to convert Constellix json files to DME Zone files

import json, os, sys
import argparse

from jinja2 import Environment, PackageLoader
env = Environment(
    loader=PackageLoader('constellix2zone', 'templates'),
    extensions=['jinja2.ext.do']
)

def main():
    # create parser
    parser = argparse.ArgumentParser()
    
    # add arguments to the parser
    parser.add_argument("--indir", help="Directory containing json zone files from Constellix")
    parser.add_argument("-i", "--infile", help="Path to a single json zone file from Constellix", action="append")
    parser.add_argument("--outdir", help="Output directory for Zone files")
    parser.add_argument("-c","--clobber", help="Overwrite existing files")
    parser.add_argument("-d", "--debug", action="store_true")

    # parse the arguments
    args = parser.parse_args()

    debug=args.debug
    clobber=args.clobber

    if args.indir:
        indir=args.indir
    else:
        indir=os.getcwd()

    if args.outdir:
        outdir=args.outdir
    else:
        outdir=os.getcwd()

    if debug:            
        import pprint
        pp = pprint.PrettyPrinter(depth=9)

    if not os.path.isdir(indir):
        print ("Error: Input Directory doesn't exist.")
        exit(1)

    if not os.path.isdir(outdir):
        os.makedirs(outdir)
        print ("Created directory: ", outdir)

    inputfiles = [f for f in os.listdir(indir) if f.endswith('.' + 'json')]
    if args.infile:
        inputfiles.extend(args.infile)


    print ("Files to process: " + " ".join(inputfiles))

    for file in inputfiles:
        outfile_name = os.path.split(file)[1]
        outfile_path = os.path.join(outdir, os.path.splitext(outfile_name)[0]+".zone")

        if os.path.exists(outfile_path) and not clobber:
            print("Error: File exists: " + outfile_path, file=sys.stderr)
            next

        handle = open(os.path.join(indir, file),'r')
        zone_data = json.load(handle)

        if debug:
            print("ZONE DATA:")
            pp.pprint(zone_data)

        from jinja2 import Template

        zone_template = env.get_template('zone.j2')
        zone_context = zone_template.new_context(zone_data)
        output = zone_template.render(zone_context)

        if debug:
            print (output)        

        outfile = open(outfile_path,"w")
        outfile.write(output)

if __name__ == "__main__":
    # execute only if run as a script
    main()

