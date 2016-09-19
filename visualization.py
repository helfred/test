from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_csv("sourcedata.txt", parse_dates = ["Start", "End"])

p = figure(x_axis_type = "datetime", height = 100, width = 500, responsive = True, title = "Motion Graph")
q = p.quad(left = df["Start"], right = df["End"], bottom = 0, top = 1, color = "green")

output_file("graph.html")
show(p)
