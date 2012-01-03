#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import simplehtmlhelper
import os

simplehtmlhelper.header()

rootdir  = "/webdir/tuvok.nl/test123/"
basedir = "images"
thumbdir = "thumbs"
lowdir = "low"
fulldir = "full"
directories = os.listdir(rootdir + basedir)

for directory in directories:
  path = basedir + "/" + directory
  #simplehtmlhelper.printline("processing " + path + "/" + fulldir)

  images = os.listdir(path + "/" + fulldir)
  for image in images:
    if not os.path.isdir(path + "/" + image):
      #simplehtmlhelper.printline("Processing image [" + path + "/" + image + "]")
      simplehtmlhelper.printli(path,image)

simplehtmlhelper.footer()
