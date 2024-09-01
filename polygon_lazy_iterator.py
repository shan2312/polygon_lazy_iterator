import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self.count_vertices = n
        self.circumradius = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @count_vertices.setter
    def count_vertices(self, n):
        self._n = n
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @circumradius.setter
    def circumradius(self, r):
        self._R = r
        self._side_length = None
        self._apothem = None
        self._area = None

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            print('calculated interior angle')
            self._interior_angle = (self._n - 2) * 180 / self._n
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
    
    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._n * self.side_length
        return self._perimeter
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented

class PolygonsIterator():
    def __init__(self, m, R):
        self.index = 3
        self.m = m
        self.r = R

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= (self.m + 1):
            raise StopIteration
        else:
            next_polygon = Polygon(self.index, self.r)
            self.index += 1
            return next_polygon


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __iter__(self):
        return PolygonsIterator(self._m, self._R)
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]
    