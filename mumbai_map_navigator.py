import folium
import heapq
from difflib import get_close_matches


class Location:

    def __init__(self, name, description, lat, lon):
        self.name = name
        self.description = description
        self.lat = lat
        self.lon = lon


class MumbaiMapNavigator:

    def __init__(self):
        self.locations = {
            'Chhatrapati Shivaji Terminus':
            Location(
                'Chhatrapati Shivaji Terminus',
                'Historic railway station and UNESCO World Heritage Site',
                18.9398, 72.8355),
            'Churchgate':
            Location('Churchgate', 'Major railway terminus in South Mumbai',
                     18.9322, 72.8264),
            'Marine Drive':
            Location('Marine Drive',
                     'Scenic 3.6-kilometer-long boulevard along the coast',
                     18.9438, 72.8231),
            'Nariman Point':
            Location('Nariman Point',
                     'Central business district with modern skyscrapers',
                     18.9256, 72.8242),
            'Byculla':
            Location(
                'Byculla',
                'Residential and commercial area with the famous Byculla Zoo',
                18.9791, 72.8304),
            'Dadar':
            Location('Dadar', 'Central Mumbai hub known for its flower market',
                     19.0178, 72.8478),
            'Bandra':
            Location('Bandra',
                     'Upscale suburban area known for shopping and seafront',
                     19.0596, 72.8295),
            'Juhu':
            Location('Juhu', 'Upmarket neighborhood famous for Juhu Beach',
                     19.0883, 72.8263),
            'Andheri':
            Location('Andheri', 'Major residential and commercial suburb',
                     19.1136, 72.8697),
            'Mahalaxmi':
            Location('Mahalaxmi', 'Home to Mahalaxmi Temple and Racecourse',
                     18.9825, 72.8122),
        }

        self.mumbai_map = {
            'Chhatrapati Shivaji Terminus': {
                'Churchgate': (2, 10, 0.5),
                'Byculla': (5, 20, 1.2),
                'Mahalaxmi': (7, 25, 1.7)
            },
            'Churchgate': {
                'Chhatrapati Shivaji Terminus': (2, 10, 0.5),
                'Marine Drive': (1, 5, 0.3),
            },
            'Marine Drive': {
                'Churchgate': (1, 5, 0.3),
                'Nariman Point': (3, 12, 0.7),
            },
            'Nariman Point': {
                'Marine Drive': (3, 12, 0.7),
                'Byculla': (7, 28, 1.7),
            },
            'Byculla': {
                'Chhatrapati Shivaji Terminus': (5, 20, 1.2),
                'Nariman Point': (7, 28, 1.7),
                'Dadar': (6, 25, 1.5),
            },
            'Dadar': {
                'Byculla': (6, 25, 1.5),
                'Bandra': (7, 30, 1.7),
            },
            'Bandra': {
                'Dadar': (7, 30, 1.7),
                'Juhu': (5, 20, 1.2),
            },
            'Juhu': {
                'Bandra': (5, 20, 1.2),
                'Andheri': (4, 18, 1.0),
            },
            'Andheri': {
                'Juhu': (4, 18, 1.0),
            },
            'Mahalaxmi': {
                'Chhatrapati Shivaji Terminus': (7, 25, 1.7),
            },
        }
        self.sorted_locations = sorted(self.locations.keys())

    def binary_search(self, target):
        left, right = 0, len(self.sorted_locations) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.sorted_locations[mid] == target:
                return mid
            elif self.sorted_locations[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def find_location(self, name):
        index = self.binary_search(name)
        if index != -1:
            return self.sorted_locations[index]
        return None

    def fuzzy_search(self, name, cutoff=0.6):
        matches = get_close_matches(name,
                                    self.sorted_locations,
                                    n=3,
                                    cutoff=cutoff)
        return matches

    def create_map_visualization(self, path):
        map_center = [18.9667, 72.8333]  # Approximate center of Mumbai
        m = folium.Map(location=map_center, zoom_start=12)

        for location in path:
            folium.Marker(
                [self.locations[location].lat, self.locations[location].lon],
                popup=location).add_to(m)

        route_coords = [[self.locations[loc].lat, self.locations[loc].lon]
                        for loc in path]
        folium.PolyLine(route_coords, color="red", weight=2.5,
                        opacity=1).add_to(m)

        return m._repr_html_()

    def dijkstra(self, start, end):
        distances = {node: float('infinity') for node in self.mumbai_map}
        distances[start] = 0
        pq = [(0, start)]
        previous = {node: None for node in self.mumbai_map}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = previous[current_node]
                path = path[::-1]
                map_html = self.create_map_visualization(path)
                return distances[end], path, map_html

            if current_distance > distances[current_node]:
                continue

            for neighbor, (distance, _,
                           _) in self.mumbai_map[current_node].items():
                total_distance = current_distance + distance
                if total_distance < distances[neighbor]:
                    distances[neighbor] = total_distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (total_distance, neighbor))

        return float('infinity'), [], ""

    def calculate_trip_details(self, path):
        total_distance = 0
        total_time = 0
        total_fuel = 0
        for i in range(len(path) - 1):
            distance, time, fuel = self.mumbai_map[path[i]][path[i + 1]]
            total_distance += distance
            total_time += time
            total_fuel += fuel
        return total_distance, total_time, total_fuel

    def get_location_info(self, name):
        location = self.locations[name]
        connections = self.mumbai_map[name]
        return {
            'name':
            location.name,
            'description':
            location.description,
            'connections': [{
                'name': neighbor,
                'distance': details[0],
                'time': details[1],
                'fuel': details[2]
            } for neighbor, details in connections.items()]
        }
