# constellix2dme

Read Constellix export files in json format and create records in DnsMadeEasy

## Background

I leaped before I looked, and moved all my domains to Constellix before realizing that,
in my case, DME was actually half the price.

This script will read a directory of .json files in the format created by constellix,
and create Zone files that can be imported into DME.

**NOTE**: I was going to use the DME API to do this, but, from their [API Docs](https://dnsmadeeasy.com/technology/rest-api/):

> Please note: free API calls are limited to 150 calls every five minutes. Additional API calls are priced at $325 for 150 calls every five minutes.

## Usage

./ constellix2dme.py <input_dir> <output_dir>
