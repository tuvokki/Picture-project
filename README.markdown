Purpose
=======
This application is made with large images in mind. It will transform your desktop-size images to reasonable web-sized thumbnails and showable pictures.
It then renders them and creates a download link for the real large image.

Version
-------
This version is tagged 1.0 since it is the production version. No history yet.

Installation
============
Preamble
--------
checkout the repository from git in a directory of your liking.
Make sure your webserver supports python and is capable of serving an index.py.

Install images
--------------
* Create or copy a directory with images into {BASEDIR}/images/[your_dir]
* run the prepareImages.py from {BASEDIR} to create the folder structure

`{BASEDIR}/images/[your_dir]/full   --> contains the images in full`  
`{BASEDIR}/images/[your_dir]/low    --> contains showable images`  
`{BASEDIR}/images/[your_dir]/thumbs --> contains the thumbnails`  

Personalize
-----------
Open simplehtmlhelper.py and change title, slogan and slug

Todo's
------
Rewrite simplehtmlhelper.py to something usefull and configurable
