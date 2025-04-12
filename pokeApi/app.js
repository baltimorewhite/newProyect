const container = document.getElementById("pokemon-container");

async function getPokemonList(limit = 500) {
  const response = await fetch(`https://pokeapi.co/api/v2/pokemon?limit=${limit}`);
  const data = await response.json();

  data.results.forEach(pokemon => {
    fetchPokemonData(pokemon.url);
  });
}

async function fetchPokemonData(url) {
  const response = await fetch(url);
  const data = await response.json();

  const card = document.createElement("div");
  card.style.border = "1px solid #ccc";
  card.style.margin = "10px";
  card.style.padding = "10px";
  card.style.display = "inline-block";
  card.style.textAlign = "center";

  const name = document.createElement("h3");
  name.innerText = data.name;

  const img = document.createElement("img");
  img.src = data.sprites.front_default;
  img.alt = data.name;

  card.appendChild(name);
  card.appendChild(img);
  container.appendChild(card);
}

getPokemonList();
