"""
This file is part of blender-osm (OpenStreetMap importer for Blender).
Copyright (C) 2014-2017 Vladimir Elistratov
prokitektura+support@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from datetime import datetime
from building.manager import BuildingManager


class Logger:
    
    def __init__(self, op, osm):
        self.parseStartTime = datetime.now()
        op.logger = self
        self.op = op
        self.osm = osm
    
    def processStart(self):
        print("Parsing OSM file: {}".format(datetime.now() - self.parseStartTime))
        self.processStartTime = datetime.now()

    def processEnd(self):
        self.numBuildings()
        print("Processing of parsed OSM data: {}".format(datetime.now() - self.processStartTime))
    
    def renderStart(self):
        self.renderStartTime = datetime.now()

    def renderEnd(self):
        t = datetime.now()
        print("Mesh creation in Blender: {}".format(t - self.renderStartTime))
        print("Total duration: {}".format(t - self.parseStartTime))
    
    def numBuildings(self):
        op = self.op
        if not (op.mode == '3D' and op.buildings):
            return
        for m in op.managers:
            if isinstance(m, BuildingManager):
                print("The number of buildings: {}".format(len(m.buildings)))