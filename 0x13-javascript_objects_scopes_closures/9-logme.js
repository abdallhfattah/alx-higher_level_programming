#!/usr/bin/node
let NumOfCalls = 0;
exports.logMe = function (item) {
  console.log(NumOfCalls + ': ' + item);
  NumOfCalls += 1;
};
