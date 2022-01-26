exports.Category = {
    products: ({ id: categoryId }, {filter}, {db}) => {
        const categoryProducts = db.products.filter((product) => product.categoryId === categoryId);
        let filteredCategoryProduct = categoryProducts;
        if(filter) {
            if(filter.onSale === true) {
                filteredCategoryProduct = filteredCategoryProduct.filter(product => {
                    return product.onSale
                });
            }
        }
        return filteredCategoryProduct
    }
}