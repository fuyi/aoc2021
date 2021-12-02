package d1

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func Increment() (int, int) {
	// Initialize 1 element slice
	nums := make([]int, 0)
	inc_count := 0
	sum_inc_count := 0

	file, err := os.Open("d1/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Use scanner to read lines from file handler
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// fmt.Println("=========")
		text := scanner.Text()
		num, _ := strconv.Atoi(text)
		// fmt.Printf("text value %v is type %T \n", num, num)
		// Append number to slice, increase capacity when needed
		nums = append(nums, num)

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// first half
	for i := 0; i < len(nums)-1; i++ {
		// fmt.Println(nums[i], nums[i+1])
		if nums[i+1] > nums[i] {
			inc_count++
		}
	}
	// second half
	for i := 0; i < len(nums)-3; i++ {
		// fmt.Println(nums[i], nums[i+1])
		if nums[i+3] > nums[i] {
			sum_inc_count++
		}
	}
	return inc_count, sum_inc_count
}
