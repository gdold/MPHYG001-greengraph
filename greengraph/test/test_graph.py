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
from itertools import cycle
import os

directory = os.path.dirname(os.path.abspath(__file__))

def test_graph_Greengraph_geolocate(): # Test Greengraph.geolocate correctly calls geopy...geocode
    # Patch geocode to avoid calling internet
    with patch.object(geopy.geocoders.GoogleV3,'geocode') as mockgeocode:
        testGreengraph = Greengraph('New York','Chicago')
        testGreengraph.geolocate('New York')
        mockgeocode.assert_called_with('New York', exactly_one=False)
    print 'geolocate'

#test_graph_Greengraph_geolocate()

def test_graph_Greengraph_location_sequence(): # Test Greengraph.location_sequence works
    with patch.object(geopy.geocoders.GoogleV3,'geocode') as mockgeocode:
        testGreengraph = Greengraph('New York','Chicago')
        result = [[-1.   ,  1.   ],
                  [-0.625,  1.125],
                  [-0.25 ,  1.25 ],
                  [ 0.125,  1.375],
                  [ 0.5  ,  1.5  ],
                  [ 0.875,  1.625],
                  [ 1.25 ,  1.75 ],
                  [ 1.625,  1.875],
                  [ 2.   ,  2.   ]]
        equalitytest = testGreengraph.location_sequence((-1,1),(2,2),9) == result
        assert equalitytest.all() == True
    print 'location_sequence'

#test_graph_Greengraph_location_sequence()

def test_graph_Greengraph_green_between():
    mock_imgfile = open(os.path.join(directory,'fixtures','London.png'),'rb')
    latlongcycle = cycle([(1,1),(2,2)])
    fakegeolocate = Mock(name="geolocate", side_effect=latlongcycle)
    steps = 10
    
    # Patch requests and return saved image data
    with patch('requests.get', return_value=Mock(content=mock_imgfile.read())) as mock_get:
        with patch.object(Greengraph,'geolocate',fakegeolocate) as mockgeolocate:
            testGreengraph = Greengraph('New York','Chicago')
            assert testGreengraph.green_between(steps) == ([106719]*steps)
    print 'green_between'

#test_graph_Greengraph_green_between()