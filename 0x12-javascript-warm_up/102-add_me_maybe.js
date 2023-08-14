#!/usr/bin/node
exports.addMeMaybe = function (a, b) {
  a = a + 1;
  b(a);
};
