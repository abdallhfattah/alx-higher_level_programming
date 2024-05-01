#!/usr/bin/node
exports.nbOccurences = function (array, num) {
  let occ = 0;
  for (let index = 0; index < array.length; index++) {
    const element = array[index];
    if (element === num) occ++;
  }
  return occ;
};
