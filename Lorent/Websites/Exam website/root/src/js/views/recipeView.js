import View from "./View.js";

// Loads Icons
const icons = new URL("src/img/icons.svg", document.location.origin).href;

class RecipeView extends View {
    _parentElement = document.querySelector('.recipe');
    _errorMessage = `Nous n'avons pas trouvé cette recette. Veuillez essayer une autre!`;
    _message = '';

    addHandlerRender(handler) {
        ['hashchange', 'load'].forEach(ev => window.addEventListener(ev, handler));
    }

    _generateMarkup() {
        return `
            <figure class="recipe__fig">
            <img src="${this._data.imageUrl}" alt="Recipe Image" class="recipe__img" />
            <h1 class="recipe__title">
                <span>${this._data.title}</span>
            </h1>
            </figure>
            <div class="recipe__details">
            <div class="recipe__info">
                <svg class="recipe__info-icon">
                <use href="${icons}#icon-clock"></use>
                </svg>
                <span class="recipe__info-data recipe__info-data--minutes">${this._data.cookingTime}</span>
                <span class="recipe__info-text">minutes</span>
            </div>
            <div class="recipe__info">
                <svg class="recipe__info-icon">
                <use href="${icons}#icon-users"></use>
                </svg>
                <span class="recipe__info-data recipe__info-data--people">${this._data.servings}</span>
                <span class="recipe__info-text">PORTIONS</span>
                <div class="recipe__info-buttons">
                <button class="btn--tiny btn--increase-servings">
                    <svg>
                    <use href="${icons}#icon-minus-circle"></use>
                    </svg>
                </button>
                <button class="btn--tiny btn--increase-servings">
                    <svg>
                    <use href="${icons}#icon-plus-circle"></use>
                    </svg>
                </button>
                </div>
            </div>
            <button class="btn--round">
                <svg class="">
                    <use href="${icons}#icon-bookmark-fill"></use>
                </svg>
            </button>
            </div>
            <div class="recipe__ingredients">
            <h2 class="heading--2">Ingrédients de la recette</h2>
            <ul class="recipe__ingredient-list">
                ${this._data.ingredients.map(this._generateMarkupIngredient).join('')}
            </div>
            <div class="recipe__directions">
            <h2 class="heading--2">Comment la préparer?</h2>
            <p class="recipe__directions-text">
                Cette recette a été soigneusement conçue par
                <span class="recipe__publisher">${this._data.publisher}</span>. Veuillez consulter les instructions sur leur site Web.
            </p>
            <a
                class="btn--small recipe__btn"
                href="${this._data.sourceUrl}"
                target="_blank"
            >
                <span>Directions</span>
                <svg class="search__icon">
                <use href="${icons}#icon-arrow-right"></use>
                </svg>
            </a>
            </div>
        `;
    }

    _generateMarkupIngredient(ing) {
        return `
        <li class="recipe__ingredient">
            <svg class="recipe__icon">
                <use href="${icons}#icon-check"></use>
            </svg>
        <div class="recipe__quantity">${ing.quantity ? ing.quantity : ''}</div>
        <div class="recipe__description">
        <span class="recipe__unit">${ing.unit}</span>
        ${ing.description}
        </div>
        </li>
        `;
    }
}

export default new RecipeView();