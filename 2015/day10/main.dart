void main() {
  String input = "1321131112";
  int currentStreak = 1;
  for (int x = 0; x < 40; x++) {
    String output = '';
    for (int i = 0; i < input.length; i++) {
      if (i == input.length - 1 && input.length != 1) {
        if (input[i] == input[i - 1]) {
          output += currentStreak.toString() + input[i];
        } else {
          output += 1.toString() + input[i];
        }
      } else if (input[i] == input[i + 1]) {
        currentStreak++;
      } else {
        output += currentStreak.toString() + input[i];
        currentStreak = 1;
        if (i + 1 == input.length) {
          output += 1.toString() + input[i + 1];
        }
      }
    }
    input = output;
    print(input.length);
  }
  // print(input.length);
}
