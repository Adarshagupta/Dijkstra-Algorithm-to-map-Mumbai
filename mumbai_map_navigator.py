import heapq
from difflib import get_close_matches


class Location:

  def __init__(self, name, description):
    self.name = name
    self.description = description


class MumbaiMapNavigator:

  def __init__(self):
    self.locations = {
        'Chhatrapati Shivaji Terminus':
        Location('Chhatrapati Shivaji Terminus',
                 'Historic railway station and UNESCO World Heritage Site'),
        'Churchgate':
        Location('Churchgate', 'Major railway terminus in South Mumbai'),
        'Marine Drive':
        Location('Marine Drive',
                 'Scenic 3.6-kilometer-long boulevard along the coast'),
        'Nariman Point':
        Location('Nariman Point',
                 'Central business district with modern skyscrapers'),
        'Byculla':
        Location(
            'Byculla',
            'Residential and commercial area with the famous Byculla Zoo'),
        'Dadar':
        Location('Dadar', 'Central Mumbai hub known for its flower market'),
        'Bandra':
        Location('Bandra',
                 'Upscale suburban area known for shopping and seafront'),
        'Juhu':
        Location('Juhu', 'Upmarket neighborhood famous for Juhu Beach'),
        'Andheri':
        Location('Andheri', 'Major residential and commercial suburb'),
        'Mahalaxmi':
        Location('Mahalaxmi', 'Home to Mahalaxmi Temple and Racecourse'),
        'Malabar Hill':
        Location('Malabar Hill', 'Affluent neighborhood with Hanging Gardens'),
        'Girgaon Chowpatty':
        Location('Girgaon Chowpatty', 'Famous beach and recreation area'),
        'Colaba':
        Location(
            'Colaba',
            'Tourist hub with Gateway of India and Taj Mahal Palace Hotel'),
        'Parel':
        Location('Parel', 'Former textile mill area now turned commercial'),
        'Mahim':
        Location('Mahim', 'Known for Mahim Fort and Mahim Creek'),
        'Kurla':
        Location('Kurla', 'Major railway junction and commercial area'),
        'Santacruz':
        Location('Santacruz', 'Residential suburb with domestic airport'),
        'Versova':
        Location('Versova',
                 'Coastal suburb known for fishing village and beach'),
        'Goregaon':
        Location('Goregaon', 'Suburban area with Film City'),
        'Powai':
        Location('Powai', 'Upmarket residential neighborhood with lake'),
        'Worli':
        Location('Worli', 'Former industrial area now a major commercial hub'),
        'Ghatkopar':
        Location(
            'Ghatkopar',
            'Eastern suburb with mix of residential and commercial areas'),
        'Vile Parle':
        Location('Vile Parle',
                 'Residential area known for schools and temples'),
        'Borivali':
        Location('Borivali', 'Suburb with Sanjay Gandhi National Park')
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
            'Malabar Hill': (6, 22, 1.5)
        },
        'Marine Drive': {
            'Churchgate': (1, 5, 0.3),
            'Nariman Point': (3, 12, 0.7),
            'Girgaon Chowpatty': (4, 15, 1.0)
        },
        'Nariman Point': {
            'Marine Drive': (3, 12, 0.7),
            'Byculla': (7, 28, 1.7),
            'Colaba': (2, 8, 0.5)
        },
        'Byculla': {
            'Chhatrapati Shivaji Terminus': (5, 20, 1.2),
            'Nariman Point': (7, 28, 1.7),
            'Dadar': (6, 25, 1.5),
            'Parel': (3, 12, 0.7)
        },
        'Dadar': {
            'Byculla': (6, 25, 1.5),
            'Bandra': (7, 30, 1.7),
            'Mahim': (4, 18, 1.0),
            'Parel': (2, 10, 0.5)
        },
        'Bandra': {
            'Dadar': (7, 30, 1.7),
            'Juhu': (5, 20, 1.2),
            'Kurla': (8, 35, 2.0),
            'Santacruz': (3, 12, 0.7)
        },
        'Juhu': {
            'Bandra': (5, 20, 1.2),
            'Andheri': (4, 18, 1.0),
            'Versova': (3, 15, 0.7)
        },
        'Andheri': {
            'Juhu': (4, 18, 1.0),
            'Goregaon': (6, 25, 1.5),
            'Powai': (9, 35, 2.2)
        },
        'Mahalaxmi': {
            'Chhatrapati Shivaji Terminus': (7, 25, 1.7),
            'Worli': (4, 15, 1.0)
        },
        'Malabar Hill': {
            'Churchgate': (6, 22, 1.5),
            'Girgaon Chowpatty': (5, 20, 1.2)
        },
        'Girgaon Chowpatty': {
            'Marine Drive': (4, 15, 1.0),
            'Malabar Hill': (5, 20, 1.2)
        },
        'Colaba': {
            'Nariman Point': (2, 8, 0.5)
        },
        'Parel': {
            'Byculla': (3, 12, 0.7),
            'Dadar': (2, 10, 0.5)
        },
        'Mahim': {
            'Dadar': (4, 18, 1.0),
            'Bandra': (3, 12, 0.7)
        },
        'Kurla': {
            'Bandra': (8, 35, 2.0),
            'Ghatkopar': (5, 22, 1.2)
        },
        'Santacruz': {
            'Bandra': (3, 12, 0.7),
            'Vile Parle': (2, 10, 0.5)
        },
        'Versova': {
            'Juhu': (3, 15, 0.7)
        },
        'Goregaon': {
            'Andheri': (6, 25, 1.5),
            'Borivali': (7, 30, 1.7)
        },
        'Powai': {
            'Andheri': (9, 35, 2.2),
            'Ghatkopar': (6, 25, 1.5)
        },
        'Worli': {
            'Mahalaxmi': (4, 15, 1.0),
            'Dadar': (5, 20, 1.2)
        },
        'Ghatkopar': {
            'Kurla': (5, 22, 1.2),
            'Powai': (6, 25, 1.5)
        },
        'Vile Parle': {
            'Santacruz': (2, 10, 0.5),
            'Andheri': (3, 12, 0.7)
        },
        'Borivali': {
            'Goregaon': (7, 30, 1.7)
        }
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
        return distances[end], path[::-1]

      if current_distance > distances[current_node]:
        continue

      for neighbor, (distance, _, _) in self.mumbai_map[current_node].items():
        total_distance = current_distance + distance
        if total_distance < distances[neighbor]:
          distances[neighbor] = total_distance
          previous[neighbor] = current_node
          heapq.heappush(pq, (total_distance, neighbor))

    return float('infinity'), []

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

  def find_all_paths(self, start, end, max_paths=3):
    paths = []
    details = []

    def dfs(node, path, distance, time, fuel):
      if node == end:
        paths.append(path[:])
        details.append((distance, time, fuel))
        return

      if len(paths) >= max_paths:
        return

      for neighbor, (d, t, f) in self.mumbai_map[node].items():
        if neighbor not in path:
          path.append(neighbor)
          dfs(neighbor, path, distance + d, time + t, fuel + f)
          path.pop()

    dfs(start, [start], 0, 0, 0)
    return list(zip(details, paths))

  def run(self):
    print("Welcome to the Mumbai Map Navigator!")
    while True:
      print("\nOptions:")
      print("1. Find shortest path between two locations")
      print("2. Search for a location")
      print("3. Find multiple paths between two locations")
      print("4. Get information about a location")
      print("5. Exit")

      choice = input("Enter your choice (1-5): ")

      if choice == '1':
        start = input("Enter starting location: ")
        end = input("Enter destination: ")
        start_match = self.find_location(start)
        end_match = self.find_location(end)

        if not start_match:
          print(
              f"Starting location '{start}' not found. Did you mean one of these?"
          )
          print(", ".join(self.fuzzy_search(start)))
          continue

        if not end_match:
          print(f"Destination '{end}' not found. Did you mean one of these?")
          print(", ".join(self.fuzzy_search(end)))
          continue

        distance, path = self.dijkstra(start_match, end_match)
        if distance != float('infinity'):
          total_distance, total_time, total_fuel = self.calculate_trip_details(
              path)
          print(f"\nShortest path from {start_match} to {end_match}:")
          print(f"Route: {' -> '.join(path)}")
          print(f"Total distance: {total_distance} km")
          print(f"Estimated travel time: {total_time} minutes")
          print(f"Estimated fuel consumption: {total_fuel:.2f} liters")
        else:
          print(f"No path found between {start_match} and {end_match}")

      elif choice == '2':
        name = input("Enter location name to search: ")
        matches = self.fuzzy_search(name)
        if matches:
          print(f"Matching locations: {', '.join(matches)}")
        else:
          print(f"No matching locations found for '{name}'")

      elif choice == '3':
        start = input("Enter starting location: ")
        end = input("Enter destination: ")
        start_match = self.find_location(start)
        end_match = self.find_location(end)

        if not start_match or not end_match:
          print("One or both locations not found.")
          continue

        paths = self.find_all_paths(start_match, end_match)
        if paths:
          print(
              f"\nFound {len(paths)} paths from {start_match} to {end_match}:")
          for i, ((distance, time, fuel), path) in enumerate(paths, 1):
            print(f"\nPath {i}:")
            print(f"Route: {' -> '.join(path)}")
            print(f"Total distance: {distance} km")
            print(f"Estimated travel time: {time} minutes")
            print(f"Estimated fuel consumption: {fuel:.2f} liters")
        else:
          print(f"No paths found between {start_match} and {end_match}")

      elif choice == '4':
        name = input("Enter location name: ")
        location = self.find_location(name)
        if location:
          print(f"\nInformation about {location}:")
          print(self.locations[location].description)
          print("\nConnections:")
          for neighbor, (distance, time,
                         fuel) in self.mumbai_map[location].items():
            print(
                f"- {neighbor}: {distance} km, {time} min, {fuel:.2f} L fuel")
        else:
          print(f"Location '{name}' not found.")
          matches = self.fuzzy_search(name)
          if matches:
            print(f"Did you mean one of these? {', '.join(matches)}")

      elif choice == '5':
        print("Thank you for using Mumbai Map Navigator. Goodbye!")
        break

      else:
        print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
  navigator = MumbaiMapNavigator()
  navigator.run()
