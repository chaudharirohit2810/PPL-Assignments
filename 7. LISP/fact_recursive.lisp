(defvar n)

(defun fact(n)	
 (if (= n 0) ( return-from fact 1))
  ( return-from fact (* n (fact (- n 1) )))
 )


(defvar a)

(princ "Enter the number: ")

(setq a (read))


(format t "The factorial of ~d is ~d" a  (fact a ))

