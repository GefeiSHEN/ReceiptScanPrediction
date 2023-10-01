import gradio as gr
import json
import pandas as pd
import altair as alt

# Load weights from CSV file
def load_weights(filename):
    with open(filename, 'r') as f:
        weights = json.load(f)
    return float(weights['m']), float(weights['b']),float(weights['mean_date']),float(weights['std_date'])

# Load model weights
m, b, mean_date, std_date = load_weights('receipt_pred.json')

# Prediction
def pred(date_normalized):
    return m * date_normalized + b

# Graphing
def make_plot(historical_dates_relative, historical_values, y_pred, range_size):
    source = pd.DataFrame({
      'Date Range': historical_dates_relative,
      'Estimated Receipt Count': historical_values
    })

    chart = alt.Chart(source).mark_line().encode(
        x='Date Range',
        y='Estimated Receipt Count'
    )

    pred_point = pd.DataFrame({
        'Date Range': [0],
        'Estimated Receipt Count': [y_pred]
    })

    point_chart = alt.Chart(pred_point).mark_point(color='red').encode(
        x='Date Range',
        y='Estimated Receipt Count'
    )

    return chart + point_chart

# Process
def process_input(date_text, range_size):
    date_ordinal = pd.to_datetime(date_text).toordinal()
    date_normalized = float((date_ordinal - mean_date) / std_date)
    y_pred = pred(date_normalized)

    historical_dates = pd.Series(range(-range_size, range_size + 1)) / 10.0 + date_normalized
    historical_dates_relative = pd.Series([float(i) for i in range(-range_size, range_size+1)])
    historical_values = pred(historical_dates)
    plot = make_plot(historical_dates_relative, historical_values, y_pred, range_size)
    return y_pred, plot

# Gradio UI
app = gr.Interface(
    fn=process_input,
    inputs=[gr.Textbox(label="Date (MM/DD/YYYY)"),
            gr.Slider(minimum=10, maximum=100, step=1, label="Range (± n Days)")],
    outputs=[gr.Textbox(label="Estimated Receipt Count"),
             gr.Plot(label="Trend Plot")],
    title="Receipt Scanned Estimation"
)

if __name__ == "__main__":
    app.launch(server_name='0.0.0.0', server_port=8020)