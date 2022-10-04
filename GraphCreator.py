from DataGetter import DataGetter
import plotly.express as px


class GraphCreator:
    image_path = "images/"
    image_width = 1200
    image_height = 700
    data_getter = DataGetter()

    def create_line_graph(self, is_guest):
        df = self.data_getter.get_chart_data(is_guest)

        fig = px.line(df, markers=True, width=self.image_width, height=self.image_height)
        fig.update_yaxes(title=None)
        fig.update_xaxes(title=None)
        fig.update_layout(legend_title=None)

        filename = "line_graph"
        if is_guest:
            filename += "_guest"
        filename += ".png"

        fig.write_image(self.image_path + filename)

    def create_bar_plot(self, is_guest):
        df = self.data_getter.get_chart_data(is_guest)

        fig = px.bar(df, width=self.image_width, height=self.image_height, text_auto=True)
        fig.update_yaxes(title=None)
        fig.update_xaxes(title=None)
        fig.update_layout(legend_title=None)

        filename = "bar_plot"
        if is_guest:
            filename += "_guest"
        filename += ".png"

        fig.write_image(self.image_path + filename)


if __name__ == '__main__':
    gc = GraphCreator()
    gc.create_bar_plot(False)
