import 'dart:io';

void main() {
  int sum = 0;
  new File('input').readAsString().then((input) {
    for(var i = 0; i < input.length - 1; i++) {
      if(input[i] == input[i + 1]) {
        sum += int.parse(input[i]);
      }
    }
    if(input[0] == input[input.length - 1]) {
      sum += int.parse(input[0]);
    }
    print('Answer to part 1: $sum');
  });
}