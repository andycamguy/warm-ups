function countBy(x, n) {
  let z = [];
  let y = 1; // start with y = 1 to get the first multiple

  while (y <= n) {
    z.push(x * y);
    y++;
  }

  return z;
}
