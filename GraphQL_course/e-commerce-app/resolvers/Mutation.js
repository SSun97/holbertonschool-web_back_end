const { v4: uuid } = require("uuid")
exports.Mutation = {
    addCategory: (parent, {input}, {db}) => {
        const {name} = input;
        const newCategory = {
            id: uuid(),
            name
        };
        db.categories.push(newCategory);
        return newCategory;
    },

    addProduct: (parent, {input}, {db}) => {
        const {name, image, price, onSale, quantity, categoryId} = input;
        const newProduct = {id:uuid(),name, image, price, onSale, quantity, categoryId};
        db.products.push(newProduct);
        return newProduct;
    }
};