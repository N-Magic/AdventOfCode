package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Code is started")
	file, err := os.Open("day6.in")
	if err != nil {
		return
	}
	defer file.Close()

	var grid [130][130]string

	scanner := bufio.NewScanner(file)
	var i = 0
	for scanner.Scan() {
		line := scanner.Text()
		for j := 0; j < 130; j++ {
			grid[i][j] = string(line[j])
		}
		fmt.Println(line)
	}
}

func updateGrid(grid [][]string) int {
	for i := 0; i < 130; i++ {
		for j := 0; j < 130; j++ {
			if grid[i][j] == "." {
				continue
			}
			if grid[i][j] == ("^") {
				if i-1 == -1 {
					return 3
				} else if grid[i-1][j] == "#" {
					grid[i][j] = ">"
					return 0
				} else {
					grid[i-1][j] = "^"
					grid[i][j] = "#"
					return 0
				}
			}
			if grid[i][j] == (">") {
				if j+1 == 130 {
					return 3
				} else if grid[i-1][j] == "#" {
					grid[i][j] = ">"
					return 0
				} else {
					grid[i-1][j] = "^"
					grid[i][j] = "#"
					return 0
				}
			}
		}
	}
	return 0
}
