class SearchView {
    _parentElement = document.querySelector('.search-field');

    getQuery() {
        const query = this._parentElement.querySelector('.search-input').value;
        console.log(query);
        // Clear field after search
        this._clearInput();
        return query;
    }

    _clearInput() {
        this._parentElement.querySelector('.search-input').value = '';
    }

    addHandlerSearch(handler) {
        this._parentElement.addEventListener('submit', function(e) {
            e.preventDefault();
            handler();
        })
    }
}

export default new SearchView();