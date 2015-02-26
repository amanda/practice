package main

import (
    "fmt"
    "strings"
)

func inttoroman(num int) []string {

    var numeral []string    
    romans := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
    arabic := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}

    for i := 0; i < len(romans); i++ {
        if num >= arabic[i] {
            repeat := num/arabic[i]
            for k := 1; k <= repeat; k++ {
                numeral = append(numeral, romans[i])
                num = num%arabic[i]
            }
        }
    }

    return numeral

}

func main() {

    s := inttoroman(1024) // edit this
    fmt.Printf(strings.Join(s, "") + "\n");

}
