(def hundred (range 101))

(def sumsqr (apply + (map (fn [x] (* x x)) hundred)))

(def sum (apply + hundred))

(def sqrsum (* sum sum))

(- sqrsum sumsqr)