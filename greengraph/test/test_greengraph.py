from nose.tools import assert_equal, assert_almost_equal
import numpy as np
import geopy
import requests
from StringIO import StringIO
from matplotlib import image as img
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import ..greengraph
from ..graph import Greengraph
from ..map import Map
from mock import Mock, patch