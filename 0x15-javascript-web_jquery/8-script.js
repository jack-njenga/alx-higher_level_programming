$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  const movies = data.results;
  for (let i = 0; i < movies.length; i++) {
    const title = $('<li></li>').text(movies[i].title);
    $('UL#list_movies').append(title);
  }
  // $("UL#list_movies").append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
