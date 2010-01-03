#!/usr/bin/env python

import os
from os import path
from glob import glob
import shutil

# The setting vars are all paths (which means they will be passed to something
# like file() or glob() etc

ASSET_DIRS       = ['./js', './img']
PAGES_DIR        = './page_bodies'
TOP_COMPONENT    = './components/top.html'
BOTTOM_COMPONENT = './components/bottom.html'
BUILD_DEST       = './build' # This guy gets cleaned up (rm *) -before- each run

print 'cleaning build dir...'
for f in glob('%s/*' % BUILD_DEST):
  print '\tremoving %s' % f
  if path.isfile(f):
    os.remove(f)
  elif path.isdir(f):
    shutil.rmtree(f)

print 'copying asset dirs...'
for dir in ASSET_DIRS:
  shutil.copytree(dir,'%s/%s' % (BUILD_DEST, dir))

print 'generating new pages...'
for page_body in glob('%s/*' % PAGES_DIR):
  page_name = page_body.split('/')[-1]
  top_contents = file(TOP_COMPONENT).read()
  bottom_contents = file(BOTTOM_COMPONENT).read()
  body_contents = file(page_body).read()
  file('%s/%s' % (BUILD_DEST, page_name),'w').write('%s\n%s\n%s' % (top_contents, body_contents, bottom_contents))

print 'done!'
