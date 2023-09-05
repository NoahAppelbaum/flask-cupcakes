"use strict";

const API_URL = "http://localhost:5001/api/";
const $cupcakeList = $("#cupcakeList");

/**
 * Gets cupcake data from the API.
 * @returns list of cupcake objects.
 */
async function getCupcakes() {
  const response = await fetch(`${API_URL}cupcakes`);
  const cupcakesData = await response.json();

  return cupcakesData.cupcakes;
}

/**
 * Displays cupcakes on DOM given a list of cupcake objects.
 *
 */
function displayCupcakes(cupcakes) {

  $cupcakeList.empty();

  for (const cupcake of cupcakes) {
    const $cupcakeItem = $("<li>");
    // image, flavor, size, rating
    const $image = $("<img>").attr({ "src": cupcake.image_url, "width": 100 });
    $cupcakeItem.append($image);

    for (const key of ["flavor", "size", "rating"]) {
      $attribute = $("<p>").text(`${key}: ${cupcake[key]}`);
      $cupcakeItem.append($attribute);
    }

    $cupcakeList.append($cupcakeItem);
  }

}

async function getAndDisplayCupcakes() {
  const cupcakes = await getCupcakes();
  displayCupcakes(cupcakes);

}

/**
 * Handles the submission of the new cupcake form and refreshed displayed
 * cupcake list.
 */
async function handleSubmitClick(event) {
  event.preventDefault();
  const apiData = {};
  const $inputs = $(".form-input");
  for (const inputField of $inputs) {
    const $inputField = $(inputField);
    console.log($inputField);
    const $input = $inputField.children("input");
    console.log($input);
    apiData[$input.attr("id")] = $input.val();
  }

  await fetch(`${API_URL}cupcakes`,
    {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(apiData)
    });

  getAndDisplayCupcakes();

}

$("#newCupcakeForm").on("submit", handleSubmitClick);


// Display cupcake list upon loading.
getAndDisplayCupcakes();
