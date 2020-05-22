(defvar a)
(princ "Enter the number: ")
(setq a (read))

(setq n 1)

(loop for x from 1 to a
 do (setq n (* n  x)))


(format t "Factorial of ~d : ~d" a n)

