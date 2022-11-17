import plotly.express as px

import data_getter

image_path = "images/"
main_image_width = 1000
main_image_height = 800


def create_line_graph(is_guest):
    df = data_getter.get_year_chart_data(is_guest)
    fig = px.line(df, markers=True, width=main_image_width, height=main_image_height)
    fig.update_yaxes(title=None)
    fig.update_xaxes(title=None)
    fig.update_layout(legend_title=None, legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    filename = "line_graph"
    if is_guest:
        filename += "_guest"
    filename += ".png"
    fig.write_image(image_path + filename)


def create_bar_plot(is_guest):
    df = data_getter.get_year_chart_data(is_guest)
    fig = px.bar(df, width=main_image_width, height=main_image_height, text_auto=True)
    fig.update_yaxes(title=None)
    fig.update_xaxes(title=None)
    fig.update_layout(legend_title=None, legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    filename = "bar_plot"
    if is_guest:
        filename += "_guest"
    filename += ".png"
    fig.write_image(image_path + filename)


def create_sum_per_day_graph():
    df = data_getter.get_sum_per_day()
    fig = px.line(df, x="date", y="total", markers=True, width=main_image_width, height=main_image_height/3)
    fig.update_layout(xaxis=dict(tickmode='linear'))
    fig.update_yaxes(title=None)
    fig.update_xaxes(title=None)
    filename = "sum_per_day.png"
    fig.write_image(image_path + filename)

def create_all_graphs():
    create_sum_per_day_graph()
    for b in (True, False):
        create_bar_plot(b)
        create_line_graph(b)
