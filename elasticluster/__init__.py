#! /usr/bin/env python
#
#   Copyright (C) 2013-2016, 2019 S3IT, University of Zurich
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
__author__ = 'Nicolas Baer <nicolas.baer@uzh.ch>'
__version__ = '1.3.dev21'


# stdlib imports
import logging


# public API
log = logging.getLogger("elasticluster")

from elasticluster.cluster import Cluster
from elasticluster.repository import AbstractClusterRepository, MultiDiskRepository
