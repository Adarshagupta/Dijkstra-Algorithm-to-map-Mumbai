# Mumbai Map Navigator

Mumbai Map Navigator is a Python-based interactive tool that helps users navigate through various locations in Mumbai, India. It provides features such as finding the shortest path between two locations, searching for locations, and retrieving information about specific areas in Mumbai.

## Features

1. **Shortest Path Finder**: Calculate the shortest route between two locations in Mumbai, including distance, estimated travel time, and fuel consumption.
2. **Location Search**: Search for locations in Mumbai using fuzzy matching to find close matches even with slight misspellings.
3. **Multiple Path Finder**: Discover up to three different paths between two locations.
4. **Location Information**: Get detailed information about a specific location, including a brief description and its connections to other areas.

## Requirements

- Python 3.6 or higher
- `heapq` module (included in Python standard library)
- `difflib` module (included in Python standard library)

## Installation

1. Clone this repository or download the `mumbai_map_navigator.py` file.
2. Ensure you have Python 3.6 or higher installed on your system.

## Usage

To run the Mumbai Map Navigator:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `mumbai_map_navigator.py`.
3. Run the following command: ```python mumbai_map_navigator.py```

4. Follow the on-screen prompts to interact with the navigator.

## Menu Options

When you run the program, you'll be presented with the following options:

1. **Find shortest path between two locations**: Enter a starting location and destination to find the shortest route.
2. **Search for a location**: Search for a location by name, with support for fuzzy matching.
3. **Find multiple paths between two locations**: Discover up to three different routes between two locations.
4. **Get information about a location**: Retrieve details about a specific location, including its description and connections.
5. **Exit**: Quit the program.

## Example Usage

Here's an example of how to use the Mumbai Map Navigator:

1. Run the program.
2. Choose option 1 to find the shortest path.
3. Enter "Bandra" as the starting location.
4. Enter "Colaba" as the destination.
5. The program will display the shortest route, total distance, estimated travel time, and fuel consumption.

## Data Structure

The Mumbai Map Navigator uses the following data structures:

- A dictionary of `Location` objects representing various locations in Mumbai.
- A graph represented as a nested dictionary, where each location is connected to its neighbors with associated distance, time, and fuel consumption values.

## Algorithms

The project implements several algorithms:

- **Dijkstra's Algorithm**: Used for finding the shortest path between two locations.
- **Depth-First Search (DFS)**: Used for finding multiple paths between two locations.
- **Binary Search**: Used for efficient location lookup.
- **Fuzzy String Matching**: Used for searching locations with similar names.

## Contributing

Contributions to the Mumbai Map Navigator project are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is open-source and available under the MIT License.
