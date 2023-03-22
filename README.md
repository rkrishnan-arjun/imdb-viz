# IMDB_Viz_R

Welcome everyone and thank you for visiting the `imdb-viz` project repository!

If you love great movies and need some help figuring out which one to watch next, then you've come to the right place as our app is exactly what you need!

[Link to the imdb-viz app](https://imdb-viz-app.onrender.com)

To read more about our wonderful app, feel free to jump over to one of the sections below or continue scrolling down.

- [Motivation and Purpose](#motivation-and-purpose)
- [Proposal](#proposal)
- [Dashboard Description](#dashboard-description)
- [Contributing](#contributing)
- [License](#license)

## Motivation and Purpose

Choosing a good movie to watch can be a struggle sometimes and there's almost nothing worse than realizing you just spent 2 hours sitting through a horrible movie that you didn't enjoy one bit. Our user-friendly and accessible dashboard aims to help movie enthusiasts avoid this problem by helping them discover and explore new movies based on their movie watching preferences. In addition, our dashboard uses a vast database of movies to provide users with information on ratings, gross revenue, directors and movie numbers presented through engaging visuals based on metrics which they can select via an interactive and intuitive interface. This dash app was built as an extension of our R [shiny app](https://arjunrk.shinyapps.io/IMDB_Viz_R/).

## Proposal

Click [here](https://github.com/UBC-MDS/IMDB_Viz_R/blob/main/reports/proposal.md) to read the initial motivation and purpose of this dashboard.

## Dashboard Description

Our dashboard contains a single landing page where users can use drop-down lists on the page to select the genre and certificate of interest. This dashboard showcases interactive visualizations which recommends top rated movies for the movie enthusiasts and can assist them in exploring top directors in the movie industry and the trend of the number of movies produced over the years.

First of all, the user can select preferred genre from the first drop-down. Based on this selection, dashboard displays

- `Gross Revenue of top Rated movies by Genre`: A bar chart that directly lists out the highest rated movies for the primary selected genre with their respective gross revenue.

Another option that users have is to select their preferred certificate from the second drop down which will be updated based on the genre input. Based on the `genre` and `certificate`, the dashboard displays the following -

- `Top directors`: A bar chart that directly lists out the directors that have directed top rated movies
- `Trend of count of movies over the years`: A line plot that shows the trend of count of movies produced over the years

Using these visualizations, the users can understand if the top rated movies are actually worth their time based on the gross revenue it made. They can also know who are the top directors in the movie industry and how many movies were produced in the selected genre and certificate over the years. This dashboard is aimed at providing users with an easy-to-use and efficient way to find and select the movies they'll love.

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/rkrishnan-arjun/imdb-viz/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/rkrishnan-arjun/imdb-viz/blob/main/CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`imdb-viz` was created by Arjun Radhakrishnan. It is licensed under the terms of the MIT license.
