const API_URL = "http://localhost:5001/api/";

async function getCupcakes() {
  const response = await fetch(`${API_URL}cupcakes`);
  const cupcakesData = await response.json();

  return cupcakesData.cupcakes;
}

function displayCupcakes(cupcakes) {

  const $cupcakeList = $("#cupcakeList");

  for (const cupcake of cupcakes){
    const $cupcakeItem = $("<li>")
    // image, flavor, size, rating
    const $image = $("<img>").attr({"src": cupcake.image_url, "width": 100});
    $cupcakeItem.append($image);

    for(const key of ["flavor", "size", "rating"]){
      $attribute = $("<p>").text(`${key}: ${cupcake[key]}`);
      $cupcakeItem.append($attribute);
    }

    $cupcakeList.append($cupcakeItem);
  }

}

async function getAndDisplayCupcakes(){
  const cupcakes = await getCupcakes();
  displayCupcakes(cupcakes);

}


// Run everything?
getAndDisplayCupcakes();
