# Import Required Modules
from flask import Flask, render_template, request, jsonify
from data_process import DataProcess


# Create Home Page Route
app = Flask(__name__)


@app.route('/')
def plot():
    process_data = DataProcess()
    mean = process_data.transform_data()
    df = mean.to_frame().reset_index()
    values = df['value'].tolist()
    time = df['end_date'].tolist()
    return render_template('chart.html', value=values, time=time)


@app.route('/process', methods=['POST'])
def process():
    updated_date = request.get_json()
    updated_startDate = updated_date['startDate']
    updated_endDate = updated_date['endDate']
    process_data = DataProcess()
    mean = process_data.transform_data(endpoint='/actual_generations_per_unit',
                                       start_date=updated_startDate+'T00:00:00%2B02:00',
                                       end_date=updated_endDate+'T23:00:00%2B02:00')
    df = mean.to_frame().reset_index()
    values = df['value'].tolist()
    time = df['end_date'].tolist()
    response = {'value': values,
                'time': time}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
