import 'dart:io';

void main() {
  new File('input').readAsString().then((input) {
    List<String> rows = input.split("\r\n");
    List<int> smallest = new List<int>();
    List<int> largest = new List<int>();
    for (var row in rows) {
      int small = 10000000;
      int large = 0;
      for(var n in row.split("\t")) {
        if( int.parse(n) < small) {
          small = int.parse(n);
        }
        if (int.parse(n) > large) {
          large = int.parse(n);
        }
      }
      smallest.add(small);
      largest.add(large);
    }
    int diff_sum = 0;
    for(var i = 0; i < smallest.length; i++) {
      diff_sum += largest[i] - smallest[i];
    }
    print(diff_sum);
  });
}
