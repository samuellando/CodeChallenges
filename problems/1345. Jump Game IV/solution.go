package solution

// For each value, keep track of nodes that can jumped to.
var ls map[int][]*node
var q []*node

type node struct {
	n   *node
	p   *node
	v   bool // visitend, to make sure we don't cycle.
	val int  // Keep the value so we can search in ls.
}

func (n node) l() []*node {
	return ls[n.val]
}

func bfs() int {
	for d := 0; len(q) > 0; d++ {
		l := len(q)
		for i := 0; i < l; i++ {
			n := q[0]
			q = q[1:]
			if (*n).n == nil {
				return d
			} else {
				for i := 0; i < len((*n).l()); i++ {
					if !(*n).l()[i].v {
						(*n).l()[i].v = true
						q = append(q, (*n).l()[i])
					}
				}
				// To reduce number of checks, empty the can be jumped to list, as we already added them all.
				ls[(*n).val] = ls[(*n).val][:0]
				if (*n).n != nil && !(*n).n.v {
					(*n).n.v = true
					q = append(q, (*n).n)
				}
				if (*n).p != nil && !(*n).p.v {
					(*n).p.v = true
					q = append(q, (*n).p)
				}
			}
		}
	}

	return -1
}

func minJumps(arr []int) int {
	ls = make(map[int][]*node)
	q = make([]*node, 0)
	// Build a graph and do a BFS.

	var np *node
	var root *node

	// Create the graph and fill up ls.
	for i := 0; i < len(arr); i++ {
		n := node{n: nil, p: nil, v: false, val: arr[i]}

		if i == 0 {
			root = &n
		}

		if _, ok := ls[arr[i]]; !ok {
			ln := make([]*node, 0)
			ls[arr[i]] = ln
		}
		l := append(ls[arr[i]], &n)
		ls[arr[i]] = l

		if i > 0 {
			n.p = np
			np.n = &n
		}
		np = &n
	}
	(*root).v = true
	q = append(q, root)

	return bfs()
}
