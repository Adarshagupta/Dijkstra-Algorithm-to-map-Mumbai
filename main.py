from flask import Flask, render_template, request, jsonify
from mumbai_map_navigator import MumbaiMapNavigator

app = Flask(__name__)
navigator = MumbaiMapNavigator()


@app.route('/')
def index():
    return render_template('index.html', locations=navigator.sorted_locations)


@app.route('/find_path', methods=['POST'])
def find_path():
    start = request.form['start']
    end = request.form['end']

    start_match = navigator.find_location(start)
    end_match = navigator.find_location(end)

    if not start_match or not end_match:
        return jsonify({
            'error': 'Invalid locations',
            'start_suggestions': navigator.fuzzy_search(start),
            'end_suggestions': navigator.fuzzy_search(end)
        })

    distance, path, map_html = navigator.dijkstra(start_match, end_match)

    if distance != float('infinity'):
        total_distance, total_time, total_fuel = navigator.calculate_trip_details(
            path)
        return jsonify({
            'success': True,
            'start': start_match,
            'end': end_match,
            'path': ' -> '.join(path),
            'distance': total_distance,
            'time': total_time,
            'fuel': total_fuel,
            'map_html': map_html
        })
    else:
        return jsonify(
            {'error': f"No path found between {start_match} and {end_match}"})


@app.route('/location_info', methods=['POST'])
def location_info():
    name = request.form['name']
    location = navigator.find_location(name)

    if location:
        info = navigator.get_location_info(location)
        return jsonify(info)
    else:
        return jsonify({
            'error': f"Location '{name}' not found",
            'suggestions': navigator.fuzzy_search(name)
        })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
