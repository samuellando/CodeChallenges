import (
    "math"
)

func stringShift(s string, shift [][]int) string {
	k := 0

	for i := 0; i < len(shift); i++ {
		if shift[i][0] == 0 {
			k += shift[i][1]
		} else {
			k -= shift[i][1]
		}
	}

	t := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
        t[i] = s[mod(k, len(s))]
		k++
	}
	return string(t)
}

func mod(a, b int) int {
    if a < 0 {
        a = b + int(math.Mod(float64(a), float64(b)))
    }
    return a % b
}}