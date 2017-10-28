// Strip "LEGO " from the front
export const trimTitle = title => title.replace(/^LEGO\s/, '');
// Only digits, and between 1 and 7 of them (valid input)
export const digitTest = RegExp(/^\d{1,7}$/);
// Only digits, and between 5 and 7 of them (valid API query)
export const digitLengthTest = RegExp(/^\d{5,7}$/)