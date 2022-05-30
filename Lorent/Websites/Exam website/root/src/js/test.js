const imageURL = new URL("../img/logo.png", document.URL)
console.log(imageURL.href);

document.body.insertAdjacentHTML("beforeend", `<img src"${imageURL.href}">`)