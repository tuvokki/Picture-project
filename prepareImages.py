#!/usr/bin/python
import os
import Image
import shutil

basedir = "images"
thumbdir = "thumbs"
thumbwidth = 75
thumbheight = 75
lowdir = "low"
lowwidth = 500
lowheight = 500
fulldir = "full"
directories = os.listdir(basedir)

for directory in directories:
  path = basedir + "/" + directory
  print "processing " + path + "/" + fulldir
  if not os.path.isdir(path + "/" + fulldir):
    os.mkdir(path + "/" + fulldir, 0755)
  print "processing " + path + "/" + thumbdir
  if not os.path.isdir(path + "/" + thumbdir):
    os.mkdir(path + "/" + thumbdir, 0755)
  print "processing " + path + "/" + lowdir
  if not os.path.isdir(path + "/" + lowdir):
    os.mkdir(path + "/" + lowdir, 0755)

  images = os.listdir(path)
  for image in images:
    if not os.path.isdir(path + "/" + image):
      print "Processing image [" + path + "/" + image + "]"
      try:
        img = Image.open(path + "/" + image)
        img.thumbnail((thumbwidth,thumbheight), Image.ANTIALIAS)
        print "Writing image [" + path + "/" + thumbdir + "/" + image + "]"
        img.save(path + "/" + thumbdir + "/" + image, "JPEG")
      except IOError:
        print "cannot create thumbnail for", path + "/" + image

      try:
        img = Image.open(path + "/" + image)
        img.thumbnail((lowwidth, lowheight), Image.ANTIALIAS)  
        print "Writing image [" + path + "/" + lowdir + "/" + image + "]"
        img.save(path + "/" + lowdir + "/" + image, "JPEG")
      except IOError:
        print "cannot create lowfile for", path + "/" + image

      print "Moving original image [" + path + "/" + fulldir + "/" + image + "]"
      try:
        shutil.move(path + "/" + image, path + "/" + fulldir + "/" + image)
      except IOError:
        print "cannot move original image to", path + "/" + image
        
    
print "Done."

