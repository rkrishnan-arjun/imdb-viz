import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Load the imdb dataset
imdb_df = pd.read_csv("../data/imdb_top_1000.csv")
imdb_df["Genre"] = imdb_df["Genre"].str.split(",")
imdb_df = imdb_df.explode("Genre")
imdb_df["Genre"] = imdb_df["Genre"].str.strip()
imdb_df = imdb_df[(imdb_df["Certificate"] != "16")]
imdb_df = imdb_df.dropna(subset=["Certificate"])
imdb_df["Gross"] = pd.to_numeric(imdb_df["Gross"].str.replace(",", "")) / 1000000

# Define the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app.title = "IMDb Dashboard"
server = app.server

# Define the layout
app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "IMDb VISUALIZATION",
                            style={
                                "backgroundColor": "",
                                "font-weight": "bold",
                                "padding": 20,
                                "color": "black",
                                "margin-left": 15,
                                "text-align": "center",
                                "font-size": "36px",
                                "border-radius": 1,
                            },
                        )
                    ],
                    width=12,
                )
            ]
        ),
        dbc.Row([
        dbc.Col(html.H4("Select a Genre", style={"font-weight": "bold"}),
                    width=2),
        dbc.Col(dcc.Dropdown(
            id="genre-dropdown",
            options=[
                {"label": genre, "value": genre} for genre in imdb_df["Genre"].unique()
            ],
            value=imdb_df["Genre"].iloc[0],
        ),
                    width=3,
        style={"padding": 0})
        ]),
        html.Br(),
        dcc.Graph(id="bar-plot", style={"backgroundColor": "rgba(0,0,0,0)"}, figure={"layout": {
            "height": 500, 
        }}),
        html.Br(),
        dbc.Row([
        dbc.Col(
        html.H4("Select a Certificate", style={"font-weight": "bold"}),
                    width=3),
        dbc.Col(
        dcc.Dropdown(id="cert-dropdown"),
                    width=3,
        style={"padding": 0})
        ]),
        html.Br(),
        dbc.Row([dbc.Col(dcc.Graph(id="director-plot")),dbc.Col(dcc.Graph(id="line-plot"))]),
    ],
    className="container",
    style={"backgroundColor": "lightgreen"},
)


@app.callback(
    [
        dash.dependencies.Output("cert-dropdown", "options"),
        dash.dependencies.Output("cert-dropdown", "value"),
    ],
    [dash.dependencies.Input("genre-dropdown", "value")],
)
def update_certs(genre):
    movies_grouped = imdb_df
    [
        (imdb_df["Released_Year"] >= "2009") & (imdb_df["Released_Year"] <= "2022")
    ]
    certs = movies_grouped[movies_grouped["Genre"] == genre]["Certificate"].unique()
    return ([{"label": cert, "value": cert} for cert in certs], certs[0])


# Define the callback to update the new plot
@app.callback(
    dash.dependencies.Output("bar-plot", "figure"),
    [dash.dependencies.Input("genre-dropdown", "value")],
)
def update_gross_plot(genre):
    grp_df = (
        imdb_df[imdb_df["Genre"] == genre]
        .sort_values("IMDB_Rating", ascending=False)
        .head(10)
    )
    grp_df = grp_df[grp_df["Gross"].notna()].sort_values("Gross")
    # Create a bar chart 
    fig = px.bar(
        grp_df,
        x="Gross",
        y="Series_Title",
        orientation="h",
        title=f"Gross Revenue of Top 10 movies by rating",
        text=grp_df["Series_Title"].tolist(),
        color="Series_Title",
        color_continuous_scale=px.colors.sequential.Plasma,
    )

    fig.update_yaxes(showticklabels=False)
    fig.update_traces(textfont_size=13)
    # Update the layout
    fig.update_layout(
        xaxis_title="Gross Revenue (Million Dollars)", yaxis_title="Movies", showlegend=False,
        plot_bgcolor='white',
        
        title='<b>Gross Revenue of Top 10 movies by rating</b>'
    )

    return fig

# Define the callback to update the plot
@app.callback(
    dash.dependencies.Output("director-plot", "figure"),
    [dash.dependencies.Input("genre-dropdown", "value"),
     dash.dependencies.Input("cert-dropdown", "value")],
)
def update_direct_plot(genre, cert):
    grp_df = (
        imdb_df[(imdb_df["Genre"] == genre) & (imdb_df["Certificate"] == cert)]
        .sort_values("IMDB_Rating", ascending=False)
        .head(3)
    )
    grp_df = grp_df[grp_df["Director"].notna()].sort_values("IMDB_Rating")
    # Create a bar chart 
    fig = px.bar(
        grp_df,
        x="IMDB_Rating",
        y="Director",
        orientation="h",
        title=f"Top Directors",
        text=grp_df["Director"].tolist(),
        color_continuous_scale=px.colors.sequential.Plasma
    )
    # Remove y-axis tick labels

    fig.update_yaxes(showticklabels=False)
    
    fig.update_traces(textfont_size=17)

    # Update the layout
    fig.update_layout(
        xaxis_title="IMDB Rating", yaxis_title="Directors", showlegend=False,        
        title='<b>Top Directors</b>',
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color='black'),
        yaxis=dict(showgrid=False,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        tickwidth=1,
        ticklen=5),
        xaxis=dict(showgrid=False,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        range=[5, 9.5],
        tickwidth=1,
        ticklen=5)
    )


    return fig


@app.callback(
    dash.dependencies.Output("line-plot", "figure"),
    [
        dash.dependencies.Input("genre-dropdown", "value"),
        dash.dependencies.Input("cert-dropdown", "value"),
    ],
)
def update_line_plot(genre, cert):
    # Filter the data by year and country
    grp_df = imdb_df[(imdb_df["Genre"] == genre) & (imdb_df["Certificate"] == cert)]
    movies_grouped = grp_df[
        (grp_df["Released_Year"] >= "2009") & (grp_df["Released_Year"] <= "2022")
    ]
    movies_grouped = (
        movies_grouped.groupby("Released_Year").size().reset_index(name="count")
    )

    # Create a line plot
    fig = px.line(movies_grouped, x="Released_Year", y="count", title=f"Trend of number of movies released over the years")
    # Remove y-axis tick labels

    # Update the layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Count of movies",
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        range=[5, 9.5],
        tickwidth=1,
        ticklen=5),
        xaxis=dict(showgrid=False,
        linecolor='black',
        ticks='outside',
        tickcolor='black',
        range=[5, 9.5],
        tickwidth=1,
        ticklen=5),
        title='<b>Trend of number of movies released over the years</b>'
    )

    # Increase the thickness of the line
    fig.update_traces(line=dict(width=7))

    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
