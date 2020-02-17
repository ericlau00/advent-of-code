import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> triangles = new ArrayList<ArrayList<Integer>>();
        try {
            File input = new File("input");
            Scanner sc = new Scanner(input);
            while (sc.hasNextLine()) {
                ArrayList<Integer> triangle = new ArrayList<Integer>();
                String data = sc.nextLine();
                String temp[] = data.trim().split(" ");
                for(String side : temp) {
                    if(!side.trim().equals("")) {
                        triangle.add(Integer.parseInt(side));
                    }
                }
                triangles.add(triangle);
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
        int validTriangles = 0;
        for(int i = 0; i < triangles.size(); i++) {
            int side0 = triangles.get(i).get(0);
            int side1 = triangles.get(i).get(1);
            int side2 = triangles.get(i).get(2);
            int shortest;
            int shorter;
            int longest;
            if(side0 <= side1 && side0 <= side2) {
                shortest = side0;
                if(side1 <= side2) {
                    shorter = side1;
                    longest = side2;
                } else {
                    shorter = side2;
                    longest = side1;
                }
            }
            else if(side1 <= side0 && side1 <= side2) {
                shortest = side1;
                if(side0 <= side2) {
                    shorter = side0;
                    longest = side2;
                } else {
                    shorter = side2;
                    longest = side0;
                }
            } else {
                shortest = side2;
                if (side1 <= side0) {
                    shorter = side1;
                    longest = side0;
                } else {
                    shorter = side0;
                    longest = side1;
                }
            }
            if (shortest + shorter > longest) {
                validTriangles++;
            }
        }
        System.out.println("Answer to part 1: " + validTriangles);
    }
}