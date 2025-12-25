(def websites
  (loop [x 0
         result []]
    (if (< x 1000)
      (recur
       (inc x)
       (conj result "codewars")) result)))