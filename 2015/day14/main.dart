import 'dart:io';

void main() {
  int seconds = 2503;
  new File('input').readAsString().then((input) {
    List<String> reindeers = input.split('\r\n');
    List<List<int>> values = new List<List<int>>();
    for (var r in reindeers) {
      List<int> stats = new List<int>();
      stats.add(int.parse(r.substring(r.indexOf('fly') + 4, r.indexOf('km/s') - 1)));
      stats.add(int.parse(r.substring(r.indexOf('for') + 4, r.indexOf('seconds') - 1)));
      stats.add(int.parse(r.substring(r.lastIndexOf('for') + 4, r.lastIndexOf('seconds') -1)));
      values.add(stats);
    }
    print(values);
    int maxDistance = 0;
    for (var stats in values) {
      int hasFlown = 0;
      int hasRested = 0;
      int distance = 0;
      for(var i = 0; i < seconds; i++) {
        if(hasFlown < stats[1]) {
          hasFlown++;
          distance += stats[0];
        } else {
          if(hasRested < stats[2]) {
            hasRested++;
          } else {
            hasRested = 0;
            hasFlown = 0;
          }
        }
      }
      print(distance);
      if (distance > maxDistance) {
        maxDistance = distance;
      }
    }
    print(maxDistance);
  });
}