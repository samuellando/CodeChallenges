package main

import (
	"regexp"
	"strings"
	"text/scanner"
	"unicode"
)

var signRegex = regexp.MustCompile("^[+-]$")

var numberRegex = regexp.MustCompile("^[0-9]+$")

var decimalRegex = regexp.MustCompile("^\\.$")

var exponentRegex = regexp.MustCompile("^e[+-]{0,1}[0-9]+$")

func isNumber(s string) bool {
	tokens := make([]string, 0)
	// Tokenize and parse.
	var snr scanner.Scanner
	snr.Init(strings.NewReader(strings.TrimSpace(s)))
	snr.Whitespace ^= 1 << ' '
	snr.Mode ^= scanner.ScanInts
	snr.Mode ^= scanner.ScanFloats
	snr.IsIdentRune = func(ch rune, i int) bool {
		return unicode.IsDigit(ch) ||
			ch == '+' && i == 1 ||
			ch == '-' && i == 1 ||
			ch == 'e' && i == 0
	}
	for tok := snr.Scan(); tok != scanner.EOF; tok = snr.Scan() {
		tokens = append(tokens, snr.TokenText())
	}
	/*
	 * breakdown:
	 * 1:[sign] 2:(number decimal number) 3:[exponent]
	 *
	 * 1 and 3 are optional however 2 is not. 2 is most complex.
	 *
	 * 1 can olny occur in position 0
	 * 3 can only occur in the final position
	 *
	 * valid 2:
	 * number
	 * number decimal
	 * decimal number
	 * number decimal number
	 */
	if len(tokens) == 0 {
		return false
	}
	if signRegex.MatchString(tokens[0]) {
		tokens = tokens[1:]
	}
	if exponentRegex.MatchString(tokens[len(tokens)-1]) {
		tokens = tokens[:len(tokens)-1]
	}
	switch len(tokens) {
	case 3:
		if !(numberRegex.MatchString(tokens[0]) &&
			decimalRegex.MatchString(tokens[1]) &&
			numberRegex.MatchString(tokens[2])) {
			return false
		}
	case 2:
		if !(numberRegex.MatchString(tokens[0]) &&
			decimalRegex.MatchString(tokens[1]) ||
			decimalRegex.MatchString(tokens[0]) &&
				numberRegex.MatchString(tokens[1])) {
			return false
		}
	case 1:
		if !(numberRegex.MatchString(tokens[0])) {
			return false
		}
	default:
		return false

	}
	return true
}

func main() {
	fmt.Println(isNumber("-0.0e-25000"))
}
