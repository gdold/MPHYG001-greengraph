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



def test_graph_Greengraph_geolocate(): # Test Greengraph.geolocate correctly calls geopy...geocode
    with patch.object(geopy.geocoders.GoogleV3,'geocode') as mockgeocode:
        testGreengraph = Greengraph('New York','Chicago')
        testGreengraph.geolocate('New York')
        mockgeocode.assert_called_with('New York', exactly_one=False)
        #print mockgeocode.mock_calls[0]

test_graph_Greengraph_geolocate()

def test_graph_Greengraph_location_sequence(): # Test Greengraph.location_sequence works
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

test_graph_Greengraph_location_sequence()

def test_graph_Greengraph_green_between():
    newyork_latlong = (1,1)
    chicago_latlong = (2,2)
    fakegeolocate = Mock(name="geolocate", side_effect=[newyork_latlong,chicago_latlong])
    fakecount_green = Mock(name="count_green", return_value=300)
    # NEED TO IMPORT PNG DATA FROM FILE
    #fakeimgdata = img.imread(StringIO(PUT FILE DATA HERE))
    
    with patch.object(Map,'count_green',fakecount_green) as mockcount_green:
        with patch.object(Greengraph,'geolocate',fakegeolocate) as mockgeolocate:
            testGreengraph = Greengraph('New York','Chicago')
            steps = 20
            print testGreengraph.location_sequence(
                testGreengraph.geolocate(testGreengraph.start),
                testGreengraph.geolocate(testGreengraph.end),
                steps)
            #with patch.object(requests,'get') as mock_get:
            #    fakeimg_imread = Mock(name='imread', return_value=fakeimgdata)
            #    with patch.object(img,'imread',fakeimg_imread):
            #        print testGreengraph.green_between(steps)
            #print testGreengraph.green_between(steps) # Test works up to here
            
 
test_graph_Greengraph_green_between()