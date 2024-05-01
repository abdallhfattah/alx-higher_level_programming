#!/usr/bin/node
exports.esrever = function (list) {
  const result = new Array();
  for (let i = list.length; i >= 0; i--) {
    const element = list[i];
    result.push(element);
  }
  return result;
};
