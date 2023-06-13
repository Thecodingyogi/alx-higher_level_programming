#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while (len - i > 0) {
    const temp = list[i];
    list[i] = list[len];
    list[len] = temp;
    i++;
    len--;
  }
  return list;
};
