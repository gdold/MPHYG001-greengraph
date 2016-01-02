from nose.tools import assert_equal, assert_almost_equal
import numpy as np
import geopy
import requests
from StringIO import StringIO
from matplotlib import image as img
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from ..graph import Greengraph
from ..map import Map
from mock import Mock, patch
import os

directory = os.path.dirname(os.path.abspath(__file__))

def test_createMap(): 
    mock_imgfile = open(os.path.join(directory,'fixtures','London.png'),'rb')
    accuratepixeldata = np.load(os.path.join(directory,'fixtures','London.npy'))
    #mock_imgdata = img.imread(StringIO(mock_imgfile.read()))
    #Patch requests.get, returning image data from file - no internet required
    with patch('requests.get', return_value=Mock(content=mock_imgfile.read())) as mock_get:
        testMap = Map(51.5072,-0.1275) #London
        np.testing.assert_allclose(testMap.pixels,accuratepixeldata) # Check testMap initialised correctly
        print 'Map'

#test_createMap()

def test_green():
    mock_imgfile = open(os.path.join(directory,'fixtures','London.png'),'rb')
    accurategreendata = np.load(os.path.join(directory,'fixtures','LondonGreen.npy'))
    threshold = 1.1
    with patch('requests.get', return_value=Mock(content=mock_imgfile.read())) as mock_get:
        testMap = Map(51.5072,-0.1275) #London
        assert (testMap.green(threshold) == accurategreendata).all() == True
        print 'green'

#test_green()

def test_count_green():
    mock_imgfile = open(os.path.join(directory,'fixtures','London.png'),'rb')
    threshold = 1.1
    with patch('requests.get', return_value=Mock(content=mock_imgfile.read())) as mock_get:
        testMap = Map(51.5072,-0.1275) #London
        assert testMap.count_green(threshold) == 106719 #Greenness for London
        print 'count_green'

#test_count_green()
            
#   If need to extend to use folders, this code snippet is platform-independent.
#   with open(os.path.join(directory,'folder','filename')) as fileobject 
 
