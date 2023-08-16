#!/usr/bin/node

exports.esrever = function (list) {
  let length = list.length - 1;
  const revlist = [];

  for (let i = 0; length >= 0; i++) {
    revlist[i] = list[length];
    length--;
  }
  return (revlist);
};
