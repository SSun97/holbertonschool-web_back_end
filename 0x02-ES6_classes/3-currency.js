export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  set code(newVal) {
    if (typeof newVal !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newVal;
  }

  set name(newVal) {
    if (typeof newVal !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newVal;
  }

  displayFullCurrency() {
    console.log(`${this._name} (${this._code})`);
  }
}
