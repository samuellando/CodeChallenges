func checkValidString(s string) bool {
    var mainStack  int
    var helpStack int
    
    for _, c := range s {
        if c ==  '(' {
            mainStack++
        } else if c == '*' {
            if mainStack > 0 {
                mainStack--
                helpStack += 2
            } else {
                helpStack++
            }
        } else {
            if mainStack > 0 {
                mainStack--
            } else if helpStack > 0 {
                helpStack--
            } else {
                return false
            }
        }
    }
    
    return mainStack == 0
}