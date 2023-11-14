#!/usr/bin/node
// Executes theFunction 'x' times
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
