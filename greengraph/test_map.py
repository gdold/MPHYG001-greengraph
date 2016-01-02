from nose.tools import assert_equal, assert_almost_equal
import numpy as np
import geopy
import requests
from StringIO import StringIO
from matplotlib import image as img
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from graph import Greengraph
from map import Map
import greengraph
from mock import Mock, patch
import os



def test_createMap(): 
    mock_imgfile = open('London.png','rb')
    #mock_imgdata = img.imread(StringIO(mock_imgfile.read()))
    #Patch requests.get, returning image data from file - no internet required
    with patch('requests.get', return_value=Mock(content=mock_imgfile.read())) as mock_get:
        testMap = Map(51.5072,-0.1275) #London
        print testMap.count_green() #106719 for London

test_createMap()


            
#           with patch('requests.get', return_value=Mock(content=png_file.read())) as mock_get
#           with open(os.path.join(dir,'folder','filename')) as fileobject 
 
