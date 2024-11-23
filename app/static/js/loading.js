'use strict';

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// script.js
window.addEventListener("load", async function() {
  await sleep(2000);
  document.getElementById("loading-screen").style.display = "none";
  document.getElementById("main-content").style.display = "block";
});


// リソースの読み込みを待機
function loadResources() {
  const dataPromise = fetchData();  // APIデータ読み込みの例
  const imagePromise = loadImage("path/to/image.jpg");

  return Promise.all([dataPromise, imagePromise]);
}

loadResources().then(() => {
  document.getElementById("loading-screen").style.display = "none";
  document.getElementById("main-content").style.display = "block";
});
