"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Rational Arithmetic

Link: https://open.kattis.com/contests/guve43/problems/rationalarithmetic

@author Leonard Hußke

@version 1.0, 08.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.89s

"""

import java.util.Objects;
import java.util.Scanner;
import java.math.BigInteger;

public class rationalArithmetic {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            BigInteger x1 = new BigInteger(scan.next());
            BigInteger y1 = new BigInteger(scan.next());

            String operand = scan.next();

            BigInteger x2 = new BigInteger(scan.next());
            BigInteger y2 = new BigInteger(scan.next());

            BigInteger r1;
            BigInteger r2;

            switch (operand) {
                case "+":
                    add(x1, y1, x2, y2, "+");
                    break;
                case "-":
                    add(x1, y1, x2, y2, "-");
                    break;
                case "*":
                    multiply(x1, y1, x2, y2);
                    break;
                default:
                    multiply(x1, y1, y2, x2);
                    break;
            }

        }
        scan.close();
    }


    private static void add(BigInteger x1, BigInteger y1, BigInteger x2, BigInteger y2, String op) {
        BigInteger b1 = x1.multiply(y2);
        BigInteger b2 = y1.multiply(x2);
        BigInteger p2 = y1.multiply(y2);
        BigInteger p1;
        if (Objects.equals(op, "+")) {
            p1 = b1.add(b2);
        } else {
            p1 = b1.subtract(b2);
        }

        BigInteger r1 = kuerzen(p1, p2);
        BigInteger r2 = kuerzen(p2, p1);

        ausgabe(r1, r2);
    }


    private static void multiply(BigInteger x1, BigInteger y1, BigInteger x2, BigInteger y2) {
        BigInteger p1 = x1.multiply(x2);
        BigInteger p2 = y1.multiply(y2);
        BigInteger r1 = kuerzen(p1, p2);
        BigInteger r2 = kuerzen(p2, p1);
        ausgabe(r1, r2);
    }

    private static BigInteger kuerzen(BigInteger p1, BigInteger p2) {
        BigInteger ggt = p1.gcd(p2);
        return p1.divide(ggt);
    }

    private static void ausgabe(BigInteger r1, BigInteger r2) {
        if (r2.compareTo(BigInteger.ZERO) < 0) {
            r2 = r2.negate();
            r1 = r1.negate();
        }
        System.out.println(r1 + " / " + r2);
    }
}
