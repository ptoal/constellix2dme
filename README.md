# constellix2zone

Read Constellix export files in json format and create BIND Zone files that can be imported into DNSMadeEasy.

## Background

I leaped before I looked, and moved all my domains to Constellix before realizing that,
in my case, DME was actually half the price.

This script will read a directory of .json files in the format created by constellix,
and create Zone files that can be imported into DME.

**NOTE**: I was going to use the DME API to do this, but, from their [API Docs](https://dnsmadeeasy.com/technology/rest-api/):

> Please note: free API calls are limited to 150 calls every five minutes. Additional API calls are priced at $325 for 150 calls every five minutes.

## Installation

Clone the repository to a local directory.  eg: `git clone https://github.com/ptoal/constellix2zone`

Install the requirements (Currently only Jinja2). eg: `pip install -r requirements.txt`

## Notes

Currently processes the following record types:

- SOA
- CNAME
- A
- AAA
- MX
- SPF
- TXT
- SRV

## Usage

./ constellix2dme.py # Process all .json files in current directory, writing <filename>.zone output

### Options

-i / --infile Specify a file to process (can be used multiple times)

--indir       Specify a directory to look for .json files

--outdir      Specify output directory (default is current directory)

-d            Debugging

-c            Clobber (overwrite) existing files

-n            Don't write files.  Just dump to stdout
